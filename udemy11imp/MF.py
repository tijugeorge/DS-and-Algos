#most frequently occuring element in array
#The most frequently occurring item in [1, 3, 1, 3, 2, 1] 

# Implement your function below.
def most_frequent(given_list):
    max_count = -1
    max_item = None
    count = {}
    for i in given_list:
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1
        if count[i] > max_count:
            max_count = count[i]
            max_item = i
    return max_item

