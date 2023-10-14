def toggle(n,idx):
    return(n ^ (1 << (idx-1)))
n = int(input())
idx = int(input())
print(toggle(n,idx))