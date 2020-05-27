from random import randint
from Crypto.Cipher import AES
from binascii import a2b_base64
import urllib

def unpad(pd):
  pl=ord(pd[len(pd)-1])
  for i in range(len(pd)-pl,len(pd)):
    if ord(pd[i])!=pl:
      return pd
  return pd[:-pl]

def enfunc(tecb,key):
  cipher=AES.new(key,AES.MODE_ECB)
  pl=((len(tecb)/16+1)*16)-len(tecb)
  tecb+=chr(pl)*pl
  return cipher.encrypt(tecb)

def defunc(dect,key):
  cipher=AES.new(key, AES.MODE_ECB)
  decr=cipher.decrypt(dect)
  decr=unpad(decr)
  return decr

def parse_string(string):
  return dict(urllib.splitvalue(s) for s in string.split('&'))

#I have taken the parsing function (lines 25 and 26) from an online source as I could not understand how a dictionary works in Python.

def _profile_for(emailid):
  emailid=emailid.replace('&','')
  emailid=emailid.replace('=','')
  return urllib.urlencode([('email',emailid),('uid',10),('role','user')])

key=''
for i in range(0,16):
  key+=chr(randint(0,255))

try1=_profile_for('jigar@iitme')
try2=_profile_for('C@S.jigZadmin')
try3=_profile_for('J@DC.DC')
try4=_profile_for('C@S.jigZ5char')

enc1=enfunc(try1,key)
enc2=enfunc(try2,key)
enc3=enfunc(try3,key)
enc4=enfunc(try4,key)

forge=enc1[0:16]+enc1[16:32]+enc2[16:32]+enc3[32:48]
#By using enc4 inplace of enc2, we can create a profile for any role of 5 characters, just specify it in place of '5char' in try4 and change checking for the role below.
test=defunc(forge,key)

val=(parse_string(test)['role']=='admin')
if val:
  print("Mission Accomplished")
else:
  print("Disavowed")
