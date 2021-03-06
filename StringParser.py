class Parser:
    def __init__(self, inputString):
        self.string = inputString
        self.index = 0

    def getValue(self):
        value = self.parseExpression()
        self.skipWhitespace()
        if self.hasNext():
            raise Exception(
                "Unknown character is here: '" +
                self.peek() +
                "' at index " +
                str(self.index))
        return value

    def peek(self):
        return self.string[self.index:self.index + 1]

    def hasNext(self):
        return self.index < len(self.string)

    def skipWhitespace(self):
        while self.hasNext():
            if self.peek() in ' \t\n\r':
                self.index += 1
            else:
                return

    def parseExpression(self):
        return self.parseAddition()

    def parseAddition(self):
        values = [self.parseMultiplication()]
        while True:
            self.skipWhitespace()
            char = self.peek()
            if char == '+':
                self.index += 1
                values.append(self.parseMultiplication())
            elif char == '-':
                self.index += 1
                values.append(-1 * self.parseMultiplication())
            else:
                break
        return sum(values)

    def parseMultiplication(self):
        values = [self.parseParenthesis()]
        while True:
            self.skipWhitespace()
            char = self.peek()
            if char == '*':
                self.index += 1
                values.append(self.parseParenthesis())
            elif char == '/':
                self.index += 1
                denominator = self.parseParenthesis()
                if denominator == 0:
                    raise Exception(
                        "Division by 0 error ")
                values.append(1.0 / denominator)
            else:
                break
        value = 1.0
        for factor in values:
            value *= factor
        return value

    def parseParenthesis(self):
        self.skipWhitespace()
        char = self.peek()
        if char == '(':
            self.index += 1
            value = self.parseExpression()
            self.skipWhitespace()
            if self.peek() != ')':
                raise Exception(
                    "Need closing ) ")
            self.index += 1
            return value
        else:
            return self.parseNegative()

    def parseNegative(self):
        self.skipWhitespace()
        char = self.peek()
        if char == '-':
            self.index += 1
            return -1 * self.parseParenthesis()
        else:
            return self.parseValue()

    def parseValue(self):
        self.skipWhitespace()
        char = self.peek()
        if char in '0123456789.':
            return self.parseNumber()

    def parseNumber(self):
        self.skipWhitespace()
        strValue = ''
        char = ''

        while self.hasNext():
            char = self.peek()
            if char in '0123456789':
                strValue += char
            else:
                break
            self.index += 1

        if len(strValue) == 0:
            if char == '':
                raise Exception("Unknown end found")

        return float(strValue)


def evaluate(expression):
    try:
        p = Parser(expression)
        value = p.getValue()
    except Exception as ex:
        msg = ex.message
        raise Exception(msg)

    # Return an integer type
    if int(value) == value:
        return int(value)

    return value

# test cases
# print(evaluate("1 + 2 * 3"))
# print(evaluate("(1 + 2) * 3"))
# print(evaluate("-(1 + 2) * 3"))
