from flask import Flask, request, jsonify
from route_prompt import route_prompt
from cache import get_cached_response, cache_response
from user_management import validate_api_key
from prompt_manager import save_prompt, get_prompts

app = Flask(__name__)

@app.route('/route_prompt', methods=['POST'])
def handle_route_prompt():
    api_key = request.headers.get('x-api-key')
    if not validate_api_key(api_key):
        return jsonify({"error": "Invalid API key"}), 401

    data = request.get_json()
    prompt = data['prompt']
    user_id = data.get('user_id', 'default_user')

    save_prompt(user_id, prompt)

    cached_response = get_cached_response(prompt)
    if cached_response:
        return jsonify({'response': cached_response})

    response = route_prompt(prompt)

    cache_response(prompt, response)

    return jsonify({'response': response})

@app.route('/prompts', methods=['GET'])
def get_user_prompts():
    api_key = request.headers.get('x-api-key')
    if not validate_api_key(api_key):
        return jsonify({"error": "Invalid API key"}), 401

    user_id = request.args.get('user_id', 'default_user')
    user_prompts = get_prompts(user_id)
    return jsonify({'prompts': user_prompts})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
