def manage_party():
    Q = int(input())
    
    queue = []
    stack = []
    front_index = 0
    
    results = []
    
    for _ in range(Q):
        query = input().strip().split()
        type_query = int(query[0])
        
        if type_query == 1:
            # Enqueue operation
            X = int(query[1])
            queue.append(X)
        
        elif type_query == 2:
            # Stack push operation
            X = int(query[1])
            stack.append(X)
        
        elif type_query == 3:
            # Output front of the queue
            if front_index < len(queue):
                results.append(queue[front_index])
            else:
                results.append(-1)
        
        elif type_query == 4:
            # Output top of the stack
            if stack:
                results.append(stack[-1])
            else:
                results.append(-1)
        
        elif type_query == 5:
            # Move front of queue to stack
            if front_index < len(queue):
                stack.append(queue[front_index])
                front_index += 1
            else:
                results.append(-1)
        
        # Reset queue if all elements have been dequeued
        if front_index >= len(queue):
            queue = []
            front_index = 0
    
    # Print results for queries 3 and 4
    for result in results:
        print(result)

# Run the function
manage_party()
