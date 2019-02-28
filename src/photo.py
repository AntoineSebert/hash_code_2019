class photo:
    id = 0
    orientation = char()
    tags = set()
    used = False

    def __init__(self, pos, orien, tag):
        id = pos;
        orientation = orien
        tags = tag
