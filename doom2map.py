import omg, sys

class VertexList:

    # vertex lists must contain a list of vertexes, that
    # define a sector, with the vertexes in order

    def __init__(self,sector_id):
        self.sector_id = sector_id
        self.vertexes = []

    def add_vertex(self,x,y):
        self.vertexes.append((x,y))

def get_sidedefs_of_sector(mapedit, sector):
    # input: mapeditor object, sector number
    # output: list of sidedef references

    output = []

    for i in range(len(mapedit.sidedefs)):
        if mapedit.sidedefs[i].sector == sector: output.append(i)

    return output

def get_linedefs_of_sidedefs(mapedit, sidedefs):
    # input: mapeditor object, list of sidedef references
    # output: list of linedef references

    output = []

    for i in range(len(mapedit.linedefs)):
        for j in sidedefs:
            if mapedit.linedefs[i].front == j: output.append(i)
            if mapedit.linedefs[i].back == j: output.append(i) # maybe flip these lines?

    return output

def trace_sector(mapedit, sector):
    # input: mapeditor object, sector number
    # output: array of VertexLists

    # get all sidedefs that have the sector id
    sidedefs = get_sidedefs_of_sector(mapedit,sector)

    # get all lines that contain the sidedefs
    linedefs = get_linedefs_of_sidedefs(mapedit,sidedefs)

    # beginning at the first vertex, find the next line
    # for each vertex, add to new vertex list, 
    # then find the next vertex
    # do until next vertex == first vertex

    # repeat until all lines are accounted for

    # split concave sectorssss

    return []

def map_to_vertexlists(wad,mapid):
    # input: wad, map number
    # output: array of VertexLists
    output = []

    # for every sector in the map, create vertex lists
    mapedit = omg.mapedit.MapEditor(wad.maps[mapid.upper()])
    trace_sector(mapedit,0)
    #for i in range(len(mapedit.sectors)):
    #    output += trace_sector(mapedit,i)

    return output

if __name__ == '__main__':
    if len(sys.argv) < 4: 
        print 'wrong number of arguments, expected 3'
        print 'python doom2map.py [wadfile] [mapname] [outfile]'
    else:
        wad = omg.WAD(sys.argv[1])
        mapid = sys.argv[2]
        outfile = sys.argv[3]

        map_to_vertexlists(wad,mapid)

# for each sector in map

# trace the sectors to create new vertex list objects, with references to sector id

# split concave vertex lists into convex vertex lists

# create brushes

# save to map