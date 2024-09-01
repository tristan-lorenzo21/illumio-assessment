import random
from flow_log_parser import get_protocol_map

# dstport,protocol,tag

protocol_map = get_protocol_map('input_files/protocols.txt')

def generate_random_lookup_table():
    # Define ranges for random values
    tags = ['SV_1', 'SV_2', 'SV_3', 'SV_4', 'SV_5']

    dst_port = random.randint(1, 5)
    protocol = random.choice(list(protocol_map.values())) 
    tag = random.choice(tags)

    # Create the log entry
    log_entry = f"{dst_port},{protocol},{tag}"
    
    return log_entry

def print_logs(lines):
    with open('input_files/sample_lookup_table.txt', 'w') as file:
        file.write('dstport,protocol,tag' + '\n')
        for _ in range(lines):
            file.write(generate_random_lookup_table() + '\n')

print_logs(15000)