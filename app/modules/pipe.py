import os

class Pipe:
    _SHUTDOWN_COMMAND = 'sudo shutdown now'

    def __init__(self, pipe_dir: str) -> None:
        self.pipe_dir = pipe_dir
        if not os.path.exists(pipe_dir):
            os.mkfifo(pipe_dir)

    def _write(self, command: str) -> None:
        with open(self.pipe_dir, 'w') as pipe:
            pipe.write(command)
            pipe.flush()

    def shutdown_command(self):
        self._write(self._SHUTDOWN_COMMAND)
