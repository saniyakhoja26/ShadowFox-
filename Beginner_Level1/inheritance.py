"""
Task Level: Beginner
Internship: ShadowFox Python Development
Name: Saniya Khoja
Task: Inheritance
"""


# Base class
class MobilePhone:
    def __init__(
        self,
        screen_type,
        network_type,
        dual_sim,
        front_camera,
        rear_camera,
        ram,
        storage,
    ):
        self.screen_type = screen_type
        self.network_type = network_type
        self.dual_sim = dual_sim
        self.front_camera = front_camera
        self.rear_camera = rear_camera
        self.ram = ram
        self.storage = storage

    def make_call(self):
        print("Making a call...")

    def receive_call(self):
        print("Receiving a call...")


# child class
class Apple(MobilePhone):
    def __init__(self, model):
        super().__init__("Touch Screen", "5G", False, "12MP", "48MP", "6GB", "128GB")
        self.model = model

    def show_details(self):
        print("Apple Model:", self.model)
        print("Screen Type:", self.screen_type)
        print("Network Type:", self.network_type)
        print("Dual SIM:", self.dual_sim)
        print("RAM:", self.ram)
        print("Storage:", self.storage)
        print()


# Child class
class Samsung(MobilePhone):
    def __init__(self, model):
        super().__init__("Touch Screen", "5G", True, "10MP", "64MP", "8GB", "256GB")
        self.model = model

    def show_details(self):
        print("Samsung Model:", self.model)
        print("Screen Type:", self.screen_type)
        print("Network Type:", self.network_type)
        print("Dual SIM:", self.dual_sim)
        print("RAM:", self.ram)
        print("Storage:", self.storage)
        print()


# Creating objects
iphone = Apple("iPhone 14")
samsung_phone = Samsung("Galaxy S23")

iphone.show_details()
iphone.make_call()

samsung_phone.show_details()
samsung_phone.receive_call()

print("\n---------------------------------------\n")
