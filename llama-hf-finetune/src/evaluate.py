from transformers import Trainer, TrainingArguments, AutoModelForCausalLM, AutoTokenizer
import datasets
import numpy as np
import json

def load_dataset(split):
    dataset = datasets.load_from_disk('data/splits')
    return dataset[split]

def compute_metrics(eval_pred):
    predictions, labels = eval_pred
    predictions = np.argmax(predictions, axis=1)
    accuracy = np.sum(predictions == labels) / len(labels)
    return {'accuracy': accuracy}

def evaluate_model(model_name, split):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)

    eval_dataset = load_dataset(split)

    training_args = TrainingArguments(
        output_dir='./results',
        per_device_eval_batch_size=8,
        do_train=False,
        do_eval=True,
        evaluation_strategy="epoch",
        logging_dir='./logs',
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        eval_dataset=eval_dataset,
        compute_metrics=compute_metrics,
    )

    eval_results = trainer.evaluate()
    
    with open(f'./experiments/evaluation_results_{split}.json', 'w') as f:
        json.dump(eval_results, f)

if __name__ == "__main__":
    model_name = "your_model_name_here"  # Replace with your model name
    evaluate_model(model_name, 'val')  # Evaluate on validation set
    evaluate_model(model_name, 'test')  # Evaluate on test set