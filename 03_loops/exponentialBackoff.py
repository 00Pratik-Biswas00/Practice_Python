import time

attempts = 0
max_attempts = 4
wait_time = 1

while attempts < max_attempts:
    print("Attempts - ", attempts+1, " - Wait time - ", wait_time)
    time.sleep(wait_time)
    wait_time *= 2
    attempts+=1
    
