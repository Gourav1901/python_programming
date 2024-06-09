def min_rounds_to_seat(T, test_cases):
    results = []
    for t in range(T):
        N = test_cases[t][0]
        heights = test_cases[t][1]
        
        rounds = 1
        last_height = heights[0]
        
        for i in range(1, N):
            if heights[i] <= last_height:
                rounds += 1
                last_height = heights[i]
            else:
                last_height = heights[i]
        
        results.append(rounds)
    
    return results

# Read input
T = int(input())
test_cases = []
for _ in range(T):
    N = int(input())
    heights = list(map(int, input().split()))
    test_cases.append((N, heights))

# Get results
results = min_rounds_to_seat(T, test_cases)

# Print results
for result in results:
    print(result)
