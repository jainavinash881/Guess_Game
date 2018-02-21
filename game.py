import random
def get_guess():     #take guess
    return input("What is your Guess : ")


def generete_code():   #generate Guess by computer
    digits = [str(num) for num in range(10)]

#shuffel digits

    random.shuffle(digits)
    return digits[:3]


#generate clue

def generate_clues(code,user_guess):

    if user_guess == code:
        return "Code Cracked!"

    clues = []

    for ind,num in enumerate(user_guess):
        if num == code[ind]:
            clues.append("match")
        elif num in code:
            clues.append("close")

    if clues == []:
        return ["nope"]
    else:
        return clues




print("Welcome! code breaker")
secrate_code = generete_code()

clue_report = []

while clue_report != "Code Cracked!":

    guess = get_guess()

    clue_report = generate_clues(guess,secrate_code)
    print("Here is the result of your Guess: ")
    for clue in clue_report:
        print(clue)
