
def substring(s):
    n = len(s)
    s = [x for x in s]
    substring = ""
    list = []

    for i in range(n):
        substring = ""
        for j in range(n - i):
            substring += s[i + j]
            list.append(substring)
    return list

def checkAnagram(s1, s2):

    hash1 = {}
    hash2 = {}
    for i in s1:
        hash1[i] = hash1.get(i, 0) + 1

    for i in s2:
        hash2[i] = hash2.get(i, 0) + 1

    for i in hash1.keys():
        if i in hash2.keys():
            if hash1[i] == hash2[i]:
                continue
            else:
                return False
        else:
            return False
    return True

print(checkAnagram("aab", "baa"))


#the sum of every number consecutively multiplied
l = [1, 2, 3, 4, 5]
f = lambda a, b: a * b
print(list(map(f, l)))
