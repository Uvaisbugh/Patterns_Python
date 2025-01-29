string = "Python is A Progeamming Language "


def lower_upper(s):
	l_dic = {
		"upper": 0,
		"lower": 0
	}

	for letter in string:
		if letter.isupper():
			l_dic["upper"] += 1
		elif letter.islower():
			l_dic["lower"] += 1
	return l_dic


print(lower_upper(string))
# What will be the output of the above code snippet?
