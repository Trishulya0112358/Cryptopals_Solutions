from curses.ascii import isprint
from binascii import a2b_hex

def txtsc(string):
  freq = dict()
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
  ret=0
  for c in string.lower():
    if c in freq:
      ret+=freq[c]
  return ret

inpstr="1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

csc=0
css=""
l=len(inpstr)
a=int(inpstr,16)
for i in range(0,256):
  b=int(("%02x"%i)*l,16)
  c="%X"%(a^b)
  if len(c)%2==1:
    c="0%s"%c
  c=a2b_hex(c)[34:]
  c=filter(isprint,c)
  if txtsc(c)>csc:
    csc=txtsc(c)
    css=c
print(css)
