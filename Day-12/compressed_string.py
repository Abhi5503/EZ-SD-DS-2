def compressed_string(s):
    if not s:
        return s
    compressed=[]
    curr = s[0]
    count = 1
    for i in range(1,len(s)):
        if s[i]==curr:
            count+=1
        else:
            compressed.append(curr+str(count))
            curr = s[i]
            count = 1
    compressed.append(s[i]+str(count))
    compressed_str=''.join(compressed)
    return compressed_str if len(compressed_str)<len(s) else s
s = input()
res = compressed_string(s)
print(res)