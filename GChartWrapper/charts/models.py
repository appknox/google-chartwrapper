from GChartWrapper.constants import *
from GChartWrapper import GChart
from GChartWrapper.encoding import Encoder
from django.db import models
from base64 import b64encode,b64decode


REQ = ('chd','chs','cht')
OPTIONAL = []
PARAMS = []
for n,t in enumerate(APIPARAMS):
    if not t in REQ:
        OPTIONAL.append(t)
    PARAMS.append((n+1,t))        
TTITLES = [(n+1,t) for n,t in enumerate(TTITLES)]    

def DataEval(args,**kwargs):
    args = [x.rstrip().replace('import','') for x in args]+['']
    txt = '\n'.join(args)
    try:
        txt = eval(txt)
    except NameError:
        return 'e:' + ','.join(args)
    print txt,kwargs        
    return Encoder('extended').encode(txt,**kwargs)

def ChartEval(args,**kwargs):
    args = [x.rstrip().replace('import','') for x in args]+['']
    lo = {'GChart':GChart,'chart':None}
    exec '\n'.join(args[:-1]) in {},lo
    return lo['chart']
    
def test():    
    datasets = DataEval("""
    10,30,50
    30,50,60
    60,40,20
    """.splitlines())    

    print ChartEval("""
    G = GChart('bhg', datasets)
    G.color('cc0000', '00aa00', 'ff0000') 
    G.bar(10,5,10) 
    G.show()
    """.splitlines(),datasets=datasets)


class Param(models.Model):
    key = models.CharField(maxlength=255,choices=PARAMS)
    data = models.CharField(maxlength=255)



class Chart(models.Model):
    type = models.IntegerField(choices=TTITLES)
    data = models.TextField()
    width = models.IntegerField()
    height = models.IntegerField()
    for param in OPTIONAL:
        exec '%s = models.CharField(maxlength=255,blank=True,null=True)'%param

    def gettitle(self,type=None):
        if not type:
            type = self.type
        return TTITLES[int(type)-1][1]

    def gettype(self,type=None):
        if not type:
            type = self.type
        return TYPES[int(type)-1]

    def getdata(self,data=None):
        # might require decoding if x:
        if not data:
            data = b64decode(self.data)
        return DataEval(data.splitlines())

    def G(self):
        ctx = {
            'chd':self.getdata(),
            'cht':self.gettype(),
            'chs':'%dx%d'%(self.width,self.height)
        }
        for param in OPTIONAL:
            ctx[param] = getattr(self,param)
        return GChart(**ctx)

    def download(self,fname):
        return self.G().save(fname) 

    def img(self, **kwargs):
        return self.G().img(**kwargs)

    def save(self, G=None):
        if G:      
            for k,v in G.data.items():
                if k in REQ:
                    if k == 'chd':  k = 'data'
                    elif k == 'cht':  k = 'type'
                    elif k == 'chs': continue
                if v: setattr(self,k,v)    
            self.width,self.height = map(int,G.data['chs'].split('x'))
            self.type = list(TYPES).index(G.data['cht']) +1              
            self.data = b64encode(str(G.getdata()))
        models.Model.save(self)
                
    def __str__(self):
        return '%s Chart #%s %s'%(self.gettitle(),self.id,self.data[:20])

    def url(self):
        return str(self.G())

    def get_absolute_url(self):
        return self.url()
        
    class Admin: 
        fields = (
            ('Required information', {'fields':('type','data','width','height')}),
            ('Optional parameters', {'fields':('chbh', 'chtt', 'chdl', 'chco', 'chf', 'chts', 'chl', 'chxt', 'chxl', 'chg', 'chxr', 'chxs', 'chls', 'chm', 'chxp',), 'classes':'collapse'}),
        )       
                        

