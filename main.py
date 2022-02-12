from typing import List

# TODO: implement division and subtraction properly


class data:
    unsafe = False
    MAX_INT = 2147483647
    MIN_INT = -2147483647
    MAX_FACTORIAL = 25000


def check_safety(operator: str, operand: int):
    if operator == "+" or operator == "-" or operator == "*":
        if operand > data.MAX_INT and not data.unsafe or operand < data.MIN_INT and not data.unsafe:
            return "Ω"
    elif operator == "!":
        if operand > data.MAX_FACTORIAL and not data.unsafe:
            return "Ω"
    return


def warn(msg):
    print("warning: " + str(msg))


def tip(msg):
    print("tip: " + str(msg))


def inform(msg):
    print("info: " + str(msg))


def check_safety_toggled(string: str):
    if string == "#unsafe":
        return not data.unsafe
    else:
        return data.unsafe


def tokenize(string: str):
    return string.split(" ")


def parse_and_execute(tokens: List[str]):
    operator = tokens[0]
    tokens.remove(operator)
    operands = tokens
    if not operands:
        return 0
    if operator == "*" or operator == "/":
        total = 1
    else:
        total = 0
    for operand in operands:
        try:
            operand = int(operand)
        except ValueError:
            return 0
        safety_result = check_safety(operator, operand)
        if safety_result is not None:
            return safety_result
        if operator == "+":
            total += operand
        elif operator == "*":
            total = operand * total
        elif operator == "!":
            i = operand
            factorial_t = 1
            while i > 0:
                factorial_t = i * factorial_t
                i -= 1
            total = factorial_t
            break
        else:
            return 0
    return str(total) + " OK"


print("------------------------------------------------------------------------------")
print("use CTRL+C to exit.")
print("enter an expression to evaluate.")
print("refer to the various lookup tables if any symbols in this program confuse you.")
print("the lookup tables can be found on the github repository.")
print("------------------------------------------------------------------------------")
print()

while True:
    userinput = ""
    try:
        userinput = input("expression>")
    except KeyboardInterrupt:
        print("\nexit...")
        exit()
    initial_safety = data.unsafe
    data.unsafe = check_safety_toggled(userinput)
    if initial_safety != data.unsafe:
        print("unsafe =", initial_safety, "->", data.unsafe)
        continue
    result = parse_and_execute(tokenize(userinput))
    if result == 0 or result == "Ω" or result is None:
        print(str(result) + " ~")
    else:
        print(result)
