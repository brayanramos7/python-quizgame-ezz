# create a quiz game that asks the user questions and gives them a score at the end

print ("Welcome to the quiz game!")

playing = input ("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print ("Okay! Let's play :)")
score = 0

answer = input ("Who created this game? ")
if answer.lower() == "you":
    print ("Correct!")
    score += 1
else:
    print ("Incorrect! oh no! ")
answer = input ("How old AM I? ")
if answer == "23":
    print ("Correct!")
    score += 1
else:
    print ("Incorrect! oh no! ")
answer = input ("Are talking to a me or AI? ")
if answer.lower() == "you":
    print ("Correct!")
    score += 1
else:
    print ("Incorrect! oh no! ")
answer = input ("Do you know you can die playing this? ")
if answer.lower() == "yes":
    print ("Correct!")
    score += 1
else:
    print ("Incorrect! oh no! ")
answer = input ("Do I can see you? ")
if answer.lower() == "yes":
    print ("Correct!")
    score += 1
else:
    print ("Incorrect! oh no! ")

print ("You got "+ str(score) + " questions correct!")
print ("You got "+ str((score / 5) * 100) + " %.")