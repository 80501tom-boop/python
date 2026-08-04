print(chr(65))
print(chr(97))
print(chr(48))

print(chr(21488))
print(chr(128522))

alphabet=[chr(i) for i in range(65,91)]
print(alphabet)

char='c'
shift=3

new_char=chr(ord(char)+shift)
print(f"'{char}'向後推3位是:'{new_char}'")