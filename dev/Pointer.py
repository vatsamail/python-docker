class Point():

    """
    Summary: 

    ----------------
    Attributes: <variable_name> : <data_type> : <purpose>
                x : float : store x coordinate value
                y : float : store y coordinate value
    ----------------
    methodName: <name>(<parameters>) : <return_type> : <purpose>
                set(x, y): void: creates a point
                show(void): void: displays a point using simple print
                quad(): [1/2/3/4] : provides the quadrant of a point
                add(point2): point : adds two points and creates a new point
                sub(point2): point : subtract two points and creates a new point

    """
    def __init__(self, x, y):
        """
        Summary: initialize a point
        ----------------
            Parameters: <input_parameter> : <data_type> : <purpose>
                        x: float : x value
                        y: float : y value
        """
        self.x = x
        self.y = y
    
    def set(self, x, y):
        """
        <name>(<parameters>) : <return_type> : <purpose>
                    set(x, y): void: creates a point
        """
        self.x = x
        self.y = y

    def show(self):
        """
        <name>(<parameters>) : <return_type> : <purpose>
                   show(void): void: displays a point using simple print
        """
        print("X:", self.x, "Y:", self.y)

    def quad(self):
        """
        <name>(<parameters>) : <return_type> : <purpose>
                   quad(void): [1/2/3/4] : provides the quadrant of a point
        """
        quad = 1
        if (self.x < 0 and self.y < 0):
            quad = 3
        elif (self.x < 0 and self.y >= 0):
            quad = 2
        elif (self.x >= 0 and self.y < 0):
            quad = 4
        return quad

    def add(self, p2):
        """
        <name>(<parameters>) : <return_type> : <purpose>
                  add(point2): point : adds two points and creates a new point
        """
        x = self.x + p2.x
        y = self.y + p2.y
        p = Point(x,y)
        return p

    def sub(self, p2):
        """
        <name>(<parameters>) : <return_type> : <purpose>
                  sub(point2): point : subtract two points and creates a new point
        """
        x = self.x - p2.x
        y = self.y - p2.y
        p = Point(x,y)
        return p

    def mul(self, p2):
        """
        place holder: https://jira.sw.nxp.com/browse/SDTOOLS-69
        """
        pass

    def __str__(self):
        return "X: "+str(self.x)+", Y: "+str(self.y)



def main():
        """
        Summary: This code is a package that can also be used as a standalone python script.
            This code will dumps out docstring and does some basic testing
        ----------------
        """

        p1 = Point(1,1)
        p2 = Point(-2,2)
        print("p1.__doc__:", p1.__doc__)
        print("P1 is:", p1, "and it is in", p1.quad(), "quad")
        print("P2 is:", p2, "and it is in", p2.quad(), "quad")

        p3 = p1.add(p2)
        p4 = p1.sub(p2)

        print("P3 is:", p3, "and it is in", p3.quad(), "quad")
        print("P4 is:", p4, "and it is in", p4.quad(), "quad")


if __name__ == "__main__":
    main()