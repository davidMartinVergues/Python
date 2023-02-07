with open('./numbers.txt','r',encoding='utf-8') as file:
    lines_list = []

    lines_list.append(file.readline().splitlines())
    lines_list.append(file.readline().rstrip())
    lines_list2 = [ line.rstrip() for line in file ]
    file.seek(0)
    lines_all = file.read()

    # print(lines_list)
    lines_all
    #print(lines_list2)


# with open('./texto_lorem.txt','r',encoding='utf-8') as file:
#     lines_list = []

#     lines_list.append(file.readline().splitlines())
#     lines_list.append(file.readline().rstrip())
#     file.seek(0)
#     lines_list2 = [ line.rstrip() for line in file ]
#     file.seek(0)
#     lines_all = file.read().splitlines()

#     #print(lines_list)
#     print(lines_all)
#     #print(lines_list2)