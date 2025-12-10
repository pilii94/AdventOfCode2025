# Which ingredients are fresh? in all ranges
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

def read_input(filename: str) -> list[IDRange]:
    ranges = []

    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:  
                continue
                
            if '-' in line:
            
                start, end = map(int, line.split('-'))
                ranges.append(IDRange(start=start, end=end))
          
    return ranges

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

def unify_ranges(input_ranges: list[IDRange]) -> List[IDRange]:
    if not input_ranges:
        return []
    
    sorted_ranges = sorted(input_ranges, key=lambda x: x.start)
    
    merged = [sorted_ranges[0]]
    
    for current in sorted_ranges[1:]:
        last_merged = merged[-1]
        
        # Check if current range overlaps with the last merged range
        if current.start <= last_merged.end + 1:  
            # Merge ranges
            merged[-1] = IDRange(
                start=last_merged.start,
                end=max(last_merged.end, current.end)
            )
        else:
            # No overlap, add current range to merged list
            merged.append(current)
    
    return merged


if __name__ == "__main__":
 
    print("TEST")


    
    test_ranges = create_test_range()

    
    unified_ranges = unify_ranges(test_ranges)
    total_count = sum(range_.end - range_.start + 1 for range_ in unified_ranges)
    print(f"Fresh ingredients count: {total_count}")

    ranges = read_input('Dec05/input.txt')
     
    unified_ranges = unify_ranges(ranges)
    total_count = sum(range_.end - range_.start + 1 for range_ in unified_ranges)
    print(f"Fresh ingredients count: {total_count}")

