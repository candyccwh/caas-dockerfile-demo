import datetime
import os
import socket
from http.server import BaseHTTPRequestHandler, HTTPServer

# MUST bind 0.0.0.0 — 127.0.0.1 is unreachable through the cluster gateway
# (the hseo-ai-portal incident, see docs/00-HANDOFF gotcha #15).
PORT = int(os.environ.get("PORT", "8080"))


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = (
            "Hello from CaaS dockerfile-demo!\n"
            f"pod:  {socket.gethostname()}\n"
            f"path: {self.path}\n"
            f"time: {datetime.datetime.now(datetime.UTC).isoformat()}\n"
        ).encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, fmt, *args):
        print(f"{self.address_string()} {fmt % args}", flush=True)


if __name__ == "__main__":
    print(f"listening on 0.0.0.0:{PORT}", flush=True)
    HTTPServer(("0.0.0.0", PORT), Handler).serve_forever()
