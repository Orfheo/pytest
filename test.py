from zaza.gigio import gigio
from zaza.papero import zizo

class Test :
    """
        Again class for testing
    """
    def __init__ ( self, x=0, y=0) :
        self.x = 0
        self.y = 0

    def __str__(self):
        return "(%s,%s)" % (self.x,self.y)

    def pippo (self):
        """
            x = 1
            y = 2
        """
        self.x = 1
        self.y = 2

t = Test ( 0, 0 )
t.pippo()
g = gigio(2)
z = zizo("a")

print ( t, g, z )

z.__str__()



