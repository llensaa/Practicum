import math

def build_graph(roads: list) -> dict:
    """
    Builds a graph from road connections between settlements.
    
    Args:
        roads: List of strings with "city1 city2 distance" format
    
    Returns:
        Dictionary representing adjacency list: {city: [(neighbor, distance), ...]}
    """
    graph = {}
    
    for road in roads:
        city1, city2, distance_str = road.split()
        distance = int(distance_str)
        
        if city1 in graph:
            graph[city1].append((city2, distance))
        else:
            graph[city1] = [(city2, distance)]
        
        if city2 in graph:
            graph[city2].append((city1, distance))
        else:
            graph[city2] = [(city1, distance)]
    
    return graph


def find_shortest_path(start: str, end: str, graph: dict) -> int:
    """
    Finds the shortest distance between two settlements using Dijkstra's algorithm.
    
    Args:
        start: Starting settlement
        end: Destination settlement
        graph: Graph representation of roads
    
    Returns:
        Shortest distance between start and end
    """
    distances = {}
    for city in graph:
        distances[city] = math.inf
    distances[start] = 0
    
    visited = set()
    unvisited = set(graph.keys())
    
    while unvisited:
        current = None
        min_distance = math.inf
        for city in unvisited:
            if distances[city] < min_distance:
                min_distance = distances[city]
                current = city
        
        if current is None or current == end:
            break
        
        unvisited.remove(current)
        visited.add(current)
        
        for neighbor, road_distance in graph[current]:
            if neighbor not in visited:
                new_distance = distances[current] + road_distance
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
    
    return distances[end]


def main():
    """
    Main function to find shortest distance between two settlements.
    """
    n = int(input())
    m = int(input())
    
    roads = []
    for _ in range(m):
        road = input()
        roads.append(road)
    
    graph = build_graph(roads)
    last_line = input()
    start, end = last_line.split()
    result = find_shortest_path(start, end, graph)
    print(result)


if __name__ == '__main__':
    main()