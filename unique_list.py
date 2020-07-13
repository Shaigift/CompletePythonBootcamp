#write a Python function that takes a list and returns a new list with unique elements if the first list


def unique_list(lst):
    seen_numbers = []
    for number in lst:
        if number not in seen_numbers:
            seen_numbers.append(number)
    return seen_numbers

