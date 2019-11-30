"""class Ring(): Simple Fifo class implemented on a ring queue
    Ring.max_length {int} maximum length of queue before head overwrites tail (max_length == 0 indicates length of 1)
    Ring.length {int} Current length of queue
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
        self.tail_ptr = 0
        self.queue = list()

    def status(self):
        print('=========== Ring Queue Fifo status =========')
        print('max_length : ', self.max_length)
        print('Current length: ', self.length)
        if self.head_ptr == -1:
            print('head_ptr == -1, nothing to see here yet...')
        for i in range(0, self.length):
            print('(', i, ')  ', self.queue[i], '  ', end='')
            if i == self.head_ptr:
                print('<Head>', end='')
            if i == self.tail_ptr:
                print('<Tail>', end='')
            print()
        print('============================================')

    def add_head(self, item):
        self.head_ptr += 1
        if self.head_ptr >= self.length:
            if self.length == self.max_length:
                self.head_ptr = 0
                self.queue[0] = item
            else:
                self.queue.append(item)
                self.length += 1
                return
        else:
            self.queue[self.head_ptr] = item

        self.tail_ptr += 1
        self.tail_ptr %= self.max_length

    def pop_head(self):
        pass

    def pop_tail(self):
        pass

    def inspect_tail(self):
        pass

    def inspect_head(self):
        pass


if __name__ == '__main__':
    print('main executing...')

x = Ring(4)
x.status()
for j in range(1, 6):
    x.add_head(j)
    x.status()
