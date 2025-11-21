from sklearn.model_selection import ParameterGrid
from transformers import Trainer, TrainingArguments
from llama_wrapper import LlamaModel
import yaml
import json

def load_config(config_path):
    with open(config_path, 'r') as file:
        return yaml.safe_load(file)

def hyperparameter_search(train_dataset, val_dataset, config_path):
    config = load_config(config_path)
    param_grid = ParameterGrid(config['hyperparameters'])

    best_metric = float('-inf')
    best_params = None

    for params in param_grid:
        print(f"Testing parameters: {params}")
        
        training_args = TrainingArguments(
            output_dir='./results',
            evaluation_strategy="epoch",
            learning_rate=params['learning_rate'],
            per_device_train_batch_size=params['batch_size'],
            num_train_epochs=params['epochs'],
            weight_decay=params['weight_decay'],
        )

        model = LlamaModel.from_pretrained(config['model_name'])
        trainer = Trainer(
            model=model,
            args=training_args,
            train_dataset=train_dataset,
            eval_dataset=val_dataset,
        )

        trainer.train()
        metrics = trainer.evaluate()

        if metrics['eval_loss'] < best_metric:
            best_metric = metrics['eval_loss']
            best_params = params

    print(f"Best parameters: {best_params} with loss: {best_metric}")
    return best_params

if __name__ == "__main__":
    # Example usage
    train_dataset = ...  # Load your training dataset here
    val_dataset = ...    # Load your validation dataset here
    config_path = './experiments/hyperparam_search/search_config.yaml'
    
    best_hyperparams = hyperparameter_search(train_dataset, val_dataset, config_path)
    with open('./experiments/hyperparam_search/best_params.json', 'w') as f:
        json.dump(best_hyperparams, f)