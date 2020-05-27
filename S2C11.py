from Crypto.Cipher import AES
from binascii import a2b_base64
from random import randint 

def encecb(tecb,key,pad=False):
  cipher=AES.new(key,AES.MODE_ECB)
  if pad:
    pl=((len(tecb)/16+1)*16)-len(tecb)
    tecb+=chr(pl)*pl
  return cipher.encrypt(tecb)

def enccbc(tcbc,key,iv):
  pl=((len(tcbc)/16+1)*16)-len(tcbc)
  tcbc+=chr(pl)*pl
  nob=len(tcbc)/16
  encdat=''
  pb=iv
  for m in range(nob):
    cb=tcbc[m*16:(m+1)*16]
    string=''
    for i in range(0,len(cb)):
      string+=(chr(ord(cb[i])^ord(pb[i])))

    encrbl=encecb(string,key)
    encdat+=encrbl
    pb=encrbl
  return encdat

def encryption_oracle(advtxt):
  global act
  key=''
  for i in range(0,16):
    key+=chr(randint(0,255))
  p1=''
  p2=''

  for i in range(0,randint(5,10)):
    p1+=chr(randint(0,255))
  for i in range(0,randint(5,10)):
    p2+=chr(randint(0,255))
  
  advtxt=p1+advtxt+p2
  EoC=randint(0,1)
  if EoC==0:
    IV=''
    for ivl in range(0,16):
      IV+=chr(randint(0,255))
    act="CBC"
    return enccbc(advtxt,key,IV)
  else:
    act="ECB"
    return encecb(advtxt,key,True)

for i in range(23):
  pltxt='J'*(48)
  ciptxt=encryption_oracle(pltxt)

  nob=len(ciptxt)/16
  f=0
  for i in range(nob):
    for j in range(i+1,nob):
      if ciptxt[i*16:(i+1)*16]==ciptxt[j*16:(j+1)*16]:
        pred="ECB"
        f=1
        break
  if f==0:
    pred="CBC"
  if pred!=act:
    print("Wrong prediction")
  else:
    print("Identified "+act+" correctly")
