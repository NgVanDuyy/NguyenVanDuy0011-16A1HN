class Dog:

    Dogcount = 0   #Thuộc tính của lớp
    #Hàm khởi tạo đối tượng
    def __init__(self,name,size,age,color):
        self.name=name
        self.size=size
        self.age=age
        self.color=color

    def Go(self):   
        print("I'm going...")
    def Stay(self,place):    
        print("I'm staying at {}".format(place))
    def Lie(self,place):      
        print("I'm lying at{}".format(place))
    def Bark(self) :print("Whoop...")    
    
    def eat(self,food):
        print("I'm eating{}".format(food))

#
bull=Dog("bull","large",2,"green")
bull.stay("garden")
bull.Bark()
bull.go()
bull.eat("mean")