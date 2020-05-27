from binascii import b2a_hex, a2b_hex

key=b2a_hex("ICE")
inpstr="Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal"
text=inpstr.rstrip()
key=a2b_hex(key)
l=len(text)
  
while len(key)!=l:
  for i in range(0,len(key)):
    if len(key)==l:
      break
    key+=key[i]
ans=("%x"%(int(b2a_hex(text),16)^int(b2a_hex(key),16)))
ans="0"*(2*l-len(ans))+ans
print("Encrypted:")
print(ans)
