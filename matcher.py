# Нам даны строки, содержащие скобки 4 видов - круглые (), квадратные [], фигурные {} и угловые <>.
# Напишите функцию, которая проверяет, является ли последовательность скобок корректной:
# любая открывающая скобка должна иметь закрывающую того же типа где-то дальше по строке;
# пары скобок не должны пересекаться, хотя они могут быть вложенными.

# Выходные данные:
# 3 значения:
# Флаг корректности строки (True или False);
# Пару из символа и индекса в строке — скобка, на которой обнаружена ошибка;
# Пару из символа и индекса в строке — скобка, для которой не удалось найти закрывающую.

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
    return closeList


def isMatch(strMatch, openBr, closeBr):
    isCorrect = False
    firstIsOpen = False
    #print(strMatch)
    stack = []
    positions = []

    # отбросили лишнее оставили только скобки и запомнили номера в строке
    for i in range(len(strMatch)):
        if (strMatch[i] in openBr) or (strMatch[i] in closeBr):
            stack.append(strMatch[i])
            positions.append(i)

    #промежуточные итоги
    #print(stack)
    #print(positions)
    lenStack=len(stack)

#поудаляли парные скобки
    n2 = len(stack)*2
    for k in range(n2+1):
        for i in range(lenStack):
            for j in range(len(openBr)):
                if (i + 1) <= len(stack) and stack[i] in openBr and stack[i + 1] in closeBr:
                    if (stack[i] == openBr[j]) and (stack[i + 1] == closeBr[j]):
                        stack.pop(i)
                        stack.pop(i)
                        positions.pop(i)
                        positions.pop(i)

    #если скобок нет значит все хорошо
    if len(stack) == 0:
        isCorrect = True
        res="{}, None, None".format(isCorrect)
        return res
    else:
        isCorrect = False
        # если четное количество скобок
        if len(stack) % 2 == 0:
            for i in range(lenStack):
                if (i + 1) <= len(stack) and stack[i] in openBr and stack[i + 1] in closeBr:
                    res = "{}, ('{}',{}), ('{}',{})".format(isCorrect, stack[i+1],positions[i+1],stack[i], positions[i])
        # если количество скобок нечетное
        else:
            #Если одинокая скобка закрывающаяся
            if stack[len(stack)//2] in closeBr:
                res = "{}, ('{}',{}), None".format(isCorrect, stack[len(stack)//2],positions[len(stack)//2])
            #Если одинокая скобка открывающаяся
            else:
                res = "{}, None,('{}',{})".format(isCorrect, stack[len(stack)//2],positions[len(stack)//2])
        return res

stringForMatch = input("Введите строку для проверки: ")
#stringForMatch = "(a+[b*c]-{d/3})"
#stringForMatch = "(a+[b*c)-17]"
#stringForMatch = "(a+]b*c)-17"

brackets = input("Введите набор открывающихся скобок ([{<: ")
#brackets = "(["
openList = list(brackets)

closeList = formBrackets(openList)
isMatch(stringForMatch, openList, closeList)
print(isMatch(stringForMatch, openList, closeList))
