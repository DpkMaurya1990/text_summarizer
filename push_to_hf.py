from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

model_path = "artifacts/model_trainer"

print("Loading model from local folder...")
model = AutoModelForSeq2SeqLM.from_pretrained(model_path)
tokenizer = AutoTokenizer.from_pretrained(model_path)

print("Pushing model to HuggingFace Hub...")
model.push_to_hub("dpkmaurya2025/text-summarizer")
tokenizer.push_to_hub("dpkmaurya2025/text-summarizer")

print("Model pushed successfully!")