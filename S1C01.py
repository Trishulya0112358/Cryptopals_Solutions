import binascii
import base64

x='49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
right='SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
decoded=binascii.unhexlify(x)
y=base64.b64encode(decoded).decode('ascii')

print("Given="+y)
print("Expected="+right)


