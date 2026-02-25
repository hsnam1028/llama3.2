from src.models.loader import load_fp16
from src.benchmarking.benchmark import run_benchmark

prompt = "Explain the trade-offs of INT8 quantization."

model, tokenizer = load_fp16("meta-llama/Llama-3.2-3B")

result = run_benchmark(model, tokenizer, prompt)

print(result)
