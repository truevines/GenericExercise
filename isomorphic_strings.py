

def isomorph(s, t):

	#boundary case
	if (len(s)!=len(t)):
		return False

	dic={}

	# s as the key; t as the value
	i=0
	while (i<len(s)):
	# i-th character:
		if (s[i] not in dic):
			dic[s[i]]=t[i]

		elif (dic[s[i]]!=t[i]):
				return False

		else: # go on
			i+=1
	return True





