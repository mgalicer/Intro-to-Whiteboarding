def is_unique(string):
	is_unique = True;

	for c in range(0, len(string)):
		if string[c] in string[c+1:len(string)-1]:
			is_unique = False
			break
	
	return is_unique
