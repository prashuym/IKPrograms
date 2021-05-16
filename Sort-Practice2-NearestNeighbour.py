# Complete the 'nearest_neighbours' function below.
# The function accepts integer p_x, p_y, k and a 2D integer array n_points as parameter.
import math
import heapq

def nearest_neighbours2(p_x, p_y, k, n_points):
    if k == 0 : return []
    res = []
    hashDistances = {}
    while n_points :
        ele = n_points.pop()
        x = abs(p_x - ele[0])
        y = abs(p_y - ele[1])
        distance = math.sqrt (x**2 + y**2)
        if distance in hashDistances : hashDistances[distance].append(ele)
        else : hashDistances[distance]= [ele]

    print (hashDistances, sorted(hashDistances.keys()))
    count = 0
    for key in sorted(hashDistances.keys()) :
        values = hashDistances[key]
        count += len(values)
        if count < k : res.extend(values)
        elif count == k : res.extend(values)
        else :
            res.extend(values[0:k-count])
            break

def nearest_neighbours(p_x, p_y, k, n_points):
    if k == 0: return []
    res = []
    while n_points:
        ele = n_points.pop()
        x = abs(p_x - ele[0])
        y = abs(p_y - ele[1])
        distance = -(math.sqrt(x ** 2 + y ** 2))
        if len(res) < k : heapq.heappush(res, (distance, ele))
        elif distance > res[0][0] : heapq.heappushpop(res, (distance, ele))
    for x in range(len(res)):
        res[x] = res[x][1]
    return res


# Write your code here

if __name__ == "__main__" :
    n_points = [[0,0], [1,0]]
    print (nearest_neighbours(1, 1, 1, n_points))