class Student:
    def __init__(self, name):
        self.name = name

    def show(self):
       print(self.name)

    class Laptop:
        def __init__(self, obj, model, cpu, memory):
            self.obj = obj
            self.model = model
            self.cpu = cpu
            self.memory = memory

        def display(self):
            print(f"{self.obj.name} => {self.model}, {self.cpu}, {self.memory}")


outer = Student('Roman')
inner = outer.Laptop(outer, 'HP', 'i7', '16')
inner.display()
print()
outer = Student('Vladimir')
inner = outer.Laptop(outer, 'HP', 'i7', '16')
inner.display()

