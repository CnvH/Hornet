"""class Ring(): Simple Fifo class implemented on a ring queue
    Ring.max_length {int} maximum length of queue before head overwrites tail (max_length == 0 indicates length of 1)
    Ring.length {int} Current length of queue list
    Ring.size {int} Current number of items in list
    Ring.head_ptr {int} pointer to current head of queue, head_ptr == -1 indicates
    Ring.tail_ptr {int} pointer to current tail of queue
    Ring.add_head {item} adds item to queue.
    Ring.pop_head removes item from head.  returns {item}
    Ring.pop.tail removes item from tail. return {item}
    Ring.inspect_tail returns copy of item at tail with removal. return {item}
    Ring.inspect_head returns copy of item at tail with removal. return {item}
    Ring.status prints out all the queue information
    """


class Ring:
    def __init__(self, max_length=8):
        self.max_length = max_length
        self.length = 0
        self.head_ptr = -1
        self.tail_ptr = -1
        self.queue = list()

    def status(self):
        print('=========== Ring Queue Fifo status =========')
        print('max_length : ', self.max_length)
        print('Current length: ', self.length)
        if self.head_ptr == -1:
            print('head_ptr == -1, nothing to see here yet...')
        for i in range(0, len(self.queue)):
            print('(', i, ')  ', self.queue[i], '  ', end='')
            if i == self.head_ptr:
                print('<Head>', end='')
            if i == self.tail_ptr:
                print('<Tail>', end='')
            print()
        print('============================================')

    def add_head(self, item):  # this routine is not right!
        if self.head_ptr >= self.length:
            if self.length == self.max_length:
                self.head_ptr = 0
                self.queue[0] = item
            else:
                self.queue.append(item)
                self.head_ptr += 1
                self.length += 1
                return
        else:
            self.head_ptr += 1
            self.queue[self.head_ptr] = item
        if self.head_ptr == self.tail_ptr:
            self.tail_ptr += 1
            self.tail_ptr %= self.max_length

    def pop_head(self):
        if self.head_ptr == -1:  # this means queue is empty
            return False, False
        else:
            item = self.queue[self.head_ptr]
            if self.head_ptr == self.tail_ptr:
                self.head_ptr = -1  # queue now empty, reset queue
                self.tail_ptr = 0
            else:
                if self.head_ptr == 0:
                    self.head_ptr = self.length - 1
                else:
                    self.head_ptr -= 1
        return True, item

    def pop_tail(self):
        if self.head_ptr == -1:  # this means queue is empty
            return False, False
        else:
            item = self.queue[self.tail_ptr]
            if self.head_ptr == self.tail_ptr:
                self.head_ptr = -1  # queue now empty, reset queue
                self.tail_ptr = 0
            else:
                if self.tail_ptr == self.length:
                    self.tail_ptr = 0
                else:
                    self.tail_ptr += 1
        return True, item

    def inspect_tail(self):
        if self.head_ptr == -1:
            return False, False
        else:
            return True, self.queue[self.tail_ptr]

    def inspect_head(self):
        if self.head_ptr == -1:
            return False, False
        else:
            return True, self.queue[self.head_ptr]


if __name__ == '__main__':
    print('main executing...')

x = Ring(5)
x.status()
for j in range(1, 9):
    x.add_head(j)
    x.status()
print('Popped from Head : ', x.pop_head()[1])
x.status()

print('Popped from tail : ', x.pop_tail()[1])
x.status()

print('Popped from Head : ', x.pop_head()[1])
x.status()

print('Popped from Head : ', x.pop_head()[1])
x.status()

for j in range(1, 10):
    x.add_head(j)
    x.status()
