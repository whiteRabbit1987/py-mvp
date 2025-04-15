# Simple Countdown Timer
import time

duration_seconds = int(input("Set the countdown duration in seconds: "))

for remaining in range(duration_seconds, 0, -1):
    sec = remaining % 60
    min = int(remaining / 60) % 60
    hr = int(remaining / 3600)
    print(f"{hr:02}:{min:02}:{sec:02}")
    time.sleep(1)

print("Countdown complete!")