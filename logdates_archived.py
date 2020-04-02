def logdates(the_month, day_start, day_end, d):

    # function full_line = logdates(the_month, day_start, day_end, d)
    # month_start is the month you want
    # day_start is the date you want to generate dates from
    # day_end is the last date you want to generate dates from
    # d = day of the week; M = 1, T = 2, etc, etc
    # log dates

    # capping dates generated to end of the month;
    if day_end > 31:
        day_end = 31
        print('You can generate upto the 31st of a month')

    the_year = 2019
    week = ['M', 'T', 'W', '&Theta;', 'F', 'S', '&Sigma;']

    #n = 1 # counter for making a new row in text cell

    full_line = []

    for day in range(day_start,day_end+1):
        day_to_print = '*{:d}-{:02d}-{:02d}*'.format(the_year, the_month, day)
        week_to_print = '**{:s}**'.format(week[d-1])

        d = (d+1) % 7
        if d == 0:
            d = 7

        full_line.append(day_to_print + ' ' + week_to_print)

    for i in full_line:
        print(i)

    fileID = open('log_life.txt', 'w')

    for line in full_line:
        fileID.write(line)
        fileID.write('\n\n')

    fileID.close()


logdates(2,1,28,6)


