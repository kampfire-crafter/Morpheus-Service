import os
from dotenv import load_dotenv

from modules.morpheus import Morpheus
from modules.cpu_checker import CPUChecker
from modules.pipe import Pipe

load_dotenv()

if __name__ == "__main__":
    pipe = Pipe(os.getenv('PIPE_DIR'))
    cpu_checker = CPUChecker(int(os.getenv('CPU_THRESHOLD')))
    morpheus = Morpheus(int(os.getenv('CHECK_INTERVAL')), int(os.getenv('INACTIVITY_TIME_THRESHOLD')), cpu_checker, pipe)

    morpheus.run()
