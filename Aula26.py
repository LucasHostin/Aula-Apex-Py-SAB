
from time import sleep

for _ in range(10):  
    for c in range(0,3):
        print("*", end="", flush=True)
        sleep(0.1)
    print()  
    sleep(0.3)