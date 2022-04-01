from itertools import combinations

def solution(n, m, k, records):
    answer = []
    arr = [i for i in range(1, m+1)]
    password_req = set()
    can_password = list(combinations(arr, len(set(records[0]))))
    tmp_can_password = []

    for record in records:
        for can_pass in can_password:
            tmp_list = sorted(list(set(record)))
            tmp_dict = dict()

            idx = 0
            for num in tmp_list:
                tmp_dict[num] = can_pass[idx]
        
            tmp_record = []
            for num in record:
                tmp_record.append(tmp_dict[num])
            
            tmp_can_password.append(tmp_record)

            if record[0] == 1:
                password_req.add(1)
            if record[len(record)-1] == n:
                password_req.add(m)

        can_password = tmp_can_password

    return answer



print(solution(8, 4, 4, [[1, 5, 1, 3], [5, 7, 5, 6]]))
print(solution(8, 4, 4, [[1, 5, 1, 3]]))
print(solution(10, 3, 3, [[1, 2, 3], [5, 7, 10]]))