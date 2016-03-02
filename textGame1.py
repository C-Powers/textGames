'''
This is a text based game
Christopher Powers
Feb 10-2016
'''
import random
import sys

gameStartText1 = "You jolt awake from sleep. It's a warm night, denoted by the open windows and sweat stained sheets."
gameStartText2 = "You immediately look to the foot of your bed where your dog sleeps. She's rather small, but her there always calms your nerves. "
gameStartText3 = "She's not by your feet. You turn your head towards the alarm clock. It reads 2:42 am. "


print gameStartText1
print gameStartText2
print gameStartText3

fromBedChoice=raw_input("You now have 2 options. You may stay in bed, and cover your face with your sheets, or get up and look around the room. (yes/no).....")
choicesInBedroom = ' closet, desk, hallway.....'


#Choices available
#Each functions represents what can happen in each area of the house.
#within each function, some choices can be made.

#creates an element of chance for some choices
#if the survive random number is greater than or equal to the attack random number
#then the protagonist survives. Otherwise, they die, and the game ends.
def attackChance():
    attackNum=random.randint(0,20)
    surviveNum=random.randint(0,30)
    if surviveNum >= attackNum:
        print "----------"
        print "You check inside."
    elif surviveNum < attackNum:
        print "You are attacked, without the chance to defend yourself."
        sys.exit()


def from_bed(fromBedChoice):
    if fromBedChoice == "yes":
        print "You got out of bed. You're wearing a pair of underwear and a baggy shirt."
        print "Looking around the room, you see a closet, a bedside desk, and the door to your hallway."
        bedRoomChoice_fromBed = raw_input("Where would you like to go?" + choicesInBedroom)
        print "----------"
    elif fromBedChoice != "yes":
        print "You eventually fall back to sleep once your heart rate returns to normal."
        print "You do not know why you awoke, and you never will."
        print "----------"
    return bedRoomChoice_fromBed

def bedroom():
    print "You have reentered your bedroom."
    print "Looking around the room, you see a closet, a bedside desk, and the door to your hallway."
    choice = raw_input("Where would you like to go?" + choicesInBedroom)
    print "----------"
    return choice

has_rifle=False #we define this as false initially, due to the fact that the protagonist would not have the rifle if they have not searched for it
def bedroomCloset():
    print "You have a small closet. There's clothes neatly hung on the rack."
    print "On the ground, you have dirty laundry in a basket, as well as some sports gear in a bag."
    rifleStr=raw_input("Leaning against the wall is bolt action rifle. Would you like to take it? (yes/no).....")
    if rifleStr=="yes":
        has_rifle=True
    elif rifleStr=="no":
        has_rifle=False
    choice=raw_input("Where would you like to go from here? " + choicesInBedroom)
    print "----------"
    return choice, has_rifle
    #We return the choice of the protagonist, and whether or not they have the rifle

has_bullets=False #Protagonist has not searched for the bullets initially
def bedroomDesk():
    print "Your desk is immediately next to your bed."
    print "Rested on top is an alarm clock, now reading 2:45am, a glass of half-full water, and a pen."
    print "Inside of your desk are more pens, various papers, as well as three bullets."
    bulletsStr=raw_input("Under a doodle there lay three bullets that go with your rifle. Would you like to take them? (yes/no).....")
    if bulletsStr == "yes":
        has_bullets=True
    elif bulletsStr == "no":
        has_bullets=False
    choice = raw_input("Where would you like to go from here? " + choicesInBedroom)
    print "----------"
    return choice, has_bullets
    #we return the next choice of the protagonist, as well as whether or not they have bullets

choices_inHallway="bedroom, bathroom, livingroom....."
def hallway():
    print "You are now inside of the hallway, and have closed the door behind you."
    print "There are 2 closed doors and a living room."
    choice = raw_input("Where would you like to go? " + choices_inHallway)
    print "----------"
    return choice


def bathroom():
    print "You open the door to the bathroom, and turn on the lights."
    print "Immediately to your left there is a bathtub/shower with the curtain closed. Further along that wall there is a toilet. "
    print "To your left there is a towel rack and a sink. The sink seems to have a leak, and emits two consistent drips every second."
    curtainChoice = raw_input("Would you like to check behind the shower curtain before you leave? (yes/no).....")
    if curtainChoice == "yes":
        print "You listen for a moment, creating the courage to check behind the curtain."
        print "Because of the drip, you are not able to hear any other sounds. "
        attackChance()
        print "You have successfully checked behind the curtain, and have found that nothing lies behind it."
        print "----------"
        return 'hallway'
    elif curtainChoide == "no":
        print "You have decided not to check behind the curtain, and instead leave the bathroom."
        print "----------"
        return 'hallway'


choices_livingroom=" hallway, backdoor, frontdoor, sittingArea, kitchen....."
def livingroom():
    print "You have entered the livingroom."
    print "Near the backdoor there is a piano."
    print "Immediately in front of the hallway is a sitting area. One couch and one arm chair. Slightly left of that there is a small table."
    print "To the left of the hallway there is the front door, as well as the entranceway to the kitchen."
    choice = raw_input("Where would you like to look first?  " +  choices_livingroom)
    print "----------"
    return choice


def sittingArea():
    print "You have entered the sitting area."
    print "Upon immediate inspection, you see nothing strange. The couch pillows and blankets are tossed slightly, however."
    choice = raw_input("Where would you like to go, now?" + choices_livingroom)
    print "----------"
    return choice

def backdoor():
    print "There is a switch near the door, which you flip to turn on the backyard light."
    print "Due to the night's heat, you have left the door open, other than the metal screen."
    print "The light casts a yellow glow, illuminating the deck, and the first 15 feet of the grassy area. "
    print "You can now see outside. Beyond the grass there is an encapsulating darkness of the forrest."
    print "You listen for a moment, but all you hear is the faint rustling of the pine trees due to the light wind."
    print "You open the door, and step outside, leaving the door open behind you."
    print "During stronger gusts, you can hear a faint thud, and the sporadic shake of branches."
    checkNoise = raw_input("Would you like to check out the noise? (yes/no).....")
    print "----------"
    if checkNoise=="yes":
        print "You walk slowly towards the noise."
        print "You can't see far, but a partial moon lights up the way just enough so that you're not blind."
        print "As you get closer towards the noise, you realize that it is bag hanging from a rope."
        print "The rope swinging and catching the branches is what is creating the sporadic shake."
        print "The rope and bag are within reach."
        checkBag = raw_input("Would you like to untie the rope and check inside the bag? (yes/no).....")
        print "----------"
        if checkBag=='yes':
            print "You walk closer to the bag, and begin to untie."
            print "As you untie the bag, it falls creating a dull thud as it hits the ground."
            print "You bend over to check inside of the bag. "
            attackChance()
            print "You find your dog, decapitated."
            print "In a moment of horror, you run inside, slamming and locking the door behind you."
            print "You stand leaning against the door."
        elif checkBag=="no":
            print "You turn around and walk quickly back inside, shutting and locking the door behind you. "
    elif checkNoise=="no":
        print "You return inside, shutting and locking the door behind you."
    print "----------"
    choice = 'livingroom'
    return choice

def frontdoor():
    print "----------"
    print "You walk towards the front of the house, and flip on the light switch."
    print "As you open the door, you notice that the light is not working."
    print "You turn around, and flip the switch on and off to double check. It must be burnt out."
    print "Looking outside, you see a short concrete walkway onto a black paved driveway. "
    print "The moon illuminates the scene. Your car is parked where you left it. Your flowers look undisturbed."
    print "The trees beyond the driveway are as dark as ever."
    print "You live a few miles from your sisters house."
    getCar=raw_input("Would you like to go to your car, and leave your home? (yes/no).....")
    if getCar == "yes":
        print "----------"
        print "You begin to walk outside, before remembering that you don't have your keys on you."
        print "You step inside for a moment, grabbing your keys and shutting and locking the door."
        print "You walk slowly outside, looking around and taking the time to see the things around you."
        attackChance()
        print "As remotely unlock the car, the lights flash and create the illusion of shapes darting in and out as the darkness receeds and returns. "
        print "You enter the driver's seat."
        if has_rifle == True:
            print "You set the rifle in the passenger seat and put the keys into the ignition."
        else:
            print "You put the keys into the ignition."
        print "You shut the door, locking the car behind you."
        print "You turn the keys, and the car begins to sputter and churn, but the engine does not start."
        print "You try again, three more times, and no luck."
        print "Now in a fit, you bang the steering wheel, and quickly walk back into your house."
    elif getCar == "no":
        print "You close the door, locking it behind you."
    choice = 'livingroom'
    return choice

def kitchen():
    print "You have entered the kitchen."
    print "As you turn on the light, a gust of wind blows through an open window clanging your pots and pans."
    print "After the sound dampens, all there is left to hear is the humming of the refridgerator."

    print "----------"
    return 'livingroom'


#this is where the game begins.
#Initial event
event=from_bed(fromBedChoice)

#these noises give a sense of how much time has passed, and what will happen to the protagonist
noises = [
"There is a small bang, as if a gust of wind rattled the windows",
"The house creaks, creating a caskade of noise from  floor to ceiling. ",
"You hear rattling in the kitchen.",
"You hear a creak and a bang, as if an old cabinet were opened.",
"Tinnitis rings in your ears at the same moment you catch a shadow in the corner of your eye."
]

#this creates a function such that a random string will be printed at the end of each choice made.
def randNoise():
    randN=random.randint(0, 4)
    print noises[randN]


#this loop exists to end the game.
#without it, it would continue forever, and it allows us to continue the game with decisions.
#There is no reason 10 was chosen. Useful for debugging/testing.
for i in range(0, 15):
    randNoise()
    if event == "bedroom":
        print "You walk towards the bedroom and open the door."
        event=bedroom()
    elif event == "closet":
        print "You look at the closet."
        event, has_rifle=bedroomCloset()
    elif event == "desk":
        print "You look towards the desk."
        event, has_bullets=bedroomDesk()
    elif event == "hallway":
        print "You walk towards the hallway, and open the door."
        event = hallway()
    elif event == "bathroom":
        print "You walk towards the bathroom, and open the door."
        event = bathroom()
    elif event == "livingroom":
        print "You walk into the livingroom, and look around."
        event = livingroom()
    elif event == "sittingArea":
        print "You walk towards the sitting area."
        event = sittingArea()
    elif event == 'backdoor':
        print "You walk towards the backdoor."
        event = backdoor()
    elif event == 'frontdoor':
        print "You walk towards the frontdoor."
        event = frontdoor()
    elif event == 'kitchen':
        print "You walk towards the kitchen."
        event = kitchen()
    else:
        print "You stand there motionless, listening for sounds."

    #Use this to demonstrate how much "time" is left in the game.
    if i <=5:
        print "You fell a lingering presence of urgency."
    elif i<=10:
        print "You feel a strong sense of urgency."
    elif i<=15:
        print "You feel an immediate sense of urgency."
