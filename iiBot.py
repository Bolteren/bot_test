import os
import json
from fuzzywuzzy import fuzz


def fileLoadText(path):
    fileOpenName = path
    with open(fileOpenName, encoding="utf-8") as fl:
        phrases = json.load(fl)
        return phrases


def iiBotResponse():
    listOfFiles = os.listdir(path="bot.say")
    i = 0
    responceBot = []
    while i < len(listOfFiles):
        x = (fileLoadText("bot.say\\" + listOfFiles[i]))
        i += 1
        responceBot.append(x)
    return responceBot


def usersBotPhrases():
    listOfFiles = os.listdir(path="user.say")
    i = 0
    usersSay = []
    while i < len(listOfFiles):
        x = fileLoadText("user.say\\" + listOfFiles[i])
        i += 1
        usersSay.append(x)
    return usersSay


responceBot = iiBotResponse()
usersSay = usersBotPhrases()


def comparison(text):
    text = text.lower()
    k = 0
    k1 = 0
    k2 = 0
    counter = 0
    while counter < len(usersSay):
        counter2 = 0
        while counter2 < len(usersSay[counter]):
            j = fuzz.ratio(usersSay[counter][counter2], text)
            counter2 += 1
            if j > k:
                k = j
                k1 = counter
                k2 = counter2
        counter += 1
        if k > 40:
            k3 = True
        else: k3 = False
    print(k)
    print(usersSay[k1][k2 - 1])
    return [k3, k1, k2 - 1]


def main():
    while True:
        text = input("Введите текст: ")
        print(comparison(text))

    print(comparison("kvh4twESDG,,jhkgGHSFAFGsf"))


if __name__ == "__main__":
    main()
