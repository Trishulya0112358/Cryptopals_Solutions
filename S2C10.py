
## Takes input from "S2C10.txt" and decrypts given ciphertext using secretkey "YELLOW SUBMARINE"
## Encryption function also written as question mentioned complete implementation, but it doesn't take an input

from Crypto.Cipher import AES
from binascii import a2b_base64
import base64
def pkcs_7_unpad(planun):
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
  return pkcs_7_unpad(decdat)

seck='YELLOW SUBMARINE'
filedec=''
for l in open('S2C10.txt'):
  filedec=filedec+l.strip()

pltxtdec = a2b_base64(filedec)
IV = '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
print defunc(pltxtdec,seck,IV).strip()

