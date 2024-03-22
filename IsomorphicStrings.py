def isIsomorphic(s, t):
    '''
    Determines if two strings are isomorphic, meaning that all occurrences of a character
    must be replaced with another character while preserving the order of characters. No two
    characters may map to the same charater, but a character may map to itself.
    '''
        
    s_dic = {}
    t_dic = {}
        
    if len(s) == len(t):
        for i in range(len(s)):
            if s[i] in s_dic and s_dic[s[i]] != t[i]:
                return False
            if t[i] in t_dic and t_dic[t[i]] != s[i]:
                return False
            s_dic[s[i]] = t[i]
            t_dic[t[i]] = s[i]
        return True
    else:
        return False

def main():
    print(isIsomorphic("egg","add"))
    print(isIsomorphic("foo","bar"))
    print(isIsomorphic("paper","title"))

if __name__ == "__main__":
    main()