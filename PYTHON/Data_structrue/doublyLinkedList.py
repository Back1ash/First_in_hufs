class Node: # 1. class Node 선언 부분
	def __init__(self, key=None):
		self.key = key
		self.next = None
		self.prev = None
	def __str__(self):
		return str(self.key)

class DoublyLinkedList: # 2. class DoublyLinkedList 선언부분
	def __init__(self):
		self.head = Node()
		self.size = 0
	
	def splice(self, a, b, x):
		if a == None or b == None or x == None:
			return
		a.prev.next = b.next
		b.next.prev = a.prev
		
		x.next.prev = b
		b.next = x.next
		x.next = a
		a.prev = x
	
	def moveAfter(self, a, x):
		self.splice(a, a, x)

	def moveBefore(self, a):
		self.splice(a, a, x.prev)
	
	def insertBefore(self, a, key):
		new = Node(key)
		if a.prev == None:
			new.next = a
			new.prev = self.head
			self.head.next = new
		else:
			new.next = a
			new.prev = a.prev
			a.prev.next = new		
		a.prev = new

	def insertAfter(self, a, key):
		new = Node(key)
		if a.next == None:
			a.next = new
			new.next = self.head
		else:
			new.next = a.next
			a.next.prev = new
			a.next = new
		new.prev = a

	def pushFront(self, key):
		self.insertAfter(self.head, key)

	def pushBack(self, key):
		self.insertBefore(self.head, key)

	def deleteNode(self, x):
		if x == None or x == self.head:
			return
		x.prev.next = x.next
		x.next.prev = x.prev
		del x

	def popFront(self):
		if self.head == self.head.next:
			return None
		key = self.head.next.key
		self.deleteNode(self.head.next)
		return key	

	def popBack(self):
		if self.head == self.head.prev:
			return None
		key = self.head.prev.key
		self.deleteNode(self.head.prev)
		return key

	def search(self, key):
		v = self.head.next
		while v:
			tmp = v if v.key == key else None
			if tmp != None:
				break
			v = v.next
		return tmp

	def first(self):
		return self.head.next
	
	def last(self):
		return self.head.prev
	
	def isEmpty(self):
		return len(self) == 0
	
	def join(self, li):
		self.splice(li.head.next, li.head.prev, self.head.prev)

	def split(self):
		pass

	def printList(self):
		v = self.head
		print(f'h', end = " -> ")
		v = v.next
		while v.key:
			print(f"{v.key}", end = " -> ")
			v = v.next
		print('h')

L = DoublyLinkedList()
while True:
	cmd = input().split()
	if cmd[0] == 'pushF':
		L.pushFront(int(cmd[1]))
		print("+ {0} is pushed at Front".format(cmd[1]))
	elif cmd[0] == 'pushB':
		L.pushBack(int(cmd[1]))
		print("+ {0} is pushed at Back".format(cmd[1]))
	elif cmd[0] == 'popF':
		key = L.popFront()
		if key == None:
			print("* list is empty")
		else:
			print("- {0} is popped from Front".format(key))
	elif cmd[0] == 'popB':
		key = L.popBack()
		if key == None:
			print("* list is empty")
		else:
			print("- {0} is popped from Back".format(key))
	elif cmd[0] == 'search':
		v = L.search(int(cmd[1]))
		if v == None: print("* {0} is not found!".format(cmd[1]))
		else: print(" * {0} is found!".format(cmd[1]))
	elif cmd[0] == 'insertA':
		# inserta key_x key : key의 새 노드를 key_x를 갖는 노드 뒤에 삽입
		x = L.search(int(cmd[1]))
		if x == None: print("* target node of key {0} doesn't exit".format(cmd[1]))
		else:
			L.insertAfter(x, int(cmd[2]))
			print("+ {0} is inserted After {1}".format(cmd[2], cmd[1]))
	elif cmd[0] == 'insertB':
		# inserta key_x key : key의 새 노드를 key_x를 갖는 노드 앞에 삽입
		x = L.search(int(cmd[1]))
		if x == None: print("* target node of key {0} doesn't exit".format(cmd[1]))
		else:
			L.insertBefore(x, int(cmd[2]))
			print("+ {0} is inserted Before {1}".format(cmd[2], cmd[1]))
	elif cmd[0] == 'delete':
		x = L.search(int(cmd[1]))
		if x == None:
			print("- {0} is not found, so nothing happens".format(cmd[1]))
		else:
			L.deleteNode(x)
			print("- {0} is deleted".format(cmd[1]))
	elif cmd[0] == "first":
		print("* {0} is the value at the front".format(L.first()))
	elif cmd[0] == "last":
		print("* {0} is the value at the back".format(L.last()))
	elif cmd[0] == 'print':
		L.printList()
	elif cmd[0] == 'exit':
		break
	else:
		print("* not allowed command. enter a proper command!")
