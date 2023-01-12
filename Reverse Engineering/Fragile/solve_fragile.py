a = 'h1_th3r3_1ts_m3'
s = 'ÐdØÓ§åÍaèÒÁ¡'
flag = ''

for i in range(15):
	flag += chr(ord(s[i]) - ord(a[i]))
print(flag)