'''
    Given two strings s and t, determine if they are isomorphic.

    Two strings are isomorphic if the characters in s can be replaced to get t.

    All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

    For example,
    Given "egg", "add", return true.

    Given "foo", "bar", return false.

    Given "paper", "title", return true.

    Note:
    You may assume both s and t have the same length.
'''

def isomorph(s, t):

	#boundary case
	if (len(s)!=len(t)):
		return False

	dic={}
	# s as the key; t as the value
	

	i=0
	while (i<len(s)):
	# i-th character:

		#if s is in key, value must match
		if (s[i] in dic) and (dic[s[i]]!=t[i]):
			return False

		#if s is not in key, t must not in value
		if (s[i] not in dic) and (t[i] in iter(dic.values())):
			return False

		#if s is not in key, t not in value -> never appear
		#add relationship 
		if (s[i] not in dic) and (t[i] not in iter(dic.values())):
			dic[s[i]]=t[i]
		
		i+=1

	return True
	




