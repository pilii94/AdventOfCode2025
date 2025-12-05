# How many rolls of paper can be accessed by a forklift?
from pydantic import BaseModel
from typing import List, Dict
import numpy as np

class Wall(BaseModel):
    wallmatrix: List[List[str]]

    @property
    def height(self) -> int:
        return len(self.wallmatrix)
    
    @property
    def width(self) -> int:
        return len(self.wallmatrix[0])
    
    def get_adjacent_counts(self, y: int, x: int) -> int:
        count = 0
        directions = [
            (-1, -1), (-1, 0), (-1, 1),  
            (0, -1),           (0, 1),   
            (1, -1),  (1, 0),  (1, 1)     
        ]
        
        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if 0 <= ny < self.height and 0 <= nx < self.width:
                if self.wallmatrix[ny][nx] == '@':
                    count += 1
        return count

    def count_accessible_rolls(self) -> int:
      
        count_accessible_rolls = 0
        
        for y in range(self.height):
            for x in range(self.width):
                if self.wallmatrix[y][x] == '@':
                    if self.get_adjacent_counts(y, x) < 4:
                        count_accessible_rolls += 1
        
        return count_accessible_rolls


def read_input(filename: str) -> Wall:
    matrix = []
    with open(filename, 'r') as f:
        for line in f:
            row = list(line.strip())
            if row: 
                matrix.append(row)
    
    return Wall(wallmatrix=matrix)


def create_test_wall() -> Wall:

    test_data = [
        "..@@.@@@@.",
        "@@@.@.@.@@",
        "@@@@@.@.@@",
        "@.@@@@..@.",
        "@@.@@@@.@@",
        ".@@@@@@@.@",
        ".@.@.@.@@@",
        "@.@@@.@@@@",
        ".@@@@@@@@.",
        "@.@.@@@.@."
    ]
    
    matrix = [list(row) for row in test_data]
    return Wall(wallmatrix=matrix)


if __name__ == "__main__":
 
    print("TEST")
    test_wall = create_test_wall()
    print(f"Test Wall dimensions: {test_wall.height} x {test_wall.width}")
    test_result = test_wall.count_accessible_rolls()
    print(f"Test accessible rolls: {test_result}")
 


    wall = read_input('Dec04/input.txt')
    print(f"Wall dimensions: {wall.height} x {wall.width}")
    print(f"Total accessible @ symbols: {wall.count_accessible_rolls()}")
