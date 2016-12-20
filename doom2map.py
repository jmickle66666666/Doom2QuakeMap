import omg, sys

class VertexList:
    def __init__(self,sector_id):
        self.sector_id = sector_id
        self.vertexes = []

    def add_vertex(self,x,y):
        self.vertexes.append((x,y))

if __name__ == '__main__':
    if len(sys.argv) != 2: print 'wrong number of arguments, expected 1'
    else:
        wad = omg.WAD(sys.argv[1])

# for each sector in map

# trace the sectors to create new vertex list objects, with references to sector id

# split concave vertex lists into convex vertex lists

# create brushes

# save to map