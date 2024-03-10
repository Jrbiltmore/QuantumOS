from transformers import BertTokenizer, BertForSequenceClassification
from transformers import Trainer, TrainingArguments
import torch
from torch.utils.data import DataLoader, Dataset
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

class SentimentDataset(Dataset):
    def __init__(self, encodings, labels):
        self.encodings = encodings
        self.labels = labels

    def __getitem__(self, idx):
        item = {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}
        item['labels'] = torch.tensor(self.labels[idx])
        return item

    def __len__(self):
        return len(self.labels)

def read_data(file_path):
    df = pd.read_csv(file_path)
    # Assuming the dataframe has 'text' and 'label' columns
    texts = df['text'].tolist()
    labels = df['label'].tolist()
    return texts, labels

def tokenize_data(tokenizer, texts, labels):
    encodings = tokenizer(texts, truncation=True, padding=True, max_length=128)
    dataset = SentimentDataset(encodings, labels)
    return dataset

def compute_metrics(pred):
    labels = pred.label_ids
    preds = pred.predictions.argmax(-1)
    acc = accuracy_score(labels, preds)
    return {'accuracy': acc}

def main():
    data_path = 'path/to/your/dataset.csv'
    model_name = 'bert-base-uncased'
    
    texts, labels = read_data(data_path)
    tokenizer = BertTokenizer.from_pretrained(model_name)
    dataset = tokenize_data(tokenizer, texts, labels)

    train_dataset, eval_dataset = train_test_split(dataset, test_size=0.1)

    model = BertForSequenceClassification.from_pretrained(model_name, num_labels=2)

    training_args = TrainingArguments(
        output_dir='./results',
        num_train_epochs=3,
        per_device_train_batch_size=16,
        per_device_eval_batch_size=64,
        warmup_steps=500,
        weight_decay=0.01,
        evaluate_during_training=True,
        logging_dir='./logs',
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=eval_dataset,
        compute_metrics=compute_metrics,
    )

    trainer.train()

if __name__ == '__main__':
    main()
