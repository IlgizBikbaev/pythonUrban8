def add_everything_up(a, b):
    try:
        c = round(a + b, 3)
        return c
    except TypeError:
        if isinstance(a,(int, float)) and isinstance(b, str):
            c = str(a) + b
        elif isinstance(b,(int, float)) and isinstance(a, str):
            c = str(b) + a
    return c

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))