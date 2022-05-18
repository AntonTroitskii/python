import re

pattern = r"spam"

if re.match(pattern, "spamspamspam"):
    print('match')
else:
    print('no match')

if re.match(pattern, "eggspamsausagespam"):
    print('match')
else:
    print('no match')

if re.search(pattern, "eggspamsausagespam"):
    print('match')
else:
    print('no match')

print(re.findall(pattern, 'eggspamsausagespam'))
finder = re.finditer(pattern, 'eggspamsausagespam')
print(type(finder))
for i in finder:
    print(str(i))

pattern = r'pam'

match = re.search(pattern, 'eggspamsausagespam')
if match:
    print(match.group())
    print(match.start())
    print(match.end())
    print(match.span())

str = "My name is David. Hi David"

pattern = r"David"
newstr = re.sub(pattern, "Any", str)
print(newstr)

pattern = r'gr.y'

if re.match(pattern, 'gray'):
    print('match1')
if re.match(pattern, 'grey'):
    print('match2')
if re.match(pattern, 'spam'):
    print('match3')


pattern = r'^gr.y$'

if re.match(pattern, 'gray'):
    print('match1')
if re.match(pattern, 'grey'):
    print('match2')
if re.match(pattern, 'stringray'):
    print('match3')


pattern = r"[aeiou]"
print('pattern = {}'.format(pattern))
if re.search(pattern, 'grey'):
    print('match1')
if re.search(pattern, 'qwertyuiop'):
    print('match2')
if re.search(pattern, 'rhythm myths'):
    print('match3')

pattern = r'[A-Z]'
match1 = 'ZZZZZ'
print('pattern = {}'.format(pattern))
if re.search(pattern, match1):
    print('match1')