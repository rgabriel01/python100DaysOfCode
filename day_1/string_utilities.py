class StringUtilities:
    def __init__(self, word=""):
        self.word = word

    def reverse_word(self):
        reversed_word= ""
        counter = len(self.word) - 1
        while (counter >= 0):
            reversed_word += self.word[counter]
            counter -= 1
        return reversed_word

new_word = StringUtilities("valhalla!").reverse_word()
print(new_word)
