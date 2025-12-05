# method 0x434C49434B

from pydantic import BaseModel
import re


class Rotation(BaseModel):
    unique_rotation: str

    @property
    def add_or_subsract(self) -> int:
        if self.unique_rotation[0] == "L":
            return -1
        else:
            return 1
        
    @property
    def get_value(self) -> int:
        rotation_value = int(re.sub("R|L", "", self.unique_rotation))
        return rotation_value


class Rotations(BaseModel):
    rotation_sequence: list[Rotation]  
        

def read_input(filename: str) -> Rotations:
    rotations = []
    with open(filename, 'r') as f:
        for line in f:
            rotations.append(Rotation(unique_rotation=line.strip()))
            
    rotations = Rotations(rotation_sequence=rotations)
    
    return rotations


def get_reached_position(current_pos, unique_rotation)-> int:
    
    new_pos = current_pos + unique_rotation.add_or_subsract * unique_rotation.get_value

    return new_pos % 100


def count_zero_crossings(current_pos: int, rotation: Rotation) -> int:
    """Count how many times the dial points at 0 during a rotation"""
    direction = rotation.add_or_subsract
    steps = rotation.get_value
    
    if steps == 0:
        return 0
    
    zero_count = 0
    
    # count every time we pass position 0
    if direction == 1:  #R
        # move right 
        # We hit 0: (current_pos + k) % 100 == 0
        # 1st time: k = (100 - current_pos) % 100
        # Then, every 100 steps 
        
        first_zero = (100 - current_pos) % 100
        if first_zero == 0:
            first_zero = 100  # if at 0, next 0 is in 100 steps
        
        if steps >= first_zero:
            zero_count = 1
            remaining_steps = steps - first_zero
            zero_count += remaining_steps // 100
    else:  # Left
      
        first_zero = current_pos if current_pos > 0 else 100
        
        if steps >= first_zero:
      
            zero_count = 1
            remaining_steps = steps - first_zero
       
            zero_count += remaining_steps // 100
    
    return zero_count


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

    print("\nTest cases (Part 2):")
    total_zeros = 0
    current_pos = 50
    
    for rotation in rotations.rotation_sequence:
        zeros_in_rotation = count_zero_crossings(current_pos, rotation)
        new_pos = get_reached_position(current_pos, rotation)
        total_zeros += zeros_in_rotation
        print(f"{rotation.unique_rotation}: {current_pos} -> {new_pos}, crosses 0 {zeros_in_rotation} time(s)")
        current_pos = new_pos

    print(f"\nTotal times pointing at 0: {total_zeros}")
    print("Expected: 6")
    print("=====")


    input_data = read_input('Dec01/input.txt')
    total_zeros = 0
    current_pos = 50
    
    for rotation in input_data.rotation_sequence:
        zeros_in_rotation = count_zero_crossings(current_pos, rotation)
        current_pos = get_reached_position(current_pos, rotation)
        total_zeros += zeros_in_rotation
        
    print(f"\nPart 2 Answer: {total_zeros}")
