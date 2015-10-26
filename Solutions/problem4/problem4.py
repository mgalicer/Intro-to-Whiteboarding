def tr(tr_from, tr_to, s):
    res = ''
    for i in xrange(len(s)):
        if s[i] in tr_from:
            index = tr_from.index(s[i])
            res.append(tr_to[index])
        else:
            res.append(s[i])
    return res
