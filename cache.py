from functools import lru_cache

cache = {}

def cache_response(prompt: str, response: str):
    cache[prompt] = response

def get_cached_response(prompt: str) -> str:
    return cache.get(prompt, None)
