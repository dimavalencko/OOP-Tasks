#Программирование на языке высокого уровня (Python).
#Задание 4.3.5.
#Выполнил: Валенко Д.В
#Группа: ПИН-б-з-22-1
#E-mail: dima.valencko@yandex.ru

import json
class VectorCollection:
    def __init__(self):
        self.data = []
    def add(self, value):
        self.data.append(value)
    def remove(self, index):
        del self.data[index]
        
    def formateVector(self):
        result = []
        for i in self.data: 
            print('Item ', i)
            result.append({'x': i.x, 'y': i.y })
        return result
            
    def save(self, filename='vectors.json'):
        formattedData = self.formateVector()
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(formattedData, f)
            
    def load(self, filename='vectors.json'):
        with open(filename, 'r', encoding='utf-8') as f:
            self.data = json.load(f)

class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
obj_vector_collection = VectorCollection()
obj_vector_1 = Vector(1, 2)
obj_vector_2 = Vector(3, 4)
obj_vector_3 = Vector(5, 6)
obj_vector_collection.add(obj_vector_1)
obj_vector_collection.add(obj_vector_2)
obj_vector_collection.add(obj_vector_3)
obj_vector_collection.save()
obj_vector_collection.load()