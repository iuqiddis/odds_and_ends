import datetime

def logdates(the_year, the_month):

    # the_year is a number in YYYY format
    # the_month is a number between 1 and 12

    d = int(datetime.date(the_year, the_month, 1).strftime('%w'))
    day_start = 1
    
    if the_month == 2:
        if the_year % 4 == 0:
            day_end = 29
        else:
            day_end = 28
    elif the_month in [1,3,5,7,8,10,12]:
        day_end = 31
    else:
        day_end = 30
    
    week = ['M', 'T', 'W', '&Theta;', 'F', 'S', '&Sigma;']
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

    fileID = open('log_dates.txt', 'w')

    for line in full_line:
        fileID.write(line)
        fileID.write('\n\n')

    fileID.close()
    
    print('\nText file saved in the same directory as "log_dates.txt"\n')
    
    return 

if __name__ == '__main__':
    the_year = int(input("Year: "))
    the_month = int(input("Month (1-12): "))
    logdates(the_year, the_month)
	


