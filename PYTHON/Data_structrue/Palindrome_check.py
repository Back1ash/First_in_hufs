class deque:
    items = []
    def __init__(self, s):
        for x in s:
            self.items.append(x)
    
    def append(self, c):
        self.items.append(c)

    def appendleft(self, c):
        self.items.insert(0, c)

    def pop(self):
        if len(self.items) == 1:
            return "last"
        return self.items.pop()
    
    def popleft(self):
        tmp = self.items[0]
        if len(self.items) == 1:
            return "last"
        for idx, val in enumerate(self.items):
            if idx == 0:
                pass
            else:
              self.items[idx-1] = self.items[idx]
        del self.items[-1]
        return tmp

    def __len__(self):
        return len(self.items)
    
    def right(self):
        return self.items[len(self.items) - 1]
    
    def left(self):
        return self.items[0]
    
def check_palindrome(s):
    dq = deque(s)
    palindrome = True
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            palindrome = False
    return palindrome

print(check_palindrome(input()))