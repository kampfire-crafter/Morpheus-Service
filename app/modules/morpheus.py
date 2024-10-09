import time 
from modules.cpu_checker import CPUChecker
from modules.pipe import Pipe

class Morpheus:
    def __init__(self, check_interval: int, inactivity_time_threshold: int, cpu_checker: CPUChecker, pipe: Pipe):
        self.cpu_checker = cpu_checker
        self.pipe = pipe
        self.is_running = True
        self.CHECK_INTERVAL = check_interval
        self.INACTIVITY_TIME_THRESHOLD = inactivity_time_threshold

    def run(self):
        inactivity_time = 0

        while self.is_running:
            self._sleep()
            
            cpu_is_working = self.cpu_checker.is_working()

            inactivity_time = self._update_inactivity_time(cpu_is_working, inactivity_time)

            if self._cpu_is_too_long_inactive(inactivity_time):
                self._shutdown()

    def _sleep(self):
        time.sleep(self.CHECK_INTERVAL)

    def _update_inactivity_time(self, cpu_is_working: bool, inactivity_time: int):
        if cpu_is_working:
            return 0
        else:
            return inactivity_time + self.CHECK_INTERVAL

    def _cpu_is_too_long_inactive(self, inactivity_time: int):
        return inactivity_time >= self.INACTIVITY_TIME_THRESHOLD

    def _shutdown(self):
        self.pipe.shutdown_command()
        self.is_running = False
