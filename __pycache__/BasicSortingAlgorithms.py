'''
Sorting algorithm Templates :
- Selection Sort    - O(n**2)
- Bubble Sort       - O(n**2)
- Insertion Sort    - O(n**2) (Worst Case) & O(n) (Best Case)
    - Recursive
    - Linear
- Merge Sort        - O(n Log n)   Aux Memory space : O(n)
- Quick Sort with 3 partitions - O(n Log n)
'''
import random
class Algorithms :
    __slots__ = ("S")
    def selection_sort (self, S) :
        slen = len (S)
        for i in range(0, slen - 1):
            for j in range(i, slen):
                if S[j] < S[i]: S[i], S[j] = S[j], S[i]
        return S

    def bubble_sort(self, S):
        slen = len(S)
        for i in range(1, slen - 1):
            for j in range(slen-i):
                pos = slen - 1 - j
                if S[pos] < S[pos-1]:
                    S[pos], S[pos-1] = S[pos-1], S[pos]

        return S

    def insertion_sort_recursive(self, S):
        def insertionsort(S, n):
            if n <= 1 : return
            insertionsort(S,n-1)
            ith = S[n-1]
            j=n-2
            while j>=0 and S[j] > ith :
                S[j+1] = S[j]
                j-=1
            S[j+1] = ith

            return
        insertionsort(S, len(S))
        return S

    def insertion_sort_linear(self, S):
        slen = len(S)
        for i in range(1, slen):
            ith = S[i]
            j = i -1
            while j >= 0 and S[j] > ith:
                S[j+1] = S[j]
                j-=1
            S[j+1] = ith

        return S

    def merge_sort(self, S):
        self.S = S
        self.merge_sort_helper(0, len(S)-1)
        return self.S

    def merge_sort_helper(self, start, end):
        # print("Calling merge sort with %s , %s, %s" % (start, end, self.S))
        def merge (start, end):
            sm = []
            mid = int((start+end)/ 2)
            i = start
            j = mid+1
            while i <= mid and j <= end :
                if self.S[i] <= self.S[j] :
                    sm.append(self.S[i])
                    i += 1
                else :
                    sm.append(self.S[j])
                    j += 1
            if i <= mid : sm.extend(self.S[i:mid+1])
            elif j <= end: sm.extend(self.S[j:end+1])
            self.S[start:end+1] = sm
            #print ("Loop %s %s %s" % (start, end, self.S))
            return

        if start >= end : return
        mid = int((start+end)/ 2)
        self.merge_sort_helper(start, mid)    # Left
        self.merge_sort_helper(mid+1, end)   # Right
        merge (start, end)
        return

    def quick_sort(self, S):
        self.S=S
        def quick_sort_recurrsive(start, end):
            #nonlocal x
            #x+=1
            if start >= end : return
            # Find the random pivot value
            pidx = random.randint(start, end)
            # Move the pivot value to the begining of active array
            self.S[start], self.S[pidx] = self.S[pidx], self.S[start]
            # Optimizing by creating middle partition for duplicate values
            pidx = 0

            left = start
            for right in range(start+1, end+1):
                # if value is less that pivot_value then move left pointer and swap value
                if self.S[right] < self.S[start] :
                    left+=1
                    self.S[left], self.S[right] = self.S[right], self.S[left]
                elif self.S[right] == self.S[start] :
                    left += 1
                    pidx += 1
                    #print (left, right, self.S)
                    self.S[left], self.S[right] = self.S[right], self.S[left]
                    self.S[left], self.S[start+pidx] = self.S[start+pidx], self.S[left]

            # Move the pivot element back to the mid b/w left and right
            for i in range(pidx+1):
                self.S[start+i], self.S[left-i] = self.S[left-i], self.S[start+i]
            left = left - pidx
            #print (S, start, end, left, right, pidx)
            quick_sort_recurrsive(start, left)
            quick_sort_recurrsive(left+pidx+1, end)

        quick_sort_recurrsive(0, len(self.S)-1)
        #print("X : ", x)
        return self.S


if __name__ == "__main__":
    alg = Algorithms()
    arr = [6,5,4,3,2,6,1,8,7,0,9,6]
    #arr = 3 * [5,5,5,5,5,5,5,5,5,5,5]
    print(arr)

    print(sorted(arr))
    print("Selection Sort : ", alg.selection_sort(arr[0:]))
    print("Bubble Sort : ", alg.bubble_sort(arr[0:]))
    print("InsertionR Sort : ", alg.insertion_sort_recursive(arr[0:]))
    print("InserationL Sort : ", alg.insertion_sort_linear(arr[0:]))
    print("Merge Sort : ", alg.merge_sort(arr[0:]))
    print("Quick Sort : ", alg.quick_sort(arr[0:]) )



