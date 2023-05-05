import itertools
from graphviz import nohtml

class GraphVizId():
    newid = itertools.count()
    def __init__(self):
        pass
    
    @staticmethod
    def getId():
        return str(next(GraphVizId.newid))
    
    @staticmethod
    def createNode(graph,label:str="",**kwargs):
        id = GraphVizId.getId()
        graph.node(id,label,kwargs) 
        return id
    
    @staticmethod
    def createUnpackNode(graph,next):
        id = GraphVizId.getId()
        graph.node(id,"**")
        graph.edge(id,next) 
        return id
    
    @staticmethod
    def content(graph,nextList,tail=False,type="List"):
        id = GraphVizId.getId()
        s=f"<i>{type}|"
        for p in range(len(nextList)):
            s+=f"<{p}>|,|"
        if not tail:
            s=s[:-3]
        else:
            s=s[:-1]
        graph.node(id,nohtml(s),shape="record")
        for p,i in enumerate(nextList):
            graph.edge(id+f":{p}",i)
        return id+":i"
    
    @staticmethod
    def pairToGraph(graph,e1,e2,l1,l2):
        entry=GraphVizId.createNode(graph,nohtml(f"<key>{l1}|<value>{l2}"))
        graph.edge(entry+f":key",e1)
        graph.edge(entry+f":value",e2)
        return entry
    
    @staticmethod
    def dictToGraph(graph,key,value):
        entry=GraphVizId.createNode(graph,nohtml("<key>KEY|<value>VALUE"))
        graph.edge(entry+":key",key)
        graph.edge(entry+":value",value)
        return entry
    
    @staticmethod
    def function(graph,function,args):
        entry=GraphVizId.createNode(graph,nohtml("<func>FUNCTION|<args>ARGS"))
        graph.edge(entry+":func",function)
        for i in args:
            graph.edge(entry+":args",i)
        return entry
    
    @staticmethod
    def multicondmatch(graph,expression,match):
        entry=GraphVizId.createNode(graph,nohtml("<expression>Expression|<match>Match"))
        graph.edge(entry+":expression",expression)
        graph.edge(entry+":match",match)
        return entry
        
        
    
    @staticmethod
    def encapsulate(graph,next,initial='[',end=']'):
        id = GraphVizId.getId()
        s=f"{initial}|<0>|{end}"
        graph.node(id,nohtml(s),shape="record")
        if next is not None:
            graph.edge(id+f":0",next)
        return id
        
        
    
        