def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value


print(repr(to_str(b'hello')))
print(repr(to_str('world')))
print(repr(to_str("한글")))


def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    return value


print(repr(to_bytes(b'hello')))
print(repr(to_bytes('bar')))
print(repr(to_bytes("한글")))
