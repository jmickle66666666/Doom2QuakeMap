import omg, sys

class VertexList:

    # vertex lists must contain a list of vertexes, that
    # define a sector, with the vertexes in order

    def __init__(self,sector_id):
        self.sector_id = sector_id
        self.vertexes = []

    def add_vertex(self,x,y):
        self.vertexes.append((x,y))

    def to_string(self):
        output = "{}:".format(self.sector_id)
        for v in self.vertexes:
            output += "({},{})".format(v[0],v[1])
        return output

def get_sidedefs_of_sector(mapedit, sector):
    # input: mapeditor object, sector number
    # output: list of sidedef references

    output = []

    for i in range(len(mapedit.sidedefs)):
        if mapedit.sidedefs[i].sector == sector: output.append(i)

    return output

def flip_line(mapedit, linedef_id):
    # flips a linedef's vx_a and vx_b, and the front/back sides
    temp_vx = mapedit.linedefs[linedef_id].vx_a
    temp_sd = mapedit.linedefs[linedef_id].front

    mapedit.linedefs[linedef_id].vx_a = mapedit.linedefs[linedef_id].vx_b
    mapedit.linedefs[linedef_id].front = mapedit.linedefs[linedef_id].back

    mapedit.linedefs[linedef_id].vx_b = temp_vx
    mapedit.linedefs[linedef_id].back = temp_sd

def get_linedefs_of_sidedefs(mapedit, sidedefs):
    # input: mapeditor object, list of sidedef references
    # output: list of linedef references

    output = []

    for i in range(len(mapedit.linedefs)):
        for j in sidedefs:
            if mapedit.linedefs[i].front == j: output.append(i)
            if mapedit.linedefs[i].back == j: 
                flip_line(mapedit,i)
                output.append(i) # maybe flip these lines?

    return output

def next_linedef(mapedit, linedefs, vertex_id):
    # input: mapeditor object, linedef list to search, vertex to look for
    # output: linedef
    for l in linedefs:
        if mapedit.linedefs[l].vx_a == vertex_id:
            return l
    print "can't find linedef in next_linedef()!"
    return -1

def trace_sector(mapedit, sector):
    # input: mapeditor object, sector number
    # output: array of VertexLists

    # get all sidedefs that have the sector id
    sidedefs = get_sidedefs_of_sector(mapedit,sector)

    # get all lines that contain the sidedefs
    linedefs = get_linedefs_of_sidedefs(mapedit,sidedefs)

    newVXL = VertexList(sector)
    # beginning at the first vertex, find the next line
    first_ld = mapedit.linedefs[linedefs[0]]
    #first_vx = mapedit.vertexes[first_ld.vx_a]
    #newVXL.add_vertex(first_vx.x,first_vx.y)

    cur_vx = first_ld.vx_b
    next_ld = -1
    # for each vertex, add to new vertex list, 
    while next_ld != linedefs[0]:
        next_ld = next_linedef(mapedit, linedefs, cur_vx)
        cur_vx = mapedit.linedefs[next_ld].vx_b
        newVXL.add_vertex(mapedit.vertexes[cur_vx].x,mapedit.vertexes[cur_vx].y)

    # split concave sectorssss

    return [newVXL]

def map_to_vertexlists(wad,mapid):
    # input: wad, map number
    # output: array of VertexLists
    output = []

    # for every sector in the map, create vertex lists
    mapedit = omg.mapedit.MapEditor(wad.maps[mapid.upper()])
    ar = trace_sector(mapedit,0)
    for v in ar:
        print v.to_string()
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