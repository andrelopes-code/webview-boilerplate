import socket
import subprocess
import sys
import time
import tkinter as tk
from threading import Thread
from tkinter import messagebox

import psutil

from src.config import CONFIG


class StaticServer:
    def start(self, timeout=5):
        thread = Thread(target=self._run_server, daemon=True)
        thread.start()

        self._wait_for_server(timeout)

    def cleanup(self):
        if hasattr(self._run_server, 'process'):
            try:
                parent = psutil.Process(self._run_server.process.pid)
                for child in parent.children(recursive=True):
                    child.terminate()
                parent.terminate()

            except (psutil.NoSuchProcess, ProcessLookupError):
                pass

    def _run_server(self):
        command = [
            'python',
            '-m',
            'http.server',
            str(CONFIG.static_port),
            '-d',
            str(CONFIG.static_dir),
        ]

        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        startupinfo.wShowWindow = subprocess.SW_HIDE

        process = subprocess.Popen(
            command,
            stderr=subprocess.PIPE,
            stdout=subprocess.PIPE,
            startupinfo=startupinfo,
        )

        self._run_server.__dict__['process'] = process

    def _is_server_up(self, port):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                return s.connect_ex(('127.0.0.1', port)) == 0
            except Exception:
                return False

    def _wait_for_server(self, timeout):
        end_time = time.time() + timeout

        while not self._is_server_up(CONFIG.static_port):
            if time.time() > end_time:
                self._show_error_and_exit()

            time.sleep(0.01)

    def _show_error_and_exit(self):
        try:
            root = tk.Tk()
            root.withdraw()
            top = tk.Toplevel()
            top.withdraw()
            top.wm_attributes('-topmost', 1)
            messagebox.showerror(
                f'{CONFIG.title} - Algo deu errado...',
                'Não foi possivel iniciar o servidor de arquivos estáticos, '
                'por favor contate o desenvolvedor.',
                parent=top,
            )

        except Exception:
            raise Exception('Unable to start static file server')

        finally:
            root.destroy()
            self.cleanup()
            sys.exit(1)
