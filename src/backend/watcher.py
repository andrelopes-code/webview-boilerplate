import threading

import watchfiles


class Watcher:
    """Class to watch for changes in a directory in a separate thread"""

    def __init__(self):
        self.watch_event = threading.Event()

    def start(self, dir_to_watch, callback):
        watch_thread = threading.Thread(
            target=self._watch_for_changes,
            args=(dir_to_watch, callback),
        )
        watch_thread.daemon = True
        watch_thread.start()

    def cleanup(self):
        self.watch_event.set()

    def _watch_for_changes(self, dir_to_watch, callback):
        for changes in watchfiles.watch(dir_to_watch):
            if self.watch_event.is_set():
                break

            for change in changes:
                print(f'file changed: {change[1]}')
                callback()
