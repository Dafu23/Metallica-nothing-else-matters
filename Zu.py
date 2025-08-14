import time 
import sys 
import os

lines = [
    "So close, no matter how far",
    "Couldn't be much more from the heart",
    "Forever trusting who we are",
    "And nothing else matters",
    "                        ",
    "Te amo mi amor <3"
]

char_delay = 0.10 
line_dalay = 2

os.system ('cls' if os.name == 'nt' else 'clear')
print ("Nothing Else Matters - Metallica\n--------------------------")
time.sleep(2)

for line in lines:
    for char in line:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(char_delay)
    print()
    time.sleep(line_dalay)