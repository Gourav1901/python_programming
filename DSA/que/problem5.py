def find_starting_point():
    t = int(input())
    
    energy_drinks = []
    distances = []
    
    for _ in range(t):
        energy, distance = map(int, input().split())
        energy_drinks.append(energy)
        distances.append(distance)
    
    total_energy = sum(energy_drinks)
    total_distance = sum(distances)
    
    if total_energy < total_distance:
        print("No starting points")
        return
    
    start_index = 0
    current_energy = 0
    
    for i in range(t):
        current_energy += energy_drinks[i] - distances[i]
        if current_energy < 0:
            start_index = i + 1
            current_energy = 0
    
    print(start_index)

# Run the function
find_starting_point()
