import os
import os.path
dir_del = '/khazaddum/apparate/imports/photos/20200221_the_end_of_us/'
# make sure to include the trailing '/' after the directory name

list_files = [i for i in os.listdir(dir_del) if '.CR2' in i]
for i in list_files:
    jpg = dir_del+i[:-3]+'JPG'
    if not(os.path.isfile(jpg)):
        print('Deleting:'+i)
        os.remove(dir_del+i)
        
#os.getcwd()
