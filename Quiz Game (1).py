name = input("Enter your name ")
print("                                                                                                                                                             ")
print("Hello! ",name )
print("                                                                                                                                                             ")
var = input("How are you? ")
print("                                                                                                                                                             ")
print("Good")
print("                                                                                                                                                             ")
print("Let's do a quiz ")
print("                                                                                                                                                             ")
print("write options in answer")
score = 0
print("                                                                                                                                                             ")
print("1)Who was the third person to walk on the moon?")
print("a)Neil Armstrong")
print("b)Edwin 'Buzz' Aldrin")
print("c)Charles 'Pete' Conrad")
print("d)Mark Hamill")
q1 = input("Answer = ")
if q1== "d":
    print("Congoratulations! Your answer is correct :)")
else:
    print("Sorry! your answer is wrong :(")
if q1 == "d":
    ascore=score+1
else:
    ascore=score+0
print(score)
print("                                                                                                                                                             ")
print("2)What is the chemical symbol for salt?")
print("a)C12H22O11")
print("b)NaCl")
print("c)Fe")
print("d)Au")
q2 = input("Answer = ")
if q2== "b":
    print("Congoratulations! Your answer is correct :)")
else:
    print("Sorry! your answer is wrong :(")
if q2 == "b":
    bscore=score+1
else:
    bscore=score+0
print(score)
print("                                                                                                                                                             ")
print("3)A strawberry is not technically a berry. What is it?")
print("a)A hybrid vegetable")
print("b)An accessory fruit")
print("c)A cruciferous vegetable")
print("d)Trick question – it's a berry")
q3 = input("Answer = ")
if q3== "b":
    print("Congoratulations! Your answer is correct :)")
else:
    print("Sorry! your answer is wrong :(")
if q3 == "b":
    cscore=score+1
else:
    cscore=score+0
print(score)
print("                                                                                                                                                             ")
print("4)How many months have 28 days?")
print("a)2")
print("b)1")
print("c)All of them")
print("d)Depends if there's a leap year or not")
q4 = input("Answer = ")
if q4=="c":
    print("Congoratulations! Your answr is correct :)")
else:
    print("Sorry! Your answer is wrong :(")
if q4 == "c":
    dscore=score+1
else:
    dscore=score+0
print(score)
print("                                                                                                                                                             ")
print("5)Jimmy's father has three sons- Paul I and Paul II. Can you guess the name of the third son?")
print("a)Jerin")
print("b)Paul III")
print("c)Jimmy")
print("d)none of above")
q5 = input("Answer = ")
if q5=="c":
    print("Congoratulations! Your answr is correct :)")
else:
    print("Sorry! Your answer is wrong :(")
if q5 == "c":
    escore=score+1
else:
    escore=score+0
print(score)
print("6)There are 45 mangoes in your basket. You take three out of the basket. How many mangoes are left?")
print("a)3")
print("b)42")
print("c)45")
print("d)I do not eat mangoes!")
q6 = input("Answer = ")
if q6=="c":
    print("Congoratulations! Your answr is correct :)")
else:
    print("Sorry! Your answer is wrong :(")
if q6 == "c":
    fscore=score+1
else:
    fscore=score+0
print(score)
print("7)What is the name of the smallest bone in human body?")
print("a)Stapes")
print("(b)Ulna")
print("c)Maxilla")
print("d)Mandible")
q7 = input("Answer = ")
if q7=="a":
    print("Congoratulations! Your answr is correct :)")
else:
    print("Sorry! Your answer is wrong :(")
if q7 == "a":
    gscore=score+1
else:
    gscore=score+0
print(score)
print("8)In which year did the first colour television come out?")
print("1936")
print("1928")
print("1945")
print("1954")
q8 = input("Answer = ")
if q8=="c":
    print("Congoratulations! Your answr is correct :)")
else:
    print("Sorry! Your answer is wrong :(")
if q8 == "c":
    hscore=score+1
else:
    hscore=score+0
print(score)
print("                                                                                                                                                             ")
finalscore=ascore+bscore+cscore+dscore+escore+fscore+gscore+hscore
print("You've scored = ",finalscore)
print("                                                                                                                                                             ")
feedback=int(input("Rate it out of 10 = "))
if feedback==8:
    print("Thankyou! :)")
if feedback>8:
    print("Thankyou! :)")
if feedback<8:
    print("Thankyou! :(")
print("                                                                                                                                                             ")
print("Thankyou",name,"for Answering.")
print("                                                                                                                                                             ")
print("Made By")
print("                                                                                                                                                             ")
print("-Yash (YS)")
print("                                                                                                                                                             ")
print("BYE")
