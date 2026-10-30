from datetime import datetime
import time

try:
    while True:
        print(datetime.now().strftime("%H:%M:%S"), end="\r", flush=True)
        time.sleep(1)
except KeyboardInterrupt:
    print("\nClock stopped.")