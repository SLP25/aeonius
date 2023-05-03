import itertools

class GraphVizId():
    newid = itertools.count()
    def __init__(self):
        pass
    
    @staticmethod
    def getId():
        return str(next(GraphVizId.newid))