Set 2 Algorithms Challenge: First Non-Repeating Character & Count Islands

A submission for the Set 2 algorithms challenge.

Student: Manuja Nagvekar
Set: 2
Repository: set2_manuja_nagvekar
Language Used: Python


1. First Non-Repeating Character

Problem Description

Write a function that returns the first non-repeating character in a given string.

Example:

Input: "swiss"

Output: "w"

Implementation Details

Case Sensitivity: The implementation treats the input as case-sensitive and assumes ASCII characters.

No Match: If no such character exists (e.g., in "aabb" or ""), the function returns an empty string ("").

Efficiency Goal: The solution is designed for O(n) time complexity using two passes:

First Pass (Counting): Uses a hash map (dictionary) to count the frequency of every character in the string.

Second Pass (Finding): Iterates through the string again and checks the character's count in the map. The first character encountered with a count of 1 is the result.

Acceptance Criteria

Handles empty strings ("") correctly.

Handles inputs where all characters repeat (e.g., "aabbaa").

Includes simple unit tests to verify the logic.


2. Count Islands in a Grid (Python)

Problem Description

Given a 2D grid composed of 1s (land) and 0s (water), count the total number of connected islands.

Example:

Input:

[[1,1,0,0],
 [0,1,0,1],
 [1,0,0,1]]

Answer: 3

Implementation Details

Connectivity: Islands are defined by 4-directional connectivity (up, down, left, right). Diagonal cells do not count as connected.

Algorithm: The solution uses Depth-First Search (DFS) to traverse and mark entire connected land masses.

The main loop iterates over every cell.

When a cell containing '1' is found, the island count is incremented.

A recursive DFS function is immediately called on that cell to "sink" the entire island (change all connected '1's to a placeholder like '0' or a visited marker) so it is not counted again.

Acceptance Criteria

The function correctly counts islands for the provided example and custom test cases.

Time Complexity: Achieves O(m · n), where $m$ and $n$ are the dimensions of the grid, as every cell is visited at most once.


Space Complexity: O(m · n) in the worst case (e.g., a grid entirely of land), primarily due to the DFS recursion stack.
