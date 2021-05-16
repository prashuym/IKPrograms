"""
140. Word Break II
https://leetcode.com/problems/word-break-ii/
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

Note:
The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:
Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]
"""
class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        if not s : return False
        # Conver the wordDict to set
        wordDict = set(wordDict)
        # Create the datastructure
        table = [ [] for _ in range(len(s)+1) ]
        table[0] = [[]]
        #words = []
        for i in range(1, len(table)):
            for j in range(0,i):
                print (i, len(table), len(table[i-j-1]))
                #print (i,j,s[i-j-1:i],len(table[i-j-1]), table)
                if s[i-j-1:i] in wordDict and len(table[i-j-1]) > 0 : 
                    for wlist in table[i-j-1] :
                        table[i].append(wlist + [s[i-j-1:i]])

        #print (table, words)
        return [" ".join(w) for w in table[-1]]

if __name__ == "__main__":
    #s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    s = "aaaaaaa"
    wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
    soln = Solution()
    result = soln.wordBreak(s,wordDict)
    print (f"Result : {result}")