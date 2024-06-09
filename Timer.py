import time


class Timer:
    def __init__(self):
        self.elapsed_time = 0
        self.start_time = None
        self.reset_time = None

    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, type_, value, traceback):
        self.end_time = time.time()
        self.elapsed_time += self.end_time - self.start_time

    def reset(self):
        self.reset_time = time.time()
        self.elapsed_time = 0


# redundant code
    # def elapse(self):  # I named the method the same as the variable
    #     if self.reset_time:
    #         return self.elapsed_time + (time.time() - self.reset_time)
    #     else:
    #         return self.elapsed_time
