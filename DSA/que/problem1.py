def queue_operations():
    t = int(input())
    queue = []
    front_index = 0

    for _ in range(t):
        operation = input().strip()
        if operation.startswith('E'):
            _, value = operation.split()
            queue.append(int(value))
        elif operation == 'D':
            if front_index < len(queue):
                print(queue[front_index])
                front_index += 1
            else:
                print('Empty')
        
        # Reset the queue if all elements are dequeued
        if front_index >= len(queue):
            queue = []
            front_index = 0

# Run the function
queue_operations()