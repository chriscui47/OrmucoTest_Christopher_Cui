import time
def seconds(seconds):
    start = time.time()
    elapsed = 0
    while elapsed < seconds:
        elapsed = time.time() - start
    if elapsed>seconds:
        print(GREATER)
        return

seconds(5)