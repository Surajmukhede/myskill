def week(date):
    if date == 1:
        return 'monday'
    elif date == 2:
        return 'tuesday'
    elif date == 3:
        return 'wed'
    elif date == 4:
        return 'thursday'
    elif date == 5:
        return 'friday'
    elif date == 6:
        return 'saturday'
    elif date == 7:
        return 'sunday'

for i in range(1, 8):
    print(week(i))
    