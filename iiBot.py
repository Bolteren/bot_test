import os
import json
from fuzzywuzzy import fuzz


class conversationBot:
    responceBot = []
    usersSay = []

    def __init__(self):
        self.iiBotResponse()
        self.usersBotPhrases()

    def fileLoadText(self, path):
        fileOpenName = path
        with open(fileOpenName, encoding="utf-8") as fl:
            phrases = json.load(fl)
            return phrases

    def iiBotResponse(self):
        listOfFiles = os.listdir(path="bot.say")
        i = 0
        while i < len(listOfFiles):
            x = (self.fileLoadText("bot.say\\" + listOfFiles[i]))
            i += 1
            self.responceBot.append(x)

    def usersBotPhrases(self):
        listOfFiles = os.listdir(path="user.say")
        i = 0
        while i < len(listOfFiles):
            x = self.fileLoadText("user.say\\" + listOfFiles[i])
            i += 1
            self.usersSay.append(x)
        return self.usersSay

    def comparison(self, text):
        text = text.lower()
        k = 0
        counterInterior = 0
        counterExternal = 0
        counter = 0
        while counter < len(self.usersSay):
            counter2 = 0
            while counter2 < len(self.usersSay[counter]):
                j = fuzz.ratio(self.usersSay[counter][counter2], text)
                counter2 += 1
                if j > k:
                    k = j
                    counterInterior = counter
                    counterExternal = counter2
            counter += 1
            if k > 40:
                result = True
            else:
                result = False
        return [result, counterInterior, counterExternal - 1]

    def dialog(self, text):
        respounce = self.comparison(text)
        if respounce[0]:
            print("asd " + str(respounce[2]))
            respounceFrase = self.responceBot[respounce[1]][respounce[2]]
        else:
            respounceFrase = "Я не смог разобраться."
        return respounceFrase


def main():
    q = conversationBot()
    print(q.dialog("привет"))


if __name__ == "__main__":
    main()
