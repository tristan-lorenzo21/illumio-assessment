import random
import time

def generate_random_log():
    # Define ranges for random values
    account_id = ''.join([str(random.randint(0, 9)) for _ in range(12)])
    interface_id = f"eni-{''.join(random.choices('abcdef0123456789', k=8))}"
    src_addr = f"10.0.{random.randint(0, 255)}.{random.randint(1, 254)}"
    dst_addr = f"198.51.100.{random.randint(1, 254)}"
    src_port = random.randint(1, 65535)
    dst_port = random.randint(1, 5)
    protocol = random.randint(1, 255) 
    packets = random.randint(1, 1000)
    bytes_transferred = random.randint(1000, 100000)
    start_time = int(time.time()) - random.randint(0, 86400)
    end_time = start_time + random.randint(1, 600)
    action = random.choice(["ACCEPT", "REJECT"])
    log_status = random.choice(["OK", "NODATA", "SKIPDATA"])

    # Create the log entry
    log_entry = f"2 {account_id} {interface_id} {src_addr} {dst_addr} {src_port} {dst_port} {protocol} {packets} {bytes_transferred} {start_time} {end_time} {action} {log_status}"
    
    return log_entry

def print_logs(lines):
    with open('input_files/sample_log.txt', 'w') as file:

        for _ in range(lines):
            file.write(generate_random_log() + '\n')

print_logs(20000)