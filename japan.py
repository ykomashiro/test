import os
from shutil import copyfile

PATH = r'C:\Users\Mashiro\Desktop\日语教程'
TO = r"C:\Users\Mashiro\Desktop\a"


def filesearch(fn):
    g = os.walk(fn)
    files = list()
    for path, _, file_list in g:
        for file in file_list:
            files.append(os.path.join(path, file))
    return files


file_list = filesearch(PATH)
for fn in file_list:
    if 'screen' in fn:
        chapter = fn.split('\\')[-1]
        chapter = chapter.split('）')[-1]
        chapter = chapter.replace('_screen', '')
        copyfile(fn, os.path.join(TO, chapter))
