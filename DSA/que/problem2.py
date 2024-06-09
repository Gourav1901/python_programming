def queue_operations():
    # Read initial input
    K, Q = map(int, input().split())
    
    queue = []
    front_index = 0
    
    for _ in range(Q):
        query = input().strip()
        if query.startswith('1'):
            _, X = query.split()
            X = int(X)
            if len(queue) - front_index < K:
                queue.append(X)
                print(X)
            else:
                print(-1)
        elif query == '2':
            if front_index < len(queue):
                print(queue[front_index])
                front_index += 1
            else:
                print(-1)
        
        # Reset the queue if all elements are dequeued
        if front_index >= len(queue):
            queue = []
            front_index = 0

# Run the function
queue_operations()
