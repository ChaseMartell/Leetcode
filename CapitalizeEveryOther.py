def capitalizeEveryOther(s):
    
    capitalize = True
    string = ""
    for i in range(len(s)):
        if not s[i].isalnum():
            string += s[i]
        else:
            if capitalize:
                string += s[i].upper()
                capitalize = False
            else:
                string += s[i]
                capitalize = True
    return string

def main():
    print(capitalizeEveryOther("hello world"))

if __name__ == "__main__":
    main()