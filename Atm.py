


class Atm:
    # whenever you create Variable in class define it in fuction called init()
    # init is constructor(special function)
    def __init__(self):
        
        self.pin=""  #Variable name pin
        self.balance=0 #Balance

        self.menu()  #Menu function

    #Method is Special function which is written in a class
    def menu(self):
        user_input=input(""" 
        Hello, How Would you like to proceed?
        1) Enter 1 to create pin
        2) Enter 2 to deposit
        3) Enter 3 to withdraw
        4) Enter 4 to check balance
        5) Enter 5 to Exit : """)    

        if user_input=="1":
            self.create_pin()
            self.menu() 
        elif user_input=="2":
            self.deposit() 
            self.menu()  
        elif user_input=="3":
            self.withdraw()
            self.menu()
        elif user_input=="4":
            self.Check_balance() 
            self.menu()
        else:
            print('Bye')

    def create_pin(self):
        self.pin=input('Enter Your PIN Number: ')
        print('Pin Set Successfully')
        

    def deposit(self):
        temp=input('Enter Your PIN Number: ')
        if temp==self.pin:
            amount=int(input('Enter Amount: '))
            self.balance=self.balance+amount
            print('Deposit Successfully')
        
        else:
            print('Invalid Pin')

    def withdraw(self):
        temp=input('Enter Your PIN Number: ')
        if temp==self.pin:
            amount=int(input('Enter Amount: '))
            if amount < self.balance:
               self.balance=self.balance-amount
               print('Withdraw Successfully')
            else:
                print('Insufficent Funds')

        else:
            print('Invalid Pin')

    def Check_balance(self):
        temp=input('Enter Your PIN Number: ')
        if temp==self.pin:
            print('Available Amount is',self.balance)
        else:
            print('Invalid Pin')


obj=Atm()