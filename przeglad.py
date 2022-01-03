from klasy import manager


@manager.assign('przeglad')
def przeglad(magazyn):
    # manager.magazyn.oblicz_aktualny_stan()
    print(manager.magazyn.historia)
    print(manager.magazyn.stan_konta)
    print(manager.magazyn.stan_magazynowy)


manager.execute('przeglad')