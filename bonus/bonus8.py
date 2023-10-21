date = input ("enter the date")
mood = input("Rate your today's mood from 1 to 10 scale")
journal = input("What's your thought today \n")

with open(f"../journal/{date}.txt","w") as file:
    file.write(mood)
    file.write(journal)
