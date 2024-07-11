DEFAULT_API_KEY = "no_api_key"
DEFAULT_CONFIG = "config.yaml"
# TODO: Consolidate --model and --model-path into one --model-path flag since we always need a path now
DEFAULT_MODEL_OLD = "merlinite-7b-lab-Q4_K_M"
DEFAULT_MODEL = "models/merlinite-7b-lab-Q4_K_M.gguf"
DEFAULT_MODEL_PATH = "models/merlinite-7b-lab-Q4_K_M.gguf"
DEFAULT_MODEL_REPO = "instructlab/granite-7b-lab"
DEFAULT_JUDGE_MODEL_MT = "prometheus-eval/prometheus-8x7b-v2.0"
DEFAULT_EVAL_PATH = "eval_data"
DEFAULT_TAXONOMY_REPO = "https://github.com/instructlab/taxonomy.git"
DEFAULT_TAXONOMY_PATH = "taxonomy"
DEFAULT_TAXONOMY_BASE = "origin/main"
MAX_CONTEXT_SIZE = 4096
# TODO: these constants should be removed, they should not leak out
DEFAULT_NUM_CPUS = 10
DEFAULT_CHUNK_WORD_COUNT = 1000
DEFAULT_NUM_INSTRUCTIONS = 20
DEFAULT_PROMPT_FILE = "prompt.txt"
DEFAULT_GENERATED_FILES_OUTPUT_DIR = "generated"
# use spawn start method, fork is not thread-safe
DEFAULT_MULTIPROCESSING_START_METHOD = "spawn"

# When otherwise unknown, ilab uses this as the default family
DEFAULT_MODEL_FAMILY = "merlinite"

# Model families understood by ilab
MODEL_FAMILIES = set(("merlinite", "mixtral"))

# Map model names to their family
MODEL_FAMILY_MAPPINGS = {
    "granite": "merlinite",
}

DEFAULT_CKPT_DIR = "checkpoints"
DEFAULT_OUT_DIR = "train-output"