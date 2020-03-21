import copy
import math
from collections import defaultdict


class Graph(object):
    def __init__(self, vertices=[]):
        self.vertices = set()
        self.neighbours = defaultdict(set)
        self.dist = {}
        print("vertices " + str(vertices))

    def add_vertex(self, *vertices):
        [self.vertices.add(n) for n in vertices]

    # find out a distance from and to node
    def add_edge(self, frm, to, d=1e309):
        self.add_vertex(frm, to)
        self.neighbours[frm].add(to)
        self.dist[frm, to] = d
        print("adjacency list with weights (distances) " + str(frm) + " " + str(to) + " " + str(d))

    def dijkstra(self, start, maxD=1e309):
        # Set the distance to zero for our initial vertex and to infinity for other vertices.
        # Returns a map of vertices to distance from start and a map of vertices to
        # the neighbouring vertex that is closest to start.
        # total distance from origin
        # total distance is infinity
        total_dist = defaultdict(lambda: 1e309)

        # for start  node total distance is 0
        total_dist[start] = 0
        print("start " + str(start))
        # neighbour that is nearest to the origin
        preceding_vertex = {}
        unvisited = copy.copy(self.vertices)
        print("unvisited " + str(unvisited))

        while unvisited:
            current = unvisited.intersection(total_dist.keys())
            print("current " + str(current))
            # if not current: break
            min_vertex = min(current, key=total_dist.get) # The key argument to min is a callable (e.g. a function) which takes one argument.
            print("min vertex " + str(min_vertex))
            unvisited.remove(min_vertex)
            print("unvisited remove " + str(unvisited))

            for neighbour in self.neighbours[min_vertex]:
                # distance from min_vertex to its neighbour
                distance = total_dist[min_vertex] + self.dist[min_vertex, neighbour]
                print("total_dist[min_vertex] " + str(total_dist[min_vertex]))
                print("distance " + str(distance))
                if total_dist[neighbour] > distance and maxD >= distance:
                    total_dist[neighbour] = distance
                    preceding_vertex[neighbour] = min_vertex
                    print("preceding vertex " + str(preceding_vertex))
        print("total_dist " + str(total_dist) + " preceding vertex " + str(preceding_vertex))
        return total_dist, preceding_vertex

    def find_min_path(self, start, end, maxD=1e309):
        # Returns the minimal distance and path from start to end
        total_distance, preceding_vertex = self.dijkstra(start, maxD)
        dist = total_distance[end]
        print("dist " + str(dist))
        backpath = [end]
        print("backpath " + str(backpath))
        try:
            while end != start:
                end = preceding_vertex[end]
                backpath.append(end)
                print("end " + str(end))
            path = list(reversed(backpath))
            print("path " + str(path))
        except KeyError:
            path = None

        return dist, path

def read_from_file(filename):
    with open(filename) as file:
        lines = file.readlines()

    num_vertices = int(lines[0].split(" ")[0])
    print("Vertices count " + str(num_vertices)) # print '3'  a number of nodes in gamesrv.in
    # create a list of clients from 2nd line in gamesrv.in      [1, 3]
    clients = list(map(int, lines[1].split(" ")))  #The map() function executes a specified function for each item in a iterable. The item is sent to the function as a parameter.
    vertices = []
    for i in range(1, num_vertices + 1):
        vertices.append(i)
    print("VERTICES " + str(vertices))   # VERTICES [1, 2, 3]
    print("CLIENTS " + str(clients))     # CLIENTS [1, 3]
    return vertices, clients, lines[2:]

def write_into_file(the_file, text):
    with open(the_file, 'a') as the_file:
        the_file.write(text)


if __name__ == '__main__':
    vertices, clients, edges = read_from_file("gamesrv.in")
    # nodes, clients, edges [1, 2, 3] [1, 3] ['1 2 50\n', '2 3 1000000000'
    graph = Graph(vertices)

    # filling the graph edges
    for edge in edges:
        values = list(map(int, edge.split(" ")))
        graph.add_edge(values[0], values[1], values[2])
        graph.add_edge(values[1], values[0], values[2])

    min_total_latency = math.inf
    # check if vertex is a client, if not - it will be a start
    for vertex in range(1, len(vertices) + 1):
        if vertex in clients:
            continue

        max_path_latency = graph.find_min_path(vertex, clients[0])[0]
        print("MAX PATH LATENCY " + str(max_path_latency))
        for j in range(1, len(clients)):
            path_latency = graph.find_min_path(vertex, clients[j])[0]
            print("PATH LATENCY " + str(path_latency))
            if max_path_latency < path_latency:
                max_path_latency = path_latency

        if min_total_latency > max_path_latency:
            min_total_latency = max_path_latency
            print("MAX TOTAL PATH LATENCY " + str(max_path_latency))
            print("MIN TOTAL PATH LATENCY " + str(min_total_latency))

    write_into_file("gamesrv.out", str(min_total_latency))
    print(min_total_latency)