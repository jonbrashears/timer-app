import time

class baseTimer:
    worked = 0

    def __init__(self, defaultw):
        worked = defaultw

    def timer(self, clock):
        sec = 0
        while sec != clock*60:
            time.sleep(1)
            sec+=1
            
    def prompt(self):
        menu = "1"
        print("Timer is: ")
        print("w: %i" % self.worked)
        print("1. Set times")
        print("2. Start timers")
        print("q. quit")
        menu = input(">> ")
        return menu
	
    def getWorked(self):
        return self.worked
				
    def setTimer(self):
        self.worked = int(input("How long do you want to work for?  >> "))
  
    def choice(self):
        code = self.prompt()
        if code == "1":
            self.getTimer()
            return 1
        if code == "2":
            self.timer(self.worked)
            print("Worked for %i" % self.worked)
            return 1
        if code == "q" or code == "Q":
            return 0
        else:
            print("Invalid input")
            return 1
    
    
class pomodoro(baseTimer):
    worked = 0
    rested = 0
    
    def __init__(self, defaultw, defaultr):
        self.worked = defaultw
        self.rested = defaultr

    def prompt(self):
        menu = "1"
        print("Timers are: ")
        print("w: %i" % self.worked)
        print("w: %i" % self.rested)
        print("1. Set times")
        print("2. Start timers")
        print("q. quit")
        menu = input(">> ")
        return menu
		
    def getRested(self):
        return self.rested
		
    def setTimer(self):
        self.worked = int(input("How long do you want to work for?  >> "))
        self.rested = int(input("How long do you want to rest for?  >> "))
  
    def choice(self):
        code = self.prompt()
        if code == "1":
            self.getTimer()
            return 1
        if code == "2":
            self.timer(self.worked)
            print("Worked for %i" % self.worked)
            self.timer(self.rested)
            print("Rested for %i" % self.rested)
            return 1
        if code == "q" or code == "Q":
            return 0
        else:
            print("Invalid input")
            return 1

def main():
    print("Welcome to the pomodoro timer!")
    timer = pomodoro(1,1)
    #timer = baseTimer(1)
    timer.setTimer()

    count = 1
    while count != 0:
        count = timer.choice()

    input("Press enter to exit")

if __name__ == '__main__':
        main()
