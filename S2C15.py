def pkcs7(message,block_size):
    if len(message)==block_size:
        return message
    ch=block_size-len(message)%block_size
    return message+chr(ch)*ch

def pkver(s):
    b=s[-1]
    f=1
    for i in range(len(s)-ord(b),len(s)):
      if i>0 and s[i]!=b:
        f=0
        break    
    val=(s[-1:]*ord(s[-1])==s[-ord(s[-1]):])
    return f

m="YELLOW SUBMARINE"
mp=pkcs7(m,20)
m2p="Yellow submarine\x05\x05\x05\x05"
print pkver(mp)
print pkver(m2p)
