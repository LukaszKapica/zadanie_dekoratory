class Magazyn:
    def __init__(self, historia):
        self.stan_magazynowy = {}
        self.historia = historia
        self.stan_konta = 0

    def saldo(self, komenda):
        if self.stan_konta + komenda[1] >= 0:
            self.stan_konta += komenda[1]

    def sprzedaz(self, komenda):
        if self.stan_magazynowy.get(komenda[1]) >= komenda[3]:
            self.stan_magazynowy[komenda[1]] -= komenda[3]
            self.stan_konta += komenda[2] * komenda[3]
        else:
            print('brak wystarczajacej ilosci produktow')

    def zakup(self, komenda):
        if self.stan_konta >= komenda[2] * komenda[3]:
            self.stan_konta -= komenda[2] * komenda[3]
        if self.stan_magazynowy.get(komenda[1], None) is None:
            self.stan_magazynowy[komenda[1]] = komenda[3]
        else:
            self.stan_magazynowy[komenda[1]] += komenda[3]

    def oblicz_aktualny_stan(self):
        self.stan_konta = 0
        self.stan_magazynowy = {}
        for komenda in self.historia:
            if komenda[0] == 'saldo':
                self.saldo(komenda)
            if komenda[0] == 'sprzedaz':
                self.sprzedaz(komenda)
            if komenda[0] == 'zakup':
                self.zakup(komenda)