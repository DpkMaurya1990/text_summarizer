from textSummarizer.config.configuration import ConfigurationManager
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch
import os


class PredictionPipeline:
    def __init__(self):
        device = "cuda" if torch.cuda.is_available() else "cpu"

        HF_MODEL_NAME = os.getenv("HF_MODEL_NAME", "dpkmaurya2025/text-summarizer")

        self.tokenizer = AutoTokenizer.from_pretrained(HF_MODEL_NAME)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(HF_MODEL_NAME).to(device)
        self.device = device
        
        
        
    def predict(self, text):
        inputs = self.tokenizer(text,
                                return_tensors="pt",
                                truncation=True,
                                padding="max_length",
                                max_length=512
                            )
        inputs = {k: v.to(self.device) for k, v in inputs.items()}                

        with torch.no_grad():
            summary_ids = self.model.generate(
                inputs["input_ids"],
                attention_mask=inputs["attention_mask"],
                length_penalty=0.8,
                num_beams=8,
                max_length=128
            )

        decoded_summary = self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)
             
        return decoded_summary
                