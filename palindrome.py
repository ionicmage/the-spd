theword = str(input("whats your word:"))
print(theword)

ispal = 1

j = len(theword)

letter = theword[0]
lastletter = theword[j-1]
print(letter, lastletter)

for r in range(j):
  print(theword[r], theword[j-1])
  if theword[r] != theword[j-1]:
    print("No palindrome")
  j = j-1
  if ispal == 1:
    print("Palindrome")
  
