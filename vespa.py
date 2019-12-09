from machine import UART


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
        self.tail_ptr = 0
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
        if self.length < self.max_length and self.head_ptr == self.length - 1:  # still appending...
            self.queue.append(item)
            self.head_ptr += 1
            self.length += 1
        elif self.head_ptr == -1:  # queue exists but has been emptied
            self.head_ptr = 0
            self.tail_ptr = 0
            self.queue[0] = item
        else:
            self.head_ptr += 1
            self.head_ptr %= self.max_length
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

""" class TF03()
TF03() implements a read and write interface for a TF03 rangefinding Lidar
The class initiatises with two Ring objects, one as a ring buffer for range data and the other as a ring
buffer for messages from the TF03.  The TF03 intersperses responses to commands with the range data it returns
which it also seems to buffer internally.  The assumption is that there are only two ways to get fairly reliable
timestamps for range data.  One is to put the TF03 in single shot trigger mode and the other is to keep up with 
the constant stream of range datagrams that the device produces. Using a ring buffer and to exhaust the UART buffer 
and accumulate range measurement means that popping the range measurement at the head of the buffer (ie as a LIFO)
gives the most up to date measurement.  Responses to commands should be handled on a FIFO basis as the commands 
report the evolution of internal state in the TF03.

The TF03 can be configured to report ranges to objects that it senses in between a minimum and maximum range 
which will be important for acquiring weak lidar returns that would be ignored if swamped out by strong signals 
that would otherwise be in range.

TF03.__init__(self, CMD_buffer_size = 6, range_buffer_size = 20, UART_channel=2, baudrate=115200, data_bits = 8,
 stop_bit = 1, checksum = False)
                sets up the TF03 and the cmd and range message queues
TF03.read1() {success {boolean}, range {boolean}, datagram {bytearray}} Returns True on success, True if the 
                datagram is for range (False for response to command) and a bytearray that contains the range
                or command response Datagram.  This function returns a singe datagram.
TF03.read()  Reads all the data available (until the TF03 buffer is empty and/or until the cmd ring buffer is full?)
TF03.write() Writes a command to the TF03 
"""

class TF03:
    def __init__(self, CMD_buffer_size = 6, range_buffer_size = 20, UART_channel=2, UART_baudrate=115200,
                 UART_data_bits = 8, UART_stop_bit = 1, UART_parity = None):
        self.uart = UART(UART_channel)
        self.uart.init(baudrate = UART_baudrate, bits = UART_data_bits, parity = UART_parity, stop = UART_stop_bit)
        self.CMD_buf = Ring(CMD_buffer_size)
        self.range_buf = Ring(range_buffer_size)

    def read(self):
        pass




