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
    yaml_config = './configs/merge240.yml'
    
    # Save the YAML configuration to a file
    with open('config.yaml', 'w', encoding="utf-8") as config_file:
        config_file.write(yaml_config)
    
    # Run mergekit to merge the models as specified in the YAML config
    subprocess.run(["mergekit", "config.yaml", "merge", "--copy-tokenizer", "--allow-crimes", 
                    "--out-shard-size", "1B", "--lazy-unpickle", "--device", "cuda", 
                    "--low-cpu-memory", "--trust-remote-code"], check=True)

generate_and_merge_models()


def upload_model_to_huggingface(username, model_name, yaml_config, license="apache-2.0"):
    token = os.getenv('HF_TOKEN')  # Ensure this environment variable is set in your VM
    if not token:
        raise ValueError("Hugging Face token not found. Please set the HF_TOKEN environment variable.")

    # Define the template for the model card
    model_card_template ="""
    ---
    license: {{ license }}
    tags:
    ---
    ---
    ```yaml
    {{ yaml_config }}
    ```
    # {{ model_name }} Model Card
    <!-- Provide a quick summary of what the model is/does. -->
    {{ model_name }} is a 

    ## Model Sources and Components 
    <!-- Provide a list of sources and components used in the model. In the bellow format-->
    - [What will appear to the user](link to the hugging face model)

    ## Key Features
     <!-- Provide a list of key features of the model. Bellow in an example -->
    - Enhanced Performance: 
    - Versatility: 
    - State-of-the-Art Integration: 

    ## Application Areas
     <!-- Provide a list of areas in which the model can be applied. Bellow in an example -->
    The model excels in:
    - Area 1
    - Area 2

    ## 💻 Usage Instructions
    <!-- Explain in simple steps how the user can apply the model-->
   
    Integrate the model into your projects with these steps:

    <!-- Example of how to generate a UI python template -->

    ```python
    # Installation
    pip install -qU transformers bitsandbytes accelerate

    # Example code
    from transformers import AutoTokenizer, pipeline
    import torch

    model = "{{ model_name }}"
    tokenizer = AutoTokenizer.from_pretrained(model)

    # Setting up the pipeline
    pipeline = pipeline(
        "text-generation",
        model=model,
        model_kwargs={"torch_dtype": torch.float16, "load_in_4bit": True},
    )

    # Example query
    messages = [{"role": "user", "content": "[Example Query]"}]
    prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)

    outputs = pipeline(prompt, max_new_tokens=256, do_sample=True, temperature=0.7, top_k=50, top_p=0.95)
    print(outputs[0]["generated_text"])
    ```

    ## Technical Specifications


    ##  Model Details and Attribution

    - Developed by: {{ username }}
    - Shared by: [Organization Name]
    - Model type: [Model Type]
    - Language(s): [Supported Languages]
    - License: [License]

    ## Environmental Impact

    [Environmental impact details]

    ## Out-of-Scope Use

    Not intended for generating harmful or biased content.

    ## Bias, Risks, and Limitations

    [To be filled]

    ## Recommendations

    Evaluate the model for biases and ethical considerations before deployment.
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

