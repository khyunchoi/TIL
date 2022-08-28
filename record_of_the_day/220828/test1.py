def solution(money, costs):
    answer = 0
    coins = [1, 5, 10, 50, 100, 500]
    change_costs = [0 for _ in range(6)]
    change_costs[0] = costs[0] * 500
    change_costs[1] = costs[1] * 100
    change_costs[2] = costs[2] * 50
    change_costs[3] = costs[3] * 10
    change_costs[4] = costs[4] * 5
    change_costs[5] = costs[5]
    
    while change_costs:
        min_index = change_costs.index(min(change_costs))

        min_coin = coins[min_index]
        coin_count = money // min_coin
        answer += coin_count * costs[min_index]
        money -= coin_count * min_coin

        change_costs = change_costs[:min_index]

    return answer

print(solution(4578, [1, 4, 99, 35, 50, 1000]))
print(solution(1999, [2, 11, 20, 100, 200, 600]))