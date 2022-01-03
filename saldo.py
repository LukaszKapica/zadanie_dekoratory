from klasy import manager
import sys


@manager.assign('saldo')
def saldo(manager):
    komenda = ['saldo', int(sys.argv[1]), sys.argv[2]]
    manager.file_handler.history.append(komenda)
    # manager.magazyn.oblicz_aktualny_stan()
    print(manager.magazyn.stan_konta)
    manager.file_handler.write_history()


manager.execute('saldo')