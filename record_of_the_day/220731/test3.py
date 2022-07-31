from collections import deque

def solution(ledgers):
    answer = 0

    stack = deque()
    for ledger in ledgers:
        date, rate, money = ledger.split()
        rate = int(rate)
        money = int(money)

        int_date = 0
        if date[0:2] == '01':
            int_date = int(date[3:5])
        elif date[0:2] == '02':
            int_date = 31 + int(date[3:5])
        elif date[0:2] == '03':
            int_date = 59 + int(date[3:5])
        elif date[0:2] == '04':
            int_date = 90 + int(date[3:5])
        elif date[0:2] == '05':
            int_date = 120 + int(date[3:5])
        elif date[0:2] == '06':
            int_date = 151 + int(date[3:5])
        elif date[0:2] == '07':
            int_date = 181 + int(date[3:5])
        elif date[0:2] == '08':
            int_date = 212 + int(date[3:5])
        elif date[0:2] == '09':
            int_date = 243 + int(date[3:5])
        elif date[0:2] == '10':
            int_date = 273 + int(date[3:5])
        elif date[0:2] == '11':
            int_date = 304 + int(date[3:5])
        elif date[0:2] == '12':
            int_date = 334 + int(date[3:5])

        if money > 0:
            stack.append([int_date, rate, money])
        else:
            while money < 0:
                bank_date, bank_rate, bank_money = stack.pop()
                if abs(money) >= bank_money:
                    answer += int((bank_money * bank_rate / 100) * ((int_date - bank_date) / 365))
                    money += bank_money
                else:
                    answer += int((abs(money) * bank_rate / 100) * ((int_date - bank_date) / 365))
                    bank_money += money
                    stack.append([bank_date, bank_rate, bank_money])
                    money = 0

    while stack:
        bank_date, bank_rate, bank_money = stack.pop()
        answer += int((bank_money * bank_rate / 100) * ((365 - bank_date) / 365))

    return answer


print(solution(["01/01 4 50000","01/11 6 3555","02/01 0 -23555","02/25 5 5000","03/25 0 -15000","06/09 8 43951","12/30 9 99999"]))
print(solution(["04/01 1 40000","05/01 5 20000","08/31 4 10000","11/11 0 -45000"]))