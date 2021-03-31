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
def formBrackets(openList):
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

def isMatch(strMatch, openBr, closeBr):
    isCorrect = False
    firstIsOpen = False
    print(strMatch)
    stack = []
    positions = []
    depth = 0

    #отбросили лишнее оставили только скобки и запомнили номера в строке
    for i in range(len(strMatch)):
        if (strMatch[i] in openBr) or (strMatch[i] in closeBr):
           stack.append(strMatch[i])
           positions.append(i)
    #промежуточные итоги
    print(stack)
    print(positions)

    n=0
    lenStack = len(stack)
    while stack !="" or n < lenStack:
        for i in range(lenStack):
            for j in range(len(openBr)):
                if (i+1) <= len(stack) and stack[i] in openBr and stack[i+1] in closeBr:
                    if (stack[i]==openBr[j]) and (stack[i+1]==closeBr[j]):
                        stack.pop(i)
                        stack.pop(i)
                        positions.pop(i)
                        positions.pop(i)
                        n+=2
                        print(stack)
                        print(positions)
        print(i)
    return isCorrect


parseList = []
#stringForMatch = input("Введите строку для проверки: ")
#stringForMatch = "(a+[b*c]-{d/3})"
stringForMatch = "(a+[b*c)-17]"
#brackets = input("Введите набор открывающихся скобок ([{<: ")
brackets = "(["
openList = list(brackets)

#
#for i in range(len(bracketsList)):
#    print(ord(bracketsList[i]))
    #print(bracketsList[i])

closeList = formBrackets(openList)
print(openList)
print(closeList)
isMatch(stringForMatch,openList,closeList)
