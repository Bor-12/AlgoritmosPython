
#Problema 58
def lengthOfLastWord(s):
    """
           :type s: str
           :rtype: int
    """
    i, longitud = len(s) -1, 0
    while s[i] == ' ':
        i -= 1
    while i >= 0 and s[i] != ' ':
        longitud += 1
        i -= 1
    return longitud
print(lengthOfLastWord("Hello World"))
print(lengthOfLastWord("luffy is still joyboy"))
