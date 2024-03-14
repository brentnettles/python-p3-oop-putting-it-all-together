#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand_param, size_param, condition_param="Used"):
        self.brand = brand_param
        self._size = size_param
        self.condition = condition_param

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, size_param):
        if isinstance(size_param, int):
            self._size = size_param
        else:
            print("size must be an integer")

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New" 


    def __repr__(self):
        return f"<Shoe {self.brand} {self.size}>"

new_shoe = Shoe('nike', 'X', "New")
print(new_shoe)
