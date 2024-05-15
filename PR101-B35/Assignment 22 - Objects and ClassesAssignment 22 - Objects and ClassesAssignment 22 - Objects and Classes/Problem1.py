class Wall:
    
    def __init__(self):
        self.width = 0.0
        self.height = 0.0

    
    def __init__(self, width=0.0, height=0.0):
        if width < 0:
            self.width = 0.0
        else:
            self.width = width
        
        if height < 0:
            self.height = 0.0
        else:
            self.height = height

    
    def get_width(self):
        return self.width

    
    def get_height(self):
        return self.height

    
    def set_width(self, width):
        if width < 0:
            self.width = 0.0
        else:
            self.width = width

    
    def set_height(self, height):
        if height < 0:
            self.height = 0.0
        else:
            self.height = height

    
    def get_area(self):
        return self.width * self.height


wall = Wall(5, 4) 
print("area= ", wall.get_area())  
wall.set_height(-1.5)  
print("width= ", wall.get_width()) 
print("height= ", wall.get_height())  
print("area= ", wall.get_area())  