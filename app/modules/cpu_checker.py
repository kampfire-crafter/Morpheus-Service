import psutil

class CPUChecker:
    def __init__(self, cpu_threshold: int):
        self.CPU_THRESHOLD = cpu_threshold

    def is_working(self):
        return self._get_cpu_usage() >= self.CPU_THRESHOLD

    def _get_cpu_usage(self):
        return psutil.cpu_percent(interval=None)
