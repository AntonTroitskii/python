from ast import arg
from typing import Dict

import re
import sys

args_pattern = re.compile(
    r"""
    ^
    (
        (--(?P<HELP>help).*)|
        ((?:-s|--separator)\s(?P<SEP>.*?)\s)?
        ((?P<OP1>-?\d+))(\s(?P<OP2>-?\d+))?(\s(?P<OP3>-?\d+))?
    )
    $
""",
    re.VERBOSE,
)



def parse(arg_line: str) -> Dict[str, str]:
    args: Dict[str, str] = {}
    if match_object := args_pattern.match(arg_line):
        args = {k: v for k, v in match_object.groupdict().items()
                if v is not None}
    return args

if __name__ == '__main__':
    arg_line = " ".join(sys.argv[1:])

    arg_line1 = '--help'
    arg_line2 = '-s '


    dict1 = parse(arg_line2)
    print(dict1)


