class Calculator:
    def calc(self, a, b, op):
        a = float(a)
        b = float(b)
        if op == "add":
            print(a + b)
        elif op == "sub":
            print(a - b)
        elif op == "mul":
            print(a * b)
        elif op == "div":
            if b != 0:
                print(a / b)
        else:
            print("Wrong operation")
a = input()
b = input()
op = input()
c = Calculator()
c.calc(a, b, op)