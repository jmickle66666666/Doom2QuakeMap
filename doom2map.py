import omg

class VertexList:
    def __init__(self,sector_id):
        self.sector_id = sector_id
        self.vertexes = []

    def add_vertex(self,x,y):
        self.vertexes.append((x,y))


# for each sector in map

# trace the sectors to create new vertex list objects, with references to sector id

# split concave vertex lists into convex vertex lists

# create brushes

# save to map