from django.template import Library,Node
from GChartWrapper import GChart
from django.template import resolve_variable
register = Library()

class AttrNode(Node):
    def __init__(self, args):
        self.args = map(str,args)
    def render(self,context):
        return self.args
def attribute(parser, token):
    return AttrNode(token.split_contents())
register.tag('label', attribute)
register.tag('title', attribute)
register.tag('color', attribute)
register.tag('line', attribute)
register.tag('grid', attribute)
register.tag('bar', attribute)
register.tag('marker', attribute)
register.tag('fill', attribute)
register.tag('legend', attribute)
register.tag('axes', attribute)
register.tag('encoding', attribute)
register.tag('scale', attribute)
register.tag('size', attribute)
register.tag('type', attribute)
register.tag('dataset', attribute)
register.tag('alt', attribute)


class ChartNode(Node):
    def __init__(self, tokens, nodelist):
        self.type = None
        self.tokens = []
        if tokens and len(tokens)>1:
            self.type = tokens[1]   
            self.tokens = tokens[2:]
        self.nodelist = nodelist
    def render(self, context): 
        args = []
        for t in self.tokens:
            try:
                args.append(resolve_variable(t,context))
            except:        
                try:
                    args.append(float(t))
                except:
                    args.append(str(t))   
        if len(args) == 1 and type(args[0]) in map(type,[[],()]):
            args = args[0]                 
        chart = GChart(self.type,args)
        altxt = ''
        for n in self.nodelist:
            rend = n.render(context)
            if type(rend) == type([]):
                if rend[0] == 'axes':
                    func = eval('chart.axes.%s'%rend[1])
                    func(*rend[2:])  
                if rend[0] == 'alt':
                    altxt = rend[1]                                      
                elif rend[0] == 'axes':
                    func = getattr(getattr(chart, rend[0]), rend[1])
                    func(*rend[2:])
                else:
                    func = getattr(chart, rend[0])
                    func(*rend[1:])
        return chart.img(alt=altxt)

def make_chart(parser, token):
    nodelist = parser.parse(('endchart',))
    parser.delete_first_token()
    tokens = token.contents.split()
    return ChartNode(tokens,nodelist)

register.tag('chart', make_chart)
