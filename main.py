from data import list_of_words
import random
import clear



random_word = random.choice(list_of_words)
length_of_word = len(random_word)
lives = 6
end_of_game = False
display = []
for _ in range(length_of_word):
    display += "_"

while not end_of_game:
    user_input = input(" Prosim vlozte pismeno: ").lower()
    # print(random_word)
    if user_input in display:
        print(f"Uz si dane pismeno {user_input} napisal")
    for l in range(length_of_word):
        letter = random_word[l]
        if letter == user_input:
            display[l]=letter

    if user_input not in random_word:
        print(f"Tvoj {user_input} sa nenachadza v slove.Prichadzas o jeden zivot.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("To ma mrzi prehral si.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("Gratulujem. Vyhral si!")







