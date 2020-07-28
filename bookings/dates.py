import datetime
import calendar


def date_list():
    today_date = datetime.date.today()
    all_dates = [('', '')]
    for i in range(10):
        each_day = []
        the_date = today_date + datetime.timedelta(days=i+1)
        each_day.append(str(the_date))
        each_day.append(str(the_date))
        all_dates.append(tuple(each_day))
    return tuple(all_dates)


def time_list():
    start_time = '8'
    end_time = '18'
    all_slots = []
    for ix in range(int(start_time), int(end_time)):
        each_slot = []
        tm1 = datetime.datetime.strptime(str(ix), '%H').time()
        tm2 = datetime.timedelta(hours=tm1.hour, minutes=tm1.minute) + datetime.timedelta(hours=1)
        tm2 = (datetime.datetime.min + tm2).time()  # .strftime('%I:%M %p')
        tm1 = tm1.strftime('%I:%M %p')
        tm2 = tm2.strftime('%I:%M %p')
        all_slots.append(str(tm1)+' - '+str(tm2))

    return all_slots
# print('Going', tm1.strftime('%I:%M %p'), '->', tm2.strftime('%I:%M %p'))


def today_day():
    return str(datetime.date.today())