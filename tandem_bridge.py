"""
Antigravity & Ollama Tandem Bridge Utility
Coordinates bidirectional collaboration between Antigravity (cloud/IDE agent)
and local Ollama LLM runtime (antigravity-skills:latest / llama3 / qwen).
"""

import os
import sys
import json
import argparse
import urllib.request
import urllib.error
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

OLLAMA_ENDPOINT = os.environ.get("OLLAMA_HOST", "http://127.0.0.1:11434")
DEFAULT_MODEL = "antigravity-skills:latest"
SCRIPT_DIR = Path(__file__).resolve().parent
PROTOCOL_PATH = SCRIPT_DIR / "OLLAMA_TANDEM_PROTOCOL.txt"


def query_ollama(prompt: str, system: str = "", model: str = DEFAULT_MODEL, temperature: float = 0.3) -> dict:
    """Send prompt to local Ollama runtime and return structured response."""
    url = f"{OLLAMA_ENDPOINT}/api/generate"
    payload = {
        "model": model,
        "prompt": prompt,
        "system": system,
        "temperature": temperature,
        "stream": False
    }
    
    headers = {"Content-Type": "application/json"}
    data = json.dumps(payload).encode("utf-8")
    
    req = urllib.request.Request(url, data=data, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            body = resp.read().decode("utf-8")
            return json.loads(body)
    except urllib.error.URLError as e:
        return {"error": f"Failed to connect to Ollama at {OLLAMA_ENDPOINT}: {e}"}


def activate_tandem(model: str = DEFAULT_MODEL) -> dict:
    """Send OLLAMA_TANDEM_PROTOCOL.txt to Ollama to initialize the tandem co-pilot state."""
    if not PROTOCOL_PATH.exists():
        raise FileNotFoundError(f"Protocol file not found: {PROTOCOL_PATH}")
    
    protocol_text = PROTOCOL_PATH.read_text(encoding="utf-8")
    init_prompt = (
        f"{protocol_text}\n\n"
        "Acknowledge the above operating protocol. Confirm your activation status and summarize your "
        "role as Antigravity's local tandem partner in 2-3 concise sentences."
    )
    
    print(f"🚀 Initializing Tandem Protocol with model '{model}' at {OLLAMA_ENDPOINT}...")
    res = query_ollama(prompt=init_prompt, model=model, temperature=0.1)
    return res


def dispatch_task(task_text: str, context_file: str = None, model: str = DEFAULT_MODEL) -> dict:
    """Dispatch a specific task or code snippet to Ollama for local tandem audit/execution."""
    context_data = ""
    if context_file and os.path.exists(context_file):
        with open(context_file, "r", encoding="utf-8", errors="replace") as f:
            context_data = f"\n\n--- Context File ({os.path.basename(context_file)}) ---\n" + f.read()
    
    prompt = (
        "Operating as Antigravity's local tandem co-pilot under the OLLAMA_TANDEM_PROTOCOL:\n\n"
        f"TASK: {task_text}\n"
        f"{context_data}\n\n"
        "Return your audit, code generation, or review matching the inter-agent JSON format where applicable."
    )
    
    return query_ollama(prompt=prompt, model=model, temperature=0.2)


def main():
    parser = argparse.ArgumentParser(description="Antigravity-Ollama Tandem Bridge")
    parser.add_argument("--init", action="store_true", help="Send the tandem protocol to Ollama to initialize co-pilot mode")
    parser.add_argument("--task", type=str, help="Prompt or task to execute with Ollama in tandem")
    parser.add_argument("--file", type=str, help="Optional path to code/script file to include as context")
    parser.add_argument("--model", type=str, default=DEFAULT_MODEL, help=f"Ollama model to use (default: {DEFAULT_MODEL})")
    
    args = parser.parse_args()
    
    if args.init or (not args.task):
        res = activate_tandem(model=args.model)
        if "error" in res:
            print(f"❌ Error: {res['error']}")
            sys.exit(1)
        print("\n✅ Ollama Tandem Activation Response:")
        print(res.get("response", "").strip())
        print(f"\n[Stats: {res.get('eval_count', 0)} tokens, {round(res.get('total_duration', 0) / 1e9, 2)}s]")
    
    if args.task:
        print(f"\n⚡ Dispatching tandem task to {args.model}...")
        res = dispatch_task(task_text=args.task, context_file=args.file, model=args.model)
        if "error" in res:
            print(f"❌ Error: {res['error']}")
            sys.exit(1)
        print("\n📥 Tandem Partner Output:")
        print(res.get("response", "").strip())


if __name__ == "__main__":
    main()
