def red_car(r,g,b):
    # for brighter red
    if r > 140 and r <= 255 and g > 0 and g <= 100 and b > 0 and b <= 100:
        return True
    # for darker red
    elif r > 45 and r <= 150 and g > 0 and g <= 35 and b > 0 and b <= 35:
        return True
    # for magenta red
    elif r > 45 and r <= 90 and g > 0 and g <= 35 and b > 45 and b <=90:
        return True
    return False

def selection_sort(all_scores):
    n = len(all_scores)
    for l in range(n):
        min_index = l
        for m in range(l+1, n):
            if all_scores[m][1] < all_scores[min_index][1]:
                min_index = m
        all_scores[l], all_scores[min_index] = all_scores[min_index], all_scores[l]
    # print(all_scores)
    return all_scores

def binary_score(sorted_scores, target):
    low = 0
    high = len(sorted_scores) - 1
    while low <= high:
        mid = (low + high) // 2
        result = int(sorted_scores[mid][1])
        if result == target:
            return mid
        elif result < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1