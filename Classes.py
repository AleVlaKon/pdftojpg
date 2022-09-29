class Translator:

    dict = {}

    def add(self, eng, rus):
        if 'dict' not in self.__dict__:
            self.dict = {}

        self.dict.setdefault(eng, [])

        if rus not in self.dict[eng]:
            self.dict[eng].append(rus)


    def remove(self, eng):
        self.dict.pop(eng, False)


    def translate(self, eng):
        return self.dict[eng]

tr  = Translator()

tr.add("tree", "дерево")
tr.add("car", "машина")
tr.add("car", "автомобиль")
tr.add("leaf", "лист")
tr.add("river", "река")
tr.add("go", "идти")
tr.add("go", "ехать")
tr.add("go", "ходить")
tr.add("milk", "молоко")



print(*tr.dict['go'])





