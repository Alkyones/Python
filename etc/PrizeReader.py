from datetime import datetime, timedelta




def friday_date(start, end):
    """
    Returns a list of friday dates between start and end dates
    """
    friday_list = []
    start_date = datetime.strptime(start, '%Y-%m-%d')
    end_date = datetime.strptime(end, '%Y-%m-%d')
    delta = end_date - start_date
    for i in range(delta.days + 1):
        day = start_date + timedelta(days=i)
        if day.weekday() == 4:
            friday_list.append(day.strftime('%Y-%m-%d'))
    return friday_list



print(friday_date('1999','2001'))