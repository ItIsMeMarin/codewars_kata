def shortest_routes(n, routes):
    list_of_cities = range(0, n)
    source = 0
    graph = {}

    for i in range(len(routes)):
        graph[(routes[i][0], routes[i][1])] = routes[i][2]

    print(graph)


    path_lengths = {v: float('inf') for v in list_of_cities}
    path_lengths[0] = 0

    adjacent_graph = {v: {} for v in list_of_cities}

    

    for (u, v), w_uv in graph.items():
        adjacent_graph[u][v] = w_uv


    temporary_city = [v for v in list_of_cities]
    while len(temporary_city) > 0:
        upper_boudns = {v: path_lengths[v] for v in temporary_city}
        u = min(upper_boudns, key= upper_boudns.get)

        temporary_city.remove(u)
        
        for v, w_uv in adjacent_graph[u].items():
            path_lengths[v] = min(path_lengths[v], path_lengths[u] + w_uv)


    return [(k, v) for k,v in path_lengths.items()][1:]










print(shortest_routes(6, [(2, 3, 32), (1, 2, 23), (0, 4, 12), (0, 1, 20), (5, 1, 2)]))