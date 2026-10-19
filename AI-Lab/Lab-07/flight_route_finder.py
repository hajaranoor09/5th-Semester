flights = {
    "Islamabad": [("Lahore", 40), ("Karachi", 90)],
    "Lahore": [("Karachi", 50), ("Peshawar", 30)],
    "Karachi": [("Quetta", 60)],
    "Peshawar": [("Quetta", 70)],
    "Quetta": []
}

def ucs(graph, start, goal):
    queue = [(0, [start])]

    while queue:
        queue.sort()
        cost, path = queue.pop(0)

        city = path[-1]

        print("Checking:", path, "Cost:", cost)

        if city == goal:
            return path, cost

        for next_city, price in graph[city]:
            if next_city not in path:
                new_path = path + [next_city]
                new_cost = cost + price
                queue.append((new_cost, new_path))

    return None, None


route, cost = ucs(flights, "Islamabad", "Quetta")

print("\nCheapest route:", route)
print("Total ticket cost:", cost)