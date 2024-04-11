

# with open('write_test.text', 'w') as file_obj:
#     file_obj.write('Writing')

with open('sample_text', 'r') as read_obj:
    with open('sample_text_copy', 'w') as write_obj:
        write_obj.write('\n' + 'Rewriting again and again')
        # for line in read_obj:
        #     write_obj.write(line)

# csv, excel  →  pandas

