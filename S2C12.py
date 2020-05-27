from binascii import a2b_base64
from random import randint
from Crypto.Cipher import AES

def pkcs_7_unpad(jtxt):
  for i in range(len(jtxt)-ord(jtxt[len(jtxt)-1]),len(jtxt)):
    if ord(jtxt[i])!=ord(jtxt[len(jtxt)-1]):
      return jtxt
  return jtxt[:-ord(jtxt[len(jtxt)-1])]

def encecb(tecb,key):
  cipher=AES.new(key,AES.MODE_ECB)
  pl=((len(tecb)/16+1)*16)-len(tecb)
  tecb+=chr(pl)*pl
  return cipher.encrypt(tecb)

def encryption_oracle(data):
  if not hasattr(encryption_oracle, "key"):
    string=''
    for i in range(0,16):
      string+=chr(randint(0,255))
    encryption_oracle.key=string
  data=data+a2b_base64('Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkg'+'aGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBq'+'dXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUg'+'YnkK')
  return encecb(data,encryption_oracle.key)

def extr(bsize,attpref):
  advpref='J'*((-1-len(attpref))%bsize)
  slicep=len(advpref)+len(attpref)+1
  testex=encryption_oracle(advpref)[:slicep]
  for i in range(0,256):
    atxt=advpref+attpref+chr(i)
    if testex==encryption_oracle(atxt)[:slicep]:
      return chr(i)

inp=''
pl=None
f=0
while f==0:
  enc=encryption_oracle(inp)
  inp+='J'
  l=len(enc)
  if pl!=None and l>pl:
    blsz=l-pl
    f=1
  else:
    pl=l

#print("blsz="+str(blsz))
inp='J'*(3*blsz)
f=0
ciptxt=encryption_oracle(inp)
nob=len(ciptxt)/blsz
for i in range(nob):
  if f==1:
    break
  for j in range(i+1,nob):
    if ciptxt[i*blsz:(i+1)*blsz]==ciptxt[j*blsz:(j+1)*blsz]:
      #print "ECB"
      f=1
      break
if f==0:
  print "Error ECB not found"
gmlen=len(encryption_oracle(''))

msg=''
for i in range(gmlen):
  c=extr(blsz,msg)
  if c==None:
    break
  else:
    msg+=c
print pkcs_7_unpad(msg)
