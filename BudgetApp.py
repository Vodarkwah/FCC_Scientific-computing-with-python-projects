class Category:

    def __init__(self,name):    # Constructor
        self.name=name
        self.ledger=[]

    def __str__(self):  # returns the string representation of the object
        title=f"{self.name:*^30}\n" #formatted string
        items=""
        total=0
        for item in self.ledger:
            items+=f"{item['description'][0:23]:23}" + f"{item['amount']:>7.2f}" +'\n' # ends description on char 23
            total+=item['amount']      #adds amounts                                   # amount in 2 dp
    
        output = title+items+"Total: "+str(total)
        return output



    def deposit(self, amount, description=""):
        self.ledger.append({"amount":amount,"description":description})


    def withdraw(self,amount, description=""):
            # negates val of amt in dic
        if self.check_funds(amount):
            self.ledger.append({"amount":-amount,"description":description})
            return True #returns true if it appends all -ive amount
        return False    #retruns false if amt val is +ive
        
    
  
    def get_balance(self):
        remaining_cash= 0
        for item in self.ledger:
            remaining_cash+=item["amount"] # add all the amts in list
        return remaining_cash   #returns the balance
   
    
  
    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount,"Transfer to "+category.name)  #i.e if amount is -ive
            category.deposit(amount,"Transfer from "+self.name)
            return True
        return False
        
  

    def check_funds(self,amount):
        if self.get_balance()>=amount:
            return True
        return False
    
    def get_withdraw(self):
        totals=0
        for item in self.ledger:
            if item["amount"] < 0:
                totals += item["amount"]
        return totals
    
# Production of chart
# (Got help from the FCC forum)
def truncate(n):
    multiplier=10
    return int(n*multiplier)/multiplier

def getTotals(categories):
    total=0
    breakdown=[]
    for category in categories:
        total+= category.get_withdraw()
        breakdown.append(category.get_withdraw())
    rounded=list(map(lambda x: truncate(x/total), breakdown))
    return rounded

def create_spend_chart(categories):
    res="Percentage spent by category\n"
    i=100
    totals=getTotals(categories)
    while i>=0:
        category_spaces= " "
        for total in totals:
            if total*100>=i:  
                category_spaces+="o  "
            else:
                category_spaces+="   "
        
        res+=str(i).rjust(3) +"|" + category_spaces + "\n"
        i-=10
    
    dashes="-"+"---"*len(categories)
    names=[]
    x_axis=""
    for category in categories:
        names.append(category.name)
    
    maxi=max(names, key=len)

    for x in range(len(maxi)):
        nameStr='     '
        for name in names:
            if x>= len(name):
                nameStr+="   "
            else:
                nameStr+=name[x]+"  "
        
        if x != len(maxi)-1:
            nameStr+='\n'
        
        x_axis+=nameStr

    res+=dashes.rjust(len(dashes)+4)+'\n'+x_axis
    return res



