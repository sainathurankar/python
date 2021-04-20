s = "ssssaaaiin"
d = {}
for l in s:
    try:
        d[l] += 1
    except KeyError:
        d[l] = 1
print(d)
