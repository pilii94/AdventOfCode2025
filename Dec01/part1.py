# The actual password is the number of times the dial is left pointing at 0 after any rotation in the sequence

from pydantic import BaseModel
import re


class Rotation(BaseModel):
    unique_rotation: str

    @property
    def add_or_subsract(self) -> int:
        """Check if the dial is pointing left"""
        if self.unique_rotation[0] == "L":
            return -1
        else:
            return 1
        
    @property
    def get_value(self) -> int:
        """get the value of the rotation"""
        rotation_value = int(re.sub("R|L", "", self.unique_rotation))
        return rotation_value


class Rotations(BaseModel):
    rotation_sequence: list[Rotation]  
        

def read_input(filename: str) -> Rotations:
    """Read the input file and parse it into Banks."""
    rotations = []
    with open(filename, 'r') as f:
        for line in f:
            rotations.append(Rotation(unique_rotation=line))
            
    rotations = Rotations(rotation_sequence=rotations)
    
    return rotations


def get_reached_position(current_pos, unique_rotation)-> int:
    
    new_pos = current_pos + unique_rotation.add_or_subsract * unique_rotation.get_value

    return new_pos % 100





if __name__ == "__main__":
    

    test_rotations = [
       "L68",
       "L30",
       "R48",
       "L5",
       "R60",
       "L55",
       "L1",
       "L99",
       "R14",
       "L82"
    ]

    input = [Rotation(unique_rotation=t) for t in test_rotations]

    rotations = Rotations(rotation_sequence=input)

    print("\nTest cases:")
    positions = []
    current_pos = 50
    for rotation in rotations.rotation_sequence:
        current_pos = get_reached_position(current_pos, rotation)
        print(f"{rotation} -> {current_pos}")
        positions.append(current_pos)

    print(positions)
    print("=====")


    input_data = read_input('Dec01/input.txt')
    positions = []
    current_pos = 50
    for rotation in input_data.rotation_sequence:
        current_pos = get_reached_position(current_pos, rotation)
        print(f"{rotation} -> {current_pos}")
        positions.append(current_pos)


    print(positions)
   
    #how many times there is a 0 in positions?
    print(positions.count(0))
    
   
  


