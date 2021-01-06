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

def compute_postfix(postfix):
	operand = Stack()
	token_list = postfix.split(" ")
	for token in token_list:
		if token == "+":
			operand.push(operand.pop() + operand.pop())			
		elif token == "-":
			operand.push(operand.pop() - operand.pop())			
		elif token == "*":
			operand.push(operand.pop() * operand.pop())			
		elif token == "/":
			a = operand.pop()
			b = operand.pop()
			operand.push(b / a)			
		elif token == "^":
			a = operand.pop()
			b = operand.pop()
			operand.push(b ^ a)			
		else:
			operand.push(int(token))
	return operand.pop()

postfix = input()
result = compute_postfix(postfix)
print(f"{result:.4f}")
