#############################################
#       Object Oriented Python
#############################################
class Students:         #Craeting class
    def __init__(self,name,contact):     # Initaiting class propertices
        self.name= name
        self.contact = contact



    def getdate(self):
        print(' Raedy to Accept Data')
        self.name = input('Enter Name : ')
        self.contact = input('Enter Contact: ')

    def putdata(self):
        print('The name is  : '+self.name, '\nThis is  the contact: '+self.contact)

shakib = Students('blank',0)
shakib.getdate()
shakib.putdata()
