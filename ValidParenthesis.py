def validParentheses(s):
    d = {'}':'{',']':'[',')':'('}
    stack = []

    for c in s:
        if c in d:
            if d[c] != stack.pop():
                return False
        else:
            stack.append(c)
    
    return len(stack) == 0
            

def main():
    print(validParentheses("()"))
    print(validParentheses("()[]{}"))
    print(validParentheses("(]"))

if __name__ == "__main__":
    main()