# for ordered lists

items = [6,20,8,19,56,23,87,41,49,53]


def binary_search(item, itemlist):
    # get the list size
    list_size = len(itemlist) - 1

    # start at the two ends of the list
    lower_idx = 0
    upper_idx = list_size

    while lower_idx < upper_idx:
        # calculate the middle point
        mid_point = (lower_idx + upper_idx) // 2
        # if item is found, return the index
        if itemlist[mid_point] == item:
            return mid_point

        # otherwise, get the next midpoint
        if item > itemlist[mid_point]:
            lower_idx += 1
        else:
            upper_idx -= 1
    
    if lower_idx > upper_idx:
        return None

print(binary_search(8, items))