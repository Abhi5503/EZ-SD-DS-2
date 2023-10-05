'''
polynomial complexity[O(n^2)]=space complexity grows prop to the sqr of the i/p size.
'''
def gen_list(n):
    tab_list=[]
    for num in range(n):
        row=[]
        for i in range (n):
            row.append(i)
        tab_list.append(row)
    return tab_list
print(gen_list(10))