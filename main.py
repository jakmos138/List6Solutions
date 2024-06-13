from collections import defaultdict

# Task 1a
def find_majority_element(arr):
    # Also known as a Boyer-Moore Voting Algorithm
    n = len(arr)
    if n == 0:
        return None

    # Find a candidate
    candidate = arr[0]
    count = 1

    for i in range(1, n):
        if arr[i] == candidate:
            count += 1
        else:
            count -= 1
            if count == 0:
                candidate = arr[i]
                count = 1

    # Verify the candidate
    count = 0
    for num in arr:
        if num == candidate:
            count += 1

    if count > n // 2:
        return candidate
    else:
        return None


# Task 1b
def smallest_subarray_with_sum_greater_than_v(A, v):
    # We use the sliding window technique
    n = len(A)
    min_length = float('inf')
    start = 0
    current_sum = 0
    min_start = -1
    min_end = -1

    # initial loop (linear) that increases the right bound of the subset with each iteration to increase the window
    for end in range(n):
        current_sum += A[end]

        # nested loop with irrelevant time complexity, used to increase the left bound to descrease the window
        while current_sum > v:
            if end - start + 1 < min_length:
                min_length = end - start + 1
                min_start = start
                min_end = end + 1 # adjust for the difference in indexing behaviour

            current_sum -= A[start]
            start += 1

    if min_length == float('inf'):
        return (-1, -1)  # No valid subarray found

    return (min_start, min_end)


# Task 1c
def smallest_missing_number(arr):
    # Assuming array is sorted and integers are distinct as per specification
    if len(arr) == 0:
        return None
    else:
        # Check if the array elements are increasing or decreasing
        variance = arr[1] - arr[0]
        result = 0
        for number in arr[::int(variance/abs(variance))]:
            if number == result+1:
                result = number
            else:
                result += 1
                break
        return result


# Task 1e
def detect_cycle_in_directed_graph(V, edges):
    # create a dictionary to store edges
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
    
    # create lists for support during search
    visited = [False] * V # used to check if a node was ever visited during dfs
    rec_stack = [False] * V # used to check if a node was visited in the current recursion cycle

    # dfs algorithm logic focusing on cycle finding
    def dfs(v):
        visited[v] = True
        rec_stack[v] = True
        
        for neighbor in graph[v]:
            if not visited[neighbor]:
                if dfs(neighbor):
                    return True
            elif rec_stack[neighbor]:
                return True
        
        rec_stack[v] = False
        return False
    
    # initialization of solving
    for node in range(V):
        if not visited[node]:
            if dfs(node):
                return True
    return False


# Example usages:
# Task 1a
A = [3, 3, 4, 2, 4, 4, 2, 4, 4]

print("Task 1a:")
print(f"A: {A}")
result = find_majority_element(A)
print(f"The majority element is: {result}", end="\n\n")

# Task 1b
A = [1, 4, 45, 6, 0, 19]
v = 51

print("Task 1b:")
print(f"A: {A}")
result = smallest_subarray_with_sum_greater_than_v(A, v)
print(f"The smallest subarray with sum greater than {v} is: {A[result[0]:result[1]]}", end="\n\n")

# Task 1c
A = [1,2,4,5,8,9,10,20,30,138]

print("Task 1c:")
print(f"A: {A}")
# checking both types of sorted arrays
print(f"The smallest missing number in the array {A} is: {smallest_missing_number(A)}")
print(f"The smallest missing number in the array {A} is: {smallest_missing_number(sorted(A, reverse=True))}", end="\n\n")

# Task 1e
# Example usage:
V = 5
edges = [(0, 1), (1, 2), (2, 4), (2, 3)]

print("Task 1e:")
print("Test 1 (no cycles):")
print(f"Edges: {edges}")
has_cycle = detect_cycle_in_directed_graph(V, edges)
print(f"Graph has a cycle: {has_cycle}")

V = 4
edges = [(0, 1), (1, 2), (2, 0), (2, 3)]

print("Test 2 (has cycles):")
print(f"Edges: {edges}")
has_cycle = detect_cycle_in_directed_graph(V, edges)
print(f"Graph has a cycle: {has_cycle}")