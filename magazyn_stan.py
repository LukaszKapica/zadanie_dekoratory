from klasy import manager
import sys


@manager.assign('magazyn')
def magazyn_stan(magazyn):
    manager.magazyn.oblicz_aktualny_stan()
    for produkt in sys.argv[1:]:
        if not produkt:
            break
        print(manager.magazyn.stan_magazynowy[produkt])


manager.execute('magazyn')