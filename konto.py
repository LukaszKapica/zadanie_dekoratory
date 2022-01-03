from klasy import manager


@manager.assign('konto')
def konto(manager):
    print(manager.magazyn.stan_konta)


manager.execute('konto')