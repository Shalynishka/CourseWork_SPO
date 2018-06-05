filename = 'mysite/Handler/user_id_file.txt'


class FileWork:
    @staticmethod
    def add_user(user_id):
        user_list = FileWork.get_user_list()
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

    @staticmethod
    def delete_user(user_id):
        user_list = FileWork.get_user_list()
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

    @staticmethod
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
