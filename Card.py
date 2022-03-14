class Card:
    def __init__(self, color, num, s_a):
        self.color = color
        self.num = num
        self.s_a = s_a

    def __str__(self):
        return f"{self.color} {self.num} {self.s_a}"

