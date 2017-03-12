#with open("insults.csv","r") as f:
#    contents = f.read()
#    print(contents)
import random
import csv

list_a = []
list_b = []
list_c = []

with open("insults.csv", "r") as f:
    for line in f:
        words = line.split(";")
        list_a.append(words[0])
        list_b.append(words[1])
        list_c.append(words[2].strip())

def insult_me():
    word_a = random.choice(list_a)
    word_b = random.choice(list_b)
    word_c = random.choice(list_c)

    insult = "Thou " + word_a + " "+ word_b + " " + word_c + "!"
    print(insult)

    rating = input("Please rate your insult from 1 - 5: ")
    print("You've given the insult: " + insult + " the rating " + rating + "!")

    writer = csv.writer(open("ratings.csv", "a", newline=""))
    writer.writerow([insult.strip() + ";" + rating.strip()])


insult_me()

def display_rating():
    display = input("Would you like to display the most rated insult? Y/N")
    if display == "Y":
        maxrate = 0
        with open("ratings.csv","r") as f:
            next(f)
            try:
                m = int(column[1])
                maxrate = max(maxrate,m)
            except:
                pass

        print (maxrate)

    else:
        print("Have a nice day")

display_rating()
