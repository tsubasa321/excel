def recursive_bracket_parser2(s, i, stack):
	#if len(stack) == 0:
	#	return i
	while i < len(s) and len(stack) != 0:
		if s[i] == '(':
			stack.append(s[i])
			i = recursive_bracket_parser2(s, i+1, stack)
			#print i
		elif s[i] == ')':
			stack.pop()
			return i+1
		else:
			# process whatever is at s[i]
			i += 1 
	return i

# Find the right parenthesis to the corresponding left parenthesis in a string, start at index i in the string
def recursive_bracket_parser(s, i):
	stack = []
	result = -1
	while i < len(s):
		if s[i] == '(':
			stack.append(s[i])
			result = recursive_bracket_parser2(s, i+1, stack)
			return result-1
		else:
			i += 1
	return result





# Test for recursive_bracket_parser
## -------------------------------------- ##
str = "(())()"
index = recursive_bracket_parser(str,4)
print index

str = "((()))"
index = recursive_bracket_parser(str,1)
print index
## -------------------------------------- ##

