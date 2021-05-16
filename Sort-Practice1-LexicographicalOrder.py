#
# Complete the solve function below.
#
def solve(arr):
    #
    # Write your code here.
    #
    res = {}
    for pair in arr :
        key, newName = pair.split(" ")
        if key in res :
            res[key][1].append(newName)
            res[key][0] += 1
        else : res[key] = [1, [newName]]

    for key, value in res.items() : res[key] = "%s:%s,%s" % (key, value[0], max(value[1]))
    return list(res.values())


if __name__ == "__main__" :
    arr = ["key1 hzbcd", "key2 zzz", "key1 hello",  "key3 world", "key1 hello"]
    print (solve(arr))