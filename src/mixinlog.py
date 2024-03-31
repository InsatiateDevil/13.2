class MixinLog:

    def print_ec(self):
        """Метод для печати информации о """
        print(repr(self))

    def __repr__(self):
        object_attributes = ''
        for k, v in self.__dict__.items():
            object_attributes += f'{k}: {v},'
        return f"Создан объект со свойствами {object_attributes})"
