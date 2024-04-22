
'''

### Open command

# 1. Using the open command with files
#       →  read  - display file, cannot overwrite
#       →  write - create a new file and include some new data
#       →  append - add to already existing content
#     default mode is read
#     once you open a file you must explicitly close it



file_obj = open('sample_text','r')
print(file_obj.name)
print(file_obj.mode)
file_obj.close()

'''

### with open  →  context managment
    # Files are closed automatically
    # .read is fine for small files  →  not good practice for larger files
    #   →  tries to load everything into memory in one shot
    #   →  for loop gives you control over what is accessed

# with open('sample_text', 'r') as file_obj:
    # print(file_obj.name)
    # # print('Inside with the open: ', file_obj.closed)
    # file_contents = file_obj.read()
    # print(file_contents)


    # To access one line at a time
    # for line in file_obj:
    #     print(line)

    # file_content = file_obj.readline()
    # print(file_content)

    # file_content = file_obj.readline()
    # print(file_content)

    # file_content = file_obj.readline()
    # print(file_content)

    # size_to_read = 100

    # file_contents = file_obj.read(size_to_read)
    # print(file_contents)

    # file_contents = file_obj.read(size_to_read)
    # print(file_contents)

    # file_contents = file_obj.read(size_to_read)
    # print(file_contents)

    # file_contents = file_obj.read(size_to_read)
    # print(file_contents)

    # When there are no more characters to return, read will return an empty string

with open('sample_text', 'r') as file_obj:
    size_to_read = 100
    file_contents = file_obj.read(size_to_read)
    while len(file_contents) > 0:
        print(file_contents, end='*')
        file_contents = file_obj.read(size_to_read)

    file_obj.write('Writing')

# print(file_obj.closed)