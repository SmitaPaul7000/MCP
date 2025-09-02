import json
from pathlib import Path
from typing import Dict

MEMORY_FILE = Path("memory.json")

def load_memory() -> Dict:
    if MEMORY_FILE.exists():
        return json.loads(MEMORY_FILE.read_text())
    return {}

def save_memory(data: Dict):
    MEMORY_FILE.write_text(json.dumps(data, indent=2))

def update_memory(agent: str, new_data: str):
    memory = load_memory()
    memory[agent] = new_data
    save_memory(memory)

def get_last(agent: str) -> str:
    return load_memory().get(agent, "")