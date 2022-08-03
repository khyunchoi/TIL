from itertools import combinations

def solution(prj, n, k):
    answer = ''

    alphabet = set()
    for project in prj:
        for p in project:
            alphabet.add(p)
    alphabet = list(alphabet)
    alphabet.sort()
    alphabet_idx = dict()
    tmp = 0
    for alpha in alphabet:
        alphabet_idx[alpha] = tmp
        tmp += 1
    
    check_n = [0 for _ in range(len(alphabet))]
    check_k = [0 for _ in range(len(alphabet))]
    
    board = [[0 for _ in range(len(alphabet))] for _ in range(len(alphabet))]
    for project in prj:
        combi_list = list(combinations(project, 2))
        
        for combi in combi_list:
            a, b = combi
            board[alphabet_idx[a]][alphabet_idx[b]] = 1
            board[alphabet_idx[b]][alphabet_idx[a]] = 1

    for i in range(len(alphabet)):
        for j in range(len(alphabet)):
            if board[i][j] == 1 and check_k[j] < k:
                check_n[i] += 1
                check_k[j] += 1
                answer += alphabet[j]
                print(check_n[i])

            if check_n[i] == n:
                break

    return answer


print(solution(["DBEX", "ACE", "CDX", "ABGX"], 2, 3))
print(solution(["OR", "QO", "R", "OQ", "OR"], 1, 2))