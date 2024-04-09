class Vehicle:
    def __init__(self, speed, weight):
        self.speed = speed
        self.weight = weight

    def checkSpeedLimitObec(self):
        if self.speed <= 50:
            return 'V obci nedostane pokutu.'
        else:
            return 'V obci dostane pokutu.'

    def checkSpeedLimitDalnice(self):
        if self.speed < 80:
            return 'Na dálnici jede moc pomalu. Dostane pokutu.'
        elif self.speed >= 80 and self.speed <= 130:
            return 'Na dálnici nedostane pokutu.'
        else:
            return 'Na dálnici jede moc rychle. Dostane pokutu.'

class Kamion(Vehicle):
    def __init__(self, speed, weight, zatizeni):
        super().__init__(speed, weight)
        self.zatizeni = zatizeni

    def checkSpeedLimitDalnice(self):
        if self.speed < 80:
            return 'Na dálnici jede kamion moc pomalu. Dostane pokutu.'
        elif self.speed >= 80 and self.speed <= 90:
            return 'Na dálnici kamion nedostane pokutu.'
        else:
            return 'Na dálnici jede kamion moc rychle. Dostane pokutu.'

auto1 = Vehicle(48, 1800)
print(auto1.checkSpeedLimitObec())
print(auto1.checkSpeedLimitDalnice())

kamion1 = Kamion(90, 20000, 16000)
print(kamion1.checkSpeedLimitObec())
print(kamion1.checkSpeedLimitDalnice())

