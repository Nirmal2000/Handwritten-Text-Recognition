
import shutil
import os
#
number_ofdigits = 3; extensions = (".jpg")
os.chdir('./test')
files = os.listdir()
for item in files:
    if item.endswith(extensions):
        name = item.split("."); zeros = number_ofdigits-len(name[0])
        newname = str(zeros*"0")+name[0]+"."+name[1]
        shutil.move(item, '{}'.format(newname))


