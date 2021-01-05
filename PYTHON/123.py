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
    prec['+'] = 2
    prec['-'] = 2
    prec['*'] = 1
    prec['/'] = 1
    prec['^'] = 1

    for token in token_list:
        if token == '(':
            opstack.push(token)
        elif token == ')':
            while opstack.pop() != '(' and len(opstack.items) != 0:
              outstack.append(opstack.pop())
        elif token in '+-/*^':
            priority = prec[token]
            for pre in opstack.items:
              if prec[pre] <= priority:
                opstack.items.pop()
                outstack.append(token)
        else:
          outstack.append(token)

    while(opstack.items != []):
      outstack.append(opstack.pop())

    return " ".join(outstack)

	
infix_expr = input()
postfix_expr = infix_to_postfix(infix_expr)
print(postfix_expr)