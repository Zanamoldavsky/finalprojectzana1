# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
#To create this code, I referenced youtube videoes from
define e = Character("Eileen", color = "#FF0044", what_prefix ="", what_suffix = "")
image picture_1 = im.Scale("1.jpg", 1280, 720)
image parkpic = im.Scale("park.jpg", 1280, 720)
image phone = im.Scale("phone.jpg", 1280, 720)
image covid = im.Scale("covid.jpg", 1280, 720)
image starbucks = im.Scale("starbucks.jpg", 1280, 720)
image expelled = im.Scale("expelled.jpg", 1280, 720)
image class = im.Scale("class.jpg", 1280, 720)
image seat = im.Scale("seat.jpg", 1280, 720)
image cheese = im.Scale("cheese.jpg", 1280,720)
image pizza = im.Scale("pizza.jpg", 1280, 720)
image sleep = im.Scale("sleep.jpg", 1280, 720)
image potion = im.Scale("potion.jpg", 1280, 720)
image hole = im.Scale("hole.jpg", 1280, 720)
image success = im.Scale("success.png", 1280, 720)
image bye = im.Scale("bye.jpg", 1280, 720)
image playground = im.Scale("playground.jpg", 1280, 720)
image backtoschool = im.Scale("backtoschool.jpg", 1280, 720)

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene picture_1

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen at left

    # These display lines of dialogue.

    e "Hello!, welcome to your first day of school. Your only task is to not get expelled! Click to pick your path:"
    menu:
        "Skip class and go to and amusement park":
            call apark
        "Go to your first class":
            jump class
    hide picture_1




    # This ends the game.

    return

label apark:
    scene parkpic
    e "ride all the rollarcoasters you want!"
    #Enter picture of amusement park
    hide parkpic
    scene phone
    e "The school calls and asks why you aren't there"
    menu:
        "Say you have COVID":
            call covid
        "Tell the truth and confess to skipping":
            call truth
    hide phone
    return

label covid:
    scene covid
    e "The school is giving you two weeks off! where do you want to go?"
    menu:
        "Starbucks":
            call starbucks
        "The playground":
            call playground
    hide covid
    return

label starbucks:
    scene starbucks
    e "You run into a teacher there and they realize you lied about being sick! your expelled!"
    jump expelled
    hide starbucks
    return

label playground:
    scene playground
    e "You see your aunt at the playground and you quickly run back to school"
    call backtoschool
    return

label backtoschool:
    scene backtoschool
    e "You run back to school in time and no one notices you left!"
    call success
    return


label expelled: # rename to expelled
    scene expelled
    e "You've gotten expelled. Would you like to try again?"
    menu:
        "Yes, restart":
            jump start
        "No, goodbye":
            call goodbye
    hide expelled
    return

label redo:
    menu:
        "Yes, play again":
            jump start
        "No, goodbye":
            call goodbye
    return


label truth:
    e "Skipping is against the rules! You're expelled!"
    e "Do you want to try again?"
    menu:
        "Yes, restart":
            jump start
        "No, goodbye":
            call goodbye
    return




label class:
    scene class
    e "glad to have you here, choose your seat please"
    menu:
        "Sit in the front":
            call front
        "Sit in the back":
            call back
    hide class
    return



label front:
    #code front seat
    scene seat
    e "You learn so much! It's time for lunch now. What would you like to eat?"
    menu:
        "Take the last grilled cheese":
            call cheese
        "Eat a slice of pizza":
            call pizza
    hide seat
    return

label cheese:
    scene cheese
    e "The school bully wanted that grilled cheese and he started a fight. Fighting is against the rules!"
    call expelled
    hide cheese
    return

label pizza:
    scene pizza
    e "I hope you enjoyed your pizza, it's time for math."
    e "In math class you start to feel really sleepy and begin to doze off"
    menu:
        "Fall asleep":
            call asleep
        "Go get a coffee":
            call coffee
    hide pizza
    return

label coffee:
    scene starbucks
    e "Leaving class without asking is against the rules!"
    jump expelled
    hide starbucks
    return

label asleep:
    scene sleep
    e "Wake up! You're lucky no one saw you!"
    call success
    hide sleep
    return

label back:
    #code back seat
    scene seat
    e "You notice someone quiet sitting next to you, do you want to start a conversation?"
    menu:
        "Yes! new friends!":
            call friend
        "No, I'm an introvert":
            call introvert
    hide seat
    return

label friend:
    scene potion
    e "You start speaking to the kid and he pulls put a magic potion, do you drink it?"
    menu:
        "Yes, I'm curious":
            call potion
        "No! I dont take random drink from strangers":
            call success
    hide potion
    return

label potion:
    scene hole
    e "The potion gave you the ability to fly, and you flew straight threw the ceiling! Damaging property is illegal, you're expelled!"
    jump expelled
    hide hole
    return

label success:
    scene success
    e "Congratulations! you picked the smart decisions and made it through your first day! Would you like to play again?"
    menu:
        "Yes":
            jump start
        "No":
            jump goodbye
    hide success
    return
label introvert:
    e "Socializing is a vital part of school! your expelled"
    call expelled
    return

label goodbye:
    scene bye
    e "farewell!"
    jump end
    hide bye
    return
label end:
    return
