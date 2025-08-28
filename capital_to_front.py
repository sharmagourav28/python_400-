mystring = "MkERTnsk"
mycap = ""
for i in mystring:
    if i.isupper():
        mycap += i
for j in mystring:
    if j.islower():
        mycap += j

print(mycap)
