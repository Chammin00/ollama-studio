import http.server
import socketserver
import webbrowser
import os
import subprocess
import time
from pathlib import Path

PORT = 8111
DIRECTORY = Path(__file__).parent.resolve()

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(DIRECTORY), **kwargs)

    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-store, must-revalidate')
        super().end_headers()

def is_ollama_running():
    import urllib.request
    try:
        urllib.request.urlopen("http://127.0.0.1:11434/api/tags", timeout=2)
        return True
    except Exception:
        return False

def ensure_ollama():
    if not is_ollama_running():
        print("Starting Ollama background service...")
        local_app_data = os.environ.get("LOCALAPPDATA", "")
        ollama_bin = Path(local_app_data) / "Programs" / "Ollama" / "ollama.exe"
        if ollama_bin.exists():
            subprocess.Popen([str(ollama_bin), "serve"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            time.sleep(2)
        else:
            subprocess.Popen(["ollama", "serve"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            time.sleep(2)

def main():
    ensure_ollama()
    print(f"Ollama Studio running at http://localhost:{PORT}")
    webbrowser.open(f"http://localhost:{PORT}")
    
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("Serving 1-Click Ollama Web Studio. Press Ctrl+C to stop.")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server.")

if __name__ == "__main__":
    main()
