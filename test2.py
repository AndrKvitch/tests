# "+" реализации: исключена потеря данных
# "-" реализации: необходимость создания доп.буфера для хранения незаписанных данных, при скорости записи превышающей скорости чтения
class CircularBufferWithoutOverwrite:
    '''проверка содержания буфера'''
    def __init__(self, length):
        self.length = length
        self.buffer = [None] * length
        self.head = 0
        self.tail = 0

    def is_full(self):
        return self.buffer[self.head] is not None

    def is_empty(self):
        return self.buffer[self.head - 1] is None

    '''запись в буфер'''
    def put(self, item):
        if self.is_full():
            print('буфер заполнен')
            return
        self.buffer[self.head] = item
        if self.head == self.length - 1:
            self.head = 0
        else:
            self.head += 1
    '''выбор элемента из буфера по указателю tail, записывая None на его место'''
    def get(self):
        if self.is_empty():
            print('буфер пуст')
            return
        item, self.buffer[self.tail] = self.buffer[self.tail], None
        if self.tail == self.length - 1:
            self.tail = 0
        else:
            self.tail += 1
        return item

# "+" реализации: нет необходимости создания доп.очередей
# "-" реализации: при работе процесса отправляющего данных, превышающего запись будет потеря данных
class CircularBufferWithOverwrite:

    def __init__(self, length):
        self.buffer = [None] * length
        self.length = length
        self.head = 0
        self.tail = 0

    def is_empty(self):
        return self.buffer[self.head - 1] is None

    def put(self, item):
        self.buffer[self.head] = item
        if self.tail == self.head and self.buffer[self.head - 1] is not None:
            self.tail_shift()
        if self.head == self.length - 1:
            self.head = 0
        else:
            self.head += 1

    def get(self):
        if self.is_empty():
            return 'буфер пуст'
        item, self.buffer[self.tail] = self.buffer[self.tail], None
        self.tail_shift()
        return item

    def tail_shift(self):
        if self.tail == self.length - 1:
            self.tail = 0
        else:
            self.tail += 1