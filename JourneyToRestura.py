from random import randint
from time import sleep

gold = 0
lantern = 0
sword = 0
map_1 = 0
map_2 = 0
sword_2 = 0
donkey = 0
items_lost = 0
tired = 0
lost = 0
kills = 0
response = 0



print("""
     ▄█  ▄██████▄  ███    █▄     ▄████████ ███▄▄▄▄      ▄████████ ▄██   ▄            ███      ▄██████▄  
    ███ ███    ███ ███    ███   ███    ███ ███▀▀▀██▄   ███    ███ ███   ██▄      ▀█████████▄ ███    ███ 
    ███ ███    ███ ███    ███   ███    ███ ███   ███   ███    █▀  ███▄▄▄███         ▀███▀▀██ ███    ███ 
    ███ ███    ███ ███    ███  ▄███▄▄▄▄██▀ ███   ███  ▄███▄▄▄     ▀▀▀▀▀▀███          ███   ▀ ███    ███ 
    ███ ███    ███ ███    ███ ▀▀███▀▀▀▀▀   ███   ███ ▀▀███▀▀▀     ▄██   ███          ███     ███    ███ 
    ███ ███    ███ ███    ███ ▀███████████ ███   ███   ███    █▄  ███   ███          ███     ███    ███ 
    ███ ███    ███ ███    ███   ███    ███ ███   ███   ███    ███ ███   ███          ███     ███    ███ 
█▄ ▄███  ▀██████▀  ████████▀    ███    ███  ▀█   █▀    ██████████  ▀█████▀          ▄████▀    ▀██████▀  
▀▀▀▀▀▀                          ███    ███                                                              
""")
sleep(3)
print("     ▄████████    ▄████████    ▄████████     ███     ███    █▄     ▄████████    ▄████████ ")
sleep(0.2)
print("    ███    ███   ███    ███   ███    ███ ▀█████████▄ ███    ███   ███    ███   ███    ███ ")
sleep(0.2)
print("    ███    ███   ███    █▀    ███    █▀     ▀███▀▀██ ███    ███   ███    ███   ███    ███ ")
sleep(0.2)
print("   ▄███▄▄▄▄██▀  ▄███▄▄▄       ███            ███   ▀ ███    ███  ▄███▄▄▄▄██▀   ███    ███ ")
sleep(0.2)
print("  ▀▀███▀▀▀▀▀   ▀▀███▀▀▀     ▀███████████     ███     ███    ███ ▀▀███▀▀▀▀▀   ▀███████████ ")
sleep(0.2)
print("  ▀███████████   ███    █▄           ███     ███     ███    ███ ▀███████████   ███    ███ ")
sleep(0.2)
print("    ███    ███   ███    ███    ▄█    ███     ███     ███    ███   ███    ███   ███    ███ ")
sleep(0.2)
print("    ███    ███   ██████████  ▄████████▀     ▄████▀   ████████▀    ███    ███   ███    █▀  ")
sleep(0.2)
print("    ███    ███                                                    ███    ███              ")


sleep(2)
while response == 0:
    menu_choice = input("""
    Menu
    Press 1 to start
    Press 2 to exit
    """)
    if menu_choice == "1":
        response += 1
        print("Starting game...")
        sleep(5)
        input("(Press enter to continue...)")
        print("""
        As you regain your consciousness, you realize that you are lying on the hard dirt ground.""")
        input("")
        print("""
        You slowly open your eyes...""")
        input("")
        print("""
        You take a moment to take in your surroundings. Nothing at all looks familiar to you. You realize that you have 
        somehow ended up in a completely new place. Looking around, you notice a small shop that you decide to head 
        towards to ask for some help.""")
        input("")
        print("""
        Shopkeeper: Welcome, traveller.""")
        input("")
        print("""
        You ask the shopkeeper where you are.""")
        input("")
        print("""
        Shopkeeper: Hm? What a strange question. We're near the edge of the Arian Province in the Kingdom of 
        Restura.""")
        input("")
        print("""
        He points to an area on a map. Strangely, nothing on the map is recognizable to you.""")
        input("")
        print("""
        Shopkeeper: What's with that look on your face? Well, anyways, I take it you travel a lot. Why not buy something 
        that may help you on your way?""")
        input("")
        print("""
        You check your pockets and find some money, but the currency looks different to you as well.""")
        input("")

        response_shop = 0
        while response_shop == 0:
            item_bought = input("""
        Shopkeeper: So, what'll it be?
        Buy sword: 1
        Buy lantern: 2
        Buy old map: 3
        """)
            if item_bought == "1":
                response_shop += 1
                print("""
        You bought the sword and some supplies.""")
                sword = 1
            elif item_bought == "2":
                response_shop += 1
                print("""
        You bought the lantern and some supplies.""")
                lantern = 1
            elif item_bought == "3":
                response_shop += 1
                print("""
        You bought the mysterious old map and some supplies.""")
                map_1 = 1
        input("")
        print("""
        Shopkeeper: Pleasure doing business with you.""")
        print("""
        You leave the shop.""")
        input("")
        print("""
        You keep heading down the path that led to the shop.""")
        print("""
        Eventually, you find yourself entering a large forest.""")
        input("")
        print("""
        After walking for a while, you notice that the sun is starting to set.""")
        input("")
        print("""
        Something about this forest feels off to you. Maybe its a good idea to set up camp for the night, you think to 
        yourself.""")
        input("")
        print("""
        On the other hand, you could make a lot more progress if you kept walking through the night.""")
        input("")
        response_forest = 0
        while response_forest == 0:
            forest_choice = input("""
        Set up camp = 1
        Keep going = 2
        """)
            if forest_choice == "1":
                response_forest = 1
            elif forest_choice =="2":
                response_forest = 1
        if forest_choice == "1":
            print("""
        You decide to set up camp for the night.""")
            input("")
            print("""
        Strange noises coming from the trees only help to confirm your suspicion that traveling at night would not be 
        safe. After starting a fire, you lie down and gaze up at the night sky.""")
            input("")
            print("""
        You cannot help but wonder how you ended up in this situation.""")
            input("")
            print("""
        Well, nothing to do now but keep pressing forward.""")
            input("")
            print("""
        You close your eyes and soon drift off into sleep.""")
            input("...")
            sleep(5)
        elif forest_choice == "2":
            tired = 1
            print("""
        You decide to keep going.""")
            input("")
            print("""
        It quickly becomes almost impossible to see as even the moonlight is blocked by layers of trees.""")
            input("")
            if lantern == 1:
                print("""
        Thank God for this lantern, you think to yourself as you pull it out and light up your path.""")
                input("")
                print("""
        As you keep walking, you cannot help but wonder how you ended up in this situation.""")
                input("")
                print("""
        Well, nothing to do now but keep pressing forward.""")
            else:
                print("""
        Despite the strange noises that you are hearing, you keep pressing forward.""")
                input("")
                print("""
        Suddenly, a goblin leaps out the trees!""")
                if sword == 1:
                    print("""
        You draw your sword.""")
                    monster_attack = (randint(1, 21) + 5)
                else:
                    print("""
        You ready yourself for battle.""")
                    monster_attack = randint(1, 21)
                print("""
        The battle begins.""")
                input("")
                print("""
        The goblin is quick. It leaps around, waiting for an opening.""")
                input("")
                print("""
        You try your best to keep up with its movements, however soon you start to get dizzy.""")
                input("")
                print("""
        The goblin snarls at you as you start to miss its movements.""")
                input("")
                print("""
        In an instant, it jumps at you with its claws pointed straight ahead.
        You stand firm and ready yourself...""")
                input("")
                if monster_attack < 7:
                    print("""
        Before you can attack, the goblin lands its lunge at full speed.""")
                    input("")
                    print("""
        You stumble to the ground as the goblin draws near.""")
                    input("")
                    print("""
        You think about the family that you had to get back to.""")
                    input("")
                    print("""
        Saying a final prayer, you close your eyes as the goblin strikes you down.""")
                    input("")
                    print("""
        Game Over...""")
                    exit()
                else:
                    print("""
        You manage to block the goblin's attack, causing it to fall.""")
                    input("")
                    print("""
        You quickly take the opportunity to plant your foot on the goblin's body, making it unable to move.""")
                    response_goblin = 0
                    while response_goblin == 0:
                        goblin_choice = input("""
        Kill: 1
        Spare: 2
        """)
                        if goblin_choice == "1":
                            response_goblin += 1
                            kills += 1
                            if sword == 1:
                                print("""
        You thrust your sword into the goblin with full force. Its body lies cold on the forest floor.""")
                            else:
                                print("""
        You grab the goblin's throat and squeeze with full force until it stops moving. Its body lies cold on
        the forest floor.""")
                        elif goblin_choice == "2":
                            response_goblin += 1
                            print("""
        You move your foot off the goblin. It dashes back into the forest. Before it disappears completely, however,
        it turns back and looks at you for a moment. Though it was just a monster, maybe it was still grateful?""")

            input("")
        print("""
        As the sun begins to rise, you finally come across an exit to the forest.""")
        input("")
        print("""
        Continuing along the path, you stumble upon a small house in the countryside.""")
        input("")
        print("""
        An old man chopping firewood nearby greets you.""")
        input("")
        print("""
        Old man: Greetings traveller. Oh my, did you really come from the forest?""")
        input("")
        print("""
        You nod your head.""")
        input("")
        print("""
        Old man: That's some walk. You must be tired then. Please, come in.""")
        input("")
        print("""
        You follow the old man into his home and sit down at his table.""")
        input("")
        print("""
        Old man: Sorry, I haven't introduced myself yet. My name is Charles Cutton.""")
        input("")
        print("""
        Charles: So, what brings you to this land? It's obvious that you don't belong here.""")
        input("")
        print("""
        You tell Charles about your situation.""")
        input("")
        print("""
        Charles: I see. Seems to me you've gotten yourself in quite the predicament. Hmmm... I know a way you might be 
        able to return to your home. There is an old legend in Restura of a being with immense power and knowledge
        that resides deep within the Chamber of Truth.""")
        input("")
        print("""
        Charles: It is said that those brave enough to venture into the dungeon and make it to the end can receive any
        wish as long as they are pure of heart.""")
        input("")
        print("""
        Charles: Of course, it's just a legend. Though, judging from that look on your face, you're going to go looking
        for the Chamber of Truth, aren't you? Go over the mountain to the east of here. If you keep going,
        I'm sure you'll find it. Well then, goodbye and good luck to you.""")
        input("")
        print("""
        As you leave Charles's home, you notice a small fenced off pasture near the house with a single donkey in it.
        Looking at the expansive mountain ranges in the east, you can't help but consider how much easier it would
        be to cross while riding the donkey.""")
        input("")
        response_donkey = 0
        while response_donkey == 0:
            donkey_choice = input("""
        Keep going: 1
        Steal the donkey: 2
        """)
            if donkey_choice == "1":
                response_donkey += 1
                print("""
        It would be cruel to steal the donkey after Charles helped you out, you think to yourself as you start
        walking towards the eastern mountains.""")
            elif donkey_choice == "2":
                response_donkey += 1
                donkey = 1
                print("""
        You carefully open the fence gate and lead the donkey out of the pasture. Mounting the donkey, you begin
        riding towards the eastern mountains.""")
        input("")
        print("""
        After some travelling, you make it to the base of a mountain.""")
        input("")
        if donkey == 1:
            print("""
        You begin your climb atop the donkey. As the path becomes increasingly steep, you can't help but feel
        relieved that you are not climbing on foot. After a while, the sun begins to set once again.""")
        else:
            print("""
        You begin to climb the mountain. Soon, the path becomes steep and difficult. You struggle to move your
        feet. Eventually, you succumb to your exhaustion and pass out.""")
            input("...")
            sleep(5)
            print("""
        After some time, you wake back up. Suddenly, you realize that all of your possessions are gone! On top
        of that, the sun is setting once again.""")
            items_lost = 1
        input("")
        if tired == 1:
            print("""
        You look around for some shelter and find a cave. Walking through the previous night has left you 
        overwhelmingly tired. You have no choice but to rest.""")
            input("")
            cave_choice = "1"
        else:
            print("""
        You look around for some shelter and find a cave. It might be a good idea to rest for the night.""")
            input("")
            response_cave = 0
            while response_cave == 0:
                cave_choice = input("""
        Sleep in cave: 1
        Keep going: 2
            """)
                if cave_choice == "1":
                    response_cave = 1
                elif cave_choice == "2":
                    response_cave = 1
        if cave_choice == "1":
            print("""
        You lie down in the cave. Before long, you're fast asleep.""")
            input("...")
            sleep(5)
            print("""
        ???: Hehehe... Good morning sleepyhead.""")
            input("")
            if lantern == 1 and items_lost == 0:
                print("""
        It's pitch black. You must have been dragged deeper into the cave. You pull out your lantern to reveal
        who was talking. It's a creature that looks like a monkey with three snakes for tails.""")
                input("")
                print("""
        ???: Hi there. My name is Gregory. What's with that look on your face? We "monsters" still have
        feelings you know.""")
                input("")
            else:
                print("""
        It's pitch black. You must have been dragged deeper into the cave. You ask who's talking to you.""")
                input("")
                print("""
        ???: You humans have all sorts of names for creatures like me. Monster, beast, demon... But us
        "monsters" have feelings too you know. And we've got names too. Mine is Gregory.""")
                input("")
            print("""
        Gregory: Hmmmm... But something about you is different. You don't seem like the other humans. Hey, I 
        know! Want to play a game with me?""")
            input("")
            print("""
        It seems like he won't let you leave without playing a game.""")
            input("")
            if sword == 1 and items_lost == 0:
                response_gregory = 0
                while response_gregory == 0:
                    gregory_choice = input("""
        Play a game: 1
        Use sword: 2
        """)
                    if gregory_choice == "1":
                        response_gregory += 1
                    elif gregory_choice == "2":
                        response_gregory += 1
            else:
                gregory_choice = "1"
            if gregory_choice == "1":
                print("""
        Gregory: Hehe... It's a simple game, you'll see. Ok, here's the game: I'm thinking of something in this cave.
        All you have to do is guess what I'm thinking of. See... simple.""")
                input("")
                if lantern == 1 and items_lost == 0:
                    print("""
        You try to look around with your lantern. You see some rocks, water flowing into a small pond from a crack
        in the cave wall, and a pile of various objects including clothes, weapons, and gold.""")
                else:
                    print("""
        You try to use your senses to guess what is in the cave. You can feel some hard objects that are probably
        rocks. You also hear water flowing nearby.""")
                input("")
                print("""
        Gregory: Oh yeah, one more think. Let's say 4 guesses before you lose. Think carefully. Hehehe...""")
                input("")
                response_gregorygame = 0
                water_response = ["water", "creek", "spring", "pond", "lake", "waterfall"]
                rock_response = ["rock", "rocks", "stone", "stones", "boulder", "boulders"]
                me_response = ["me", "I", "myself"]
                correct_response = ["you", "yourself", "gregory"]
                while response_gregorygame < 3:
                    gregory_game = input("""
        Gregory: So, what am I thinking of?
        """)
                    if gregory_game.lower() in water_response:
                        response_gregorygame += 1
                        print("""
        Gregory: Hm? The water? The water is always moving. Always flowing. A continuous motion, yet it never gets
        tired. Hehehe... It's not what I'm thinking of.""")
                        input("")
                    elif gregory_game.lower() in rock_response:
                        response_gregorygame += 1
                        print("""
        Gregory: The rocks. Rocks are firm and resolute. They stand their ground without budging. There are many rocks
        in this cave of course. But, it's not what I'm thinking of.""")
                        input("")
                    elif gregory_game.lower() in me_response:
                        response_gregorygame += 1
                        print("""
        Gregory: You? Well, it is true that you are a curious fellow. Unlike other humans I have seen. Though you humans
        may each look different, you're all really the same on the inside. Oh, right. I wasn't thinking of you.""")
                        input("")
                    elif gregory_game.lower() in correct_response:
                        response_gregorygame = 10
                        print("""
        Gregory: Me... Hehehe... That's right. You humans see creatures like me as "things," don't you... Well, well,
        well. Looks like you beat me.""")
                        input("")
                    elif gregory_game == "":
                        pass
                    else:
                        print("""
        Gregory: Hehehehehe... Nope. That's not it.""")
                        input("")
                if response_gregorygame == 3:
                    print("""
        Gregory: Looks like you're all out of guesses. Hehe... You lose. You're luck seems to have run out, traveling
        human.""")
                    input("")
                    print("""
        Gregory lunges onto you, causing you to fall over.""")
                    input("")
                    print("""
        He pins you to the ground as you feel snakes start to coil around your body.""")
                    input("")
                    print("""
        Your neck is soon wrapped up so you cannot breathe.""")
                    input("")
                    print("""
        As you feel yourself drifting off, you say a final prayer before completely losing consciousness.""")
                    input("")
                    print("""
        Game over...""")
                    exit()
                elif response_gregorygame == 10:
                    print("""
        That was fun. Thanks, human. You're free to go, but you can always come back for more games. Hehehehehe...""")
                    if items_lost == 1:
                        print("""
        Oh yeah. One more thing... You can have this back. Hehe...""")
                        items_lost = 0
                        input("")
                        if sword == 1:
                            print("""
        Gregory hands you your sword.""")
                        elif lantern == 1:
                            print("""
        Gregory hands you your lantern.""")
                        elif map_1 == 1:
                            print("""
        Gregory hands you your strange map.""")
                    input("")
            elif gregory_choice == "2":
                kills += 1
                print("""
        You tell Gregory that you will play his game.""")
                input("")
                print("""
        Gregory: Hehehe... It's a simple game, you'll see...""")
                input("")
                print("""
        You move towards the sound of Gregory's voice.""")
                input("")
                print("""
        Gregory: I'm thinking of something in this cave...""")
                input("")
                print("""
        You move until you are right in front of the voice.""")
                input("")
                print("""
        Gregory: You need to guess what I'm...""")
                input("")
                print("""
        Before he can finish talking, you quickly draw your sword and swing and full force directly in front of you.""")
                input("")
                print("""
        You feel the blood splatter and hear Gregory's body hit the floor as you pull your sword out.""")
                input("")
            print("""
        You leave the cave. The sun is rising.""")
            input("")
            if donkey == 1:
                print("""
        You untie the donkey and keep riding.""")
                input("")
            else:
                print("""
        You keep walking. Thankfully, the path becomes easier than before.""")
                input("")
            print("""
        Before long, you reach the other side of the mountain.""")
        elif cave_choice == "2":
            print("""
        You decide not to sleep in the cave.""")
            input("")
            if lantern == 1 and items_lost == 0:
                print("""
        Using the light of your lantern, you continue your travels through the night.""")
                input("")
                print("""
        As you keep moving, you think back to what Charles told you.""")
                input("")
                print("""
        The Chamber of Truth... You have to find it. You have to get back to your home.""")
                input("")
                print("""
        As the sun begins to rise, you finally reach the other side of the mountain.""")
            else:
                print("""
        You continue your travels despite being enveloped in darkness.""")
                input("")
                print("""
        After some time, you hear something flying towards you.""")
                input("")
                print("""
        ???: Human... What is a human doing here?""")
                input("")
                print("""
        Through a gap in the clouds, the moonlight reveals a creature that looks like a giant owl.""")
                input("")
                response_owl = 0
                while response_owl == 0:
                    owl_choice = input("""
        Talk: 1
        Fight: 2
        """)
                    if owl_choice == "1":
                        response_owl = 1
                    elif owl_choice == "2":
                        response_owl = 1
                if owl_choice == "1":
                    print("""
        You tell the owl that you are just passing through.""")
                    input("")
                    print("""
        Owl: Hmm... The human says it is passing through. What compels a human to pass through a place like this?""")
                    input("")
                    print("""
        You tell the owl that you need to get home.""")
                    input("")
                    print("""
        Owl: The human is traveling home. Very well, human. You seem different than the other humans I have met.
        You've greeted me with a conversation rather than a blade. I will return the favor now by letting you go.
        Farewell, human.""")
                    input("")
                    print("""
        With that, the owl flaps its wings and vanishes as quickly as it appeared.""")
                if owl_choice == "2":
                    if sword == 1 and items_lost == 0:
                        print("""
        You draw your sword.""")
                        owl_fight = (randint(0, 22) + 7)
                    else:
                        print("""
        You get ready to fight.""")
                        owl_fight = randint(0, 22)
                    input("")
                    if owl_fight < 15:
                        print("""
        Before you can even move, the owl pins you to the ground with its leg.""")
                        input("")
                        print("""
        Owl: How sad. Another insolent human tries to fight. Oh well, say your prayers human.""")
                        input("")
                        print("""
        The owl grabs you and takes off into the sky. After flying a hundred feet or so into the air, the owl stops
        and drops you.""")
                        input("")
                        print("""
        As you are falling, you think about your family back home. Saying a final prayer, you close your eyes and
        hit the ground.""")
                        input("")
                        print("""
        Game over...""")
                        exit()
                    else:
                        kills += 1
                        print("""
        You run at the owl with full speed.""")
                        input("")
                        if sword == 1 and items_lost == 0:
                            print("""
        The owl tries to pin you down with its leg, but you dodge it and cut its leg off.""")
                            input("")
                            print("""
        As it is taken aback, you seize the opportunity to climb up a small rock and jump at it.""")
                            input("")
                            print("""
        The owl's head falls to the floor as you sheathe your sword.""")
                        else:
                            print("""
        The owl tries to pin you down with its leg, but you dodge it and keep running.""")
                            input("")
                            print("""
        You make it to some rocks that you jump on and use to land on the owl's back.""")
                            input("")
                            print("""
        The owl struggles to get you off as you wrap your arm around its head and squeeze.""")
                            input("")
                            print("""
        Struggling to breathe, the owl attempts to fly into the air but cannot get high before it falls back down.
        You keep choking until it stops moving.""")
                        input("")
                        print("""
        As the sun begins to rise, you finally reach the other side of the mountain.""")
        input("")
        print("""
        You continue following a path that leads to a large town in the distance.""")
        input("")
        if donkey == 1:
            print("""
        Suddenly, the donkey collapses from exhaustion. It looks like it desperately needs some food and water.""")
            input("")
            response_helpdonkey = 0
            while response_helpdonkey == 0:
                help_donkey_choice = input("""
        Help: 1
        Abandon: 2
        """)
                if help_donkey_choice == "1":
                    response_helpdonkey = 1
                elif help_donkey_choice == "2":
                    response_helpdonkey = 1
            if help_donkey_choice == "1":
                print("""
        You run nearby looking for some help. A young girl comes towards you.""")
                input("")
                print("""
        Girl: Excuse me mister. Why are you calling for help? Is something wrong?""")
                input("")
                print("""
        You tell the girl that you need to help the donkey that has collapsed.""")
                input("")
                print("""
        Girl: Oh, poor donkey. Hey, I know mister. You can borrow this to help it. There's a river right that way.""")
                input("")
                print("""
        The girl hands you a bucket and points in the direction of a river.""")
                input("")
                print("""
        Thanking her, you run to the river and fill the bucket. You then run back to where the donkey was to find it
        still lying there. You give it the water, which it enthusiastically drinks. After finishing the water, it manages
        to stand back up.""")
                input("")
                print("""
        You lead the donkey to a field so it can graze. While it is eating, you go back to the girl and thank her again
        before returning the bucket.""")
                input("")
                print("""
        Once you feel that the donkey is feeling better, you lead it into the town.""")
            elif help_donkey_choice == "2":
                kills += 1
                print("""
        You leave the donkey behind and keep moving. Soon, you enter the town.""")
        else:
            print("""
        You follow the path until arriving in the town.""")
        input("")
        print("""
        The town is full of people. It looks like it is a gathering place for all sorts of traders and merchants.""")
        input("")
        print("""
        As you keep walking through the town, you spot a familiar face nearby.""")
        input("")
        if donkey_choice == "1":
            print("""
        Charles: It's you! How are you doing? I hope the mountain wasn't too difficult for you... Listen, I've been doing
        some more research about the Chamber of Truth. I think I might know where you can find it from here.""")
            input("")
            print("""
        He pulls out a roughly drawn map and hands it to you.""")
            input("")
            print("""
        Charles: If what I have uncovered is right, this is where you need to go. Look for the eye. You are close to the 
        end of your journey now. Good luck.""")
            input("")
            print("""
        As you thank Charles and turn to leave, he grabs your shoulder.""")
            input("")
            print("""
        One more thing. The Chamber of Truth may be dangerous to explore. I hear there are some rare items being sold in
        this town. Maybe they can help you. Take this money. It's not much, but it's a start. Now then, farewell.""")
            input("")
            gold = 50
        elif donkey_choice == "2" and help_donkey_choice == "1":
            print("""
        Charles: Alexandria! Hey, it's you. When I first discovered that you had taken Alexandria, I was furious. After
        everything I did to help you, you stole my donkey without a second thought! Then I realized that you probably
        have people you care about just as I once did. I know you must be doing everything you can to get back to them.""")
            input("")
            print("""
        You give Alexandria back to Charles and apologize for what you did.""")
            input("")
            print("""
        Charles: It looks like you took good care of her. She looks well fed. I can see that though you have 
        made some mistakes, you still have compassion. Listen, I've been doing some more research about the Chamber of 
        Truth. I think I might know where you can find it from here.""")
            input("")
            print("""
        He pulls out a roughly drawn map and hands it to you.""")
            input("")
            print("""
        Charles: If what I have uncovered is right, this is where you need to go. Look for the eye. You are close to the 
        end of your journey now. Good luck.""")
            input("")
            print("""
        As you thank Charles and turn to leave, he grabs your shoulder.""")
            input("")
            print("""
        One more thing. The Chamber of Truth may be dangerous to explore. I hear there are some rare items being sold in
        this town. Maybe they can help you. Take this money. It's not much, but it's a start. Now then, farewell.""")
            input("")
            gold = 50
        else:
            print("""
        Charles: You! How could you? I helped you and you stole my donkey. Where is Alexandria? You thief!""")
            input("")
            print("""
        Charles starts yelling out "thief." You try to shut him up, but the town militia soon arrives. There are too
        many to try and fight, so you are forced to run. They chase you out of the village before you finally lose them.""")
            lost = 1
        if gold == 50:
            print("""
        You look around the town and find two items that you think could help you: a powerful sword and an old map.""")
            input("")
            if map_1 == 1 and items_lost == 0:
                print("""
        Something about the old map looks familiar to you. You pull out the map you had bought before. Sure enough,
        they go together to form a complete map.""")
                input("")
            print("""
        Both items cost 150 gold. You look for some way to make some money.""")
            input("")
            print("""
        Your search lands you in a gambling street. It may not be the most honorable way of making some money, but it's
        all you got.""")
            input("")
            response_gambling = 0
            leave = 0
            while response_gambling == 0:
                if gold > 149 or gold < 5:
                    response_gambling = 1
                else:
                    print("""
        Gold: """ + str(gold))
                    gambling_choice = input("""
        Dice Game: 1
        Cup Game: 2
        Leave: 3
        """)
                    if gambling_choice == "1":
                        print("""
        You go over to the dice game.""")
                        input("")
                        print("""
        Dice Man: Hey, welcome. Rules are simple: Guess where the dice'll land and ya win 40 gold. 5 gold to play.""")
                        gold -= 5
                        input("")
                        dice_roll = randint(1, 6)
                        response_dice = 0
                        while response_dice == 0:
                            dice_guess = input("""
        Dice Man: So, what's your guess?
        """)
                            dice_guesses = ["1", "2", "3", "4", "5", "6"]
                            if dice_guess in dice_guesses:
                                response_dice += 1
                        print("""
        Dice Man: Ok, I roll a...""")
                        input("")
                        print("""
        Dice Man: """ + str(dice_roll))
                        input("")
                        if dice_roll == int(dice_guess):
                            print("""
        Dice Man: Well, aren't you lucky? Ok, here's 40 gold as promised.""")
                            input("")
                            gold += 40
                        else:
                            print("""
        Dice Man: Too bad. Try again next time.""")
                            input("")
                    elif gambling_choice == "2":
                        print("""
        You go over to the cup game.""")
                        input("")
                        print("""
        Cup Man: Welcome to the cup game. You got two guesses to guess which cup the stone is in. 10 gold to play. 
        I'll give you 60 gold for winning.""")
                        gold -= 10
                        input("")
                        board = []
                        for row in range(3):
                            board.append(["o"] * 3)


                        def print_board(board):
                            for row in board:
                                print(" ".join(row))


                        print_board(board)
                        stone_row = randint(1, 3)
                        stone_column = randint(1, 3)
                        for turn in range(2):
                            response_row = 0
                            while response_row == 0:
                                guess_row = input("""
        Cup Man: So, what row do you guess?
        """)
                                valid_cup = ["1", "2", "3"]
                                if guess_row in valid_cup:
                                    response_row = 1
                            response_column = 0
                            while response_column == 0:
                                guess_column = input("""
        Cup Man: And what column?
        """)
                                if guess_column in valid_cup:
                                    response_column = 1
                            if int(guess_row) == stone_row and int(guess_column) == stone_column:
                                print("""
        The man lifts up the cup that you guessed.""")
                                input("")
                                print("""
        The stone is there!""")
                                input("")
                                print("""
        Cup Man: Guess you win. Here's 60 gold.""")
                                input("")
                                gold += 60
                                break
                            else:
                                if board[int(guess_row) - 1][int(guess_column) - 1] == "x":
                                    print("""
        Cup Man: You just guessed that one genius...""")
                                else:
                                    print("""
        The man lifts up the cup that you guessed.""")
                                    input("")
                                    print("""
        There's nothing there.""")
                                    input("")
                                    print("""
        Cup Man: Too bad. Wrong choice.""")
                                    board[int(guess_row) - 1][int(guess_column) - 1] = "x"
                                    turn += 1
                                    print_board(board)
                                if turn == 2:
                                    print("""
        Cup Man: That's it. You lose.""")
                                    input("")
                    elif gambling_choice == "3":
                        leave = 1
                        response_gambling = 1
            if leave == 1:
                print("""
        You decide to leave without making enough money to buy anything. Exiting the town, you refer to the map
        Charles gave you to continue your journey.""")
            elif gold < 10:
                print("""
        Having lost all your money, you have no choice but to leave. You exit the town and start following the map
        Charles gave you.""")
            elif gold > 149:
                print("""
        Having made enough money, you leave the gambling street before getting too greedy and go back to the merchant 
        selling the items.""")
                input("")
                response_merchant = 0
                while response_merchant == 0:
                    merchant_choice = input("""
        Buy powerful sword: 1
        Buy strange map: 2
        """)
                    if merchant_choice == "1":
                        response_merchant = 1
                    elif merchant_choice == "2":
                        response_merchant = 2
                if merchant_choice == "1":
                    sword_2 = 1
                    print("""
        You bought the powerful sword.""")
                elif merchant_choice == "2":
                    map_2 = 1
                    print("""
        You bought the strange map.""")
        input("")
        print("""
        You continue your journey.""")
        input("")
        if lost == 1:
            print("""
        After wandering for hours, you finally find yourself in front of a giant stone doorway. You've finally made
        it to the Chamber of Truth.""")
        else:
            print("""
        After following Charles's map for hours, you finally find yourself in front of a giant stone doorway.
        You've finally made it to the Chamber of Truth.""")
        input("")
        print("""
        The door has a closed eye on it. Examining it closer, you notice some writing carved into the stone.""")
        input("")
        print("""
        It reads: Those who seek answers. Speak this and enter. What is it that men desire in public, yet fear in private?""")
        input("")
        print("""
        It must be some sort of riddle, you think to yourself.""")
        input("")
        response_door = 0
        while response_door == 0:
            door = input("""
        What is it that men desire in public, yet fear in private?
        """)
            if door.lower() == "truth" or door.lower() == "the truth":
                response_door = 1
            else:
                print("""
        ...Nothing happened.""")
                input("")
        print("""
        You speak the answer aloud. Suddenly, the ground starts to shake. The eye on the door slowly opens as an 
        entrance is revealed.""")
        input("")
        print("""
        You make your way down the corridor until finally reaching an entrance to a room. Outside the room there is
        some more writing.""")
        input("")
        print("""
        The road to truth is always blocked by ignorance.""")
        input("")
        if map_1 == 1 and items_lost == 0:
            print("""
        You remember reading this before. You pull out your old map and sure enough, it has the same thing written on it.""")
            input("")
        print("""
        You walk into the room and the door slams shut behind you. No more turning back. The room is dark, but you can see
        just enough to notice the complex layout. It's a maze.""")
        input("")
        if map_1 == 1 and items_lost == 0:
            print("""
        Just as you expected, your map fits the layout of the room perfectly. Despite barely being able to read in the 
        darkness, you manage to follow the map to the other side of the room. You exit the room and start walking
        through another corridor.""")
        else:
            if lantern == 1 and items_lost == 0:
                print("""
        You pull out your lantern to lighten up the room. Everything become a bit clearer to you. You start walking
        through the maze.""")
                input("")
            else:
                print("""
        You start walking through the dark maze.""")
                input("")
            response_maze = 0
            response_solve = 0
            while response_solve == 0:
                if lantern == 1 and items_lost == 0:
                    answer = ["right", "right", "left"]
                    guesses = []
                    while response_maze < 3:
                        choices = input("""
        There's a fork. Do you go left or right?
        """)
                        if choices.lower() == "left" or choices.lower() == "right":
                            guesses.append(choices.lower())
                            response_maze += 1
                    if guesses == answer:
                        response_solve = 1
                    else:
                        print("""
        Huh? Somehow, you ended up back where you started...""")
                        response_maze = 0
                else:
                    answer = ["left", "left", "right", "left"]
                    guesses = []
                    while response_maze < 4:
                        choices = input("""
        There's a fork. Do you go left or right?
        """)
                        if choices.lower() == "left" or choices.lower() == "right":
                            guesses.append(choices.lower())
                            response_maze += 1
                    if guesses == answer:
                        response_solve = 1
                    else:
                        input("")
                        print("""
        Huh? Somehow, you ended up back where you started...""")
                        response_maze = 0
            print("""
        You finally see an exit. You leave the maze and keep walking through another corridor.""")
        input("")
        print("""
        As you keep walking, you notice the temperature getting warmer and warmer. Upon reaching the next room, you
        discover the source of this heat.""")
        input("")
        print("""
        To your surprise, a dragon lays in the center of a giant room full of treasures. It's scales are a dark red
        color and its eyes are closed. As you walk closer, it snorts and moves its head towards you.""")
        input("")
        print("""
        Dragon: HUMAN... I SMELL A HUMAN.""")
        input("")
        print("""
        You quickly move behind a nearby pile of gold as quietly as you can.""")
        input("")
        print("""
        You can hear the dragon moving closer to you. It seems like it cannot see, but it can still smell and hear 
        you.""")
        input("")
        if map_2 == 1:
            print("""
        You refer back to your strange map, which you remember mentioned something about a room of fire and gold. A
        hidden switch is shown on the map near where you are. You start moving towards it carefully.""")
            input("")
            print("""
        Before the dragon can tell where you went, you hit the switch on the wall, causing some of the bricks to move
        out of the way and let you in. Once you enter, the bricks are pushed back into place.""")
            input("")
            print("""
        As you are walking through the narrow passage, you hear the dragon through the wall.""")
            input("")
            print("""
        Dragon: I SEE. VERY CLEVER OF YOU. THROUGH THE RIGHT KNOWLEDGE, EVEN THE GREATEST OF OBSTACLES CAN BE PASSED.
        GO ON THEN, HUMAN. SEE THE TRUTH.""")
        else:
            response_dragon = 0
            while response_dragon == 0:
                dragon_choice = input("""
        Fight: 1
        Sneak: 2
        """)
                if dragon_choice == "1" or dragon_choice == "2":
                    response_dragon = 1
            if dragon_choice == "2":
                print("""
        You start sneaking towards the other side of the room. The dragon seems to have a hard time finding exactly
        where you are.""")
                input("")
                print("""
        Dragon: I KNOW YOU ARE HERE. WHERE ARE YOU HIDING?""")
                dragon_sneak = randint(1, 9)
                input("")
                if dragon_sneak < 4:
                    print("""
        You keep sneaking without making a sound. Somehow, you make it to the other side without the dragon finding
        you.""")
                else:
                    print("""
        You keep sneaking without making a sound. Suddenly, your heart sinks.""")
                    input("")
                    print("""
        A single coin falls to the ground.""")
                    input("")
                    print("""
        The dragon immediately turns towards you.""")
                    input("")
                    response_dragon2 = 0
                    while response_dragon2 == 0:
                        dragon_choice2 = input("""
        Fight: 1
        Run: 2
        """)
                        if dragon_choice2 == "1" or dragon_choice2 == "2":
                            response_dragon2 = 1

            if dragon_choice == "1" or dragon_choice2 == "1":
                if sword_2 == 1:
                    print("""
        You draw your sword. It shines with power.""")
                    input("")
                    print("""
        Taking a deep breath, you run at the dragon.""")
                    input("")
                    print("""
        Dragon: OH, THERE YOU ARE, HUMAN.""")
                    input("")
                    print("""
        A pillar of fire erupts from the dragon's mouth, but your sword absorbs the flames and glows even brighter.""")
                    input("")
                    print("""
        You close the distance between you and the dragon and jump onto its tail. It tries to shake you off, but you cling
        to its burning scales.""")
                    input("")
                    print("""
        Dragon: GET OFF OF ME!""")
                    input("")
                    print("""
        You keep climbing the dragon until you make it all the way to its head. Holding your glowing sword high, you
        thrust it into dragon with all of your might. It screams with pain as it blasts fire to all corners of the room.
        After a few seconds, the fire becomes smoke. The smoke then also clears, leaving the body of the dragon on the floor, 
        dead. You are victorious.""")
                    kills += 1
                elif sword == 1 and items_lost == 0:
                    if kills == 3:
                        print("""
        You draw your sword once more. It is already stained with the blood of past enemies.""")
                        input("")
                        print("""
        You run at the dragon. Hearing your footsteps, it opens its mouth to shoot flames. Before it can act, you throw
        your sword into its mouth. It screams in pain as the sword goes through its mouth and out the other end.""")
                        input("")
                        print("""
        You reach your sword and go back to finish the dragon. It tries to attack you with its claws, but you dodge them
        and push your sword into its heart. It immediately falls over, dead. You remove the sword and sheathe it with
        a cold look on your face. You are victorious.""")
                        kills += 1
                    else:
                        dragon_fight = randint(1, 9)
                        print("""
        You draw your sword.""")
                        input("")
                        print("""
        Taking a deep breath, you run at the dragon.""")
                        input("")
                        print("""
        Dragon: OH, THERE YOU ARE, HUMAN.""")
                        input("")
                        if dragon_fight < 4:
                            print("""
        A pillar of fire erupts from the dragon's mouth. You try to jump out of the way.""")
                            input("")
                            print("""
        Dragon: IT'S TOO BAD. YOU REALLY WERE CLOSE TO THE TRUTH.""")
                            input("")
                            print("""
        The dragon's fire follows you. Despite reaching this far, it seems this is the end. As you are engulfed in 
        flames, you close your eyes and say a final prayer.""")
                            input("")
                            print("""
        Game over...""")
                            exit()
                        else:
                            print("""
        A pillar of fire erupts from the dragon's mouth, but you react quickly and jump out of the way.""")
                            input("")
                            print("""
        You close the distance between you and the dragon and jump onto its tail. It tries to shake you off, but you cling
        to its burning scales.""")
                            input("")
                            print("""
        Dragon: GET OFF OF ME!""")
                            input("")
                            print("""
        You keep climbing the dragon until you make it all the way to its head. Holding your sword high, you thrust it 
        into dragon with all of your might. It screams with pain as it blasts fire to all corners of the room. After a few
        seconds, the fire becomes smoke. The smoke then also clears, leaving the body of the dragon on the floor, dead. 
        You are victorious.""")
                            kills += 1
                else:
                    print("""
        You take a deep breath and run at the dragon.""")
                    input("")
                    print("""
        Dragon: OH, THERE YOU ARE, HUMAN.""")
                    print("""
        A pillar of fire erupts from the dragon's mouth. You try to jump out of the way.""")
                    input("")
                    print("""
        Dragon: IT'S TOO BAD. YOU REALLY WERE CLOSE TO THE TRUTH.""")
                    input("")
                    print("""
        The dragon's fire follows you. Despite reaching this far, it seems this is the end. As you are engulfed in 
        flames, you close your eyes and say a final prayer.""")
                    input("")
                    print("""
        Game over...""")
                    exit()
            elif dragon_choice2 == "2":
                dragon_run = randint(1, 2)
                print("""
        You run as fast as you can towards the exit.""")
                input("")
                if dragon_run == "1":
                    print("""
        Before you can make it to the other side, pillars of flame engulf you. Despite reaching this far, it seems this 
        is the end. As you are burning, you close your eyes and say a final prayer.""")
                    input("")
                    print("""
        Game over...""")
                    exit()
                else:
                    print("""
        As you are nearing the exit, you feel a wave of heat behind you. You reach the open door and move to the side 
        as fast as you can.""")
                    input("")
                    print("""
        Pillars of flame burst out from the other side of the door, almost causing you to burn alive. Thankfully, the
        fire is extinguished by the door, which closes itself.""")
        input("")
        print("""
        You finally made it. You make your way to the end of one final corridor. Standing before you is an old man
        in robes.""")
        input("")
        print("""
        Wizard: Welcome. My name is Avius, the Wizard of Restura.""")
        input("")
        print("""
        Avius: You have made it to the end of the Chamber of Truth. You are the first human to make it here in a long 
        time. Tell me, what is your purpose for coming here?""")
        input("")
        print("""
        You tell him why you have come.""")
        input("")
        print("""
        Avius: Yes, I see. I can help you find your way home. Before I do, however, I must read your heart.""")
        input("")
        print("""
        Avius closes his eyes. You feel yourself being judged.""")
        input("")
        if kills == 4:
            print("""
        Suddenly, Avius opens his eyes and stumbles back.""")
            input("")
            print("""
        Avius: You... There is nothing in your heart but cruelty and hatred. You slay monsters and yet the real monster
        is you.... It makes me sick...""")
            input("")
            print("""
        Avius: I will not help someone like you.""")
            input("")
            print("""
        You feel a wave of anger flood over you. In a matter of seconds, your sword is in your hand and you are standing
        where Avius was. His head falls to the floor next to his body. Blood pools out onto your feet.""")
            input("")
            print("""
        You sheathe your sword and turn to leave.""")
        elif kills == 0:
            print("""
        Suddenly, Avius opens his eyes.""")
            input("")
            print("""
        Avius: Your heart is pure and full of compassion. You came to the Chamber of Truth having already discovered
        the truth for yourself. A truly noble human...""")
            input("")
            print("""
        Avius: I will help you reach your home.""")
            input("")
            print("""
        You feel an overwhelming drowsiness wash over your body. Your eyes start to close.""")
            input("...")
            sleep(5)
            print("""
        When you awaken, you find yourself back in your bed. You stand up and look out the window. A feeling of 
        contentment comes to you as you smile to yourself.""")
            input("")
            print("""
        Home at last...""")
        else:
            print("""
        Suddenly, Avius opens his eyes.""")
            input("")
            print("""
        Avius: Hmmm... Your heart is troubled. A battle between dark and light. There is still much you have to learn 
        about the world. When you are ready, come find me again. Until then, farewell.""")
            input("")
            print("""
        You feel an overwhelming drowsiness wash over your body. Your eyes start to close.""")
            input("...")
            sleep(5)
            print("""
        When you awaken, you realize that you are lying on the hard dirt ground.""")
            input("")
            print("""
        You take in your surroundings. Nothing at all is familiar to you.""")
            input("")
            print("""
        You realize that you have somehow ended up in a completely new place.""")
        input("")
        print("""
   ▄████████ ███▄▄▄▄   ████████▄  
  ███    ███ ███▀▀▀██▄ ███   ▀███ 
  ███    █▀  ███   ███ ███    ███ 
 ▄███▄▄▄     ███   ███ ███    ███ 
▀▀███▀▀▀     ███   ███ ███    ███ 
  ███    █▄  ███   ███ ███    ███ 
  ███    ███ ███   ███ ███   ▄███ 
  ██████████  ▀█   █▀  ████████▀                                 
        """)
        input("")
    elif menu_choice == "2":
        response += 1
        exit()
