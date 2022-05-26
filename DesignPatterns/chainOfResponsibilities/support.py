from abc import ABCMeta, abstractmethod


class Support(metaclass=ABCMeta):
    # supportworkers name
    def __init__(self, name):
        self.__name = name
        self.__next = None

    # who is upper in the chain
    def setNext(self, next):
        self.__next = next
        return next
    # function of support how it works
    def support(self, trouble):
        if self.resolve(trouble):
            self.done(trouble)
        elif self.__next is not None:
            self.__next.support(trouble)
        else:
            self.fail(trouble)

    def __str__(self):
        return "[{0}]".format(self.__name)

    @abstractmethod
    def resolve(self, trouble):
        pass
    # if the problem is solved
    def done(self, trouble):
        print("{0} is resolved by {1}.".format(trouble, self))
    # if the problem is not solved
    def fail(self, trouble):
        print("{0} cannot be resolved.".format(trouble))

# they are ametours they can solve anything
class NoSupport(Support):
    def __init__(self, name):
        super(NoSupport, self).__init__(name)

    def resolve(self, trouble):
        return False
# person can check the all numbers untill it crosses their limit
class LimitSupport(Support):
    def __init__(self, name, limit):
        super(LimitSupport, self).__init__(name)
        self.__limit = limit

    def resolve(self, trouble):
        return True if trouble.getNumber() < self.__limit else False
# person check if the problem given trouble number is odd
class OddSupport(Support):
    def __init__(self, name):
        super(OddSupport, self).__init__(name)

    def resolve(self, trouble):
        return True if trouble.getNumber() % 2 == 1 else False
# person only checks if the given trouble number is equals to their number
class SpecialSupport(Support):
    def __init__(self, name, number):
        super(SpecialSupport, self).__init__(name)
        self.__number = number

    def resolve(self, trouble):
        return True if trouble.getNumber() == self.__number else False