## Decorating
def checker(function):
    def checker(*args, **kwargs):
        try:
            result = function(*args, **kwargs)
        except Exception as exc:
            print(f"We have problems {exc}")
        else:
            print(f"No problems. Result – {result}")
    return checker
# @checker
def calculate(expression):
    return eval(expression)

calculate = checker(calculate)

calculate('33+33')