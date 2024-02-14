import os
import subprocess
import yaml
from huggingface_hub import HfApi, HfFolder


import shutil

def setup_environment():
    # Define the path to the mergekit directory
    mergekit_dir = "mergekit"

    # Check if the directory already exists
    if os.path.exists(mergekit_dir):
        # Remove the directory and its contents
        shutil.rmtree(mergekit_dir)

    # Proceed to clone the mergekit repository
    subprocess.run(["git", "clone", "-b", "mixtral", "https://github.com/cg123/mergekit.git"], check=True)
    
    # Install mergekit and its dependencies
    os.chdir("mergekit")
    subprocess.run(["pip", "install", "-e", "."], check=True)
    os.chdir("..")
    
    # Install additional required libraries
    subprocess.run(["pip", "install", "--quiet", "--upgrade", "transformers", "huggingface_hub"], check=True)

setup_environment()


def generate_and_merge_models():
    # Define the YAML configuration for the model
    yaml_config = """
    base_model: mistralai/Mistral-7B-Instruct-v0.2
    gate_mode: hidden
    dtype: bfloat16
    experts_per_token: 2
    experts:
      - source_model: Wtzwho/Prometh-merge-test2
        positive_prompts:
          - "You are a helpful general-purpose assistant."
      - source_model: mistralai/Mistral-7B-Instruct-v0.2
        positive_prompts:
          - "You provide instruction-based assistance."
      - source_model: Wtzwho/Prometh-merge-test3
        positive_prompts:
          - "You are helpful for coding-related queries."
      - source_model: meta-math/MetaMath-Mistral-7B
        positive_prompts:
          - "You excel in mathematical problem solving."
    """
    
    # Save the YAML configuration to a file
    with open('config.yaml', 'w', encoding="utf-8") as config_file:
        config_file.write(yaml_config)
    
    # Run mergekit to merge the models as specified in the YAML config
    subprocess.run(["mergekit-moe", "config.yaml", "merge", "--copy-tokenizer", "--allow-crimes", 
                    "--out-shard-size", "1B", "--lazy-unpickle", "--device", "cuda", 
                    "--low-cpu-memory", "--trust-remote-code"], check=True)

generate_and_merge_models()


def upload_model_to_huggingface(username, model_name, yaml_config, license="apache-2.0"):
    token = os.getenv('HF_TOKEN')  # Ensure this environment variable is set in your VM
    if not token:
        raise ValueError("Hugging Face token not found. Please set the HF_TOKEN environment variable.")

    # Define the template for the model card
    model_card_template = """
    ---
    license: {{ license }}
    tags:
    - merge
    ---

    # {{ model_name }}

    {{ model_name }} is a merged model using mergekit with the following configuration:

    ```yaml
    {{ yaml_config }}
    ```

    ## 💻 Usage

    To use this model, install the `transformers` library and then use the following code:

    ```python
    from transformers import AutoModelForCausalLM, AutoTokenizer

    model_name = "{{ username }}/{{ model_name }}"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)

    prompt = "Your prompt here"
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs)
    print(tokenizer.decode(outputs[0], skip_special_tokens=True))
    ```
    """

    # Fill in the template
    model_card_content = model_card_template.format(
        model_name=model_name,
        yaml_config=yaml_config,
        username=username,
        license=license
    )

    # Initialize Hugging Face API and create a new repository
    api = HfApi()
    api.create_repo(token=token, name=model_name, organization=username, private=False)

    # Save the model card content to a README.md file
    with open("README.md", "w") as readme_file:
        readme_file.write(model_card_content)

    # Assume the merged model is saved in a directory named "model_directory"
    model_directory_path = "./merged"  

    # Upload the model and the README.md file to Hugging Face Hub
    api.upload_folder(token=token, repo_id=f"{username}/{model_name}", folder_path=model_directory_path)

