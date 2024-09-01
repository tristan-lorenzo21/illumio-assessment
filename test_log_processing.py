import unittest
import os
import textwrap
from flow_log_parser import get_protocol_map, get_parsed_log, get_lookup_table, get_tag_counts, get_combination_counts

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
        result = get_parsed_log('test_flow_log.txt', get_protocol_map('input_files/protocols.txt'))
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
        parsed_log = get_parsed_log('test_flow_log.txt', get_protocol_map('input_files/protocols.txt'))
        lookup_table = get_lookup_table('test_lookup_table.txt')
        result = get_tag_counts(parsed_log, lookup_table)
        expected = {
            'sv_P1': 1, 'sv_P2': 1, 'email': 1, 'Untagged': 1
        }
        self.assertEqual(result, expected)

    def test_get_combination_counts(self):
        parsed_log = get_parsed_log('test_flow_log.txt', get_protocol_map('input_files/protocols.txt'))
        result = get_combination_counts(parsed_log)
        expected = [
            [49153, 'tcp', 1], [49154, 'tcp', 1], [49155, 'tcp', 1], [80, 'tcp', 1]
        ]
        self.assertEqual(result, expected)

    def test_invalid_log_file(self):
        result = get_parsed_log('input_files/test_txt_file.txt', get_protocol_map('input_files/protocols.txt'))

        expected = 'Cannot use flow file because the size is: 11.000000 MB, which is greater than 10 MB'

        self.assertEqual(result, expected)

    def test_missing_log_file(self):
        result = get_parsed_log('missing.txt', get_protocol_map('input_files/protocols.txt'))

        expected = 'File missing.txt not found'

        self.assertEqual(result, expected)

    def test_missing_lookup_table_file(self):
        result = get_lookup_table('missing.txt')

        expected = 'File missing.txt not found'

        self.assertEqual(result, expected)

    def test_ascii_check_log(self):
        result = get_parsed_log('input_files/ascii.txt', get_protocol_map('input_files/protocols.txt'))

        expected = 'input_files/ascii.txt is not in plain text ascii format'

        self.assertEqual(result, expected)

    def test_ascii_check_lookup_table(self):
        result = get_lookup_table('input_files/ascii.txt')

        expected = 'input_files/ascii.txt is not in plain text ascii format'

        self.assertEqual(result, expected)

    def test_protocol_map(self):
        result = get_protocol_map('input_files/protocols.txt')

        expected = {
            0: "hopopt",
            1: "icmp",
            2: "igmp",
            3: "ggp",
            4: "ipv4",
            5: "st",
            6: "tcp",
            7: "cbt",
            8: "egp",
            9: "igp",
            10: "bbn-rcc-mon",
            11: "nvp-ii",
            12: "pup",
            13: "argus (deprecated)",
            14: "emcon",
            15: "xnet",
            16: "chaos",
            17: "udp",
            18: "mux",
            19: "dcn-meas",
            20: "hmp",
            21: "prm",
            22: "xns-idp",
            23: "trunk-1",
            24: "trunk-2",
            25: "leaf-1",
            26: "leaf-2",
            27: "rdp",
            28: "irtp",
            29: "iso-tp4",
            30: "netblt",
            31: "mfe-nsp",
            32: "merit-inp",
            33: "dccp",
            34: "3pc",
            35: "idpr",
            36: "xtp",
            37: "ddp",
            38: "idpr-cmtp",
            39: "tp++",
            40: "il",
            41: "ipv6",
            42: "sdrp",
            43: "ipv6-route",
            44: "ipv6-frag",
            45: "idrp",
            46: "rsvp",
            47: "gre",
            48: "dsr",
            49: "bna",
            50: "esp",
            51: "ah",
            52: "i-nlsp",
            53: "swipe (deprecated)",
            54: "narp",
            55: "min-ipv4",
            56: "tlsp",
            57: "skip",
            58: "ipv6-icmp",
            59: "ipv6-nonxt",
            60: "ipv6-opts",
            61: "anyhostprotocol",
            62: "cftp",
            63: "anylocalnetwork",
            64: "sat-expak",
            65: "kryptolan",
            66: "rvd",
            67: "ippc",
            68: "anydfs",
            69: "sat-mon",
            70: "visa",
            71: "ipcv",
            72: "cpnx",
            73: "cphb",
            74: "wsn",
            75: "pvp",
            76: "br-sat-mon",
            77: "sun-nd",
            78: "wb-mon",
            79: "wb-expak",
            80: "iso-ip",
            81: "vmtp",
            82: "secure-vmtp",
            83: "vines",
            84: "iptm",
            85: "nsfnet-igp",
            86: "dgp",
            87: "tcf",
            88: "eigrp",
            89: "ospfigp",
            90: "sprite-rpc",
            91: "larp",
            92: "mtp",
            93: "ax.25",
            94: "ipip",
            95: "micp (deprecated)",
            96: "scc-sp",
            97: "etherip",
            98: "encap",
            99: "anyprivencscheme",
            100: "gmtp",
            101: "ifmp",
            102: "pnni",
            103: "pim",
            104: "aris",
            105: "scps",
            106: "qnx",
            107: "a/n",
            108: "ipcomp",
            109: "snp",
            110: "compaq-peer",
            111: "ipx-in-ip",
            112: "vrrp",
            113: "pgm",
            114: "any0hopprotocol",
            115: "l2tp",
            116: "ddx",
            117: "iatp",
            118: "stp",
            119: "srp",
            120: "uti",
            121: "smp",
            122: "sm (deprecated)",
            123: "ptp",
            124: "isis over ipv4",
            125: "fire",
            126: "crtp",
            127: "crudp",
            128: "sscopmce",
            129: "iplt",
            130: "sps",
            131: "pipe",
            132: "sctp",
            133: "fc",
            134: "rsvp-e2e-ignore",
            135: "mobility header",
            136: "udplite",
            137: "mpls-in-ip",
            138: "manet",
            139: "hip",
            140: "shim6",
            141: "wesp",
            142: "rohc",
            143: "ethernet",
            144: "aggfrag",
            145: "nsh",
            255: "reserved",
        }

        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
