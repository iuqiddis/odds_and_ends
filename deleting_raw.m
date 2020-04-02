% script for deleting files

%%

clear

dir_del = '/Users/iuqiddis/Downloads/today/';
cd(dir_del)

list_raw = dir([dir_del '*.CR2'])
%list_raw = dir([dir_del '*.NEF'])
%%

for n = 1:numel(list_raw)
    cur_file = list_raw(n).name;
    fprintf('\ncurrent file: %s\n', cur_file);
    cur_jpg = [cur_file(1:end-3) 'JPG'];
    if (exist(cur_jpg, 'file') == 0)
        fprintf('This file will be deleted\n')
        sys_cmd = ['rm ' cur_file];
        system(sys_cmd);
    else
        fprintf('This file has a JPG file\n')
    end
end