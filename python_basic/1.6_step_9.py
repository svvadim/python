import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))

class LoggableList(list,Loggable):
    def append(self, *args, **kwargs):
        self.log(*args, **kwargs)
        list.append(self, *args, **kwargs)
