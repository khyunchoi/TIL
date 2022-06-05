def solution(alp, cop, problems):
    problems = [[0, 0, 1, 0, 1], [0, 0, 0, 1, 1]] + problems
    goal_alp = alp
    goal_cop = cop
    for problem in problems:
        goal_alp = max(goal_alp, problem[0])
        goal_cop = max(goal_cop, problem[1])

    answer = (goal_alp + goal_cop) - (alp + cop)
    answer_list = [answer]


    def dfs(now_alp, now_cop, cost):
        if cost >= answer_list[0]:
            return

        if now_alp >= goal_alp and now_cop >= goal_cop:
            answer_list[0] = min(answer_list[0], cost)
            return

        for problem in problems:
            if now_alp >= problem[0] and now_cop >= problem[1]:
                dfs(now_alp + problem[2], now_cop + problem[3], cost + problem[4])


    dfs(alp, cop, 0)
    
    return answer_list[0]


print(solution(10, 10, [[10,15,2,1,2],[20,20,3,3,4]]))
print(solution(0, 0, [[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]]))