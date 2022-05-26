from support import NoSupport, LimitSupport, SpecialSupport, OddSupport
from trouble import Trouble

def startMain():
    amatour = NoSupport("amatour")
    beginner = LimitSupport("workerA", 100)
    specialist = SpecialSupport("workerB", 429)
    Ubeginner = LimitSupport("workerC", 200)
    oddSupporter = OddSupport("Odd_supporter")
    senior = LimitSupport("workerD", 400)

    amatour.setNext(beginner).setNext(specialist).setNext(Ubeginner).setNext(oddSupporter).setNext(senior)

    for i in range(0, 500, 33):
        amatour.support(Trouble(i))

if __name__ == '__main__':
    startMain()