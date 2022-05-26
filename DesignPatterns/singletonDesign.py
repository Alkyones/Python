class Logger:
    _instance = None

    def __init__(self):
        self.__passwd = None
    
    def __new__(cls,):
        if cls._instance is None:
            print('object has been created.')
            cls._instance = super().__new__(cls)
        return cls._instance


log1 = Logger()
log2 = Logger()

print('They are same ' + str(log1 is log2))