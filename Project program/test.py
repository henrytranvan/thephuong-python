import regex

text = input(str(''))
list = regex.findall(r'(?i)\b\p{L}+\b' ,text)
chuyen =  "".join(map(str, list))
print(chuyen)