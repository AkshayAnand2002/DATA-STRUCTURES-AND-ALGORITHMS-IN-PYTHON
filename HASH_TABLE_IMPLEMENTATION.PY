#HASHTABLE IMPLEMENTATION
hashtable=[[],]*10
def checkprime(n):
    if n==1 or n==0:
        return 0
    for i in range(2,n//2):
        if n%i==0:
            return 0
    return 1
def getprime(n):
    if n%2==0:
        n=n+1
    while not checkprime(n):
        n+=2
    return n
def hashfunction(key):
    capacity=getprime(10)
    return key%capacity
def insertdata(key,data):
    index=hashfunction(key)
    hashtable[index]=[key,data]
def removedata(key):
    index=hashfunction(key)
    hashtable[index]=0
insertdata(123, "apple")
insertdata(432, "mango")
insertdata(213, "banana")
insertdata(654, "guava")
print(hashtable)
removedata(123)
print(hashtable)
