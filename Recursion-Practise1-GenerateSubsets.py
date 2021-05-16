"""
https://oj.interviewkickstart.com/view_test_problem/16068/85/
Generate All Subsets Of A Set
Generate ALL possible subsets of a given set. The set is givet in the form of a string s containing distinct lowercase characters 'a' - 'z'.

Example
Input: "xy"
Output: ["", "x", "y", "xy"]

Notes
Input Parameters: There is only one argument denoting string s.
Output: Return array of strings res, containing ALL possible subsets of given string. You need not to worry about order of strings in your output array. E.g. s = "a", arrays ["", "a"] and ["a", ""]  both will be accepted.
Order of characters in any subset must be same as in the input string. For s = "xy", array ["", "x", "y", "xy"] will be accepted, but ["", "x", "y", "yx"] will not be accepted.

Constraints:
0 <= |s| <= 20
s only contains distinct lowercase alphabetical letters ('a' - 'z').
Empty set is a subset of any set.
Any set is a subset of itself.
"""
# Complete the function below.

def generate_all_subsets(string):
    res = []
    slate = []
    def genSubsetHelper(idx, slate):
        #print (s, idx, slate)
        # Base case
        if idx == len(s):
            return ["".join(slate)]

        # Recurssive case
        x = genSubsetHelper(idx+1, slate)
        slate.append(s[idx])
        y = genSubsetHelper(idx+1, slate)
        slate.pop()
        return x+y

    return genSubsetHelper(0, slate)

if __name__ == "__main__":
    s = "xyzre"
    print ("Result : ", generate_all_subsets(s))