# Permutations
def permutations(arr):
    res = []

    def permHelper(ptr, slate):
        # Base condition
        if ptr == len(arr):
            res.append(slate[:])
            return

        # Parent condition
        for i in range(len(arr)):
            slate.append(arr[i])
            permHelper(ptr + 1, slate)
            slate.pop()

        return

    permHelper(0, [])
    return res


if __name__ == "__main__":
    arr = [1, 2, 3]
    print(permutations(arr))
