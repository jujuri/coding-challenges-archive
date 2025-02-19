import sys
input = sys.stdin.readline

n = int(input())
dp = [1] * 10

for i in range(1, n):
    for j in range(1, 10):
        dp[j] += dp[j-1]
        
print(sum(dp)%10007) 

# 0 => 1
# 1 => 2
# 2 => 3
# 3 => 4
# 4 => 5
# 5 => 6
# 6 => 7
# 7 => 8
# 8 => 9
# 9 => 10

# i) n=3

# 0 => 1 (000)
# 1 => 3 ()
# 2 => 6 (002 012 022 112 122 222)
# dp[i] = dp[i] + dp[i-1]