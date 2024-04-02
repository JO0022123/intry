def rearrange_list(lst):
    if len(lst) >= 2:
        lst[0], lst[1] = lst[1], lst[0]  # Swap the first and second elements
    return lst

input_list = [5, 7, 9, 3, 4]
output_list = rearrange_list(input_list)
print(output_list)