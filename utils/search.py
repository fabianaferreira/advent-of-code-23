# Returns index of x in arr if present, else -1
from collections import deque


def binary_search(arr, low, high, x):
    # Check base case
    if high >= low:
        mid = (high + low) // 2

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)

        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        # Element is not present in the array
        return -1


def bfs(graph, start):
    search_queue = [(start, 0)]
    visited = set()
    max_distance = 0

    while len(search_queue) > 0:
        current_node, distance = search_queue.pop(0)
        visited.add(current_node)
        max_distance = max(max_distance, distance)

        for next in graph[current_node] - visited:
            search_queue.append((next, distance + 1))

    return max_distance
