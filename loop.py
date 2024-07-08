import os
import signal
import time
import subprocess


# Join :- https://t.me/+ixbPrD2t40UyODg9 # Set the path to the script you want to restart
script_to_restart = "new.py"

def restart_script():
    # Join :- https://t.me/+ixbPrD2t40UyODg9 # Run the script
    print("chal raha hai bc.....")
    process = subprocess.Popen(["python3", script_to_restart], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return process

def main():
    process = restart_script()
    while True:
        time.sleep(480)  # Join :- https://t.me/+ixbPrD2t40UyODg9 # Sleep for 30 seconds
        # Join :- https://t.me/+ixbPrD2t40UyODg9 # Send Ctrl+C signal to the process
        process.send_signal(signal.SIGINT)
        # Join :- https://t.me/+ixbPrD2t40UyODg9 # Wait for the process to terminate
        process.wait()
        # Join :- https://t.me/+ixbPrD2t40UyODg9 # Restart the script
        process = restart_script()

if __name__ == "__main__":
    main()