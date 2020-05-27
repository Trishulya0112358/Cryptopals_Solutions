x='YELLOW SUBMARINE'
y='YELLOW SUBMARINE\x04\x04\x04\x04'
ap=20-(len(x)%20)
x+=chr(ap)*ap
print(x)
print(y)
if x!=y:
  print("Gadbad")
else:
  print("Done")
