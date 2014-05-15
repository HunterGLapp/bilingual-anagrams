from loadwords import loadwords, getword
import random
import time
eng_word_counters, span_word_counters, stripped_eng_words, stripped_span_lines = loadwords()
points = 0
print "Bilingual Word scramble! Guess the word in english or spanish. Get 50 points. Spanish words are worth more." 
while True:
    exit = raw_input("Press Enter to play, 9 then Enter to exit\n")
    if exit == '9'or points == 50:
        break
    else:
        eng, span = getword(eng_word_counters, span_word_counters, stripped_eng_words, stripped_span_lines)
        eng_random = list()
        #print eng
        for letter in eng:
            eng_random.append(letter)
        #print eng_random
        random.shuffle(eng_random)
        #print eng_random
        counter = 0
        choice = "2"
        known_chars = list()
        while counter < len(eng_random):
            known_chars.append(eng_random[counter])
            for letter in known_chars:
                print letter,
            print "_ " * (len(eng_random) - counter - 1)
            counter += 1
            choice = raw_input("3 to guess english, 4 to guess spanish, Enter to continue\n")
            if choice == "3":
                eng_guess = raw_input("input your guess\n")
                if eng_guess == eng:
                    print "you win! +5 points"
                    points += 5
                else:
                    if eng_guess in stripped_eng_words:
                        print "that's not the one i was thinking of, but ok. Have 3 points"
                        print " I was thinking of", eng
                        points += 3
                    else:
                        print "sorry, wrong answer\n"
                        if counter == len(eng_random):
                            print "the correct answer was", eng
            if choice == "4":
                span_guess = raw_input("pon tu respuesto\n")
                if span_guess == span:
                    print "goooooooool\n + 10 puntos"
                    points += 10
                else:
                    if span_guess in stripped_span_lines:
                        print "casi... + 5 puntos"
                        print "pensaba de", span
                        points += 5
                    else:
                        print "lo siento, es incorrecto\n"
                        if counter == len(eng_random):
                            print "la respuesta correcta fue", span
