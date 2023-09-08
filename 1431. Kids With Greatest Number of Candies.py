"""
Leetcode Problem 
Kids With the Greatest Number of Candies
"""

def kidsWithCandies(candies: list[int], extraCandies: int) -> list[bool]:
    mostCandies = max(candies)
    winner = []

    for kid in candies: 
        if kid + extraCandies >= mostCandies:
            winner.append(True)
        else: 
            winner.append(False)

    return winner