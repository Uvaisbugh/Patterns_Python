def anagram(str1,str2):
	str1 = str1.replace(" ", "").lower()
	str2 = str2.replace(" ", "").lower()
	return sorted(str1) == sorted(str2)

print(anagram("Lis ten","Si lent"))