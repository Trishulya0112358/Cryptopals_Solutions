#takes input from input_8.txt

from binascii import a2b_hex
filename='input_8.txt'
for l in open(filename):
  l=l.strip()
  inpstr=a2b_hex(l)
  val=0
  f=0
  nob=len(inpstr)/16
  for i in range(nob):
    if f==1:
      break
    for j in range(i+1,nob):
      if inpstr[i*16:(i+1)*16]==inpstr[j*16:(j+1)*16]:
        val=1
        f=1
        break
  if val==1:
    print("Detected:")
    print(l)
