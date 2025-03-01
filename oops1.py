class employee:
    def __init__(self):
        print("Started the data processing")
        self.id = 24
        self.salary = 60000
        self.designation = "python developer"
        print("Data processing completed")
    
    def travel(self,destination):
        print("this is calling manually")
        print(f"I am travelling to {destination}")
    
# __init__ is a constructor: when you login to the facebook the facebook connects to 
# to the cloud and various api's of ads etc.
# Create and object and istance of a class
sam = employee()
#print(sam.id)
#print(sam.salary)
sam.travel("Google office to work")

