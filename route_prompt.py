from routellm.controller import Controller

controller = Controller(
    routers=["mf"],
    strong_model="gpt-4o-mini",
    weak_model="ollama_chat/llama3.1"
)

def route_prompt(prompt: str) -> str:
    response = controller.chat.completions.create(
        model="router-mf-0.11593",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message['content']
