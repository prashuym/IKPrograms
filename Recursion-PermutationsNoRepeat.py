# Permutations
def permutations(arr):
    res = []

    def permHelper(ptr, slate):
        # Base condition
        if ptr == len(arr):
            # print (arr, slate)
            res.append(slate[:])
            return

        # Parent condition
        for i in range(len(arr[ptr:])):
            # Swapping the element.
            arr[ptr], arr[ptr + i] = arr[ptr + i], arr[ptr]
            slate.append(arr[ptr])
            permHelper(ptr + 1, slate)
            slate.pop()
            arr[ptr + i], arr[ptr] = arr[ptr], arr[ptr + i]

        return

    permHelper(0, [])
    return res


if __name__ == "__main__":
    arr = [1, 2, 3]
    print(permutations(arr))
