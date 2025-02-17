
class Bank:
    name='BOB'
     

    def __init__(self,branch,city):
        self.branch=branch
        self.city=city
     
    def __str__(self):
        return f"bank details {self.branch} {self.city} , Bank Name {self.name}"
     
# creating an object

bankDemo= Bank("JP Nagar","BLR")


print(bankDemo.branch,bankDemo.city)