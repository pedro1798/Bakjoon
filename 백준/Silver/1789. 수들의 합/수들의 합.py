# S = 200
# 서로다른 자연수의 합 최댓값 N
S = int(input())
sum = 0
tf = True
add = 1
count = 0
while (tf):
    sum += add
    add += 1
    count += 1
    if sum > S:
        count -= 1
        tf = False
print(count)

