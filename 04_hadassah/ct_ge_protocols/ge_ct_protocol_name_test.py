from ge_ct_protocol_name import ANATOMY_PATTERN
import unittest
import re

from pathlib import Path

PROTOCOL_NAMES_PATH = Path('protocols_lists') / \
    '2022-04-18- GE. Discovery.EXAM_ALL_protocols_list.csv'


class TestProtocolNames(unittest.TestCase):

    def test_adult_head_1(self):
        str_test = 'ADULT HEAD 1.1 Head (adult) 1.25'
        self.assertTrue(bool(re.match(ANATOMY_PATTERN, str_test)))

    def test_adult_head_2(self):
        str_test = 'ADULT HEAD  1.1 Head (adult) 1.25'
        self.assertTrue(not bool(re.match(ANATOMY_PATTERN, str_test)))

    def test_adult_head_3(self):
        str_test = 'ADULT HEAD 1 .1 Head (adult) 1.25'
        self.assertTrue(not bool(re.match(ANATOMY_PATTERN, str_test)))

    def test_adult_head_4(self):
        str_test = 'ADULT HEAD 1. 1 Head (adult) 1.25'
        self.assertTrue(not bool(re.match(ANATOMY_PATTERN, str_test)))

    def test_adult_head_5(self):
        str_test = ' ADULT HEAD 1.1 Head (adult) 1.25'
        self.assertTrue(not bool(re.match(ANATOMY_PATTERN, str_test)))

    def test_all_protocols_names(self):
        with open(PROTOCOL_NAMES_PATH, 'r') as file:
            lines = file.readlines()

        TEST = []
        for line in lines:
            TEST.append(bool(re.match(ANATOMY_PATTERN, line)))

        self.assertTrue(any(TEST))


if __name__ == '__main':
    unittest.main()
