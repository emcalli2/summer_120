print("ADD DOCSTRINGS")
class Simplest:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c 

class Rotate:
    def __init__(self,first,second,third):
        self.first = first
        self.second = second
        self.third = third
    
    def get_first(self):
        return self.first

    def get_second(self):
        return self.second

    def get_third(self):
        return self.third

    def rotate(self):
        first = self.get_first()
        second = self.get_second()
        third = self.get_third()
        self.first = second
        self.second = third
        self.third = first

class Band:
    def __init__(self,singer):
        self.singer = singer
        self.drummer = None
        self.guitars = []

    def get_singer(self):
        return self.singer

    def set_singer(self, new_singer):
        self.singer = new_singer
    
    def get_drummer(self):
        if self.drummer is not None:
            return self.drummer

    def set_drummer(self, new_drummer):
        self.drummer = new_drummer

    def add_guitar_player(self, new_guitar_player):
        self.guitars.append(new_guitar_player)

    def fire_all_guitar_players(self):
        self.guitars = []

    def get_guitar_players(self):
        new_list = []
        for i in range(len(self.guitars)):
            new_list.append(self.guitars[i])
        return new_list

    def play_music(self):
        if self.get_singer() in "Frank Sinatra":
            print("Do be do be do")
        elif self.get_singer() in "Kurt Cobain":
            print("bargle nawdle zouss")
        else:
            print("La la la")
        if self.get_drummer() is not None:
            print("Bang bang bang!")
        for i in range(len(self.guitars)):
            print("Strum!")

class Color:
    def bounds(self,color):
        if color > 255:
            color = 255
        if color < 0:
            color = 0
        return color 

    def __init__(self, r, g, b):
        self.r = self.bounds(r)
        self.g = self.bounds(g)
        self.b = self.bounds(b)

    def __str__(self):
        return f"rgb{self.r,self.g,self.b}"

    def html_hex_color(self):
        return f"#{int(self.r):02X}{int(self.g):02X}{int(self.b):02X}"

    def get_rgb(self):
        return (self.r,self.g,self.b)

    def set_standard_color(self,name):
        if "yellow" in name.lower():
            self.r = 255
            self.g = 255
            self.b = 0
        if "red" in name.lower():
            self.r = 255
            self.g = 0
            self.b = 0

        if "black" in name.lower():
            self.r = 0
            self.g = 0
            self.b = 0

        if "white" in name.lower():
            self.r = 255
            self.g = 255
            self.b = 255

    def remove_red(self):
        self.r = 0

