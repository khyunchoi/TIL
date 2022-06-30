def solution(S):
    file_list = S.split('\n')
    city_dict = dict()
    temp_file_list = []
    result = ''

    for i in range(len(file_list)):
        photo_name, city_name, date, time = file_list[i].split()
        extension = photo_name.rstrip(',')[photo_name.index('.'):]
        city_name = city_name.rstrip(',')

        date = date.replace('-', '')
        time = time.replace(':', '')
        datetime = int(date + time)

        if city_name in city_dict:
            city_dict[city_name].append([i, extension, datetime])
        else:
            city_dict[city_name] = [[i, extension, datetime]]
    
    for key, value in city_dict.items():
        value.sort(key=lambda x:x[2])
        if len(value) == 100:
            for i in range(1, len(value)+1):
                if 1 <= i <= 9:
                    temp_file_list.append([value[i-1][0], key+'00'+str(i)+value[i-1][1]])
                elif 10 <= i <= 99:
                    temp_file_list.append([value[i-1][0], key+'0'+str(i)+value[i-1][1]])
                else:
                    temp_file_list.append([value[i-1][0], key+str(i)+value[i-1][1]])
        elif len(value) >= 10:
            for i in range(1, len(value)+1):
                if 1 <= i <= 9:
                    temp_file_list.append([value[i-1][0], key+'0'+str(i)+value[i-1][1]])
                else:
                    temp_file_list.append([value[i-1][0], key+str(i)+value[i-1][1]])
        else:
            for i in range(1, len(value)+1):
                temp_file_list.append([value[i-1][0], key+str(i)+value[i-1][1]])

    temp_file_list.sort(key=lambda x:x[0])
    
    for temp_file in temp_file_list:
        result = result + temp_file[1] + '\n'

    return result.rstrip()

print(solution('photo.jpg, Warsaw, 2013-09-05 14:08:15\njohn.png, London, 2015-06-20 15:13:22\nmyFriends.png, Warsaw, 2013-09-05 14:07:13\nEiffel.jpg, Paris, 2015-07-23 08:03:02\npisatower.jpg, Paris, 2015-07-22 23:59:59\nBOB.jpg, London, 2015-08-05 00:02:03\nnotredame.png, Paris, 2015-09-01 12:00:00\nme.jpg, Warsaw, 2013-09-06 15:40:22\na.png, Warsaw, 2016-02-13 13:33:50\nb.jpg, Warsaw, 2016-01-02 15:12:22\nc.jpg, Warsaw, 2016-01-02 14:34:30\nd.jpg, Warsaw, 2016-01-02 15:15:01\ne.png, Warsaw, 2016-01-02 09:49:09\nf.png, Warsaw, 2016-01-02 10:55:32\ng.jpg, Warsaw, 2016-02-29 22:13:11'))