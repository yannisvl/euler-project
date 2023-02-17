f = open('./0022/p022_names.txt', 'r')
onomata = []
s = ""
while True:
    c = f.read(1)
    if not c:
      print ("End of file")
      break
    if 64 < ord(c) < 91:
        s = s + c
    elif s!="":
        onomata.append(s)
        s=""

sunolo = len(onomata)
katalogos = sorted(onomata)
print (katalogos)

total = 0
for i in range (sunolo):
    pro = 0
    for char in katalogos[i]:
        pro+= ord(char) - 64
    pro*= i+1
    total+=pro
print(total)
f.close()