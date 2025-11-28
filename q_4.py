class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adjacency_matrix = [[0]* num_vertices for _ in range(num_vertices)]
        self.vertex_labels = [""] * num_vertices

    def set_vertex_label(self, index, label):
        # assign a lable to each vertex index like 0
        self.vertex_labels[index] = label
    
    def add_edge(self, source, target, weight):
        # source to target with given weight
        # only goes one direction
        self.adjacency_matrix[source][target] = weight
    
    def dijkstra(self, start_label):
        #convert the label to its index number
        start_index = self.vertex_labels.index(start_label)

        #minimum cost from star to each vertex
        min_cost = [float("inf")] * self.num_vertices
        min_cost[start_index] = 0

        processed = [False] * self.num_vertices

        for n in range(self.num_vertices):
            
            #select the unprocessed vertes with the smallest known cost
            current_vertex = self.find_smallest_vertex(min_cost, processed)

            if current_vertex is None:
                break

            processed[current_vertex] = True

            #update the cost of neighbours
            self.update_neighbour(current_vertex, min_cost, processed)

        return min_cost
    
    def find_smallest_vertex(self, min_cost, processed):
        #return the index of the smallest cost uprocessed vertex
        smallest_cost = float("inf")
        smallest_vertex = None

        #checks every vertex 
        for v in range(self.num_vertices):
            if not processed[v] and min_cost[v] < smallest_cost:
                smallest_cost = min_cost[v]
                smallest_vertex = v

        return smallest_vertex
    
    def update_neighbour(self, current_vertex, min_cost, processed):
        # updates cost to reach each neighbour
        for neighbour in range(self.num_vertices):
            weight = self.adjacency_matrix[current_vertex][neighbour]

            if weight != 0 and not processed[neighbour]:
                new_cost = min_cost[current_vertex] + weight

                if new_cost < min_cost[neighbour]:
                    min_cost[neighbour] = new_cost

#creates a graph with 7 vertices
g = Graph(7)

#labels for each vertex
g.set_vertex_label(0, 'A')
g.set_vertex_label(1, 'B')
g.set_vertex_label(2, 'C')
g.set_vertex_label(3, 'D')
g.set_vertex_label(4, 'E')
g.set_vertex_label(5, 'F')
g.set_vertex_label(6, 'G')

g.add_edge(3, 0, 4)  # D → A
g.add_edge(3, 4, 2)  # D → E
g.add_edge(0, 2, 3)  # A → C
g.add_edge(0, 4, 4)  # A → E
g.add_edge(4, 2, 4)  # E → C
g.add_edge(4, 6, 5)  # E → G
g.add_edge(2, 5, 5)  # C → F
g.add_edge(1, 2, 2)  # B → C
g.add_edge(1, 5, 2)  # B → F
g.add_edge(6, 5, 5)  # G → F
g.add_edge(0, 1, 1)  # A → B 

# run dijsktra from D
distances = g.dijkstra("D")

for i, cost in enumerate(distances):
    print(f"Cost from D to {g.vertex_labels[i]}: {cost}")



        
        