def run_benchmark(model, tokenizer, prompt, max_new_tokens=128):
    from .metrics import bench_stream_generate
    return bench_stream_generate(model, tokenizer, prompt, max_new_tokens)
