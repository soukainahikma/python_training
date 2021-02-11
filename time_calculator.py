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
def add_time(start, duration, day_of_the_week = ""):
    liste1 = start.split()
    duration = duration.split(':')
    start = liste1[0].split(':')
    if(liste1[1] == "PM"):
        start[0] = int(start[0]) + 12
    result_min = time_convertor_to_min(int(start[0]) + int(duration[0]),int(start[1]) + int(duration[1]))
    result_time = time_convertor_inverse(result_min)
    print(result_min)
    print(result_time)
    return
print(add_time("3:30 PM", "2:12"))
#print(time_convertor_inverse((20+466) * 60 +18))