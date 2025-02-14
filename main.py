#s = {5, 7, 9,};
#for el in s:
#    print(el)
class Counter:
    def __init__(self, max_number):
        self.i = 0
        self.max_number = max_number

    def __iter__(self):
        self.i = 2
        return self

    def __next__(self):
        self.i += 3
        if self.i > self.max_number:
            raise StopIteration()
        return self.i

count = Counter(50)
for m in count:
    print(m)