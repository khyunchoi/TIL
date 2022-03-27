def solution(goods):
    answer = []
    for item in goods:
        results = []
        item_size = len(item)
        for i in range(1, item_size+1):
            if results:
                break

            for j in range(item_size-i+1):

                for another_item in goods:
                    if another_item == item:
                        continue

                    if item[j:i+j] in another_item:
                        break
                else:
                    results.append(item[j:i+j])

        results = list(set(results))
        results.sort()
        
        tmp = ''
        for result in results:
            tmp += result + ' '
        tmp = tmp.strip()

        if tmp:
            answer.append(tmp)
        else:
            answer.append('None')

    return answer


print(solution(["pencil","cilicon","contrabase","picturelist"]))
print(solution(["abcdeabcd","cdabe","abce","bcdeab"]))