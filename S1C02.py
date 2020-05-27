import binascii
from Crypto.Util.strxor import strxor

S1='1c0111001f010100061a024b53535009181c'
S2='686974207468652062756c6c277320657965'
R1='746865206b696420646f6e277420706c6179'

s1=binascii.unhexlify(S1)
s2=binascii.unhexlify(S2)
r1=binascii.unhexlify(R1)

u=strxor(s1,s2)
print(u)
print(r1)
