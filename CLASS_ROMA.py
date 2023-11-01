class Arco:
    def __init__(self, n1, n2, w1, w2):
        self.n1 = n1
        self.n2 = n2
        self.w1 = w1
        self.w2 = w2

class Grafo:
    def __init__(self):
        self.arcs = []
        self.set_nodes = []
        self.set_spots = []

    def add_arc(self, arco):
        self.arcs.append(arco)

    def translate_node(self, nd):
        self.nd = int(nd)
        if self.nd != self.get_node_max():
            print(self.set_spots[nd], end=' -> ')
        else:
            print(self.set_spots[nd])

    def read_file(self, file_name):
        fhandle = open(file_name, 'r')
        for line in fhandle:
            line = line.strip()
            n = line.split()
            # blanks=r"\s+"
            if len(line) == 0:
                break
            elif not line.startswith('#'):
                # line=re.sub(blanks,'',line)
                n1 = int(n[0])
                n2 = int(n[1])
                w1 = int(n[2])
                w2 = int(n[3])
                self.add_arc(Arco(n1, n2, w1, w2))
            elif line.startswith('# Node'):
                colon = line.find(':')
                node = int(line[colon - 1])  # key
                self.set_nodes.append(node)
                spot = line[colon + 1:]  # value
                self.set_spots.append(spot)
        fhandle.close()

    def get_node_min(self):
        min = 1000
        for i in self.arcs:
            if i.n1 < min:
                min = i.n1
            if i.n2 < min:
                min = i.n2
        return min

    def get_node_max(self):
        max = 0
        for i in self.arcs:
            if i.n1 > max:
                max = i.n1
            if i.n2 > max:
                max = i.n2
        return max

    def get_incident_arcs(self, n):
        list_arcs = []
        for i in self.arcs:
            if i.n1 == n:
                list_arcs.append(i)
        return list_arcs

    def out_graph(self):
        # print('### ROAD TRIP TO ROMA ###')
        for n in range(self.get_node_min(), self.get_node_max() + 1):
            print('*** NODE:', n)
            for i in self.get_incident_arcs(n):
                print(i.n1, i.n2, '-->', i.w1, 'min,', i.w2, '€')
        return ('')



# g=Grafo()

# g.read_file('Road.txt')

# print(g.set_nodes)
# print(g.set_spots)
# g.translate_node(2)

# g.out_graph()
