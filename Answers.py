Peer_ Group_170

class Pet:
    def __init__(self, pet_name):
        # Set up the pet's name and initial state
        self.name = pet_name
        self.hunger = 5         # 0 = well fed, 10 = starving
        self.energy = 5         # 0 = exhausted, 10 = fully energized
        self.mood = 5           # Happiness level
        self.skills = []        # Tricks the pet can do

    def feed(self):
        # Feeding decreases hunger and boosts mood
        self.hunger = max(0, self.hunger - 3)
        self.mood = min(10, self.mood + 1)
        print(f"{self.name} ate some food. Hunger: {self.hunger}, Mood: {self.mood}")

    def nap(self):
        # Sleeping increases energy, but not beyond 10
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} took a nap. Energy is now {self.energy}")

    def have_fun(self):
        # Playtime uses energy, increases happiness, and makes the pet a bit hungry
        if self.energy >= 2:
            self.energy -= 2
            self.mood = min(10, self.mood + 2)
            self.hunger = min(10, self.hunger + 1)
            print(f"{self.name} had fun! Energy: {self.energy}, Mood: {self.mood}, Hunger: {self.hunger}")
        else:
            print(f"{self.name} is too tired to play right now.")

    def show_status(self):
        # Displays how the pet is doing
        print(f"\n[{self.name}'s Status]")
        print(f"Hunger: {self.hunger}/10")
        print(f"Energy: {self.energy}/10")
        print(f"Mood  : {self.mood}/10\n")

    def learn(self, new_trick):
        # Add a new skill to the pet’s list
        self.skills.append(new_trick)
        print(f"{self.name} learned how to {new_trick}!")

    def list_tricks(self):
        # Show all tricks the pet has learned
        if self.skills:
            print(f"{self.name} can do the following tricks:")
            for trick in self.skills:
                print(f"- {trick}")
        else:
            print(f"{self.name} hasn’t learned any tricks yet.")


# Sample usage block
if __name__ == "__main__":
    my_pet = Pet("Zuri")

    my_pet.show_status()
    my_pet.feed()
    my_pet.have_fun()
    my_pet.nap()
    my_pet.learn("roll over")
    my_pet.learn("spin around")
    my_pet.list_tricks()
    my_pet.show_status()
