#takes input from input_7.txt

from Crypto.Cipher import AES
from binascii import a2b_base64

key = 'YELLOW SUBMARINE'
data=''
for line in open('input_7.txt'):
  data+=line.strip()
data=a2b_base64(data)
cipher=AES.new(key,AES.MODE_ECB)
print(cipher.decrypt(data))
