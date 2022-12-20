def add_binary(a,b):
    bi = []
    c = a+b
    while c != 0:
        rem = c%2
        bi.append(rem)
        c = c//2
    #reversing the list
    l= len(bi)
    for i in range(0,l//2):
        bi[i], bi[l-i-1] = bi[l-i-1], bi[i]
    bi = [str(i) for i in bi] #converting the interger contents of the list into strings
    bi = "".join(bi)
    return bi

print(add_binary(51,12))
