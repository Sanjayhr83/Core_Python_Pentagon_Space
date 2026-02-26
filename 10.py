#string(immutable)
w="sita"
print(w)
for i in w:
    #print(i)   #it is print one character in one line
    print(i, end="") #the end is print str in one line

#indexing(starts with 0)
str="abhi"
print(str)
print(len(str)) #len is print the length of the string
print(str[0])
print(str[-1])

#arthmetic operator in string
str1="arjun"
str2="anju"
str3=str1+str2 #the addition in string is concatenate the string
print(str3)

str4=str1*4 #the substitution in string only works with digits
print(str4)

#string interning
str1="Loki"
str2="john"
str3="Loki"
str4="shaky"
str5="loki"
str6="rahul"
print(id(str1))
print(id(str2))
print(id(str3))
print(id(str4))
print(id(str5))
print(id(str6))

#slicing(it is depending on step value
str0="rajarammohanroy"
print(str0[2:8])
print(str0[1:11:2])
print(str0[-3:-12])#no output because
print(str0[-2:-7:-1])
print(str0[-2:-12:-3])
print(str0[-11:12])
print(str0[-13:-2])
print(str0[11:7:1])
print(str0[::])
print(str0[::2])
print(str0[::-4])
print(str0[1:9:-2])
print(str0[5:-2])
print(str0[5:-2])
print(str0[::-1])
#print(str0[1:8:0]) its show error because of step value is zero

#removing spacing
print("STRING REMOVE SPACING")
n=" rahul is drinking "
print(n)    #print actual string
strn=n.lstrip() #lstrip is remove left side space
print(strn)
stnO=n.rstrip() #rstrip is remove right side space
print(stnO)

m="u m a"   #remove all space in string
print(m)
z=""#space is not their
for i in m:
    if i==" ":#space is their
        pass
    else:
        z=z+i
print(z)

#reverse the string
a="raj"
print(a)
b=""
for i in a:
    b=i+b
print(b)

#reverse the sentence(split())
r=input("enter the sentence : ")
rev=""
s=r.split()
for i in s:
    rev=i+" "+rev
print(rev)

t="guru is drinking"
print(str)
s=t.split()
print(s)
for i in reversed(s):
    print(i, end=" ")

a=input("enter a string: ")
for i in  reversed(a.split()):
    print(i,end=" ")

#palindrome
p=input("enter the sentence : ")
rev=""
for i in p:
    rev=i+rev
print(rev)
if p==rev:
    print("palindrome")
else:
    print("not palindrome")

#check it is number or string or others
n=input("enter the string : ")
print(n)
if n.isalpha():
    print("str contains only alphabets")
elif n.isdigit():
    print("str contains only digits")
elif n.isalnum():
    print("str contains only alphanumeric characters")
else:
    print("other characters")

#upper(),lower(),swapcase()
m=input("enter the string : ")
print(m)
m1=m.upper()
print(m1)
m2=m.lower()
print(m2)
m3=m.swapcase()
print(m3)
m4=m.title()
print(m4)
m5=m.replace("S","_")
print(m5)
m6=m.capitalize()
print(m6)

#finding the sub-string from the given string
sb="if you think you can or you can't, you are right"
print(sb)
print(sb.count("you"))
sb1="you"
print(sb1 in sb)
print(sb.index("you"))
print(sb.find("you"))
print(sb.rindex("you"))
print(sb.rfind("you"))
print(sb.find("python"))
#print(sb.index("python")) #it is through error

#packing and unpacking
g="rama"
print(g)
r1,r2,r3,r4=g
print(r1)
print(r2)
print(r3)
print(r4)

#string replace
h='arjun is dancing'
print(h)
h1=h.replace("arjun","nithin")
print(h1.startswith("arjun"))
print(h1.endswith("dancing"))
print(h1.endswith("singing"))

text = input("Enter sentence: ")
vowels = "aeiouAEIOU"
result = ""
for ch in text:
    if ch in vowels:
        result += "*"
    else:
        result += ch
print(result)

#string formating
name=input("enter your name : ")
print("my name is ", name)
print(f"my friend is also {name}")
