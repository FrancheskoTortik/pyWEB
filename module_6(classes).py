def one():
    class KitchenUtensil:
        def heat_up(self):
            pass


    class Pan(KitchenUtensil):
        def __init__(self, size):
            self.size = size

        def heat_up(self):
            print("Сковорода подогревается")


    class Saucepan(KitchenUtensil):
        def __init__(self, volume, height):
            self.volume = volume
            self.height = height
            self.diameter = (4*volume / (3.14*height))**(1/2)

        def heat_up(self):
            print("Кастрюля диаметром %d см нагревается" % 100*self.diameter)

    utensils = [Pan(20), Saucepan(3, 0.125)]
    for u in utensils:
        u.heat_up()


class User:
    def __init__(self, name, email):
        self.name = name.title()
        self.email = email.lower()

    def is_active(self):
        return False

    def is_superuser(self):
        return False

    def __str__(self):
        kind = "пользователь"
        if self.is_superuser():
            kind = "админ"

        return "%s %s <%s>" % (kind, self.name, self.email)


class RegularUser(User):
    pass


class SuperUser(User):
    def is_superuser(self):
        return True

u1 = RegularUser("Vasiliy", "vasily@mail.ru")
u2 = SuperUser("Larisa", "larisa@mail.ru")
for u in (u1, u2):
    print(u)