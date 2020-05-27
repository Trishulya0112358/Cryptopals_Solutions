from random import randint
from Crypto.Cipher import AES
from binascii import a2b_base64
from fractions import gcd

def unpad(planun):
  pl=ord(planun[len(planun)-1])
  for i in range(len(planun)-pl,len(planun)):
    if ord(planun[i])!=pl:
      return planun
  return planun[:-pl]

def enfunc(plaintext,key,iv):
  lf=(len(plaintext)/16+1)*16
  pl=lf-len(plaintext)
  padpltxt=plaintext+chr(pl)*pl
  nob=len(padpltxt)/16
  encdat=''
  pb=iv
  for m in range(nob):
    cb=padpltxt[m*16:(m+1)*16]
    string=''
    for i in range(0,len(cb)):
      string+=(chr(ord(cb[i])^ord(pb[i])))
    enb=AES.new(key,AES.MODE_ECB).encrypt(string)
    encdat+=enb
    pb=enb
  return encdat

def defunc(ciptxt,key,iv):
  nob=len(ciptxt)/16
  decdat=''
  pb=iv
  for b in range(nob):
    cb=ciptxt[b*16:(b+1)*16]
    deb=AES.new(key,AES.MODE_ECB).decrypt(cb)
    string=''
    for i in range(0,len(deb)):
      string+=(chr(ord(deb[i])^ord(pb[i])))

    decdat+=string
    pb=cb
  return unpad(decdat)

def encryption_oracle(ordat):
  ordat=ordat.replace(';','%3b')
  ordat=ordat.replace('=','%3d')
  ordat="comment1=cooking%20MCs;userdata="+ordat+";comment2=%20like%20a%20pound%20of%20bacon"
  return enfunc(ordat,key,IV)

def decryption_oracle(dordat):
  return defunc(dordat,key,IV).count(';admin=true;')

def halxor(A,B):
  if len(A)<len(B):
    return halxor(B,A)
  alen=len(A)
  string=''
  for i in range(0,alen):
    string+=chr(ord(A[i])^ord(B[i]))
  return string

key=''
for i in range(0,16):
  key+=chr(randint(0,255))
IV=''
for i in range(0,16):
  IV+=chr(randint(0,255))
ls=-1
for i in range(256):
  l=len(encryption_oracle('A'*randint(0,256)))
  if ls==-1:
    ls=l
  ls=gcd(l,ls)
r1=encryption_oracle('')
r2=encryption_oracle('A')

for i in range(len(r1)):
  if r1[i]!=r2[i]:
    cbeg=i
    break
igb=cbeg/ls

for count in range(0,2*ls):
  r=encryption_oracle('A'*count+'Y')[igb*ls:]
  s=encryption_oracle('A'*count+'X')[igb*ls:]
  if r[0:ls]==s[0:ls]:
    nbp=count
    break

ts='J'*ls
rs=';admin=true;'
rs+='J'*(ls-len(rs))
enc=encryption_oracle('A'*nbp+'B'*ls+ts)
chb=halxor(halxor(ts,rs),enc[(igb+1)*ls:(igb+2)*ls])
advtxt=enc[:(igb+1)*ls]+chb+enc[(igb+2)*ls:]
co=decryption_oracle(advtxt)

if co>0:
  print("Eureka!")
else:
  print("Error 404 not found")
