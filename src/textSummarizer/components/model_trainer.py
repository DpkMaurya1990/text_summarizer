from transformers import TrainingArguments, Trainer, Seq2SeqTrainingArguments, Seq2SeqTrainer
from textSummarizer.config.configuration import ConfigurationManager, ModelTrainingConfig
from transformers import DataCollatorForSeq2Seq
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from datasets import load_dataset, load_from_disk
import torch
from textSummarizer.entity import ModelTrainingConfig
import os

class ModelTrainer:
    def __init__(self, config: ModelTrainingConfig):
        self.config = config
        
    def train(self):
        device = "cuda" if torch.cuda.is_available() else "cpu"
        tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckpt)
        model_pegasus = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckpt).to(device)
        seq2seq_data_collator = DataCollatorForSeq2Seq(tokenizer, model=model_pegasus)
        
        dataset_samsum_pt = load_from_disk(self.config.data_path)
        
        dataset_samsum_pt["train"] = dataset_samsum_pt["train"].select(range(500))
        dataset_samsum_pt["validation"] = dataset_samsum_pt["validation"].select(range(100))

        
        training_args = Seq2SeqTrainingArguments(
            output_dir=self.config.root_dir,
            num_train_epochs=self.config.num_train_epochs,
            warmup_steps=self.config.warmup_steps,
            per_device_train_batch_size=self.config.per_device_train_batch_size,
            weight_decay=self.config.weight_decay,
            logging_steps=self.config.logging_steps,
            eval_strategy=self.config.evaluation_strategy,
            eval_steps=self.config.eval_steps,
            save_steps=self.config.save_steps,
            gradient_accumulation_steps=self.config.gradient_accumulation_steps,
            predict_with_generate=True,
            gradient_checkpointing=True
        )
        
        trainer = Seq2SeqTrainer(
            model=model_pegasus,
            args=training_args,
            processing_class=tokenizer,
            data_collator=seq2seq_data_collator,
            train_dataset=dataset_samsum_pt["train"],
            eval_dataset=dataset_samsum_pt["validation"],
            
        )
        
        trainer.train()    
        
        #Save the trained model
        trainer.save_model(self.config.root_dir)
        tokenizer.save_pretrained(self.config.root_dir)
        #save Tokenizer
        tokenizer.save_pretrained(os.path.join(self.config.root_dir, "Tokenizer"))
        