
#### CWD
    # → Current working Directory

# print(os.getcwd())

# Change to a different directory

# os.chdir('C:\\Users\\rlc100\\OneDrive - University of Pittsburgh\\Spring24\\Fundamentals of Programming')
# print(os.getcwd())

# List all the files at the current location

# mkdir →  create a single directory
# makedirs  →  used to create a hierarchy of directories
# rmdir  →  remove directory
# removedirs  →  remove tree of directories
#     → Best practice is to remove one directory at a time
# print(os.listdir())

# os.mkdir('Test_Dir')
# os.makedirs('Test_Dir1\\sub1\\sub2')
# os.rmdir('Test_Dir')
# os.removedirs('Test_Dir1\\sub1\\sub2')
import os
os.get