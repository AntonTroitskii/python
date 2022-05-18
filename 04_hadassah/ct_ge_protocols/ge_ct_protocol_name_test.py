import unittest
import re

from ge_ct_protocol_name import PROTOCOL_NAME_ADULT_HEAD

class TestProtocolNames(unittest.TestCase):
    
    def testAdultHead(self):
        str1 = 'ADULT HEAD 1.1 Head (adult) 1.25'

        self.assertTrue(bool(re.match(str1, PROTOCOL_NAME_ADULT_HEAD)))


if __name__ == '__main':
    unittest.main()