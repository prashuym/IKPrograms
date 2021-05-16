'''
https://oj.interviewkickstart.com/view_test_problem/16313/27/
Levenshtein Distance
Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)
You have the following 3 operations permitted on a word:
a) Insert a character
b) Delete a character
c) Replace a character
The minimum number of steps required to convert word1 to word2 with the given set of allowed operations is called edit distance.
e.g. Minimum edit distance between the words 'kitten' and 'sitting', is 3.
kitten → sitten (substitution of "s" for "k")
sitten → sittin (substitution of "i" for "e")
sittin → sitting (insertion of "g" at the end)
Read more about edit distance here: https://en.wikipedia.org/wiki/Edit_distance

Example One
Input: cat, bat
Output: 1
Replace c with b.

Example Two
Input: qwe, q
Output: 2
1: Add w
2: Add e
'''
def  levenshteinDistance(strWord1, strWord2):
    lenStr1 = len(strWord1)
    lenStr2 = len(strWord2)
    # DP table
    table = [ [0] * (lenStr2+1) for _ in range(lenStr1+1) ]
    table[0][0] = 0 
    #print (table, lenStr2)
    for i in range(lenStr1+1) : table[i][0] = i
    for i in range(lenStr2+1) : table[0][i] = i
    for i in range(1, lenStr1+1):
        for j in range(1, lenStr2+1):
            found=1
            if strWord1[i-1] == strWord2[j-1] : found = 0
            table[i][j] = min ( 
                table[i][j-1] + 1,
                table[i-1][j] + 1,
                table[i-1][j-1] + found
             )
    #print (table)
    return table[-1][-1]

if __name__ == "__main__":
    strWord1 = "qwe"
    strWord2 = "q"
    result = levenshteinDistance(strWord1, strWord2)
    print (f"Result : {result}")

