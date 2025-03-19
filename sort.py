b = 0
dosort=1
swapnums = 0
mynums = []
for t in range(5):
  n = int(input("enter a number:"))
  mynums.append(n)
for r in mynums:
  print(r) 

while dosort == 1:
  for b in range(len(mynums)-1):
    doswap = 0
    if mynums[b] > mynums[b+1]:
      temp = mynums[b]
      mynums[b] = mynums[b+1]
      mynums[b+1] = temp
      doswap = 1
if swapnums == 0:
  dosort = 0
  print("sorted")
for r in mynums:
  print(r)
print("done")