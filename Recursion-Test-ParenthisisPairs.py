def findParenthisisPairs(n):
    res = []
    slate = []
    def parenHelper(countF, countB, slate) :
        print (countF, countB, slate)
        if countF < 0 or countB < 0 or countB < countF: return
        if countF == 0 and countB == 0:
            res.append("".join(slate[:]))
            return

        slate.append("(")
        parenHelper(countF - 1, countB, slate )
        slate.pop()

        slate.append(")")
        parenHelper(countF, countB - 1, slate)
        slate.pop()

    parenHelper (n, n, slate)
    return res

if __name__ == "__main__" :
    n = 3
    print ("Pairs : ", findParenthisisPairs(n))