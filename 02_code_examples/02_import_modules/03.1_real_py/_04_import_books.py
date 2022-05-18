from importlib import resources

with resources.open_text("_04_books", "alice_in_wonderland.txt") as fid:
    alice = fid.readlines()

print("".join(alice[:7]))
# test print list
print(alice[:7])


with resources.open_binary('_04_books', 'alice_in_wonderland.png') as fid:
    cover = fid.read()

print(cover[:6])

