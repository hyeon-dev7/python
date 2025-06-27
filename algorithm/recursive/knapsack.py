
"""
배낭 문제
  입력 : [물건의 무게 리스트], [각 물건의 가치 리스트], 배낭에 넣을 수 있는 최대 무게
  출력 : 배낭에 넣을 수 있는 물건들 가치의 최대값
  입출력 예시
    item_weight = [6, 4, 3, 5] # capacity 7, 출력 14
    item_val = [13, 8, 6, 12]

    item_weight = [ 2, 3, 5] # capacity 5, 출력 5
    item_val = [3, 2, 4]

    item_weight = [90,4,6,100,101,103] # capacity 304, 출력 304
    item_val = [90,4,6,100,101,103]
"""

def knapsack(weight_val, capacity):
    if capacity <= 0:
        return 0
    best = [0]
    for i, v in enumerate(weight_val):
        if capacity >= v[0] :
            frac = fractional_knapsack(weight_val[i+1:], v[1], capacity-v[0])

            b = v[1]
            if frac > max(best) :
                b += knapsack(weight_val[i+1:], capacity-v[0])
            best.append(b)
    return max(best)


def fractional_knapsack(lst, current_val, capacity):
    for i in lst:
        if capacity == 0:
            break
        if capacity >= i[0] :
            capacity -= i[0]
            current_val += i[1]
        else :
            current_val += i[1]/i[0]*capacity
            capacity = 0
    return current_val


item_weight = [1, 1, 1, 2, 2, 3, 3] # capacity 12, 출력 37
item_val = [7, 4, 5, 6, 5, 5, 9]

weight_val = sorted(zip(item_weight, item_val), key=lambda x: x[1] / x[0], reverse=True)
# print(weight_val)
print(knapsack(weight_val,12))
