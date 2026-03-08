import http.server
import json


PORT = 8000


class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/":
            self._send_text_response(200, "Hello, this is a simple API!")

        elif self.path == "/data":
            data = {"name": "John", "age": 30, "city": "New York"}
            self._send_json_response(200, data)

        elif self.path == "/status":
            self._send_text_response(200, "OK")

        elif self.path == "/info":
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self._send_json_response(200, info)

        else:
            self._send_text_response(404, "Endpoint not found")

    def _send_text_response(self, status_code, message):
        """Helper to send a plain text response."""
        self.send_response(status_code)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(message.encode("utf-8"))

    def _send_json_response(self, status_code, data):
        """Helper to send a JSON response."""
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))

    def log_message(self, format, *args):
        """Override to produce cleaner log output."""
        print(f"[{self.address_string()}] {format % args}")


if __name__ == "__main__":
    server = http.server.HTTPServer(("", PORT), SimpleAPIHandler)
    print(f"Server started on http://localhost:{PORT}")
    print("Available endpoints:")
    print(f"  GET /        -> Plain text greeting")
    print(f"  GET /data    -> JSON dataset")
    print(f"  GET /status  -> API status")
    print(f"  GET /info    -> API info")
    print("Press Ctrl+C to stop the server.\n")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
        server.server_close()
