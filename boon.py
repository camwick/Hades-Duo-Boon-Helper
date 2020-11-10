class Boon:
    # constructor
    def __init__(self, name, god1, god2, details1, details2):
        self.name = name
        self.gods = [god1, god2]
        self.details = [details1, details2]

    # acts as a toString method, but tests if parameter list is in the object
    def containsGod(self, list, size):
        amt = 0

        text = ""
        for i in range(size):
            amt += self.gods[0].count(list[i])
            amt += self.gods[1].count(list[i])

            # if both gods are in the list, then return a toString
            if amt == 2:
                text += self.name + '\n' + self.gods[0] + ': ' + self.details[0] + '\n' + self.gods[1] + ': ' + self.details[1] + '\n\n'

        return text