import unittest
import os
import csv
import textwrap
from flow_log_parser import get_parsed_log, get_lookup_table, get_tag_counts, get_combination_counts, get_output_file

class TestLogProcessing(unittest.TestCase):

    def setUp(self):
        self.flow_log_data = textwrap.dedent("""\
            2 123456789012 eni-0a1b2c3d 10.0.1.201 198.51.100.2 443 49153 6 25 20000 1620140761 1620140821 ACCEPT OK
            2 123456789012 eni-4d3c2b1a 192.168.1.100 203.0.113.101 23 49154 6 15 12000 1620140761 1620140821 REJECT OK
            2 123456789012 eni-5e6f7g8h 192.168.1.101 198.51.100.3 25 49155 6 10 8000 1620140761 1620140821 ACCEPT OK
            2 123456789012 eni-1a2b3c4d 192.168.0.1 203.0.113.12 1024 80 6 10 5000 1620140661 1620140721 ACCEPT OK""")

        self.lookup_table_data = textwrap.dedent("""\
            dstport,protocol,tag
            49153,tcp,sv_P1
            49154,tcp,sv_P2
            49155,tcp,email""")

        with open('test_flow_log.txt', 'w') as f:
            f.write(self.flow_log_data)
        
        with open('test_lookup_table.txt', 'w') as f:
            f.write(self.lookup_table_data)

    def tearDown(self):
        os.remove('test_flow_log.txt')
        os.remove('test_lookup_table.txt')
        if os.path.exists('output.txt'):
            os.remove('output.txt')

    def test_get_parsed_log(self):
        result = get_parsed_log('test_flow_log.txt')
        expected = [
            (49153, 'tcp'), (49154, 'tcp'), (49155, 'tcp'), (80, 'tcp')
        ]
        self.assertEqual(result, expected)

    def test_get_lookup_table(self):
        result = get_lookup_table('test_lookup_table.txt')
        expected = {
            (49153, 'tcp'): 'sv_P1', (49154, 'tcp'): 'sv_P2', (49155, 'tcp'): 'email'
        }
        self.assertCountEqual(result, expected)

    def test_get_tag_counts(self):
        parsed_log = get_parsed_log('test_flow_log.txt')
        lookup_table = get_lookup_table('test_lookup_table.txt')
        result = get_tag_counts(parsed_log, lookup_table)
        expected = {
            'sv_P1': 1, 'sv_P2': 1, 'email': 1, 'Untagged': 1
        }
        self.assertEqual(result, expected)

    def test_get_combination_counts(self):
        parsed_log = get_parsed_log('test_flow_log.txt')
        result = get_combination_counts(parsed_log)
        expected = [
            [49153, 'tcp', 1], [49154, 'tcp', 1], [49155, 'tcp', 1], [80, 'tcp', 1]
        ]
        self.assertEqual(result, expected)

    def test_invalid_log_file(self):
        result = get_parsed_log('input_files/test_txt_file.txt')

        expected = 'Cannot use flow file because the size is: 11.000000 MB, which is greater than 10 MB'

        self.assertEqual(result, expected)

    def test_missing_log_file(self):
        result = get_parsed_log('missing.txt')

        expected = 'File missing.txt not found'

        self.assertEqual(result, expected)

    def test_missing_lookup_table_file(self):
        result = get_lookup_table('missing.txt')

        expected = 'File missing.txt not found'

        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
