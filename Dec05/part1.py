# Which ingredients are fresh?
from pydantic import BaseModel
from typing import List, Dict, Tuple
import numpy as np

class Ingredients(BaseModel):
    ids_list: List[int]

class IDRange(BaseModel):
    start: int
    end: int

    def contains(self, number: int) -> bool:
        """Check if a number is within the range (inclusive of start and end)"""
        return self.start <= number <= self.end

def read_input(filename: str) -> Tuple[list[IDRange], Ingredients]:
    ranges = []
    ingredient_ids = []
    
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:  
                continue
                
            if '-' in line:
            
                start, end = map(int, line.split('-'))
                ranges.append(IDRange(start=start, end=end))
            else:
            
                ingredient_ids.append(int(line))
    
    ingredients = Ingredients(ids_list=ingredient_ids)
    return ranges, ingredients

def create_test_range() -> list[IDRange]:

    test_data = [
        "3-5",
        "10-14", 
        "16-20",
        "12-18",
    ]
    
    ranges = []
    for range_str in test_data:
        start, end = map(int, range_str.split('-'))
        ranges.append(IDRange(start=start, end=end))
    
    return ranges


def create_test_ingredients() -> Ingredients:

    test_data = [
       1, 5, 8, 11, 17, 32
    ]
    
    return Ingredients(ids_list=test_data)

if __name__ == "__main__":
 
    print("TEST")


    
    test_ranges = create_test_range()
    test_ingredients = create_test_ingredients()

    fresh_ingredients = []
    for ing in test_ingredients.ids_list:
        for range in test_ranges:
            if range.contains(ing):
                print(f"Ingredient {ing} is fresh in range {range}")
                fresh_ingredients.append(ing)
            
    print(f"Fresh ingredients count: {len(set(fresh_ingredients))}")

    ranges, ingredients = read_input('Dec05/input.txt')

    fresh_ingredients = []
    for ing in ingredients.ids_list:
        for range in ranges:
            if range.contains(ing):
                print(f"Ingredient {ing} is fresh in range {range}")
                fresh_ingredients.append(ing)
            
    print(f"Fresh ingredients count: {len(set(fresh_ingredients))}")

