from magazyn_klasa import Magazyn


class FileHandler:
    def __init__(self, file_path_read, file_path_write=None):
        self.history = []
        self.file_path_read = file_path_read
        if file_path_write:
            self.file_path_write = file_path_write
        else:
            file_path_write = file_path_read

    def read_history(self):
        with open(self.file_path_read) as file:
            for line in file:
                line = line.rstrip()
                komenda = [line]
                if line == 'stop':
                    break
                if line == 'saldo':
                    value = int(file.readline().rstrip())
                    comment = file.readline().rstrip()
                    komenda.extend([value, comment])
                if line in ['zakup', 'sprzedaz']:
                    product_name = file.readline().rstrip()
                    product_price = int(file.readline().rstrip())
                    product_value = int(file.readline().rstrip())
                    komenda.extend([product_name, product_price, product_value])
                self.history.append(komenda)

    def write_history(self):
        with open(self.file_path_write, 'w') as file:
            for komenda in self.history:
                for element in komenda:
                    file.write(str(element) + '\n')
            file.write('stop')


class Manager:
    def __init__(self):
        self.actions = {}
        # self.account = account
        self.file_handler = FileHandler(file_path_read='pliki/history.txt', file_path_write='pliki/history.txt')
        self.file_handler.read_history()
        self.magazyn = Magazyn(self.file_handler.history)
        self.magazyn.oblicz_aktualny_stan()

    def assign(self, name):
        def decorate(cb):
            self.actions[name] = cb
        return decorate

    def execute(self, name):
        if name not in self.actions:
            print("Action not defined")
        else:
            self.actions[name](self)


manager = Manager()