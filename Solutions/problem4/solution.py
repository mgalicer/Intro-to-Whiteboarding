def tr(from, to, str):
	dict = {}
	for c in range(0, len(from)-1:
		dict[from[c]] = to[c]
	for r in range(0, len(str)-1):
		if str[r] in dict.keys:
			str[r] = dict[str[r]]
	return str
