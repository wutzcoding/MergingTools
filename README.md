# MergingTools

MergingTools is a Python-based automation tool designed to streamline the process of merging pre-trained language models. Leveraging the powerful capabilities of `mergekit`, MergingTools facilitates elaborate merges of models such as Llama, Mistral, GPT-NeoX, StableLM, and more, under resource-constrained situations. The tool supports both CPU and GPU execution, offering an out-of-core approach to perform merges efficiently with minimal resource requirements.

## Features

- **Broad Model Support:** Compatible with various models including Llama, Mistral, GPT-NeoX, and StableLM.
- **Flexible Merge Methods:** Incorporates numerous merge methods, with the ability to add more as needed.
- **Resource Efficiency:** Utilizes lazy loading of tensors and interpolated gradients for low memory use.
- **Versatility:** Supports both GPU and CPU execution for flexible deployment options.
- **Frankenmerging:** Enables piecewise assembly of language models from layers, allowing for creative model constructions.

## Installation

Ensure you have Python 3.6+ and `pip` installed on your system. Clone the repository and set up the environment by running:

```sh
git clone https://github.com/wutzcoding/MergingTools.git
cd AutoMerge
python -m pip install --upgrade pip
python setup_environment.py
```

## Usage

To start a merge process, create a YAML configuration file specifying your merge parameters and run:

```sh
python automerge.py path/to/your/config.yml
```

For detailed information on creating a YAML configuration for your merge, see [Merge Configuration](#merge-configuration).

## Merge Configuration

AutoMerge uses YAML documents for specifying merge operations. Key elements include:

- `merge_method`: Method used for merging (e.g., `linear`, `slerp`).
- `models`: Defines models for merging.
- `base_model`: Specifies the base model used in some merge methods.
- `parameters`: Holds various parameters such as weights and densities.

For an example configuration and more details, refer to the [`examples/`](examples/) directory.

## Uploading to Hugging Face

After merging, you can share your model on the Hugging Face Hub. AutoMerge generates a basic `README.md` for your model card. Customize it as needed, and upload your model using the `huggingface_hub` library:

```sh
huggingface-cli login
huggingface-cli upload your_hf_username/my-cool-model ./output-model-directory
```

## Contributing

Contributions to AutoMerge are welcome! Please read our [Contributing Guide](CONTRIBUTING.md) for details on how to submit pull requests, report issues, and suggest improvements.

## License

AutoMerge is open-source software licensed under the [Apache2.0](LICENSE).

## Acknowledgements

AutoMerge was built using `mergekit`, developed by [Charles Goddard](https://github.com/cg123) and supported by [arcee.ai](https://www.arcee.ai/). Special thanks to the contributors of `mergekit` and the AI research community for their invaluable work.
