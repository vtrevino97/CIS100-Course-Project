print(f"Hello, everyone! I have a hilarious story to tell you about a pet. I'm excited to tell you all about it.")
print(f"Before I tell you the story, I have a few questions I would like to ask you.")
print(f"After typing your answer, please don't forget to press the enter key.")
input(f"\nPress the enter key to continue on.")

keepPlaying = "yes"
while keepPlaying.lower() == "yes":
    
    #5 Questions before the story begins
    petType = input(f"\nWhat type of pet is it:  ")
    while len(petType) == 0:
        petType = input(f"Please enter a pet type:  ")
    #Second Question
    petName = input(f"What is the pet's name:  ")
    while len(petName) == 0:
        petName = input(f"Please enter a pet's name:  ")
    #Third Question
    parkName = input(f"What park are you playing at:  ")
    while len(parkName) == 0:
        parkName = input(f"Please enter a park name:  ")
    #Fourth Question
    time = input(f"What time is it:  ")
    while not time.isdigit():
        time = input(f"Value is not recognized. Please enter a numeric value:  ")
    #Fifth Question
    foodType = input(f"What is your favorite food:  ")
    while len(foodType) == 0:
        foodType = input(f"Please enter a type of food:  ")
        
    #StoryStarts
    print(f"\nHERE WE GO EVERYONE!!")
    print(f"Long ago, there was a sparkling gray {petType} named {petName}.")
    print(f"{petName} loved to go to the {parkName} every day at {time} to play and enjoy the weather.")
    print(f"{petName} is hopping the trail looking for something to eat when suddenly he notices a huge bear glaring right at him.")
    print(f"He isn't sure what to do because he found {foodType} to eat.")
    
    #Decision 1
    hideFromBear = input(f"\nShould {petName} hide from bear?  Type yes or no:  ")
    while hideFromBear.lower() != "yes" and hideFromBear.lower() != "no":
        hideFromBear = input("Please type yes or no:  ")
        
    if hideFromBear == "yes":
        print(f"\n{petName} decides to hide from the bear and hops in the nearest bush in {parkName}.")
        print(f"He is really scared and hopes the bear will go away but.")
        print(f"the bear decides to walk towards {petName} to prank scare him.")
        print(f"He zooms away and screeches as he doesn't know what the bear wants.")
        print(f"The bear yells and chases him to let him know that he means no harm and just wants to play.")
        print(f"{petName} gets tired of running and decides to see what the bear wants.")
        print(f"After learning the truth from the bear, they start playing together and shortly become friends.")
    else:
        print(f"\n{petName} decides to approach the bear and see whether it is friendly or not.")
        print(f"The bear smiles and looks happier when {petName} approaches and says hello.")
        print(f"The bear says hello back and decides to ask if he would like to play at the {parkName}.")
        print(f"{petName} agrees to play with the bear but first shares {foodType} to get energized up.")
        print(f"After they finish eating, they run around the park together chasing the flies away.")
        
    print(f"\n{petName} and the bear are having fun playing when all of a sudden they notice an eagle watching them.")
    print(f"They stop playing and pause for a moment as they are unsure of what to do.")
    
    #Decision 2
    runAtEagle = input(f"\nShould the bear run at the eagle? Type yes or no:  ")
    while runAtEagle.lower() != "yes" and runAtEagle.lower() != "no":
        runAtEagle = input(f"Please type yes or no:  ")

    if runAtEagle == "yes":
        print(f"{petName} tells the bear he has a fear of eagles because they always chase him away.")
        print(f"The bear notices his friend's worried look and makes a quick decision by roaring and rushing towards the eagle.")
        print(f"The eagle screams in horror and flies away quickly.")
        print(f"{petName} gives his friend a big hug and says thanks. They both notice it is now {time} and they decide whether to call it a day.")
    else:
        print(f"\As they are playing, they notice a big eagle watching them.")
        print(f"They are both scared but the bear decides to distract the eagle and tells {petName} to run away but it doesn't seem to work.")
        print(f"The eagle quickly flies straight at {petName}, taunting him by being above his head.")
        print(f"The bear tries to scare the eagle away but nothing. Luckily ,the eagle noticed a snake nearby so he flew away in a hurry and left them alone.")
    
    #AlternateEndings
    if hideFromBear == "yes" and runAtEagle == "yes":
        print(f"\nWhat a day it was of hiding from a bear and almost being attacked by an eagle.")
        print(f"{petName} and the bear decide to leave the park. They head towards a nearby store in search for food.")
        print(f"All of that running around made them super hungry. {petName} finally finds a pizza and shares it with the bear.")
        print(f"The bear is thankful for meeting his new friend. After eating, they make plans to hang out the next day.")
    elif hideFromBear == "no" and runAtEagle == "no":
        print(f"\n{petName} and the bear choose to keep playing at the park and ignore the eagle.")
        print(f"After minutes go by, the eagle gets distracted with another animal in the park and disappears.")
        print(f"They see a possible friend nearby and decide to see if they would want to play too.")
        print(f"Their new friend agrees to play with them and next they jump in a pond to relax and cool off for awhile.")
    else:
        print(f"\{petName} hides from the bear and waits for it to go away.")
        print(f"The bear gets distracted with trash near it and runs away.")
        print(f"{petName} feels relief as the bear goes away and hops to a nearby chair to read a book.")
        print(f"As he's reading a book, a snake comes close and tries to bite him.")
        print(f"He screams and dashes out of the park faster than you would think. Once he sees the snake is gone, he walks home scared of what he will run into next.")
    print("\nThe End")
    
    keepPlaying = input(f"\nDo you want to play again? Enter yes or no:  ")
    while keepPlaying.lower() != "yes" and keepPlaying.lower() != "no":
        keepPlaying = input(f"Please type yes or no:  ")