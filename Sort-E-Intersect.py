#  Variation of merge sort - 2 pointer approach to find the intersection values
def intersect (m, n) :
    i = j = 0
    inter = set()
    len_m = len(m)
    len_n = len(n)
    while (i < len_m) and (j < len_n) :
        if m[i] == n[j]:
            inter.add(m[i])
            i+=1
            j+=1
        elif m[i] > n[j] :
            j+=1
        else :
            i+=1

    return list(inter)

if __name__ == "__main__":
    print (intersect([2,3,4,4,6], [3,4,7]))
