filename = 'user_id_file.txt'


def add_user(user_id):
    user_list = get_user_list()
    if user_list is None:
        return
    if str(user_id) in user_list:
        return
    else:
        file = open(filename, 'at')
        try:
            file.write(str(user_id) + '\n')
        finally:
            file.close()
    return


def delete_user(user_id):
    user_list = get_user_list()
    if user_list is None:
        return
    if str(user_id) in user_list:
        user_list.remove(str(user_id))
        file = open(filename, 'wt')
        try:
            for l in user_list:
                file.write(str(l) + '\n')
        finally:
            file.close()
    return


def get_user_list():
    user_list = list()
    file = open(filename)
    try:
        for line in file:
            line = line[:-1]
            user_list.append(line)
    except OSError:
        user_list = None
    finally:
        file.close()
    return user_list


for c in range(20):
    add_user(c)
print(get_user_list())
delete_user(3)
print(get_user_list())
#data = {'body': '/spam:Привет все\nHow are u?'}
#
#if '/' == data['body'].lower()[0]:
#    print(True)
#    mes_to_spam = data['body'][6:]
#else:
#    print(False)
#print(mes_to_spam)
