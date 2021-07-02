anagram={}
str1=input("Enter first string:")
str2=input("Enter second string:")
if str1==str2 or sorted(str1)!=sorted(str2):
    anagram[(str1,str2)]="not_anagram"
elif sorted(str1)==sorted(str2):
    anagram[(str1, str2)]='is_anagram'
print(anagram)

def is_max(lis):
    return max(lis)

def average(lis):
    return sum(lis)/len(lis)

print("my house is on fire")