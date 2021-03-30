#Нам даны строки, содержащие скобки 4 видов - круглые (), квадратные [], фигурные {} и угловые <>.
#Напишите функцию, которая проверяет, является ли последовательность скобок корректной:
#любая открывающая скобка должна иметь закрывающую того же типа где-то дальше по строке;
#пары скобок не должны пересекаться, хотя они могут быть вложенными.

#Входные данные:
#строка для проверки;
#список скобок, которые нужно проверять.

#Выходные данные:
#3 значения:
#Флаг корректности строки (True или False);
#Пару из символа и индекса в строке — скобка, на которой обнаружена ошибка;
#Пару из символа и индекса в строке — скобка, для которой не удалось найти закрывающую.
#40 91 123 60 ([{<
#41 93 125 62 )]}>
def isMatch(strMatch, *brackets):
    isCorrect = True
    for ch in strMatch:
       print(strMatch)
    print(*brackets)

def formBrackets(closeList):
    closeList = []
    for ch in openList:
        if ch == "(":
            closeList.append(")")
        elif ch == "{":
            closeList.append("}")
        elif ch == "[":
            closeList.append("]")
        elif ch == "<":
            closeList.append(">")
    #brList.sort()
    #print(closeList)
    return closeList

parseList = []

#stringForMatch = input("Введите строку для проверки: ")
brackets = input("Введите набор открывающихся скобок ([{<: ")
openList = list(brackets)

#
#for i in range(len(bracketsList)):
#    print(ord(bracketsList[i]))
    #print(bracketsList[i])
print(openList)
closeList = formBrackets(openList)
print(closeList)

