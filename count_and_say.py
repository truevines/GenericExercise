'''
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string
'''


def cns(n):
	if (n == 1):
		return '1'
	if (n==2):
		return '11'

	#n=3, 4, 5 . . 

	ret='11'
	for i in range(3,n+1):
		ret=next_term(ret)
	return ret




# next term
def next_term(current_term):
	#current term length > 3
	temp=current_term
	count=1
	prev=temp[0]

	result=''

	for i in range(1, len(current_term)):
		if(prev==temp[i]):
			count+=1
			if i == (len(current_term)-1): #last term
				result=result+str(count)+str(prev)
		else:
			result=result+str(count)+str(prev)
			count=1
			if i == (len(current_term)-1):  #last term
				result=result+str(count)+str(temp[i])
		prev=temp[i]

	return result

