a, z = map(ord, 'az')
size = z - a + 1

a_z = ''.join(chr(a+i) for i in range(size))
z_a = ''.join(chr(z-i) for i in range(size))

reverse_lookup = {character: mirror for character, mirror in zip(a_z, z_a)}


def helper(text):
    for character in text:
        if character.islower():
            yield reverse_lookup[character]
        else:
            yield character


def answer(s):
    return ''.join(helper(s))
