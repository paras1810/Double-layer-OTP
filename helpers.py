import csv
import math
import string
import random

def seive():
    l = []
    for i in range(2,10000):
        flag=0
        for j in range(2,int(math.sqrt(i))):
            if i%j==0 :
                flag=1
                break
        if flag==0:
            l.append(i)
    return l

def genOTP(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

class user():
    name = ""
    password = ""
    id_no = ""
    otp = "0"


def isPrime(n):
    for i in range(2, int(math.sqrt(n))):
        if n%i == 0:
            return False
    return True

def getPrime():
    import random
    p = random.randint(10, 100)
    q = random.randint(100, 10000)
    primes = [i for i in range(p,q) if isPrime(i)]
    n = random.choice(primes)
    return n


def getAppid(client):
    import pandas as pd
    otp = pd.read_csv("otp.csv")
    #print(otp.head())
    l = seive()
    k=0

    for i in range(otp.shape[0]):
        if otp.iloc[i,0]==client:
            value=0
            for j in range(otp.shape[1]):
                s = otp.iloc[i,j]
                st = str(s)
                for k in range(len(st)):
                    value = value + int(k)
                value *= l[k]
                k = k+1
            return str(value)

def hashAppId(otp, value):
    mid = len(value)/2
    return value[:mid] + otp + value[mid:]


def getotpvalue(num,otp):
    print(num)
    print(otp)
    l = len(num)
    ans=""
    ans = num[:l-6]
    return ans,otp


# print(getotpvalue("XYAZAKAJABHVJVH", "AKAJAB"))


# id = getAppid("87:i8:a5:r2:d2:03")

