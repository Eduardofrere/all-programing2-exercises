import time

def scheduler(seconds):
    start_time = time.time()
    while True:
        elapsed = time.time() - start_time
        yield elapsed
        time.sleep(seconds)
