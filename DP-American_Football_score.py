# American Football score

def scoreWays(score_grid, final_score):
    maxScore = max(score_grid) +1 
    dp = [0] * (maxScore+1)
    dp[0] = 1
    for i in range(1,final_score+1):
        dp[i%maxScore] = 0
        for s in score_grid :
            if i >=s : dp[i%maxScore] += dp[(i-s) % maxScore] 
            print (i,s, dp, maxScore)

    return dp[final_score%maxScore]

if __name__  == "__main__" :
    score_grid = [2,3,6]
    final_score = 9
    result = scoreWays(score_grid, final_score)
    print (f"result : {result}")