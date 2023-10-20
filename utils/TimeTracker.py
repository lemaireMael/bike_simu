import time


class TimeTracker:

    def __init__(self):
        self._previous_time = time.time()
        self._current_time = time.time()

    @property
    def get_time(self):
        return self._current_time - self._previous_time

    def set_time(self):
        self._current_time = time.time()

    def reset(self):
        self._previous_time = self._current_time
