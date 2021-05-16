'''
https://oj.interviewkickstart.com/view_test_problem/16188/42/
String Transformation Using Given Dictionary Of Words

You are given a dictionary of words and two strings, start and stop. All given strings have equal length.
Transform string start to string stop one character per step using words from the dictionary. For example, "abc" -> "abd" is a valid transformation step because only one character is changed (c->d) while "abc" -> "axy" is not a valid step transformation because two characters are changed (c->x and c->y).
You need to find the shortest possible sequence of strings (two or more) such that:

First string is start.
Last string is stop.
Every string (except the first one) differs from the previous one by exactly one character.
Every string (except, possibly, first and last ones) are in the dictionary of words.
i.e. output = [start, <strings from the given dictionary>, stop] and len(output) >= 2.

If two or more such sequences exist, any one of them is a correct answer.
If no such sequence is there to be found, [“-1”] (a sequence of one string, “-1”) is the correct answer.

Example One
Input:
words = ["cat", "hat", "bad", "had"]
start = "bat"
stop = "had"
Output:
["bat", "bad", "had"]
or 
["bat", "hat", "had"]
'''
from collections import defaultdict, deque
import string

def getMyNeighbour(w, words) :
    #print ("Nodes : ", w)
    adjList = []
    if len(words) > 26 :
        for i in string.ascii_lowercase :
            for pos in range(len(w)):
                possible_word = w[:pos] + i + w[pos+1:]
                if possible_word in words : adjList.append(possible_word)        
    else : 
        for compareW in words : 
            sdiff = 0
            for i in range(len(w)):
                if w[i] != compareW[i] : sdiff += 1
                if sdiff > 1 : break
            if sdiff == 1 : adjList.append(compareW)
    #print (f"My Neighbour: {w} \n {adjList}")
    return adjList


def bfs (start, words, stop):
    visitedMap = defaultdict(int)
    parent = {start: None}
    q = [start]   
    visitedMap[start] = 1
    while q :
        nextQ = []
        for node in q : 
            #print (f"Node : {node} {len(adjList} {len(visitedMap)}")
            for neighbour in getMyNeighbour(node, words):
                if neighbour == stop : 
                    # Build parent list
                    parent_list = deque([stop])
                    cur = node 
                    while cur :
                        parent_list.appendleft(cur)
                        cur = parent[cur]
                    return parent_list

                if visitedMap[neighbour] == 0 :
                    visitedMap[neighbour] = 1
                    parent[neighbour] = node
                    nextQ.append(neighbour)     
                
        q = nextQ
    return ["-1"]

def string_transformation(words, start, stop):
    if words == [] and start == stop : return ["-1"]
    result = []
    words = set(words)
    words.add(stop)
    # Find path
    return bfs (start, words, stop)


if __name__ == "__main__":
    import input, time
    words = input.words
    words = [ "cccw", 'accc', 'accw' ]
    start = input.start
    stop = input.stop
    start = "cccc"
    stop = "cccc"
    s = time.perf_counter()
    res = string_transformation(words, start, stop)
    elapsed = time.perf_counter() - s

    #res = getMyNeighbour(start, words + [start, stop])
    print (f"Time : {elapsed}, Result : {res}")

