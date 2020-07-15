from threading import *
from time import sleep

class BuyATicket():
    def __init__(self,availableSeats):
        self.availableSeats=availableSeats
        self.l = Lock()
    
    def buy(self,requestedSeats):
        self.l.acquire()
        print("Total number of seats available are: ",self.availableSeats)
        if requestedSeats<=self.availableSeats:
        
            print("Processing Ticket")
            print("Processing Payment")
            print("Printing Ticket") 
            self.availableSeats-=requestedSeats
        else:
            print("Sorry, You have to wait for the next bus")
        sleep(3)
        self.l.release()

obj = BuyATicket(10)

t1 = Thread(target=obj.buy,args=(3,))
t2 = Thread(target=obj.buy,args=(4,))
t3 = Thread(target=obj.buy,args=(5,))


t1.start()
t2.start()
t3.start()