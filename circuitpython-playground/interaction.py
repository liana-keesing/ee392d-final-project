# Write your code here :-)
# interaction.py

import supervisor
import time

def wait_for_input():
    print("\n" + "-" * 10)
    print("Pick a mode!")
    print("Type here: ")
    while True:
        mode = ""
        if supervisor.runtime.serial_bytes_available:
            mode = input().strip() 
            break
    print("You selected: [" + mode + "]")
    print("-" * 10)
    print("How many samples do you want to collect?")
    print("Type a time in seconds here: ")
    t = 0
    while True:
        t = ""
        if supervisor.runtime.serial_bytes_available:
            t = int(input().strip())
            if t > 0:
                break
            else:
                print("[!] Sorry, that's not a valid number! Please try again.")
                print("Type here: ")
    print("You selected: [" + str(t) + " samples]")
    print("-" * 10)
    print("Capturing data now...")
    time.sleep(2)
    return mode, t
