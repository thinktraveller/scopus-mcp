import json
import os
from pathlib import Path
from typing import Dict, Any, Optional
from dotenv import load_dotenv

# Load environment variables from .env file if present
load_dotenv()

# Define base paths
BASE_DIR = Path(__file__).resolve().parent.parent.parent
CONFIG_FILE = BASE_DIR / 'config.json'

def load_config_file() -> Dict[str, Any]:
    """Loads the configuration from config.json if it exists."""
    if CONFIG_FILE.exists():
        try:
            with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {}
    return {}

def get_api_key() -> str:
    """
    Retrieves the API key with the following precedence:
    1. Environment variable 'SCOPUS_API_KEY'
    2. config.json 'api_key' field
    """
    # 1. Check Environment Variable
    api_key = os.getenv('SCOPUS_API_KEY')
    if api_key:
        return api_key

    # 2. Check config.json
    config = load_config_file()
    api_key = config.get('api_key')
    
    if not api_key:
        raise ValueError(
            "Scopus API Key not found. Please set the 'SCOPUS_API_KEY' environment variable "
            "or add 'api_key' to config.json."
        )
        
    return api_key
