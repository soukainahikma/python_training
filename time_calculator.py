def time_convertor_to_min(hours_,minutes_):
    result = hours_ * 60 + minutes_
    return(result)
def time_convertor_inverse(minutes_):
    days = minutes_ / (24 * 60)
    minutes_ = minutes_ % (24 * 60)
    hours_ = minutes_ / 60
    minutes_ = minutes_ % 60
    minutes = minutes_
    liste = [int(days),int(hours_),int(minutes)]
    return liste
def get_day(day_nb,day_of_the_week):
    days =["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    day_of_the_week = day_of_the_week.capitalize()
    index  = day_nb % 7 + days.index(day_of_the_week)
    if index >= 7:
        index = index -7
    return(days[index])
def time_printer(result_time, day_of_the_week):
    result_time.append('AM')
    if result_time[2] + result_time[1] > 12 and result_time[1] == 12:
        result_time[3] = 'PM'
    if result_time[2] < 10:
        result_time[2] = '0' + str(result_time[2])
    if result_time[1] > 12:
        result_time[1] = result_time[1] - 12
        result_time[3] = 'PM'
    elif result_time[1] == 0:
        result_time[1] = result_time[1] + 12
    res = str(result_time[1]) + ':' + str(result_time[2])+ ' ' + result_time[3]
    if day_of_the_week != "":
        res = res +', ' + get_day(result_time[0],day_of_the_week)
    if result_time[0] == 1:
        res = res + " (next day)"
    elif result_time[0] > 1:
        res = res + ' (' +str(result_time[0]) + " days later)"
    return(res)
def add_time(start, duration, day_of_the_week = ""):
    liste1 = start.split()
    duration = duration.split(':')
    start = liste1[0].split(':')
    if(liste1[1] == "PM"):
        start[0] = int(start[0]) + 12
    result_min = time_convertor_to_min(int(start[0]) + int(duration[0]),int(start[1]) + int(duration[1]))
    result_time = time_convertor_inverse(result_min)
    return(time_printer(result_time, day_of_the_week))
print(add_time("8:16 PM", "466:02", "tuesday"))