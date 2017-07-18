#User starts or stops game
while True:
    start = input("Type STOP to stop the game. Type anything else to start game.")
    #input.lower()
    if start == "stop":
        break

#Choosing ur campsite
    else:
        print("Aye. Welcome to ur new fave game. Imagine u r on a cool camping trip.")
        ans1 = input("Where do you go? Type 1 for the ocean. Type 2 for the mountains. ")
        if ans1 == "1":
            print("U go to the ocean. U go swimming. A shark bites you and you die of blood loss. GAME OVER.")
        elif ans1 == "2":
            print("So you're alone in the mountains.")
            print("While you're checking out your campsite, you find an eerily calm young man meditating on a rock.")
            ans2 = input("Type 1 to talk to the man. Type 2 to ignore him.")

            #Talk to man
            if ans2 == "1":
                print("Man says, 'Hey, my name is Jisoo and I am here to save u fr a potentially fatal future.")
                print("One of these objects will protect you during ur adventure.'")
                ans3 = input("Type 1 for an amulet. Type 2 for bear spray.")

                #Choosing your "weapon"
                if ans3 == "1":
                    print("He says 'ok ok ok' and hands u a shiny red amulet.")
                    print("You ended up taking all day exploring ur campsite and it's dark now.")
                    print("TIME TO GO TO BED!")
                    print("You're sleeping and a bear almost attacks you, but your magic amulet starts shining rlly brightly.")
                    print("You're suddenly transported into an alternate universe. Woohoo. You achieve all ur greatest dreams and live a fun fun life.")
                elif ans3 == "2":
                    print("He says, 'alrighty then.' You regret your decision and ask for the amulet and he says 'noPE,'")
                    print("pats ur head, then disappears in a cloud of glitter.")
                    print("It's dark. U go to sleep.")
                    print("u almost die, but then u grab ur trusty bear spray.")
                    print("Jisoo suddenly appears and u accidentally spray the bear spray in his eyes.")
                    print("He gets eaten by the bear and you live the rest of your life feeling guilty abt Jisoo's death.")
                else:
                    print("You typed the wrong thing. You must restart ur adventure. :(")

            elif ans2 == "2":
                print("Bad choice. While you're sleeping, u get attacked by a bear and barely escape with ur life. GAME OVER!!!")
            else:
                print("You typed the wrong thing. You must restart ur adventure. :(")

        else:
            print("You typed the wrong thing. You must restart ur adventure. :(")
