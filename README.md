# Python_Peer_Group_170

Digital Pet – Python OOP Project

Group Work

This project is a Python-based group assignment focused on applying Object-Oriented Programming (OOP) principles to create a virtual pet.


---

Project Summary

We built a digital pet using Python's class structure. The pet can perform basic actions like eating, sleeping, and playing. It can also learn and showcase new tricks, making the interaction more dynamic and fun.


---

Key Components

Attributes

name: The pet’s given name

hunger: Ranges from 0 (well fed) to 10 (starving)

energy: Ranges from 0 (drained) to 10 (fully energized)

mood: Represents the happiness level, from 0 to 10

skills: A list of tricks the pet has learned


Methods

feed(): Decreases hunger and slightly lifts the pet's mood

nap(): Restores energy, capped at a maximum of 10

have_fun(): Boosts mood, consumes energy, and increases hunger a bit

show_status(): Displays current hunger, energy, and mood levels

learn(trick): Adds a new trick to the pet’s skills list

list_tricks(): Shows all tricks the pet has mastered



---

Sample Usage

my_pet = Pet("Zuri")

my_pet.feed()
my_pet.have_fun()
my_pet.nap()
my_pet.learn("roll over")
my_pet.learn("spin around")
my_pet.list_tricks()
my_pet.show_status()


---

Conclusion

This assignment helped us strengthen our understanding of how classes work in Python. It was fun and practical, giving us hands-on experience with constructors, methods, and state changes through an interactive digital pet.
