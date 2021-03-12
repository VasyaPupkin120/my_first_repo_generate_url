f = open('file_to_upload_wget.txt', 'w')
for i in range(0, 1157):
    l = 'https://another_url.com/parametrs1/' + str(i) + '/parametrs2'
    for index in l:
        f.write(index)
    f.write('\n')
f.close()

