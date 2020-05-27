#Reads input from input_6.txt

from binascii import a2b_base64,b2a_hex,a2b_hex
from curses.ascii import isprint

def score(string):
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
  ans=0

  for c in string.lower():
    if c in freq:
      ans+=freq[c]

  return ans

def dec(inpstr,lddat):
  inpstr=b2a_hex(inpstr)
  csc=0
  css=""
  l=len(inpstr)
  a=int(inpstr,16)
  for i in range(256):
    b=int(("%02x"%i)*l,16)
    c="%X"%(a^b)
    if len(c)%2==1:
      c="0%s"%c
    c=a2b_hex(c)[lddat:]
    c=filter(isprint,c)
    if score(c)>csc:
      css=c
      csk=i
      csc=score(c)
  return (chr(csk),css)

inpstr=""
filename='input_6.txt'
for line in open(filename):
  inpstr+=line.strip()
inpstr=a2b_base64(inpstr)

hdmax=float('inf')
for k in range(2,80):
  hsum=0
  for i in range(len(inpstr)/k-1):
    hd1=inpstr[(i+0)*k:(i+1)*k]
    hd2=inpstr[(i+1)*k:(i+2)*k]
    hdxor=int(b2a_hex(hd1),16)^int(b2a_hex(hd2),16)
    co1=0
    while(hdxor!=0):
      co1+=1
      hdxor&=(hdxor-1)
    hsum+=co1
  havg=(1.0*hsum)/(len(inpstr)/k-1)
  ham=havg/k

  if ham<hdmax:
    hdmax=ham
    kfit=k
k=kfit
dpar=[]
decdat=[]
key=''

for i in range (0,k):
  dpar.append(inpstr[i::k])

for d in dpar:
  lddat=200
  if len(d)<200:
    lddat=len(d)
  decdat.append(dec(d,lddat))

for d in (decdat):
  key+=d[0]
length=len(inpstr)
  
while len(key)!=length:
  for i in range(len(key)):
    if len(key)==length:
      break
    key=key+key[i]
ret=("%x"%(int(b2a_hex(inpstr),16)^int(b2a_hex(key),16)))
ret="0"*(2*length-len(ret))+ret
decdat=a2b_hex(ret)
print decdat.strip()
