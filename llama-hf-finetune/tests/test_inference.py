import pytest
from src.inference import run_inference
from src.models.llama_wrapper import LlamaModel

def test_run_inference():
    # Initialize the model
    model = LlamaModel(model_name="llama-base")
    model.load_model()

    # Define a sample prompt
    prompt = "What is the capital of France?"

    # Run inference
    output = run_inference(model, prompt)

    # Check if the output is not empty
    assert output is not None
    assert len(output) > 0

    # Check if the output contains expected information
    assert "Paris" in output  # Assuming the model should return this information

def test_run_inference_with_invalid_prompt():
    model = LlamaModel(model_name="llama-base")
    model.load_model()

    # Define an invalid prompt
    invalid_prompt = ""

    # Run inference
    output = run_inference(model, invalid_prompt)

    # Check if the output is None or an error message
    assert output is None or "error" in output.lower()  # Assuming the model handles errors this way

def test_model_loading():
    model = LlamaModel(model_name="llama-base")
    assert model.load_model() is True  # Ensure the model loads successfully

    # Check if the model is ready for inference
    assert model.is_ready() is True  # Assuming there's a method to check readiness