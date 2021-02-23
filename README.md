# bonus_work

Python Bonus Work

## Searching for Largest Rectangle:

Write a small python function that will generate a list of rectangle tuples with integer dimensions (w, h). The width dimension can vary from 2 to 10 (not including 10). The height dimension should vary between whatever the width is and 10 (not including 10). The resulting list of tuples should be sorted in order from largest enclosed area to smallest.

To sort according to enclosed area, use the formula (w - 1) \* (h - 1). This will compensate for the off-by-1 indexing that is introduced by using the range() function for the w and h values.
