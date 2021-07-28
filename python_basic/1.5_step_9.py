class Buffer:
    def __init__(self):
        self.buffer = []

    def add(self, *a):
        for value in a:
            self.buffer.append(value)
            if len(self.buffer) == 5:
                print(sum(self.buffer))
                self.buffer.clear()

    def get_current_part(self):
        return self.buffer
