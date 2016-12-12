class Student:
    def __init__(self, name, hometown, age, height, favoriteicecreamflavor):
        self.name=name
        self.hometowm=hometown
        self.age=age
        self.height=height
        self.favoriteicecreamflavor=favoriteicecreamflavor
    def print_summery(self):
        print("hello my name is "+ str(self.name))
        print ("i live in " + str(self.hometown))
        print ("im " + str(age) +" years old")
        print ("and my favorite ice cream flavor is " + str(self.favoriteicecreamflavor))
    def get_giraffe_gap(self):
        return(500 - int(self.height))
