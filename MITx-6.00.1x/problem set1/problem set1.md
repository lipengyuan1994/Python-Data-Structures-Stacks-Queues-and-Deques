```python


#Problem 2: Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print
#
#Number of times bob occurs is: 2

s = 'azcbobobegghakl'

string = 'bob'
count = 0
index = 0
while index <= (len(s)-3):
	if s[index]+s[index+1]+s[index+2] == string:
		count +=1 
	index += 1

print (count)


#Problem 3: Assume s is a string of lower case characters.
#
#Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print
#
#Longest substring in alphabetical order is: beggh
#In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print
#
#Longest substring in alphabetical order is: abc

s = 'avfxvoffr'
	
answer = ''
swap = ''
list = []


for i in range(len(s)-1):
	answer = s[i]
	for j in range (i +1,len(s)):
		if s[j] >= answer[-1]:
			answer += s[j]
		else:
			break	
	if len(answer) > len(swap) :
		list.append(answer)
		swap = answer
				
print (list[-1])
```