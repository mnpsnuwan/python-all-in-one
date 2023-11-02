# copyfile() = Copies content of a file
# copy() = copyfile() + permission + destination can be a directory
# copy2() = copy() + copies metadata (file's creation and modification times)

import shutil

shutil.copyfile('../../data/test.txt', '../../data/copy.txt')  # src, des
shutil.copy('../../data/test.txt', '../../data/copy.txt')  # src, des
shutil.copy2('../../data/test.txt', '../../data/copy.txt')  # src, des


