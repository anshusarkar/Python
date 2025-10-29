class MyNumber: #__init__, __add__, __str__ are all dunder / magic methods 
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return MyNumber(self.value + other.value)

    def __str__(self):
        return f"MyNumber({self.value})"

num1 = MyNumber(5)
num2 = MyNumber(10)
sum_num = num1 + num2  # Calls num1.__add__(num2)
print(sum_num)         # Calls sum_num.__str__()