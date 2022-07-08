def solution(masks, dates):
    answer_list = []
    change_dates = set()
    month_dict = {
        '01': 0,
        '02': 31,
        '03': 59,
        '04': 90,
        '05': 120,
        '06': 151,
        '07': 181,
        '08': 212,
        '09': 243,
        '10': 273,
        '11': 304,
        '12': 334
    }


    def dfs(depth, cost):
        if depth == len(visited):
            answer_list.append(cost)
            return

        if not visited[depth]:
            for mask in masks:
                price, day = mask
                for i in range(change_dates[depth], change_dates[depth]+day):
                    if i in change_dates:
                        visited[change_dates.index(i)] = 1
                dfs(depth+1, cost+price)
                for i in range(change_dates[depth], change_dates[depth]+day):
                    if i in change_dates:
                        visited[change_dates.index(i)] = 0
        else:
            dfs(depth+1, cost)


    for date in dates:
        if len(date) == 10:
            change_date = (int(date[:4]) - 2021) * 365 + month_dict[date[5:7]] + int(date[8:]) - 1
            change_dates.add(change_date)
        else:
            change_date_start = (int(date[:4]) - 2021) * 365 + month_dict[date[5:7]] + int(date[8:10]) - 1
            change_date_end = (int(date[11:15]) - 2021) * 365 + month_dict[date[16:18]] + int(date[19:]) - 1
            for date in range(change_date_start, change_date_end+1):
                change_dates.add(date)

    change_dates = list(change_dates)
    change_dates.sort()
    visited = [0 for _ in range(len(change_dates))]

    dfs(0, 0)
    
    return min(answer_list)

print(solution([[3200, 4], [2300, 2], [1100, 1], [4200, 6]], ["2022/05/02", "2022/05/01", "2022/05/07", "2022/05/05", "2022/05/08", "2022/05/13~2022/05/15", "2022/05/14~2022/05/17", "2022/05/01~2022/05/02", "2022/05/16"])) # 9600
print(solution([[600, 2], [500, 1], [1015, 400]], ["2023/01/01~2023/01/02", "2021/12/31"])) # 1015
print(solution([[3651, 365], [10, 1]], ["2025/01/01~2025/12/31"])) # 3650