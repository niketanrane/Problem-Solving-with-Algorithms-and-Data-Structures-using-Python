__author__ = "niketanrane"

def anagramSolution1(s1,s2):
    '''
        Check off each character from s1 in s2 and mark it as None(visited) in s2. First ocnvert s2 to list for the same.
        :param s1:
        :param s2:
        :return:
    '''
    if len(s1) != len(s2):
        stillOK = False

    alist = list(s2)

    pos1 = 0
    stillOK = True

    while pos1 < len(s1) and stillOK:
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found:
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 = pos2 + 1

        if found:
            alist[pos2] = None
        else:
            stillOK = False

        pos1 = pos1 + 1

    return stillOK

print(anagramSolution1('abcd','dcba'))

def anagramSolution2(s1, s2):
    s1 = list(s1)
    s2 = list(s2)
    s1.sort()
    s2.sort()

    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False

    return True

print(anagramSolution2('abcde','edcba'))

def anagramSolution3(s1, s2):
    #brute force of O(n!) . Generate each possible set of s1 and check s2 is in that or not. Highly inefficient.
    pass


def anagramSolution4(s1, s2):
    arr1 = [0] * 26
    arr2 = [0] * 26

    for ch in s1:
        loc = ord(ch) - ord('a')
        arr1[loc] += 1

    for ch in s2:
        loc = ord(ch) - ord('a')
        arr2[loc] += 1

    for i in range(26):
        if arr1[i] != arr2[i]:
            return False
    return True

print(anagramSolution4('abcde', 'edcba'))
print(anagramSolution4("ada", "dgfd"))