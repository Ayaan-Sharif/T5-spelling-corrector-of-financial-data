# Setup Instructions

## Files Needed from Hugging Face

### From Space: https://huggingface.co/spaces/Ayaan-Sharif/T5-spelling-corrector

The following files need to be copied from the Hugging Face Space:

1. **app.py** - Main application file (typically contains Gradio interface)
2. **requirements.txt** - Python dependencies
3. **README.md** - Space documentation (if different from model README)
4. Any additional Python files or configuration files
5. Any example files or assets

To download these files manually:
1. Visit the space URL: https://huggingface.co/spaces/Ayaan-Sharif/T5-spelling-corrector
2. Click on "Files" or "Files and versions" tab
3. Download each file individually
4. Place them in this repository

### From Model: https://huggingface.co/Ayaan-Sharif/t5-spelling-corrector-finetuned-v3

The model card README.md should be incorporated into the main README.md or saved as MODEL_CARD.md

To download:
1. Visit the model URL: https://huggingface.co/Ayaan-Sharif/t5-spelling-corrector-finetuned-v3
2. View the README.md and copy its content
3. Optionally download model configuration files if needed locally

## Alternative Method: Using Git

You can also clone the repositories directly using git:

```bash
# Clone the Space
git clone https://huggingface.co/spaces/Ayaan-Sharif/T5-spelling-corrector space-files

# Clone the Model (for README)
git clone https://huggingface.co/Ayaan-Sharif/t5-spelling-corrector-finetuned-v3 model-files

# Copy files to this repository
cp space-files/* .
cp model-files/README.md MODEL_CARD.md

# Clean up
rm -rf space-files model-files
```

## Network Restriction Note

The current environment cannot access huggingface.co due to network restrictions. The files need to be provided through an alternative method or the domain needs to be whitelisted.
