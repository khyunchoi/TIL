switch = int(input())
switch_stat = list(map(bool, map(int, input().split())))
N = int(input())

for _ in range(N):
    gender, num = map(int, input().split())

    if gender == 1:
        for i in range(num-1, len(switch_stat), num):
            switch_stat[i] = not switch_stat[i]
    else:
        x = 0
        switch_stat[num-1] = not switch_stat[num-1]
        while switch_stat[num-1-x] == switch_stat[num-1+x]:
            switch_stat[num-1-x] = not switch_stat[num-1-x]
            switch_stat[num-1+x] = not switch_stat[num-1+x]
            x += 1
            if (num-1-x < 0) or (num-1+x >= len(switch_stat)):
                break

#출력
result = ''
for i in range(len(switch_stat)):
    if switch_stat[i]:
        result += '1 '
    else:
        result += '0 '

    if (i+1) % 20 == 0:
        result += '\n'

print(result)