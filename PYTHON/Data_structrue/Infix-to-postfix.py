'''
Infix to postfix
'''


class Stack:
    def __init__(self):
        self.items = []

    def push(self, val):
        self.items.append(val)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            print("Stack is empty")

    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            print("Stack is empty")

    def __len__(self):
        return len(self.items)

    def isEmpty(self):
        return self.__len__() == 0


def infix_to_postfix(infix):

    opstack = Stack()
    outstack = []
    token_list = infix.split(' ')

    prec = {}
    prec['('] = 0
    prec['+'] = 1
    prec['-'] = 1
    prec['*'] = 2
    prec['/'] = 2
    prec['^'] = 2

    for token in token_list:
        if token == '(':
            opstack.push(token)
        elif token == ')':
            while opstack.top() != '(' and opstack.isEmpty() == False:
                outstack.append(opstack.pop())
            opstack.pop()
        elif token in '+-/*^':
            if len(opstack.items) == 0:
                opstack.push(token)
            else:
                priority = prec[token]
                r_list = reversed(opstack.items)
                count = 1
                for pre in r_list:
                    if prec[pre] > priority:
                        outstack.append(opstack.items.pop(0-count))
                    count += 1
                count = 0
                opstack.push(token)
        else:
            outstack.append(token)

    while opstack.isEmpty() == False:
        outstack.append(opstack.pop())

    return " ".join(outstack)


infix_expr = input()
postfix_expr = infix_to_postfix(infix_expr)
print(postfix_expr)
