"""
Задача на циклический итератор.

Надо написать класс CyclicIterator.
Итератор должен итерироваться по итерируемому объекту (list, tuple, set, range, Range2, и т. д.), и когда достигнет последнего элемента, начинать сначала.
"""

class CyclicIterator:
    
    def __init__(self, collection):
        self.collection = collection
    
    def __iter__(self):
        self.next = 0
        return self

    def __next__(self):
        if self.next == len(self.collection):
            self.next = 0
        result = self.collection[self.next]
        self.next += 1
        return result
    
cyclic_iterator = CyclicIterator(range(5))
for i in cyclic_iterator:
    print(i)
