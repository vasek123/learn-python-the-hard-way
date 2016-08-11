print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
    print "There's a giant bear here eating a cheese cake. What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."

    bear = raw_input("> ")

    if bear == "1":
        print "The bear eats your face off. Good job!"
    elif bear == "2":
        print "The bear eats your legg off. Good job!"
    else:
        print "Well, doing %s is probably better. Bear runs away." % bear

elif door == "2":
    print "There's a duck relaxing on a beach. What do you do?"
    print "1. Chill"
    print "2. Beach Football"
    print "3. Cheese cake"

    duck = raw_input("> ")

    if duck == "1" or duck == "2":
        print "You're having a great day at beach! Good job!"
    else:
        print "You don't have the ingredients to make cheese cake, so you play beach football! Good job!"

else:
    print "You turn around and escape from ladies rest room! Good job!"
