import re


# list anatomy for adult protocols
ANATOMY_LIST = ['ADULT HEAD', 'ADULT ORBIT', 'ADULT CSPINE', 'ADULT SHOULDER', 'ADULT CHEST',
                'ADULT ABDOMEN', 'ADULT LUMBAR', 'ADULT PELVIS', 'ADULT LOWER EXTREMITY', 'ADULT MISCELLANEOUS']

ANATOMY_PATTERN_LIST = list(
    map(lambda x: x + r'\s\d{1,2}\.\d{1,2}.+', ANATOMY_LIST))

# regex pattern for all adult anatomies
ANATOMY_PATTERN = '|'.join(ANATOMY_PATTERN_LIST)
