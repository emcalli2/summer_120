""" 
    File: simple_classes.py
    Author: Elizabeth McAllister
    Purpose: This program has four simple classes: simplest - a simple class, 
    rotate - a class that rotates values, band - builds a band, and color - gives information
    about a certain color
    Class: Csc 120 Summer 2024
"""
class Simplest:
    """
    This class represents a trivial object and has three public fields,a,b,c.
    The constructor builds three objects and must be passed the public fields a,b,c
    The class defines no methods.

    """
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c 

class Rotate:
    """
    This class represents a rotation of values in a counterclockwise motion.
    First to third, third to second, and second to first.
    The constructor builds three objects using three public fields, first, second, and third
    The class defines several methods: get_[first,second,third]()) - a getter for all three assignments
                                        rotate() - rotates the values counterclockwise
                                       

    """
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
        """
        This function rotates the values counterclockwise
        Arguments: self
        Returns: none
        pre-conditions: None
        """
        first = self.get_first()
        second = self.get_second()
        third = self.get_third()
        self.first = second
        self.second = third
        self.third = first

class Band:
    """
    This class represents a band with at least one singer and a drummer that can
    be set later. The singer is the public field
    The constructor builds a singer, sets drummer to None, and sets guiarts to an empty list
    The class defines several methods:
        get_[singer,drummer]() = getter for the singer and drummer
        set_singer(new_singer) = setter for the new_singer
        set_drummer(new_drummer) = setter for the new_drummer
        add_guitar_player(new_guitar_player) = adds the new player to the guitars list
        fire_all_guitar_players() = resets the guitar list to an empty list
        get_guitar_player() = creates a new list that is a copy of the guitar list
        play_music() = plays the music based on who is in the band

    """
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
        """
        This function adds a new guitar player to the guitar list
        arguments: new_guitar_player - the new player to be added
        returns: none
        preconditions: none
        """
        self.guitars.append(new_guitar_player)

    def fire_all_guitar_players(self):
        """
        This function fires(get rid of) all of the guitar players by 
        reseting the guitars to an empty list
        arguments: self
        returns: none
        preconditions: none
        """
        self.guitars = []

    def get_guitar_players(self):
        """
        This function copies the guitars list so that the user can access the 
        new_list of guitar players
        arguments: self
        returns: new_list - the copied list of guitar players
        """
        new_list = []
        for i in range(len(self.guitars)):
            new_list.append(self.guitars[i])
        return new_list

    def play_music(self):
        """
        This function plays(prints out lyrics) different music based on 
        who is in the band
        Arguments: self
        returns: none
        preconditions: none
        """
        if self.get_singer() in "Frank Sinatra":
            print("Do be do be do")
        elif self.get_singer() in "Kurt Cobain":
            print("bargle nawdle zouss")
        else:
            # the singer always sings la la la unless meeting the qualifications above
            print("La la la")
        # if there is a drummer in the band, they play
        if self.get_drummer() is not None:
            print("Bang bang bang!")
        # each guitar player in the band strums
        for i in range(len(self.guitars)):
            print("Strum!")

class Color:
    """
    This class represents different attributes of colors
    The constructor builds three color objects based on three public
    fields, r, g, b.
    The class defines several methods
        html_hex_color() = returns the hex representation of the overall color
        get_rgb() = gets the color in tuple form
        set_standard_color() = sets the r,g,b fields for standard colors
        remove_red() = removed the red from the overall color
        bounds(color) = sets the bounds for the color(r,g, or b)

    """
    def bounds(self,color):
        """
        This function sets the bounds for the colors, no color can be greater
        than 255 or less than 0.
        Arguments: color - a specific color field, either r, g, or b
        Returns: color - the modified color to meet the bounds
        preconditions: color must be an integer
        """
        if color > 255:
            # if the color is greater than 255, it is set to 255
            color = 255
        if color < 0:
            # if the color is less than zero, it is set to 0
            color = 0
        return color 

    def __init__(self, r, g, b):
        self.r = self.bounds(r)
        self.g = self.bounds(g)
        self.b = self.bounds(b)

    def __str__(self):
        return f"rgb{self.r,self.g,self.b}"

    def html_hex_color(self):
        """
        This function returns the hex version of the overall color
        Arguments: self
        Returns: the hex representation of the overall colo
        Precondition: none
        """
        return f"#{int(self.r):02X}{int(self.g):02X}{int(self.b):02X}"

    def get_rgb(self):
        return (self.r,self.g,self.b)

    def set_standard_color(self,name):
        """
        This function sets the color fields for standard colors
        Arguments: name - a standard color
        Returns: None
        Precinditions: name is a standard color
        """
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
        """
        This function removed the red from a color
        Arguments: self
        Returns: None
        Preconditions: None
        """
        self.r = 0

