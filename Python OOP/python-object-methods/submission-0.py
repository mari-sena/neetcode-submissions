class Pet:
    def __init__(self, name: str):
        self.name = name
        self.hunger = 5

    def feed(self):
        # TODO: Implement this method
        self.hunger -= 1
        # It should decrease the pet's hunger by 1
        print(f"{self.name} has been fed.")
        # and print a message about feeding the pet
        print(f"{self.name}'s hunger level: {self.hunger}")
        pass

# Create a pet
my_pet = Pet("Fluffy")
my_pet.feed()
my_pet.feed()
my_pet.feed()
# TODO: Feed the pet three times
