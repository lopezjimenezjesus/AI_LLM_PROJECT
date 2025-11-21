def fine_tune_model(model, train_dataset, val_dataset, hyperparameters):
    # Set up the training arguments
    training_args = TrainingArguments(
        output_dir='./results',
        evaluation_strategy='epoch',
        learning_rate=hyperparameters['learning_rate'],
        per_device_train_batch_size=hyperparameters['batch_size'],
        num_train_epochs=hyperparameters['epochs'],
        weight_decay=hyperparameters['weight_decay'],
        logging_dir='./logs',
        logging_steps=10,
    )

    # Initialize the Trainer
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=val_dataset,
        compute_metrics=compute_metrics,
    )

    # Start training
    trainer.train()

    # Save the model
    trainer.save_model()

def compute_metrics(eval_pred):
    predictions, labels = eval_pred
    predictions = np.argmax(predictions, axis=1)
    accuracy = accuracy_score(labels, predictions)
    return {'accuracy': accuracy}

def load_data(data_path):
    # Load and preprocess the dataset
    dataset = load_dataset('json', data_files=data_path)
    return dataset

if __name__ == "__main__":
    # Load the pre-trained model
    model = LlamaModel.from_pretrained('path/to/pretrained/model')

    # Load the datasets
    train_dataset = load_data('data/splits/train.jsonl')
    val_dataset = load_data('data/splits/val.jsonl')

    # Define hyperparameters
    hyperparameters = {
        'learning_rate': 5e-5,
        'batch_size': 16,
        'epochs': 3,
        'weight_decay': 0.01,
    }

    # Fine-tune the model
    fine_tune_model(model, train_dataset, val_dataset, hyperparameters)