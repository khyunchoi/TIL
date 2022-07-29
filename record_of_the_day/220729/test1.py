def solution(k, m, names, amounts):
    answer = 0
    
    for i in range(len(names)):
        flag_m = 0
        if amounts[i] >= m:
            flag_m = 1
        
        flag_k = 0
        if i >= k-1:
            flag_k = 1
            for j in range(i-k+1, i+1):
                if names[j].lower() != names[i].lower():
                    flag_k = 0
                    break
        
        if flag_m or flag_k:
            answer += 1
    
    return answer






print(solution(3, 50000, ["msLEE", "jsKim", "jsKIM", "jskiM", "jskim", "John", "john", "John", "msLEE", "msLEE", "jsKIM", "roy"], [950, 52524, 1400, 6055, 10000, 4512, 512, 52000, 9000, 49000, 1400, 50000]))
print(solution(2, 3451, ["abcd", "aBCd", "jsKIM", "rrr", "rrr"], [950, 1000, 1400, 4000, 10000]))