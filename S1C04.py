from curses.ascii import isprint
from binascii import a2b_hex

##Takes input from S1C04_input.txt
##Frequency dictionary has been taken from an online source

def txtsc(string):
  freq=dict()
  freq['a']=834
  freq['b']=154
  freq['c']=273
  freq['d']=414
  freq['e']=1260
  freq['f']=203
  freq['g']=192
  freq['h']=611
  freq['i']=671
  freq['j']=23
  freq['k']=87
  freq['l']=424
  freq['m']=253
  freq['n']=680
  freq['o']=770
  freq['p']=166
  freq['q']=9
  freq['r']=568
  freq['s']=611
  freq['t']=937
  freq['u']=285
  freq['v']=106
  freq['w']=234
  freq['x']=20
  freq['y']=204
  freq['z']=6
  freq[' ']=2320
  ret = 0
  for c in string.lower():
    if c in freq:
      ret+=freq[c]
  return ret

def decoder(string):
  csc=0
  css=""
  l=len(string)
  a=int(string,16)
  for i in range(0,256):
    b=int(("%02x"%i)*l,16)
    c="%X"%(a^b)
    if len(c)%2==1:
      c="0%s"%c
    c=a2b_hex(c)[31:]
    c=filter(isprint,c)
    if txtsc(c)>csc:
      csc=txtsc(c)
      css=c
  return css

filename="S1C04_input.txt"
csc=0
css=""
for line in open(filename):
  s=decoder(line)
  if txtsc(s)>csc:
    csc=txtsc(s)
    css=s
print(css)
