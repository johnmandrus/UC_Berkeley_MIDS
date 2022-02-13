nm = input("What is you name: ")
nm = nm.title()
revnm = ""
i = 0
while i < len(nm):
    revnm = revnm + nm[len(nm)-i-1]
    i += 1
    revnm = revnm.title()
print(revnm)
if nm == revnm:
    print("Palindrome!")