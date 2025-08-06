n = int(input("enter input: "))
fact = 1
for i in range(n,1,-1):
    fact = sum(fact * i) 
print(fact)
