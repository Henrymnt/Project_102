import os
import shutil

from_dir="C:/Users/Henry/Downloads"
to_dir="C:/Users/Henry/OneDrive/Documents"

list_of_files=os.listdir(from_dir)
print(list_of_files)

for file in list_of_files:
    name,extension = os.path.splitext(file)

    if extension=='':
        continue
    if extension in ['.gif', '.png', '.jpg', '.jpeg', '.jfif']:
        path1=from_dir+'/'+file
        path2=to_dir + '/' + 'documents'
        path3=to_dir + '/' + 'documents' + '/'+file
    if os.path.exists(path2):
        print('Moving ' + file + "... ")
        shutil.move(path1, path3)
    else:
        os.makedirs(path2)
        print('Moving ' + file + "... ")
        shutil.move(path1, path3)
