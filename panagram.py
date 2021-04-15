#Program to find panagram

import string
def isPanagram(s):

    alphabets=set(string.ascii_lowercase)     # stores all alphabets in the set
    return alphabets<=set(s.lower())           #checks whether length of set is less than or equal to len of alphabet set


s = input("Enter a string : ")

if isPanagram(s):
    print('It is a panagram')
else:
    print('Not a panagram')



#program to find missing charecters

total = 26

def missingChars(Str):
	
	present = [False for i in range(total)]

	for i in range(len(Str)):
		if (Str[i] >= 'a' and Str[i] <= 'z'):
			present[ord(Str[i]) - ord('a')] = True
		elif (Str[i] >= 'A' and Str[i] <= 'Z'):
			present[ord(Str[i]) - ord('A')] = True


	res = ""

	for i in range(total):
		if (present[i] == False):
			res += chr(i + ord('a'))
			
	return res


Str = input("Enter a string : ")

print('required charecters are :' + missingChars(Str))


