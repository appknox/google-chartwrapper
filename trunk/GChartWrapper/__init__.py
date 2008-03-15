################################################################################
#  Copyright (C) 2008  Justin Quick <justquick@gmail.com>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License version 3 as published 
#  by the Free Software Foundation.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
################################################################################
"""
GChartWrapper - Google Chart API Wrapper

The wrapper can render the URL of the Google chart based on your parameters.
With the chart you can render an HTML img tag to insert into webpages on the fly, 
show it directly in a webbrowser, or save the chart PNG to disk.

Example

    >>> G = GChart('lc',['simpleisbetterthancomplexcomplexisbetterthancomplicated'])
    >>> G.title('The Zen of Python','00cc00',36)
    >>> G.color('00cc00')
    >>> str(G)
    '''http://chart.apis.google.com/chart?
        chd=s:simpleisbetterthancomplexcomplexisbetterthancomplicated
        &chco=00cc00
        &chts=00cc00,36
        &chs=300x150
        &cht=lc
        &chtt=The+Zen+of+Python'''

See testing for unit test and other examples
"""


import sys
from UserDict import UserDict
from urllib import urlretrieve,quote
from webbrowser import open as webopen
from GChartWrapper.constants import *
from GChartWrapper.encoding import Encoder

class Axes(UserDict):
    """Axes attr storage"""
    def __init__(self):
        self.labels = []
        self.styles = []    
        UserDict.__init__(self)
    def render(self):
        if self.labels:            
            self.data['chxl'] = '|'.join(self.labels)   
        if self.styles:
            self.data['chxs'] = '|'.join(self.styles)              
        return self.data
    def label(self, *args):
        label = '|'.join(map(str,args))
        id = len(self.labels)
        self.labels.append( str('%d:|%s'%(id,label)).replace('None','') )
    def position(self, *args):
        self.data['chxp'] = ','.join(map(str,args))
    def range(self, *args):
        self.data['chxr'] = '%d,%d,%d'%args
    def type(self, atype):
        if not ',' in atype:
            atype = ','.join(atype)
        self.data['chxt'] = atype
    def style(self, *args):  
        id = str(len(self.styles))
        self.styles.append(','.join([id]+map(str,args)))
        
class GChart(UserDict):
    """Main chart class
    
    chart type must be valid for cht parameter
    dataset can be any python iterable
    kwargs will be put into chart params if valid"""
    def __init__(self, ctype=None, dataset=[], **kwargs):
        self.lines = []
        self.fills = []
        self.markers = []
        self._dataset = dataset
        self.axes = Axes()        
        UserDict.__init__(self)
        if ctype:
            self.check_type(ctype)
            self.data['cht'] = ctype
        self._scale = None
        if 'scale' in kwargs:
            self._scale = float(kwargs['scale'])
            del kwargs['scale']            
        self._encoding = None
        if 'encoding' in kwargs:
            self._encoding = kwargs['encoding']
            del kwargs['encoding']            

        self.apiurl = 'http://chart.apis.google.com/chart?'                
        if 'apiurl' in kwargs:
            self.apiurl = kwargs['apiurl']
            del kwargs['apiurl']                     
        for k,v in kwargs.items():
            assert(k in APIPARAMS), 'Invalid chart parameter: %s'%k                
            self.data[k] = v
       
    def encoding(self, encoding): 
        self._encoding = encoding

    def scale(self, scale):
        self._scale = float(scale)

    def dataset(self, data):
        self._dataset = data                   
       
    def marker(self, *args):
        assert(args[0] in MARKERS), 'Invalid marker type: %s'%args[0]
        assert(len(args) == 5), 'Incorrect arguments %s'%str(args)
        self.markers.append(','.join(map(str,args)) )
        
    def line(self, *args):
        self.lines.append(','.join(['%.1f'%x for x in map(float,args)]))
        
    def fill(self, *args):
        assert(args[0] in ('c','bg')), 'Fill must be bg/c not %s'%args[0]
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
       
    def title(self, title, *args): 
        self.data['chtt'] = title        
        if args:
            self.data['chts'] = ','.join(map(str,args))
            
    def render(self):
        """Renders the chart context and axes into the dict data"""
        self.data.update(**self.axes.render())     
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
            self.data['chd'] = encoder.encode(self._dataset,scale=self._scale)             
        else: pass
            #assert('chd' in self.data), 'You must have a dataset, or use chd'            
        if self.lines:
            self.data['chls'] = '|'.join(self.lines)            
        if self.markers:
            self.data['chm'] = '|'.join(self.markers)           
        if self.fills:
            self.data['chf'] = '|'.join(self.fills)
       
                          
    def check_size(self,x,y):
        """Make sure the chart size fits the standards"""
        assert(x <= 10**3), 'Width larger than 1000'         
        assert(y <= 10**3), 'Height larger than 1000'        
        assert(x*y <= 3*(10**5)), 'Resolution larger than 300000' 
          
    def check_type(self, type):
        """Check to see if the type is either in TYPES or fits type name
        
        Returns proper type"""
        tdict = dict(zip(TYPES,TYPES))
        tdict['line'] = 'lc'
        tdict['bar'] = 'bvs'
        tdict['pie'] = 'p'
        tdict['venn'] = 'v'
        tdict['scater'] = 's'
        assert(type in tdict), 'Invalid chart type: %s'%type  
        return tdict[type]
             
    def size(self,*args):
        """Set the size of the chart, args are width,height and can be tuple"""
        if len(args) == 2:
            x,y = map(int,args)
        else:
            x,y = map(int,args[0])
        self.check_size(x,y)
        self.data['chs'] = '%dx%d'%(x,y)  

    def getname(self):
        """Gets the name of the chart, if it exists"""
        if 'chtt' in self.data:
            return self.data['chtt']
    
    def getdata(self):
        return Encoder().decode(self.data['chd'])        
        
    def __repr__(self):  self.__str__()
    def __str__(self):
        """Returns the rendered URL of the chart"""
        self.render()
        params = '&'.join(['%s=%s'%x for x in self.data.items() if x[1]])
        return self.apiurl + params.replace(' ','+')
           
    def show(self):
        """Shows the chart URL in a webbrowser"""
        webopen(str(self))
    
    def save(self, fname=None):
        """Download the chart from the URL into a filename as a PNG
        
        The filename defaults to the chart title (chtt) if any"""
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
        """Returns an HTML <img> tag of the chart
        
        kwargs can be other img tag attributes, which are strictly enforced"""
        attrs = ''
        href = str(self)
        title = self.getname()
        for item in kwargs.items():
            if not item[0] in IMGATTRS:
                raise AttributeError, 'Invalid img tag attribute: %s'%item[0]
            attrs += '%s="%s" '%item
        return '<img alt="%s" title="%s" src="%s" %s>'%(title,title,href,attrs)
        
if __name__=='__main__':
    from GChartWrapper.tests import test
    test()
