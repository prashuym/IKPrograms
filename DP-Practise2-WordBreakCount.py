"""
https://oj.interviewkickstart.com/view_test_problem/16313/211/
Word Break Count
Given a dictionary of words and a string, find the number of ways the string can be broken down into the dictionary words. Return the answer modulo 10^9 + 7.

Example
Input: Dictionary: [“kick", "start", "kickstart", "is", "awe", "some", "awesome”]. 
String: “kickstartisawesome”.
Output: 4
Here are all four ways to break down the string into the dictionary words:
kick start is awe some
kick start is awesome
kickstart is awe some
kickstart is awesome
4 % 1000000007 = 4 so the correct output is 4.

Notes
Input Parameters: Function has two parameters. 1) an array of strings, the dictionary, 2) a string to be broken down in dictionary words.
Output: Return an integer, the number of distinct ways to break down the string into the dictionary words modulo 10^9 + 7.

Constraints:
1 <= number of words in the dictionary <= 200000
1 <= length of any dictionary word <= 100
1 <= length of the string <= 2000
Dictionary words and the string all consist of lowercase latin characters (no whitespace, in particular).
"""

def wordBreakCount(dictionary, txt):
    # Write your code here
    if txt == "" : return 0
    lenTxt = len(txt)+1
    dictionary = set(dictionary)
    # Create DP Table 
    table = [0] * (lenTxt)
    table[0] = 1
    for i in range(1,lenTxt):
        for j in range(0,i):
            if txt[i-j-1:i] in dictionary :
                table[i] += table[i-j-1]
    return table[-1]  % 1000000007

if __name__ == "__main__" :
    dictionary = ["kick", "start", "kickstart", "is", "awe", "some", "awesome" ]
    txt = "kickstartisawesome"
    result = wordBreakCount(dictionary, txt)
    print (f"Result : {result}")

