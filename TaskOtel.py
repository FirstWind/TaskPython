class Hotel:
    """Родительский класс отеля"""

    def __init__(self):
        self.count_room = 10
        self.rooms = {1: ['бизнес', 3000, '2-комнатная'], 2: ['бизнес', 5000, '2-комнатная'],
                      3: ['люкс', 10000, '3-комнатная'], 4: ['эконом', 2500, '1-комнатная'],
                      5: ['эконом', 1500, '1-комнатная'], 6: ['эконом', 2000, '1-комнатная'],
                      7: ['эконом', 1500, '1-комнатная'], 8: ['эконом', 2000, '1-комнатная'],
                      9: ['эконом', 1500, '1-комнатная'], 10: ['эконом', 2000, '1-комнатная']}
        self.status = ['занята', 'свободна', 'на ремонте']
        self.status_rooms = {1: [self.status[1], ''], 2: [self.status[1], ''], 3: [self.status[1], ''],
                             4: [self.status[1], ''], 5: [self.status[1], ''], 6: [self.status[1], ''],
                             7: [self.status[1], ''], 8: [self.status[1], ''], 9: [self.status[1], ''],
                             10: [self.status[1], '']}


class HotelRoom(Hotel):
    """Класс комнат отеля"""

    def __init__(self, *args, **kwargs):
        super().__init__()

    def check_in_status_room(self, number_room):
        return self.status_rooms.get(number_room)

    def update_status_room(self, number_room, status):
        state_check = self.check_in_status_room(number_room)
        if state_check is not None:
            self.status_rooms[number_room][0] = status
            return True
        else:
            print(f'комната № {number_room} - Не существует')
            return False

    def update_human_in_room(self, name, number_room):
        self.status_rooms[number_room][1] = name
        self.view_rooms_free()
        print(f'комната № {number_room} - {self.status_rooms[number_room][0]} {self.status_rooms[number_room][1]}')

    def view_rooms(self):
        for key, value in self.status_rooms.items():
            print(f'комната № {key} - {" ".join(value)} {self.rooms[key][0]} {self.rooms[key][1]}')

    def view_rooms_free(self):
        for key, value in self.status_rooms.items():
            if value[0] == self.status[1]:
                print(f'комната № {key} - {" ".join(value)} {self.rooms[key][0]} {self.rooms[key][1]}')


class Visitor(HotelRoom):
    """Класс посетителя"""

    def __init__(self):
        super().__init__()

    def check_into(self, name, number_room):  # заселиться в оте8ль
        if self.update_status_room(number_room, 'занята'):
            self.update_human_in_room(name, number_room)
        # print(f'{self.name} Ваш номер №{self.number_room} {self.rooms[self.number_room]}')

    def view_gost(self):
        for key, value in self.status_rooms.items():
            print(f'комната №{key} - {value} {self.rooms[key]}')


def main():
    rooms = HotelRoom()
    gost = Visitor()
    while True:
        quest = '1 - Заселиться\n2 - Выселиться\n3 - Сменить номер\n4 - Отремонтировать\
        \n5 - Выход\n'
        try:
            str_vibor = input(quest)
        except ValueError:
            print("Ввели не число")
            continue
        if str_vibor == '1':
            name = input('Введите имя ')
            rooms.view_rooms_free()
            gost.check_into(name, int(input('Введите № номера для заселения ')))
        elif str_vibor == '2':
            pass
        elif str_vibor == '3':
            pass
        elif str_vibor == '4':
            pass
        elif str_vibor == '5':
            # gost.viewGost()
            exit()


if __name__ == '__main__':
    main()
