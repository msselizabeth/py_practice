def isValid(string: str):
    # closing = {"]", ")", "}"}
    # opening = {"[", "(", "{"}
    pairs = {")": "(", "]": "[", "}": "{"}
    checked = []
   
    for char in string:
        if char in pairs: #checks by key
            if checked and checked[-1] == pairs[char]:
                checked.pop()
            else:
                return False
        else:
            checked.append(char)

    return True if not checked else False


s = "([]"
print(isValid(s))

