def solution(s, times):
    answer = []
    days = set()

    year = int(s[0:4])
    month = int(s[5:7])
    day = int(s[8:10])
    hour = int(s[11:13])
    minute = int(s[14:16])
    second = int(s[17:19])

    first_year = year
    first_month = month
    first_day = day
    days.add((first_year, first_month, first_day))

    for time in times:
        time_day = int(time[0:2])
        time_hour = int(time[3:5])
        time_minute = int(time[6:8])
        time_second = int(time[9:11])

        second += time_second
        if second >= 60:
            second -= 60
            minute += 1
        
        minute += time_minute
        if minute >= 60:
            minute -= 60
            hour += 1
        
        hour += time_hour
        if hour >= 24:
            hour -= 24
            day += 1
        
        day += time_day
        while day > 30:
            day -= 30
            month += 1

        if month > 12:
            month -= 12
            year += 1

        days.add((year, month, day))

    period = (year * 360 + month * 30 + day) - (first_year * 360 + first_month * 30 + first_day) + 1
    
    if len(days) == period:
        answer.append(1)
        answer.append(period)
    else:
        answer.append(0)
        answer.append(period)

    return answer


print(solution("2021:04:12:16:08:35", ["01:06:30:00", "01:04:12:00"]))
print(solution("2021:04:12:16:08:35", ["01:06:30:00", "00:01:12:00"]))
print(solution("2021:04:12:16:10:42", ["01:06:30:00"]))
print(solution("2021:04:12:16:08:35", ["01:06:30:00", "01:01:12:00", "00:00:09:25"]))