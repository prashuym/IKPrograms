'''
139. Word Break
https://leetcode.com/problems/word-break/
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:
The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.

Example 1:
Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
'''
class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        if not s : return False
        # Conver the wordDict to set
        wordDict = set(wordDict)
        # Create the datastructure
        table = [False] * (len(s)+1)
        #words = []
        for i in range(1, len(table)):
            if s[:i] in wordDict : 
                table[i] = True
                #words.append(s[:i])
                continue
            for j in range(0,i):
                if s[i-j-1:i] in wordDict and table[i-j-1] == True : 
                    #words.append(s[i-j-1:i])
                    table[i] = True
                    continue

        #print (table, words)
        return table[-1]
            

if __name__ == "__main__":
    s = "leetcodeleet"
    wordDict = ["leet", "code", "co"] 
    soln = Solution()
    result = soln.wordBreak(s,wordDict)
    print (f"Result : {result}")