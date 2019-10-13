from random import randint


class Spearman:
    def __init__(self, name):
        """Initiating warrior with basic stats"""
        self.health = randint(100, 150)
        self.power = randint(20, 30)
        self.name = name
        self.basic_health = self.health
        print('Warrior', self.name, 'was created with following stats:')
        print('Health:', self.health)
        print('Power:', self.power)

    def get_health(self):
        """Method returns int health"""
        return self.health

    def get_power(self):
        """Method returns int power"""
        return self.power

    def get_damage(self, other):
        """Method makes warrior take damage from another warrior and die if he has no health left"""
        hit = other.get_power()
        self.health -= hit
        if self.health > 0:
            print(self.name, 'took', hit, 'damage. He has', self.health, 'health left.')
        else:
            print(self.name, 'took', hit, 'damage and died.')

    def go_fight(self, other):
        """Enters  a mortal battle with an opponent"""
        print('The fight between', self.name, 'and', other.name, 'begins!')
        print(self.name, 'has', self.health, 'health and', other.name, 'has', other.health)
        while self.health > 0:
            other.get_damage(self)
            if other.health > 0:
                self.get_damage(other)
            else:
                break
        if self.health > 0:
            print('Fight has ended.', self.name, 'wins!')
            print('')
        else:
            print('Fight has ended.', other.name, 'wins!')
            print('')

    def heal(self):
        """Restores warriors health to basic level"""
        self.health = self.basic_health
        print(self.name, 'has been healed.')
        print('')


class Infantryman(Spearman):
    def __init__(self, name):
        """Same stats as super Class has"""
        super().__init__(name)
        self.defence = randint(5, 10)
        print('Shield defence:', self.defence)

    def get_damage(self, other):
        """Extra parameter - defence. Reflects part of damage dealt to Infantryman"""
        hit = other.get_power()
        self.health -= (hit - self.defence)
        if self.health > 0:
            print(self.name, 'took', hit, 'damage.', self.defence, 'reflected with shield. He has',
                  self.health, 'health left.')
        else:
            print(self.name, 'took', hit, 'damage and died.')


class Knight(Spearman):
    def __init__(self, name):
        """Same stats as super Class has"""
        super().__init__(name)

    def get_power(self):
        """With 20% chance Knight deals double damage"""
        critical_rate = randint(1, 10)
        if critical_rate == 1 or critical_rate == 2:
            return self.power * 2
        else:
            return self.power
