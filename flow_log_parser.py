import csv, os

def ascii_check(filename):
    """
    Checks if the inputted file is in plain-text
    ascii format
    """

    try:
        with open(filename, 'r') as file:
            content = file.read()
            return content.isascii()
    except UnicodeDecodeError:
        return False

def get_parsed_log(input_file):
    """
    Takes the flow log file and returns it as 
    a parseable array.
    """

    parsed_log = []

    try: 
        if ascii_check(input_file) == False:
            return(f'{input_file} is not in plain text ascii format')

        # check if file size is above 10 mb
        file_size = os.path.getsize(input_file)

        size_in_mb = file_size / (1024 * 1024)

        if size_in_mb > 10: 
            return(f'Cannot use flow file because the size is: {size_in_mb:2f} MB, which is greater than 10 MB')

        with open(input_file, 'r') as file:
            for line in file: 
                # check if current log is not empty, if so, process the log
                if line.strip():
                    parsed_line = line.split()

                    protocol_keyword = ''
                    formatted_dstport = int(parsed_line[6])

                    if parsed_line[7] == '6':
                        protocol_keyword = 'tcp'
                    elif parsed_line[7] == '17':
                        protocol_keyword = 'udp'

                    parsed_log.append((formatted_dstport, protocol_keyword))
        
        return parsed_log

    except FileNotFoundError:
        return(f'File {input_file} not found')
    except TypeError as error:
        if "'NoneType' object is not iterable" in str(error):
            return('Cannot iterate through file')
        else:
            return(f'The following error occured: {error}')

def get_lookup_table(lookup_table_file):
    """
    Takes the lookup table file and returns it as 
    a parseable dictionary.
    """

    lookup_table = {}

    try: 
        if ascii_check(lookup_table_file) == False:
            return(f'{lookup_table_file} is not in plain text ascii format')

        with open(lookup_table_file, 'r') as file:
            csv_reader = csv.DictReader(file)

            for row in csv_reader:
                lookup_table[int(row['dstport']), row['protocol'].lower()] = row['tag']

        return lookup_table

    except FileNotFoundError:
        return(f"File {lookup_table_file} not found")

def get_tag_counts(parsed_log, lookup_table):
    """
    Takes the parsed log file and the lookup table file
    and creates a dictionary using the tag as a key
    and the frequency of the tag as a value.
    """

    tag_counts = {'Untagged': 0}

    try:
        for combination in parsed_log:
            if combination in lookup_table:
                
                if lookup_table[combination] in tag_counts:
                    tag_counts[lookup_table[combination]] += 1
                else:
                    tag_counts[lookup_table[combination]] = 1
            else:
                tag_counts['Untagged'] += 1
    except TypeError as error:
        if "'NoneType' object is not iterable" in str(error):
            return("Cannot iterate through the log or lookup table file - get_tag_counts")
        else:
            return(f'The following error occured: {error}')

    return tag_counts

def get_combination_counts(parsed_log):
    """
    Takes the parsed log file and returns an
    array that contains all of the dstport, protocol 
    and tag combinations from the file
    """

    combination_counts = {}
    formatted_combination_counts = []

    for combination in parsed_log:
        if combination in combination_counts:
            combination_counts[combination] += 1
        else:
            combination_counts[combination] = 1

    for (dstport, protocol), tag in combination_counts.items():
        formatted_combination_counts.append([dstport, protocol, tag])

    return formatted_combination_counts

def get_output_file(tag_counts, combination_counts):
    """
    Takes the tag counts and combination counts and
    outputs the results into a txt file.
    """

    if len(tag_counts) <= 1 or combination_counts is None:
        print('The flow log or lookup table file is invalid. Please try again with valid files. - get_output_file')
    else:
        with open('output_files/output.txt', 'w') as file:
            # start outputting tag counts
            file.write('Tag Counts:' + '\n')
            file.write('Tag,Count' + '\n')

            for (tag, count) in tag_counts.items():
                file.write('\n' + tag + ',' + str(count) + '\n')

            # start outputting combination counts
            file.write('\n''Port/Protocol Combination Counts:' + '\n')
            file.write('Port,Protocol,Count' + '\n')

            for combination in combination_counts:
                file.write('\n' + str(combination[0]) + ',' + combination[1] + ',' + str(combination[2]) + '\n')
        
        print("Successfully printed output file.")

# tag_counts = get_tag_counts(get_parsed_log('input_files/ascii.txt'), get_lookup_table('input_files/lookup_table.txt'))
# combination_counts = get_combination_counts(get_parsed_log('input_files/input.txt'))
# get_output_file(tag_counts, combination_counts)