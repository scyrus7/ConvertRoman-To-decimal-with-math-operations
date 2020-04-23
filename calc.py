# Python program to convert Roman Numerals
# to Numbers
import StringParser

letters26 = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def helperForMain(s):
    return covertRomantoInteger(list(s), 0)


def covertRomantoInteger(s, index):
    ret = 0
    pre = s[index]
    ret = getValue(pre)

    for x in range(index + 1, len(s)):
        if compare(s[x], s[x - 1]) == 0:
            ret += getValue(s[x])
        elif compare(s[x], s[x - 1]) > 0:
            return covertRomantoInteger(s, x) - ret
        else:
            return ret + covertRomantoInteger(s, x)

    return ret


def compare(a, b):
    return letters26[a] - letters26[b]


def getValue(c):
    return letters26[c]


def checkOperation(incoming):
    operators = ['+', '-', '*', '%', '(', ')', '/']

    for element in range(0, len(incoming)):
        if incoming[element] in operators:
            return True

    return False


# Driver code
def main():
    print("Integer form of Roman Numeral is")
    x = list(map(str, input("Input your roman number or math operation: ").split()))
    inputString = ""

    for elem in range(0, len(x)):
        if checkOperation(x[elem]):
            inputString += x[elem]
        else:
            inputString += str(helperForMain(x[elem]))

    # print(eval(inputString))

    print(StringParser.evaluate(inputString))


if __name__ == "__main__":
    main()
