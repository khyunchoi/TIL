def solution(dist):
    answer = []
    tmp_answer = []
    tmp_list = []

    def make_list(arr, idx):
        if idx == len(dist):
            tmp_list.append(arr)
            return

        make_list(arr + [dist[0][idx]], idx+1)
        make_list(arr + [-dist[0][idx]], idx+1)

    make_list([0], 1)
    
    for tmp in tmp_list:
        flag = 0
        for i in range(len(dist)):
            for j in range(len(dist)):
                if abs(tmp[i] - tmp[j]) != dist[i][j]:
                    flag = 1
                    break
            if flag:
                break
        else:
            tmp_answer.append(tmp)

    for tmp in tmp_answer:
        tmp_idx_list = []
        for i in range(len(tmp)):
            tmp_idx_list.append([tmp[i], i])
        tmp_idx_list.sort(key=lambda x:x[0])

        answer_list = []
        for tmp_idx in tmp_idx_list:
            answer_list.append(tmp_idx[1])
        answer.append(answer_list)

    answer.sort()
    return answer

print(solution([[0,5,2,4,1],[5,0,3,9,6],[2,3,0,6,3],[4,9,6,0,3],[1,6,3,3,0]]))
print(solution([[0,2,3,1],[2,0,1,1],[3,1,0,2],[1,1,2,0]]))