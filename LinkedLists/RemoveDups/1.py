class Node:
    def __init__(self, val = None):
        self.next = None
        self.val = val


class LList:
    def __init__(self):
        self.Head = None
        self.size = 0

    def print_list(self):
        next = self.Head
        while next.next != None:
            print(str(next.val) + ' -> ', end='')
            next = next.next
        print(str(next.val))

    def insert_end(self, val):
        NewNode = Node(val)
        if self.Head == None:
            self.Head = NewNode
        else:
            next = self.Head
            while next.next != None:
                next = next.next
            next.next = NewNode
        self.size += 1

    def insert_start(self, val):
        NewNode = Node(val)
        if self.Head == None:
            self.Head = NewNode
        else:
            NewNode.next = self.Head
            self.Head = NewNode
        self.size += 1
    
    def delete(self, val):
        if self.Head == None:
            return
        elif self.Head.val == val:
            temp = self.Head
            self.Head = self.Head.next
            del(temp)
        else:
            prev = self.Head
            next = self.Head.next
            while next != None:
                if next.val == val:
                    temp = next
                    prev.next = next.next
                    del(temp)
                    break
                prev = next
                next = next.next
        self.size -= 1
    
    def remove_dups(self):
        H = [0 for i in range(self.size)]
        prev = self.Head
        next = self.Head.next
        H[prev.val%self.size] = 1
        while next != None:
            if H[next.val%self.size] > 0:
                temp = next
                prev.next = next.next
                next = next.next
                del(temp)
                self.size -= 1
                continue
            else:
                H[next.val%self.size] = 1
            prev = next
            next = next.next


if __name__ == '__main__':
    l = LList()
    l.insert_end(2)
    l.insert_end(3)
    l.insert_end(3)
    l.insert_end(1)
    l.insert_end(4)
    l.insert_start(109)
    l.insert_start(20)
    l.insert_end(9)
    l.insert_start(20)
    l.insert_end(4)
    l.insert_end(2)
    l.insert_end(3)
    l.print_list()
    l.remove_dups()
    l.print_list()
    print(l.size)