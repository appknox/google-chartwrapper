from UserDict import UserDict
from urllib import urlretrieve,quote,unquote
from webbrowser import open as webopen
from constants import *
from encoding import Encoder

class Axes(UserDict):
    """
    Axes attribute dictionary storage
    
    Use this class via GChart(...).axes
    """
    def __init__(self):
        self.labels = []
        self.positions = []
        self.ranges = []
        self.styles = []    
        UserDict.__init__(self)
    def render(self):
        if self.labels:            
            self.data['chxl'] = '|'.join(self.labels)   
        if self.styles:
            self.data['chxs'] = '|'.join(self.styles)              
        if self.positions:
            self.data['chxp'] = '|'.join(self.positions)
        if self.ranges:
            self.data['chxr'] = '|'.join(self.ranges)
        return self.data
    def label(self, *args):
        label = '|'.join(map(str,args))
        id = len(self.labels)
        self.labels.append( str('%d:|%s'%(id,label)).replace('None','') )
    def position(self, *args):
        position = ','.join(map(str,args))
        id = len(self.positions)
        self.positions.append( str('%d,%s'%(id,position)).replace('None','') )
    def range(self, *args):
        self.ranges.append('%d,%s,%s'%(len(self.ranges), args[0], args[1]))
    def type(self, atype):
        if not ',' in atype:
            atype = ','.join(atype)
        self.data['chxt'] = atype
    def style(self, *args):  
        id = str(len(self.styles))
        self.styles.append(','.join([id]+map(str,args)))
        
class GChart(UserDict):
    """Main chart class
    
    Chart type must be valid for cht parameter
    Dataset can be any python iterable and be multi dimensional
    Kwargs will be put into chart API params if valid"""
    def __init__(self, ctype=None, dataset=[], **kwargs):
        self.lines = []
        self.fills = []
        self.bar_heights = ''
        self._geo = ''
        self._ld = ''
        self.markers = []
        self._dataset = dataset
        self.scales = []
        self.axes = Axes()        
        UserDict.__init__(self)
        if ctype:
            self.check_type(ctype)
            self.data['cht'] = ctype          
        self._encoding = None
        self._scale = None
        if 'encoding' in kwargs:
            self._encoding = kwargs['encoding']
            del kwargs['encoding']            
        if 'scale' in kwargs:
            self._scale = kwargs['scale']
            del kwargs['scale']          
        self.apiurl = 'http://chart.apis.google.com/chart?'                
        if 'apiurl' in kwargs:
            self.apiurl = kwargs['apiurl']
            del kwargs['apiurl']                     
        for k,v in kwargs.items():
            assert(k in APIPARAMS), 'Invalid chart parameter: %s'%k                
            self.data[k] = v

    def map(self, geo, country_codes):
        assert(geo in GEO), 'Geograpic area %s not recognized'%geo
        self._geo = geo
        self._cc = country_codes
    
    def level_data(self, level, margin):
        assert(level.lower() in 'lmqh'), 'Unknown EC level %s'%level
        self.data['chld'] = '%s|%d'%(level,margin)

    def bar_height(self, *heights):
        self.bar_heights = ','.join(map(str,heights))
       
    def encoding(self, encoding): 
        self._encoding = encoding

    def output_encoding(self, encoding):
        assert(encoding in ('Shift_JIS','UTF-8','ISO-8859-1')),\
            'Unknown encoding %s'%encoding
        self.data['choe'] = encoding

    def scale(self, *scale):
        self.scales.append('%s,%s'%scale)

    def dataset(self, data):
        self._dataset = data                   
       
    def marker(self, *args):
        assert(args[0] in MARKERS), 'Invalid marker type: %s'%args[0]
        assert(len(args) <= 6), 'Incorrect arguments %s'%str(args)
        self.markers.append(','.join(map(str,args)) )
        
    def line(self, *args):
        self.lines.append(','.join(['%.1f'%x for x in map(float,args)]))
        
    def fill(self, *args):
        assert(args[0] in ('c','bg','a')), 'Fill must be bg/c/a not %s'%args[0]
        assert(args[1] in ('s','lg','ls')), 'Fill type must be s/lg/ls not %s'%args[1]
        self.fills.append(','.join(map(str,args)))
        
    def grid(self, *args):
        grids =  map(str,map(float,args))
        self.data['chg'] = ','.join(grids).replace('None','')          
        
    def bar(self, *args):
        bars = ['%.1f'%b for b in map(float,args)]        
        self.data['chbh'] = ','.join(bars).replace('None','')

    def color(self, *args): 
        self.data['chco'] = ','.join(args)  

    def type(self, type):        
        self.data['cht'] = str(type)
        
    def label(self, *args):
        self.data['chl'] = '|'.join(args)   
        
    def legend(self, *args):
        self.data['chdl'] = '|'.join(args)
    
    def legend_pos(self, arg):
        self.data['chdlp'] = str(arg)
       
    def title(self, title, *args): 
        self.data['chtt'] = title        
        if args:
            self.data['chts'] = ','.join(map(str,args))
            
    def render(self):
        """
        Renders the chart context and axes into the dict data
        """
        self.data.update(self.axes.render())     
        encoder = Encoder(self._encoding)  
        if not 'chs' in self.data:
            self.data['chs'] = '300x150'
        else:            
            size = self.data['chs'].split('x')
            assert(len(size) == 2), 'Invalid size, must be in the format WxH'
            self.check_size(*map(int,size))
        assert('cht' in self.data), 'No chart type defined, use type method'
        self.data['cht'] = self.check_type(self.data['cht'])   
        if self._dataset:
            self.data['chd'] = encoder.encode(self._dataset)             
          # except: raise IndexError, 'Data encoding went screwy'                
        elif not 'choe' in self.data:
            assert('chd' in self.data), 'You must have a dataset, or use chd'            
        if self.scales:
            assert(self.data['chd'].startswith('t:')), 'You must use text encoding with chds'
            self.data['chds'] = ','.join(self.scales)
        if self.bar_heights:
            self.data['chbh'] = self.bar_heights
        if self._geo and self._ld:
            self.data['chtm'] = self._geo
            self.data['chld'] = self._ld
        if self.lines:
            self.data['chls'] = '|'.join(self.lines)            
        if self.markers:
            self.data['chm'] = '|'.join(self.markers)           
        if self.fills:
            self.data['chf'] = '|'.join(self.fills)
        if 'choe' in self.data:
            self.data['chl'] = quote(self.data['chl'])
                          
    def check_size(self,x,y):
        """
        Make sure the chart size fits the standards
        """
        assert(x <= 10**3), 'Width larger than 1000'         
        assert(y <= 10**3), 'Height larger than 1000'        
        assert(x*y <= 3*(10**5)), 'Resolution larger than 300000' 
          
    def check_type(self, type):
        """Check to see if the type is either in TYPES or fits type name
        
        Returns proper type
        """
        tdict = dict(zip(TYPES,TYPES))
        tdict['line'] = 'lc'
        tdict['bar'] = 'bvs'
        tdict['pie'] = 'p'
        tdict['venn'] = 'v'
        tdict['scater'] = 's'
        assert(type in tdict), 'Invalid chart type: %s'%type  
        return tdict[type]
             
    def size(self,*args):
        """
        Set the size of the chart, args are width,height and can be tuple
        """
        if len(args) == 2:
            x,y = map(int,args)
        else:
            x,y = map(int,args[0])
        self.check_size(x,y)
        self.data['chs'] = '%dx%d'%(x,y)  

    def getname(self):
        """
        Gets the name of the chart, if it exists
        """
        if 'chtt' in self.data:
            return self.data['chtt']
    
    def getdata(self):
        return Encoder().decode(self.data['chd'])        
        
    def __repr__(self):  return self.__str__()
    def __str__(self):
        """
        Returns the rendered URL of the chart
        """
        self.render()
        params = '&'.join(['%s=%s'%x for x in self.data.items() if x[1]])
        return self.apiurl + params.replace(' ','+')
    def url(self): return str(self)           
    def show(self):
        """
        Shows the chart URL in a webbrowser
        """
        webopen(str(self))
    
    def save(self, fname=None):
        """
        Download the chart from the URL into a filename as a PNG
        
        The filename defaults to the chart title (chtt) if any
        """
        if not fname:
            fname = self.getname()               
        assert(fname != None), 'You must specify a filename to save to'
        if not fname.endswith('.png'):
            fname += '.png'
        try:
            urlretrieve(str(self), fname)           
        except IOError, e:
            raise IOError, 'Problem saving chart to file: %s'%e   
        return fname                     

    def img(self, **kwargs): 
        """
        Returns an HTML <img> tag of the chart
        
        kwargs can be other img tag attributes, which are strictly enforced
        """
        attrs = ''
        for item in kwargs.items():
            if not item[0] in IMGATTRS:
                raise AttributeError, 'Invalid img tag attribute: %s'%item[0]
            attrs += '%s="%s" '%item
        return '<img src="%s" %s>'%(str(self),attrs)



if __name__=='__main__':
    from tests import test
    test()
