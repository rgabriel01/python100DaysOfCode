#import helpers
from helpers import Capitalize, Hello, Later

class Main:
    def formalize(self, word):
        return Capitalize(word)

    def greet(self):
        return Hello()

    def bye(self):
        return Later()

main = Main()
formatted_word = main.formalize("incredible hulk")
print("Let's format this word:", formatted_word)
main.greet()
main.bye()



