#Iain Thorpe Per.3 This is a fan demo based off the 3DS game Miitopia. I hope you enjoy!
#Digital Miitopia Mark II
#Beginning/Prompt
vars = [0,0]
def start_program():
    vars[1] = 0
    print('Welcome to the digital world of Miitopia!\n I will be your host, Nick Crogar.\n')
    print('Miitopia is a world full of magic, mystery, and most importantly, monsters.\n')
    print('Lately, monsters have been sighted outside the town of Greenhorne, so today, we ask you to determine your hero that will fight off these monsters.\n')
    print('To determine your hero, follow these instructions.\n')
    print('First, my cohost, Benny, will ask you a series of questions to depict the type of hero you will send into battle.\n')
    print('For each series of questions, you will respond with either yes or no.\n If you respond with anything else, my friend Doctor Doom over here will foot dive you until you choose yes or no.\n')
    while vars[1] == 0:
        print('Are you ready to begin?\n')
        answer = raw_input()
        print('\n'*5)
        answer = answer.lower()
        if answer == "yes" or answer == "Yes" or answer == "y" or answer == "YES" or answer == "YEs" or answer == "yES":
            print('Okay, then!\n Benny, if you please!\n')
            personality_quiz()
        elif answer == "no" or answer == "No" or answer == "n" or answer == "NO":
            print('Wrong answer!\n Doom says moooooooove on!\n')
            personality_quiz()
        else:
            print('FOOT DIVE!\n')
#Code for the personality quiz.
def personality_quiz():
    vars[1] = 2
    print('Hello, player. My name is Benny. First, I will determine the personality of your hero. This quiz will be three questions long.')
    while vars[1] == 2:
        print('Question 1: Do you consider yourself an average person?')
        answer = raw_input()
        print('\n'*5)
        answer = answer.lower()
        if answer == "yes" or answer == "Yes" or answer == "y" or answer == "YES" or answer == "YEs" or answer == "yES":
            print('Okay, next question!\n Are you smart?\n')
            answer = raw_input()
            print('\n'*5)
            answer = answer.lower()
            if answer == "yes" or answer == "Yes" or answer == "y" or answer == "YES" or answer == "YEs" or answer == "yES":
                print("Okay, and don't worry.\n I'm not playing the Are You Smart game.\n")
                print('Final question! Do you think you might not forget everything in the future?')
                answer = raw_input()
                print('\n'*5)
                answer = answer.lower()
                if answer == "yes" or answer == "Yes" or answer == "y" or answer == "YES" or answer == "YEs" or answer == "yES":
                    print('I have determined that you are Air-Headed!\n Now, let me get some dog treats.\n Give me a second.\n')
                    job_quiz()
                elif answer == "no" or answer == "No" or answer == "n" or answer == "NO":
                    print('I have determined that you are Cool!\n Now, let me get some dog treats.\n Give me a second.\n')
                    job_quiz()
                else:
                    print('FOOT DIVE!\n')
            elif answer == "no" or answer == "No" or answer == "n" or answer == "NO":
                print("Okay, and don't worry.\n I'm not playing the Are You Smart game.\n")
                print('Final question!\n Are you always prepared?')
                answer = raw_input()
                print('\n'*5)
                answer = answer.lower()
                if answer == "yes" or answer == "Yes" or answer == "y" or answer == "YES" or answer == "YEs" or answer == "yES":
                    print('I have determined that you are Cautious!\n Give me a second while I grab some dog treats.\n')
                    job_quiz()
                elif answer == "no" or answer == "No" or answer == "n" or answer == "NO":
                    print('I have determined that you are Average!\n Give me a second while I grab some dog treats.\n')
                    job_quiz()
                else:
                    print('FOOT DIVE!')
            else:
                print('FOOT DIVE!')
        elif answer == "no" or answer == "No" or answer == "n" or answer == "NO":
            print('Okay, next question!\n Do you care about the type of person you are?\n')
            answer = raw_input()
            print('\n'*5)
            answer = answer.lower()
            if answer == "yes" or answer == "Yes" or answer == "y" or answer == "YES" or answer == "YEs" or answer == "yES":
                print("Good.\n I'm glad someone cares about their own life.\n")
                print('Final question!\n Are you full of energy?')
                answer = raw_input()
                print('\n'*5)
                answer = answer.lower()
                if answer == "yes" or answer == "Yes" or answer == "y" or answer == "YES" or answer == "YEs" or answer == "yES":
                    print("I have determined that you are Energetic!\n I'm now hungry.\n Let me go get some dog treats.\n")
                    job_quiz()
                elif answer == "no" or answer == "No" or answer == "n" or answer == "NO":
                    print("I have determined that you are Laid-Back!\n I'm now hungry.\n Let me go get some dog treats.\n")
                    job_quiz()
                else:
                    print('FOOT DIVE!')
            elif answer == "no" or answer == "No" or answer == "n" or answer == "NO":
                print('Well.\n I guess to each their own.\n')
                print('Final question! Do you take criticism well?')
                answer = raw_input()
                print('\n'*5)
                answer = answer.lower()
                if answer == "yes" or answer == "Yes" or answer == "y" or answer == "YES" or answer == "YEs" or answer == "yES":
                    print("I have determined that you are Kind!\n Do you mind if I go get some dog treats?\n Ok, I'll be right back.\n")
                    job_quiz()
                elif answer == "no" or answer == "No" or answer == "n" or answer == "NO":
                    print("I have determined that you are Stubborn!\n Do you mind if I go get some dog treats?\n Ok, I'll be right back.\n")
                    job_quiz()
                else:
                    print('FOOT DIVE!')
            else:
                print('FOOT DIVE!')
        else:
            print('FOOT DIVE!')
#Code for the job quiz.
def job_quiz():
    vars[2] = 3
    print("Okay, I'm back.\n What, you didn't know I was a dog?\n I thought everyone knew that!\n")
    print("Anyway, now I'll determine your job.\n Your job is basically what your career is in Miitopia!\n This quiz will be four questions long.\n")
    print("Let's begin with Question 1!")
    while vars[2] == 3:
        print('Do you prefer close quarters combat?\n')
        answer = raw_input()
        print('\n'*5)
        answer = answer.lower()
        if answer == "yes" or answer == "Yes" or answer == "y" or answer == "YES" or answer == "YEs" or answer == "yES":
            print('Okay, next question!\n Would you prefer to be something related to a village?\n')
            answer = raw_input()
            print('\n'*5)
            answer = answer.lower()
            if answer == "yes" or answer == "Yes" or answer == "y" or answer == "YES" or answer == "YEs" or answer == "yES":
                print("Okay, your opinion.\n I'm not stopping you.\n")
                print('Question 3: Would you just want to live a normal life?\n')
                answer = raw_input()
                print('\n'*5)
                answer = answer.lower()
                if answer == "yes" or answer == "Yes" or answer == "y" or answer == "YES" or answer == "YEs" or answer == "yES":
                    print('Ok.\n Nothing unusual.\n I get you.\n')
                    print('Final question! Would you rather be a human?')
                    answer = raw_input()
                    print('\n'*5)
                    answer = answer.lower()
                    if answer == "yes" or answer == "Yes" or answer == "y" or answer == "YES" or answer == "YEs" or answer == "yES":
                        print('I have determined that you are a Villager!\n You found a canon class!\n Conglaturations!\n')
                        vars[2] = 0
                        finish_game()
                    elif answer == "no" or answer == "No" or answer == "n" or answer == "NO":
                        print('I have determined that you are a Cat!\n And no, you may not switch to a dog!\n')
                        vars[2] = 0
                        finish_game()
                    else:
                        print('FOOT DIVE!')
                elif answer == "no" or answer == "No" or answer == "n" or answer == "NO":
                    print('Ok.\n Something out of the ordinary.\n I get you.\n')
                    print('Final question!\n Which type of weapon would you prefer: Swords(yes) or daggers(no)?\n')
                    answer = raw_input()
                    print('\n'*5)
                    answer = answer.lower()
                    if answer == "yes" or answer == "Yes" or answer == "y" or answer == "YES" or answer == "YEs" or answer == "yES":
                        print('I have determined that you are a Warrior!\n Those swords look pretty pointy!\n')
                        vars[2] = 0
                        finish_game()
                    elif answer == "no" or answer == "No" or answer == "n" or answer == "NO":
                        print('I have determined that you are a Thief!\n Hey, give me back my Bone Biscuit!\n')
                        vars[2] = 0
                        finish_game()
                    else:
                        print('FOOT DIVE!')
                else:
                    print('FOOT DIVE!\n')
            elif answer == "no" or answer == "No" or answer == "n" or answer == "NO":
                print("Okay, your opinion.\n I'm not stopping you.\n")
                print('Question 3: Would you prefer to be something out of the ordinary?\n')
                answer = raw_input()
                print('\n'*5)
                answer = answer.lower()
                if answer == "yes" or answer == "Yes" or answer == "y" or answer == "YES" or answer == "YEs" or answer == "yES":
                    print('Ok.\n Something unusual.\n I get you.\n')
                    print('Final question!\n Would you prefer to be royalty?\n')
                    answer = raw_input()
                    print('\n'*5)
                    answer = answer.lower()
                    if answer == "yes" or answer == "Yes" or answer == "y" or answer == "YES" or answer == "YEs" or answer == "yES":
                        print('I have determined that you are a Princess!\n Take a bow, Your Highness!\n')
                        vars[2] = 0
                        finish_game()
                    elif answer == "no" or answer == "No" or answer == "n" or answer == "NO":
                        print('I have determined that you are a Pop Star!\n What, you wanted something unusual.\n')
                        vars[2] = 0
                        finish_game()
                    else:
                        print('FOOT DIVE!')
                elif answer == "no" or answer == "No" or answer == "n" or answer == "NO":
                    print('Ok.\n Something cool.\n I get you.\n')
                    print('Final question!\n Which would you prefer: The science of science(yes), or the magic of cooking(no)?\n')
                    answer = raw_input()
                    print('\n'*5)
                    answer = answer.lower()
                    if answer == "yes" or answer == "Yes" or answer == "y" or answer == "YES" or answer == "YEs" or answer == "yES":
                        print('I have determined that you are a Scientist!\n Can I call you Bill Nye?\n')
                        vars[2] = 0
                        finish_game()
                    elif answer == "no" or answer == "No" or answer == "n" or answer == "NO":
                        print('I have determined that you are a Chef!\n Can you cook me some bacon?\n')
                        vars[2] = 0
                        finish_game()
                    else:
                        print('FOOT DIVE!')
                else:
                    print('FOOT DIVE!')
            else:
                print('FOOT DIVE!')
        elif answer == "no" or answer == "No" or answer == "n" or answer == "NO":
            print('Okay, next question!\n Would you prefer to be something realistic?\n')
            answer = raw_input()
            print('\n'*5)
            answer = answer.lower()
            if answer == "yes" or answer == "Yes" or answer == "y" or answer == "YES" or answer == "YEs" or answer == "yES":
                print("That's as real as real can get!\n")
                print('Queston 3: Would you like to be one with nature?\n')
                answer = raw_input()
                print('\n'*5)
                answer = answer.lower()
                if answer == "yes" or answer == "Yes" or answer == "y" or answer == "YES" or answer == "YEs" or answer == "yES":
                    print("Alright.\n Your opinion.\n")
                    print('Final question: Would you prefer to be completely one with nature?\n')
                    answer = raw_input()
                    print('\n'*5)
                    answer = answer.lower()
                    if answer == "yes" or answer == "Yes" or answer == "y" or answer == "YES" or answer == "YEs" or answer == "yES":
                        print('I have determined that you are a Flower!\n Howdy!\n')
                        vars[2] = 0
                        finish_game()
                    elif answer == "no" or answer == "No" or answer == "n" or answer == "NO":
                        print('I have determined that you are an Elf!\n Have you seen that movie, by the way?\n')
                        vars[2] = 0
                        finish_game()
                    else:
                        print('FOOT DIVE!')
                elif answer == "no" or answer == "No" or answer == "n" or answer == "NO":
                    print("No?\n Okay, your opinion.\n")
                    print('Final question!\n Do you like DC?\n')
                    answer = raw_input()
                    print('\n'*5)
                    answer = answer.lower()
                    if answer == "yes" or answer == "Yes" or answer == "y" or answer == "YES" or answer == "YEs" or answer == "yES":
                        print("I have determined that you are a Cyborg!\n What's your secret for looking so young?\n")
                        vars[2] = 0
                        finish_game()
                    elif answer == "no" or answer == "No" or answer == "n" or answer == "NO":
                        print('I have determined that you are a Tank!\n Thanks for your service, veterans!\n')
                        vars[2] = 0
                        finish_game()
                    else:
                        print('FOOT DIVE!')
                else:
                    print('FOOT DIVE!')
            elif answer == "no" or answer == "No" or answer == "n" or answer == "NO":
                print("Well.\n Okay, you're a fantasy loving person.\n I get you.\n")
                print('Question 3: Would you prefer to be a white magic user?\n')
                answer = raw_input()
                print('\n'*5)
                answer = answer.lower()
                if answer == "yes" or answer == "Yes" or answer == "y" or answer == "YES" or answer == "YEs" or answer == "yES":
                    print("Okay, I can see where you're going with this.\n")
                    print('Final question: Would you use magic for battle?\n')
                    answer = raw_input()
                    print('\n'*5)
                    answer = answer.lower()
                    if answer == "yes" or answer == "Yes" or answer == "y" or answer == "YES" or answer == "YEs" or answer == "yES":
                        print('I have determined that you are a Mage!\n The classiest magic class out there.\n')
                        vars[2] = 0
                        finish_game()
                    elif answer == "no" or answer == "No" or answer == "n" or answer == "NO":
                        print('I have determined that you are a Cleric!\n The healer of the party!\n')
                        vars[2] = 0
                        finish_game()
                    else:
                        print('FOOT DIVE!')
                elif answer == "no" or answer == "No" or answer == "n" or answer == "NO":
                    print("Okay, dark magic.\n That's weird.\n")
                    print('Final question: Would you hold a pitchfork in protest?\n')
                    answer = raw_input()
                    print('\n'*5)
                    answer = answer.lower()
                    if answer == "yes" or answer == "Yes" or answer == "y" or answer == "YES" or answer == "YEs" or answer == "yES":
                        print('I have determined that you are an Imp!\n The darkness crawls on your back.\n')
                        vars[2] = 0
                        finish_game()
                    elif answer == "no" or answer == "No" or answer == "n" or answer == "NO":
                        print('I have determined that you are a vampire!\n Do you vant to suck a tomato instead of me?\n')
                        vars[2] = 0
                        finish_game()
                    else:
                        print('FOOT DIVE!')
                else:
                    print('FOOT DIVE!')
            else:
                print('FOOT DIVE!')
        else:
            print('FOOT DIVE!')
#Code for the end of the game.
def finish_game():
    vars[3] = 1
    print("Congratulations!\n You survived the quiz.\n Hopefully Doom over here didn't foot dive you.\n")
    while vars[3] == 1:
        print('Did you have fun?')
        answer = raw_input()
        print('\n'*5)
        answer = answer.lower()
        if answer == "yes" or answer == "Yes" or answer == "y" or answer == "YES" or answer == "YEs" or answer == "yES":
            print("Good!\n Then I'll see you next time!\n Goodbye!\n")
            vars[3] = 0
        elif answer == "no" or answer == "No" or answer == "n" or answer == "NO":
            print('FOOT DIVE, FOOT DIVE, FOOT DIVE, FOOT DIVE, FOOT DIVE! YOU HAD NO FUN? DOOM SAYS GET LOST!')
            vars[3] = 0
        else:
            print('Genius, that is not an answer. Nevertheless, Goodbye!')
            vars[3] = 0

start_program()