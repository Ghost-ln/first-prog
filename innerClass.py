# class Outer:
#     def __init__(self):
#         self.name = "Emil"

#     class Inner:
#         def __init__(self,outer):
#             self.outer = outer

#         def display(self):
#             print(f"The outer is: {self.outer.name}")

# outer = Outer()
# inner = outer.Inner(outer)
# inner.display()

class car:
    def __init__(self, brand,model):
        self.brand = brand
        self.model = model
        self.engine = self.Engine()

    class Engine:
        def __init__(self):
            self.status = "Off"
            

        def start(self):
            self.status = "running"
            print("Start the Engine")

        def stop (self):
            self.status = "off"
            print("Stop the Engine")

    def drive(self):
        if self.engine.status == "running":
            print(f"The car {self.brand}: {self.model} is driving")
        else:
            print("Start the engine first")
c1 = car("Suzuki","Fronx")
c1.drive()
c1.engine.start()
c1.drive()
        