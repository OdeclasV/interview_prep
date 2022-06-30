items = [6,20,8,19,5,23,87,41,49,53]


def selection_sort(dataset):
    suffix_start = 0
    while suffix_start != len(dataset):
        for i in range(suffix_start, len(dataset)):
            print(dataset[i])
            print(dataset[suffix_start])
            if dataset[i] < dataset[suffix_start]:
                dataset[suffix_start], dataset[i] = dataset[i], dataset[suffix_start]
        suffix_start += 1
    return dataset

print(selection_sort(items))