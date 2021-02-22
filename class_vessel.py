class Vessel:
    "Родительский класс сосуда"
    def __init__(self, name='кувшин', capacity=1000, part=0):
        self.name = name  # название сосуда
        self.capacity = capacity  # объем сосуда
        self.part = part  # наливаемая часть

    def __checkValue(part):
        if isinstance(part, int) or isinstance(part, float):
            return True
        return False

    def setPart(self, part):
        if Vessel.__checkValue(part):
            self.part = part
        else:
            print('Мл. должны быть в числовом формате')



class Jug(Vessel):
    "Дочерний класс кувшина"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__capacity_part = self.part

    def setCapacity_part(self):
        if self.capacity - (self.__capacity_part + self.part) >= 0:
            self.__capacity_part += self.part
        else:
            if input(f'{self.name} уже пуст, хотите наполнить его? y/n ') == 'y':
                self.__capacity_part = 0
            else:
                return False  # Прекращаем работу

    def print_info(self):
        return (f'{self.name}-{self.capacity}мл.({self.capacity - self.__capacity_part}мл.)')

class Glass(Vessel):
    "Дочерний класс стакана"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__capacity_part = self.part

    def proverkaIsFull(self):
        "Проверка полон ли стакан"
        if self.__capacity_part + self.part <= self.capacity:
            return True
        return False

    def setCapacity_part(self):
        "процесс добавления жидкости в стакан.Контроль за наполняемостью в __capacity_part"
        if self.proverkaIsFull():

            self.__capacity_part += self.part
        else:
            if input(f'{self.name} уже полон, хотите опустошить? y/n ') == 'y':
                self.__capacity_part = 0
            else:
                return False

    def print_info(self):
        return (f'{self.name}-{self.capacity}мл.({self.__capacity_part}мл.)')


def main():
    part = 100
    jug = Jug('кувшин', 100)
    glass = Glass('стакан', 200)
    print(f"{jug.print_info()} и {glass.print_info()}")

    while input(f"хотите налить {part}мл. из кувшина в стакан? y/n ") == 'y':
        if glass.proverkaIsFull():
            jug.part = part
            if jug.setCapacity_part() == False:
                break

        glass.part = part
        if glass.setCapacity_part() == False:
            break

        print(f"{jug.print_info()} и {glass.print_info()}")
    print('Закончили')

if __name__ == '__main__':
    main()