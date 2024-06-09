import time
import Timer


# Testing:
with Timer.Timer() as t:
    time.sleep(1)
print(t.elapsed_time)  # # ER: ~1 second
time.sleep(1)
with t:
    time.sleep(2)
print(t.elapsed_time)  # # ER: ~3 seconds


with Timer.Timer() as t2:
    time.sleep(1)
print(t2.elapsed_time)  # # ER: ~1 second
t2.reset()
with t2:
    time.sleep(2)
print(t2.elapsed_time)  # # ER: ~2 seconds


