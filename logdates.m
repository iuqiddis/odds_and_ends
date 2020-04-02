function full_line = logdates(the_month, day_start, day_end, d)

% function full_line = logdates(the_month, day_start, day_end, d)
% month_start is the month you want
% day_start is the date you want to generate dates from
% day_end is the last date you want to generate dates from
% d = day of the week; M = 1, T = 2, etc, etc
% log dates

% capping the dates generated to end of a month;
if day_end > 31;
    day_end = 31;
    display('You can generate upto the 31st of a month')
end

the_year = 2018;
week = {'M', 'T', 'W', '&Theta;', 'F', 'S', '&Sigma;'};


n=1; % counter for making a new row in text cell

for day = day_start:day_end
    
    day_to_print = sprintf('*%d* ', day);
        day_to_print = sprintf('*%d-%02d-%02d* ', the_year, the_month, day);
    week_to_print = strcat('**',week{d},'**');
    
    d = mod(d+1,8); % only seven days in a week
    if d == 0
        d = 1;
    end
    
    full_line{n,:} = [day_to_print, week_to_print];
    n=n+1;
end

n = n -1;
fileID = fopen('logdates.txt','w');

for m = 1:n
    fprintf(fileID, '%s\n\n', full_line{m,:});
end

fclose(fileID);

end
