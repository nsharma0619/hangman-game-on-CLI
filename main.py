from random_word_generator import pick_random_word

def change_state(current_state, selected_word, input_char):
    modified_state = ""
    for i in range(len(selected_word)):
        if current_state[i] == "_" and selected_word[i] == input_char:
            modified_state+=selected_word[i]
        else:
            modified_state+=current_state[i]
    return modified_state


def check_state(input_char, attempts_left, selected_word, current_state):
    if input_char in selected_word:
        current_state = change_state(current_state, selected_word, input_char)
    else:
        attempts_left-=1

    return current_state, attempts_left



def print_current_state(current_state, attempts_left):
    print("current word state : ", end="")
    for i in current_state:
        print(i,end=" ")
    print("\tAttempts Remaining :",attempts_left)



def check_the_game(selected_word, current_state, attempts_left):
    if(attempts_left<=0):
        print("Sorry You Lost")
        print("The Word Was :",selected_word)
        return True

    if(current_state==selected_word):
        print("Congratulation you won")
        return True

    return False

    
def play_game():
    selected_word = pick_random_word()
    current_state = ""
    for i in selected_word:
        if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
            current_state+=i
        else:
            current_state+="_"
    attempts_left = 5
    print_current_state(current_state, attempts_left)
    while True:
        input_char = input("Guess the character : ")
        current_state, attempts_left = check_state(input_char, attempts_left, selected_word, current_state)
        print_current_state(current_state, attempts_left)

        game_state = check_the_game(selected_word, current_state, attempts_left)

        if game_state:
            break


if __name__=="__main__":
    play_game()