import base64
import string

def woah(s1,s2):
    return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(s1,s2))

re = 'JCspODwqJC4sOgwCSQ4GOiMeBUo+ODodRFoVDRI2FDclXhccQA8XBTJSB0YdWBw='

b = base64.b64decode(re, altchars=None).decode('utf-8')

key = "meownyameownyameownyameownyakiayameownyameownya"

flag = woah(key, b)

print(flag)

