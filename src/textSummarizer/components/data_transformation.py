import os
from textSummarizer.logging import logger
from transformers import AutoTokenizer
from datasets import load_dataset, load_from_disk
from textSummarizer.entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(config.tokenizer_name)
        
    def convert_example_to_features(self, example_batch):

        inputs = example_batch["dialogue"]
        targets = example_batch["summary"]

        # Ensure all elements are strings
        inputs = [str(x) for x in inputs]
        targets = [str(x) for x in targets]

        model_inputs = self.tokenizer(
            inputs,
            max_length=1024,
            padding="max_length",
            truncation=True
        )

        labels = self.tokenizer(
            targets,
            max_length=128,
            padding="max_length",
            truncation=True
        )

        model_inputs["labels"] = labels["input_ids"]

        return model_inputs

    
    
    def convert(self):
        dataset = load_dataset(
            "csv",
            data_files={
                "train": "artifacts/data_ingestion/samsum-train.csv",
                "test": "artifacts/data_ingestion/samsum-test.csv",
                "validation": "artifacts/data_ingestion/samsum-validation.csv"
            }
        )

        dataset_pt = dataset.map(self.convert_example_to_features, batched=True)

        dataset_pt.save_to_disk(
            os.path.join(self.config.root_dir, "samsum_dataset")
        )