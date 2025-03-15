import threading
from functools import partial
from http.server import HTTPServer, SimpleHTTPRequestHandler

from src.config import CONFIG


class LocalStaticServer:
    """Server for serving static files locally"""

    def __init__(self, port=0):
        self.port = port
        self.server = None
        self._start_server()

    def _start_server(self):
        handler = partial(SimpleHTTPRequestHandler, directory=str(CONFIG.static_dir))
        self.server = HTTPServer(('127.0.0.1', self.port), handler)
        self.port = self.server.server_port

        thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        thread.start()

    def get_url(self, path):
        return f'http://127.0.0.1:{self.port}/{path}'

    def stop(self):
        if self.server:
            self.server.shutdown()
            self.server.server_close()


static_server = LocalStaticServer()
