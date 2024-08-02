prompts = {}

def save_prompt(user_id: str, prompt: str):
    if user_id not in prompts:
        prompts[user_id] = []
    prompts[user_id].append(prompt)

def get_prompts(user_id: str):
    return prompts.get(user_id, [])
