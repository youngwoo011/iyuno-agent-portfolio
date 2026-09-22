def calculator(a, b, operation):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        if b == 0:
            return "0으로 나눌 수 없습니다."
        return a / b
    else:
        return "지원하지 않는 연산입니다."