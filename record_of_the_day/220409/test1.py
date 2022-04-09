def solution(path):
    answer = []

    flag = 1
    for i in range(len(path)):
        if i != 0 and path[i] != path[i-1]:
            flag = 1
        
        if flag:
            for j in range(i+1, min(i+6, len(path))):
                if path[i] != path[j]:
                    if path[i] == "N":
                        if path[j] == "W":
                            direction = "left"
                        else:
                            direction = "right"
                    elif path[i] == "E":
                        if path[j] == "N":
                            direction = "left"
                        else:
                            direction = "right"
                    elif path[i] == "S":
                        if path[j] == "E":
                            direction = "left"
                        else:
                            direction = "right"
                    elif path[i] == "W":
                        if path[j] == "S":
                            direction = "left"
                        else:
                            direction = "right"


                    answer.append("Time "+str(i)+": Go straight "+str(j-i)+"00m and turn "+direction)
                    flag = 0
                    break

    return answer


print(solution("EEESEEEEEENNNN"))
print(solution("SSSSSSWWWNNNNNN"))

"Time 0: Go straight 300m and turn right"