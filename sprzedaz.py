from klasy import manager
import sys


@manager.assign('sprzedaz')
def sprzedaz(manager):
    komenda = ['sprzedaz', sys.argv[1], int(sys.argv[2]), int(sys.argv[3])]
    manager.file_handler.history.append(komenda)
    manager.file_handler.write_history()
    print(manager.magazyn.stan_magazynowy)
    print(manager.magazyn.stan_konta)


manager.execute('sprzedaz')