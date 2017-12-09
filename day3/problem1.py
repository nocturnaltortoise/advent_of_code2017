import math

input_position = 368078

# i = input_position
# lower_odd_square = None
# while not lower_odd_square and i > 1:
#     if math.sqrt(i) % 2 == 1:
#         lower_odd_square = i
#     i -= 1
#
# i = input_position
# upper_even_square = None
# while not upper_even_square:
#     if math.sqrt(i) % 2 == 0:
#         upper_even_square = i
#     i += 1

even_square = math.floor(math.sqrt(input_position)) ** 2
odd_square = math.floor(math.sqrt(input_position) + 1) ** 2
width = math.sqrt(odd_square)
corners = [odd_square - (width - 1) * i for i in range(1, 4)]
corners = corners[::-1]
if input_position < odd_square:
    corners.append(corners[-1] + (width - 1))
# min_distance_to_corner = min([abs(input_position - corner) for corner in corners])
midpoints = [corner - math.floor(width / 2) for corner in corners]
min_distance_to_midpoint = min([abs(input_position - midpoint) for midpoint in midpoints])
odd_numbers = [i for i in range(input_position) if i % 2 == 1 and math.sqrt(i).is_integer()]
distance_to_middle = len(odd_numbers)

print(odd_square, even_square, width, corners, min_distance_to_midpoint + distance_to_middle)
