def find_first_unique_gift(stream):
    from collections import deque, Counter
    
    queue = deque()
    frequency = Counter()
    result = []
    
    for char in stream:
        queue.append(char)
        frequency[char] += 1
        
        while queue and frequency[queue[0]] > 1:
            queue.popleft()
        
        if queue:
            result.append(queue[0])
        else:
            result.append('#')
    
    return ''.join(result)

def main():
    t = int(input())
    results = []
    
    for _ in range(t):
        stream = input().strip()
        result = find_first_unique_gift(stream)
        results.append(result)
    
    for result in results:
        print(result)

# Run the main function
main()
