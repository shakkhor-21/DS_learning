class Human:
    def __init__(self, n, o):
        self.name = n
        self.occupation = o

    def do_work(self):
        if self.occupation == "Data Scientis":
            print(self.name , "loves python")
        elif self.occupation == "Data Analyst":
            print(self.name , "Loves Excel")

    def speaks(self):
        print(self.name , "How are you?")

tom = Human("tom larvae" , "Data Analyst")

tom.do_work()
tom.speaks()