"""
https://oj.interviewkickstart.com/view_test_problem/16068/84/
Palindromic Decomposition Of A String

Find all palindromic decompositions of a given string s.
A palindromic decomposition of string is a decomposition of the string into substrings, such that all those substrings are valid palindromes.

Example
Input: "abracadabra"
Output: [ "a|b|r|a|c|a|d|a|b|r|a", "a|b|r|a|c|ada|b|r|a", "a|b|r|aca|d|a|b|r|a" ]

Notes
Input Parameters: There is only one argument: string s.

Output: Return array of string res, containing ALL possible palindromic decompositions of given string. To separate substrings in the decomposed string, use '|' as a separator between them.
You need not to worry about the order of strings in your output array. Like for s = "aa", arrays ["a|a", "aa"] and ["aa", "a|a"] both will be accepted.
In any string in your returned array res, order of characters should remain the same as in the given string. (i.e. for s = "ab" you should return ["a|b"] and not ["b|a"].)
Any string in the returned array should not contain any spaces. e.g. s = "ab" then ["a|b"] is expected, ["a |b"] or ["a| b"] or ["a | b"] will give the wrong answer.

Constraints:
1 <= |s| <= 20
s only contains lowercase letters ('a' - 'z').
Any string is its own substring.
"""
def isPalin(slist):
    if len(slist) == 0 : return False
    left = 0
    right = len(slist) - 1
    while left < right :
        if slist[left] != slist[right] :
            return False
        left +=1
        right -= 1

    return True

def generate_palindromic_decompositions(s):
    if len (s) < 2 : return [s]
    slate = []
    res = []
    memo = {}
    def getPalinhelper (idx, slate):
        # print (idx, slate, len(s))
        # Base case
        if idx == len(s):
            res.append("|".join(slate))
            return

        # Recurssion condition
        # Include case
        for i in range(idx, len(s)):
            cur = s[idx:i+1]
            if memo.get(cur, None) == None :
                memo[cur] = isPalin(cur)
            if memo[cur] == True:
                memo[cur] = 1
                slate.append(cur)
                getPalinhelper(i+1, slate)
                slate.pop()

        #getPalinhelper(idx+1, slate)
    getPalinhelper(0, slate)
    return res


if __name__ == "__main__" :
    s = "abraacaadabra"
    print ("Result : ", generate_palindromic_decompositions(s))
