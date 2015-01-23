class Food:
    def __init__(self, name, calories, flavor=''):
        self.name = name
        self.calories = calories
        self.flavor = flavor

    def tastesLike(self):
        print "%s is a %s and has %s calories and tastes like %s" % (self.name, self.__class__.__name__, self.calories, self.flavor)


class HotDog(Food):
    pass


class Hamburger(Food):
    pass


class ChickenPatty(Food):
    pass


dinner = []

dinner.append(HotDog('Beef/Turkey BallPark', 230, 'Extremely processed meat'))
dinner.append(Hamburger('Lowfat Beef Patty', 260, 'Grilled goodness'))
dinner.append(ChickenPatty('Mickey Mouse shaped Chicken Tenders', 170, 'Chicken'))

for course in dinner:
    course.tastesLike()