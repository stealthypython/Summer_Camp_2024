def intro():
  print("Welcome to the Adventure game!")
  print("You find yourself in a mysterious place.")
  print("Which direction do you want to go?")
  print("left")
  print("right")
def player_choice():
    choice = input("Enter your choice: ")
    return choice
def handle_choice(choice):
  if choice == "left":
    print("You choose to go left..")
    print("As you walk to the left path..")
    print("You found a diamond! Let's keep it!!")
    print("Now we are in a branching path.")
    sub_choice = input("What is your sub choice? ").lower()
    if sub_choice == "left":
      print("We continued going left.. A village! Should we go in?")
      village = input("Make your decision... ")
      if village == "yes":
        print("You went in the village and found a witch that turned you into a frog.. GAME OVER!")
        exit()
      else:
        print("You decided not to go in the village and went on..")
    elif sub_choice == "right":
      print("We went right this time!")
      berries = input("Hmm... I'm hungry.. should we get berries? ")
      if berries == "yes":
        print("You ate the berries.. I don't feel so good...")
        print("You fainted and was found by a search team. GAME OVER!")
        exit()
      elif berries == "no":
        print("You did not eat the berries.. Let's find some other food!")
        branch = input("Another branching path? Where do we go? ")
        if branch == "right":
          print("You chose to go right..")
          print("As you walk to the right path..")
          cave = input("Ooh! A cave! Should we go in? ")
          if cave == "yes":
            print("You go in the cave..")
            print("You found a sword! Wonder what we could do with this...")
            print("We are in a branching path.")
            sub_choice = input("What is your sub choice? ").lower()
            if sub_choice == "left":
              print("You go left.. I am so hungry..")
              honey = input("Should we eat the honey? There's no bees... ")
              if honey == "yes":
                print("Delicious! The bees didn't see anyway...")
                home = input("You see your house across the mountains... Let's go.")
                print("You went home safely. Good Ending!")
              elif honey == "no":
                print("Too.. Hungry... You starved to death. GAME OVER!")
                exit()
            elif sub_choice == "right":
              print("You go right. I need food!")
              print("You found some berries! We  have to eat these or I'll faint...")
              print("Those berries were SO. GOOD.")
              print("You look across and see your house.. It's been a long day. Let's go home.")
              print("You made it home safely. Good Ending!")
            if cave == "no":
              print("You chose not to go in the cave.")
              print("You encountered a monster that ate you. GAME OVER!")
              exit()
  elif choice == "right":
    print("You chose to go right..")
    print("As you walk to the right path..")
    cave = input("Ooh! A cave! Should we go in? ")
    if cave == "yes":
      print("You go in the cave..")
      print("You found a sword! Wonder what we could do with this...")
      print("We are in a branching path.")
      sub_choice = input("What is your sub choice? ").lower()
      if sub_choice == "left":
        print("You go left.. I am so hungry..")
        honey = input("Should we eat the honey? There's no bees... ")
        if honey == "yes":
          print("Delicious! The bees didn't see anyway...")
          home = input("You see your house across the mountains... Let's go.")
          print("You went home safely. Good Ending!")
        elif honey == "no":
          print("Too.. Hungry... You starved to death. GAME OVER!")
          exit()
      elif sub_choice == "right":
        print("You go right. I need food!")
        print("You found some berries! We  have to eat these or I'll faint...")
        print("Those berries were SO. GOOD.")
        print("You look across and see your house.. It's been a long day. Let's go home.")
        print("You made it home safely. Good Ending!")
      if choice == "left":
        print("You chose to go left.")
      bee = input("You see a honeycomb. Should we eat it? ")
      if bee == "yes":
        print("That was so sweet! SUGAR RUSH!!!!!!!")
        print("You are very fast! POWER UP!")
        print("Whew.. You ran a lot! I'm tired. Let's go home.")
        print("You went home safely. Good Ending!")
  else:
    print("Invalid choice. Please try again.")
def main():
  intro()
  while True:
    choice = player_choice()
    handle_choice(choice)
main()
