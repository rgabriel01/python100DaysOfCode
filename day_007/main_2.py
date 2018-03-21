import helpers

class Main2:
    def __init__(self, name):
        self.name = name

    def formalize(self):
        return helpers.Capitalize(self.name)

    def greet(self):
        return helpers.Hello()

main = Main2('raymond')
print("Say hi to ", main.formalize())
main.greet()
