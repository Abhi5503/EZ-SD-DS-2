def parans(inp):
    arr = []
    open_br = '([{'
    close_br = ')]}'
    br_pairs = {')': '(', ']': '[', '}': '{'}

    for i in inp:
        if i in open_br:
            arr.append(i)
        elif i in close_br:
            if not arr:
                return False  
            if arr[-1] == br_pairs[i]:
                arr.pop()
            else:
                return False  
    return len(arr) == 0  

inp = input()
print(parans(inp))