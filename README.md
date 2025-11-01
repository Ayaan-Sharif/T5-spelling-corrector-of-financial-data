# T5 Spelling Corrector Fine-tuned v3 - Indian Financial Text Domain

## Model Description

This T5-based spelling correction model has been specifically fine-tuned on Indian financial documents containing monetary amounts, numeric text, and financial terminology written in English. The model addresses the critical challenge of correcting OCR errors and phonetic misspellings commonly found in Indian financial documents, invoices, receipts, and banking records.

- **Developed by:** Ayaan-Sharif
- **Model type:** T5ForConditionalGeneration
- **Base model:** T5-base (768 hidden size, 12 layers, 12 heads)
- **Language:** English
- **Domain:** Indian Financial Documents
- **License:** MIT

## Intended Use

The model excels at post-OCR text correction for Indian financial documents, where scanning quality issues create systematic spelling errors in monetary amounts. It's designed to handle:

- **Invoice processing** - Correcting scanned invoice amounts
- **Banking document digitization** - Cleaning up amount fields from cheques, passbooks, statements
- **Accounting system data entry** - Preprocessing before numerical extraction
- **Legal/compliance documents** - Ensuring accurate monetary representation in contracts and agreements

## Usage

### Quick Start

```python
from transformers import T5Tokenizer, T5ForConditionalGeneration

# Load model and tokenizer
model_name = "Ayaan-Sharif/t5-spelling-corrector-finetuned-v3"
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

# Example input (financial amount with OCR errors)
text = "One Hunderd Thousand Rupees"
inputs = tokenizer(text, return_tensors="pt")
outputs = model.generate(**inputs, max_length=50, num_beams=4, early_stopping=True)
corrected = tokenizer.decode(outputs[0], skip_special_tokens=True)
print("Original:", text)
print("Corrected:", corrected)
```

### Sample Output

**Input:** "One Hunderd Thousand Rupees"  
**Output:** "One Hundred Thousand Rupees"

## Limitations

- Specifically trained on Indian financial terminology and monetary amounts; may not perform well on general English text
- Performance depends on the type and severity of OCR/phonetic errors in financial contexts
- May not handle context-dependent corrections outside financial domain
- Not evaluated on non-English languages or non-financial text

## Training Details

- Fine-tuned from T5-base checkpoint
- **Training data:** Over 9,000+ samples of Indian financial documents
- **Covers corrections for:**
  - Crore/Lakh denominations: "krore", "cor e", "laakh", "lkhs" → "Crore", "Lakh"
  - Thousand/Hundred: "thosand", "thousnd", "hundad", "hunderd" → "Thousand", "Hundred"
  - Complex amounts: Ranges from thousands to hundreds of crores
  - Currency terms: "Paise", "Rupees", proper capitalization
  - Contextual markers: Preserves "[invoice no]", "(pvt ltd)", etc.
- **Training progression:** v1 (base), v2 (Lakh/Crore patterns), v3 (comprehensive 9000+ samples)
- Uses SentencePiece tokenizer (spiece.model)
- Generation config: decoder_start_token_id=0, eos_token_id=1, pad_token_id=0

## Requirements

- Python 3.8+
- transformers >= 4.21.0
- torch >= 1.9.0
- safetensors

Install with:
```bash
pip install transformers torch safetensors
```

## Hugging Face Links

- **Model:** https://huggingface.co/Ayaan-Sharif/t5-spelling-corrector-finetuned-v3
- **Space (Demo):** https://huggingface.co/spaces/Ayaan-Sharif/T5-spelling-corrector

## Citation

If you use this model, please cite:

```bibtex
@misc{t5-spelling-corrector-indian-financial-v3,
  title={T5 Spelling Corrector Fine-tuned v3 - Indian Financial Text Domain},
  author={Ayaan-Sharif},
  year={2025},
  publisher={Hugging Face},
  url={https://huggingface.co/Ayaan-Sharif/t5-spelling-corrector-finetuned-v3}
}
```

## Contact

For questions or issues, please open an issue on this repository or contact the maintainer.
