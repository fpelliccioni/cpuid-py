# # https://gist.github.com/ianoxley/865912/e10cb707cda6aac9e9a6b61d846381300e91498c

# alphabet = '123456789abcdefghijkmnopqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ'
# base_count = len(alphabet)
		
# def encode(num):
#     encode = ''

#     if (num < 0):
#         return ''

#     while (num >= base_count):	
#         mod = int(num % base_count)
#         print(mod)
#         encode = alphabet[mod] + encode
#         num = num / base_count

#     if (num):
#         encode = alphabet[num] + encode

#     return encode

# def decode(s):
#     decoded = 0
#     multi = 1
#     s = s[::-1]
#     for char in s:
#         decoded += multi * alphabet.index(char)
#         multi = multi * base_count

#     return decoded



from collections import deque
base94 = ''.join(map(chr, range(33,127)))
base58 = '123456789abcdefghijkmnopqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ'

def flex_encode(val, chrset=base58):
    """\
    Returns a value encoded using 'chrset' regardless of length and 
    composition... well, needs 2 printable asccii chars minimum...

    :param val: base-10 integer value to encode as base*
    :param chrset: the characters to use for encoding

    Note: While this could encrypt some value, it is an insecure toy. 

    """
    basect = len(chrset)
    assert basect > 1
    encode = deque()

    while val > 0:
        val, mod = divmod(val, basect)
        encode.appendleft(chrset[mod])

    return ''.join(encode)

def flex_decode(enc, chrset=base58):
    """\
    Returns the 'chrset'-decoded value of 'enc'. Of course this needs to use 
    the exact same charset as when to encoding the value.

    :param enc: base-* encoded value to decode
    :param chrset: the character-set used for original encoding of 'enc' value

    Note: Did you read the 'encode' note above? Splendid, now have 
             some fun... somewhere...

    """
    basect = len(chrset)
    decoded = 0

    for e, c in enumerate(enc[::-1]):
        decoded += ((basect**e) * chrset.index(c))

    return decoded