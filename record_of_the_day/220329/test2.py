def solution(arr, processes):
    answer = []
    tmp_answer = []
    working_list = []
    waiting_list = []
    time = 0
    time_result = 0
    waiting_write_cnt = 0
    working_write_cnt = 0

    while processes or waiting_list or working_list:
        if processes and int(processes[0].split()[1]) <= time:
            process = processes.pop(0)
            process_list = list(process.split())
            waiting_list.append(process_list)
            if process_list[0] == 'write':
                waiting_write_cnt += 1

        if working_list:
            idx_list= []
            for i in range(len(working_list)):
                if working_list[i][1] + int(working_list[i][0][2]) == time:
                    idx_list.append(i)

                    if working_list[i][0][0] == 'write':
                        for j in range(int(working_list[i][0][3]), int(working_list[i][0][4])+1):
                            arr[j] = working_list[i][0][5]
                        working_write_cnt -= 1
                    else:
                        tmp = ''
                        for j in range(int(working_list[i][0][3]), int(working_list[i][0][4])+1):
                            tmp += arr[j]
                        
                        tmp_answer.append((int(working_list[i][0][1]), tmp))
            idx_tmp = 0
            for idx in idx_list:
                working_list.pop(idx-idx_tmp)
                idx_tmp += 1

        if waiting_list:
            if not working_list:
                if waiting_write_cnt:
                    for i in range(len(waiting_list)):
                        if waiting_list[i][0] == 'write':
                            working_list.append((waiting_list.pop(i), time))
                            waiting_write_cnt -= 1
                            working_write_cnt += 1
                            break
                else:
                    while waiting_list:
                        working_list.append((waiting_list.pop(0), time))
            else:
                if not working_write_cnt and not waiting_write_cnt:
                    while waiting_list:
                        working_list.append((waiting_list.pop(0), time))

        if working_list:
            time_result += 1

        time += 1
    
    tmp_answer.sort(key=lambda x:x[0])
    for i in range(len(tmp_answer)):
        answer.append(tmp_answer[i][1])

    answer.append(str(time_result))

    return answer



print(solution(["1","2","4","3","3","4","1","5"], ["read 1 3 1 2","read 2 6 4 7","write 4 3 3 5 2","read 5 2 2 5","write 6 1 3 3 9", "read 9 1 0 7"]))
print(solution(["1","1","1","1","1","1","1"], ["write 1 12 1 5 8","read 2 3 0 2","read 5 5 1 2","read 7 5 2 5","write 13 4 0 1 3","write 19 3 3 5 5","read 30 4 0 6","read 32 3 1 5"]))