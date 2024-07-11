from flask import Flask, request, jsonify
import subprocess
import threading
import logging
import configuration as config

logger = logging.getLogger(__name__)
app = Flask(__name__)

@app.route('/')
def health():
    return "Working!"

def run_ilab_command(endpoint_url, model_family, num_instructions, model):
    from instructlab.sdg.generate_data import generate_data
    from instructlab.sdg.utils import GenerateException

    try:
        print(
            f"Generating synthetic data using '{model}' model, taxonomy:'{config.DEFAULT_TAXONOMY_PATH}' against {endpoint_url} server"
        )
        generate_data(
            logger=logging.getLogger("instructlab.sdg"),  # TODO: remove
            api_base=endpoint_url,
            api_key=config.DEFAULT_API_KEY,
            model_family=model_family,
            model_name=model,
            num_cpus=config.DEFAULT_NUM_CPUS,
            num_instructions_to_generate=num_instructions,
            taxonomy=config.DEFAULT_TAXONOMY_PATH,
            taxonomy_base=config.DEFAULT_TAXONOMY_BASE,
            output_dir=config.DEFAULT_OUT_DIR,
            prompt_file_path=config.DEFAULT_PROMPT_FILE,
            rouge_threshold=0.9,
            console_output=True,
            yaml_rules=None,
            chunk_word_count=config.DEFAULT_CHUNK_WORD_COUNT,
            server_ctx_size=config.MAX_CONTEXT_SIZE,
            tls_insecure=True,
            tls_client_cert="",
            tls_client_key="",
            tls_client_passwd="",
            pipeline="simple",
        )
    except GenerateException as exc:
        print(
            f"Generating dataset failed with the following error: {exc}"
        )


@app.route('/generate', methods=['POST'])
def generate():
    # Check if the request contains JSON
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400
    
    # Parse the JSON payload
    data = request.get_json()
    
    # Extract required fields
    endpoint_url = data.get('endpoint_url')
    model_family = data.get('model_family')
    num_instructions = data.get('num_instructions')
    model = data.get('model')
    
    # Validate the fields
    if not endpoint_url or not model_family or not num_instructions or not model:
        return jsonify({"error": "Missing required fields"}), 400
    
    # Start the command in a new thread
    thread = threading.Thread(target=run_ilab_command, args=(endpoint_url, model_family, num_instructions, model))
    thread.start()
    
    return jsonify({"message": "Started generating SGD data"}), 200

if __name__ == '__main__':
    from waitress import serve;
    print("Server started!")
    serve(app, host="0.0.0.0", port=8080)
