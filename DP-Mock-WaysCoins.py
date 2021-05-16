'''
  Find number of ways to make the amount using the coins provided
Assume that you have infinite coins of each denomination

input: coin_denominations, amount
coin_denonimations = [1,2,5]
amount = 5

output: 4

Possibilities:
1+1+1+1+1
1+1+1+2
1+2+2
5


3:
T(3-1) + T(3-2)
T(2) + T(1). 
1 1, 2 + 1 -- 1 1 1 , 2 1
1 , 2      -- 1 2

T(2) -> T(2-1)+ T(0)

1 1, 2


DP Table : [1, 1, 2, 2, 3, 4]
[1,1,1]
[1,2,2]
3 - 1,1,1 or 2,1 or 3

3 1-1-1, 1-2

i = T(i-5) + T(i-2) + T(i-1)


      1,  2 , 3
    
    1.     2.   3
    
  1 2 3    2 3
'''

def findCoinWays( coin_denominations, amount):
    if amount == 0 : return 0
    DP_table = [0] * (amount+1)
    DP_table[0] = 1
    print (list(range(1,amount+1)))
    for coin in coin_denominations :
        for i in range(1, amount+1) :
            if coin <= i:
                DP_table[i] += DP_table[i-coin]
        print (DP_table[1:])
    return DP_table[-1]

if __name__ == "__main__" :
    coin_denonimations = [1,2,5]
    amount = 15
    print (findCoinWays(coin_denonimations, amount))

# [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
# [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]
# [1, 1, 2, 2, 3, 4, 5, 6, 7, 8, 10]
