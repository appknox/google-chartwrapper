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

class Axes(object):
    """Axes attr storage"""
    def __init__(self):
        self._type = ''
        self.labels = []
        self.positions = []
        self.ranges = [] 
        self.styles = []
        self._lid = None
        self._sid = None        
    def render(self):
        data = {}
        if self._type:
            data['chxt'] = ','.join(self._type)
        if self.labels:            
            data['chxl'] = '|'.join(self.labels)   
        if self.positions:                 
            data['chxp'] = '|'.join(self.positions)  
        if self.ranges:
            data['chxp'] = '|'.join(self.ranges)  
        if self.styles:
            data['chxs'] = '|'.join(self.styles)              
        return data
    def label(self, *args):
        assert(self._lid != None), 'Need to call type before labeling'
        self.labels.append('%d:|%s'%(self._lid,'|'.join(map(str,args))))
        self._lid += 1
    def position(self, *args):
        self.positions.append(','.join(map(str,args)))
    def range(self, *args):
        self.ranges.append('%d,%d,%d'%args)
    def type(self, typ):
        self._lid = 0
        self._sid = 0
        self._type = typ.replace(',','')     
    def style(self, *args):  
        assert(self._sid != None), 'Need to call type before labeling'
        self.styles.append(','.join([str(self._sid)]+map(str,args)))
        
class GChart(UserDict):
    """Main chart class
    
    chart type must be valid for cht parameter
    dataset can be any python iterable
    kwargs will be put into chart params if valid"""
    def __init__(self, ctype, dataset, **kwargs):
        self._type = ctype
        self.labels = []
        self._title = ''
        self.title_style = ''
        self.legends = []
        self.colors = []  
        self.bars = []  
        self.lines = []
        self.grids = []
        self.markers = []
        self.dataset = dataset
        UserDict.__init__(self)
        self.encoding = 'simple'
        self.maxValue = None
        if 'encoding' in kwargs:
            self.encoding = kwargs['encoding']
            del kwargs['encoding']
        self.encoder = Encoder(self.encoding)            
        if 'maxValue' in kwargs:
            self.maxValue = kwargs['maxValue']
            del kwargs['maxValue']         
        if 'apiurl' in kwargs:
            self.apiurl = kwargs['apiurl']
            del kwargs['apiurl']                  
        else:
            self.apiurl = 'http://chart.apis.google.com/chart?'                    
        self.axes = Axes()
        self.data.update(cht=ctype)        
        for k,v in kwargs:
            assert(k in APIPARAMS), 'Invalid chart parameter: %s'%k                
            self.data[k] = v
    def marker(self, *args):
        assert(args[0] in MARKERS), 'Invalid marker type: %s'%args[0]
        assert(len(args) == 5), 'Incorrect arguments %s'%str(args)
        self.markers.append(','.join(map(str,args)) )
    def line(self, *args):
        self.lines.append(','.join(['%.1f'%x for x in args]))
    def grid(self, *args):
        self.grids = map(float,args)             
    def bar(self, *args):
        self.bars = map(int,args)                 
    def color(self, *args):
        self.colors = list(args)       
    def type(self, type):
        self._type = type      
    def label(self, *args):
        self.labels = list(args)    
    def legend(self, *args):
        self.legends = list(args)
    def title(self, title, *args): 
        self._title = title
        if args:
            self.title_style = ','.join(map(str,args))
    def render(self):
        """Renders the chart context and axes into the dict data"""
        if not 'chs' in self.data:
            self.size(300,150)
        else:
            self.checkSize(*map(int,self.data['chs'].split('x')))
        assert('cht' in self.data), 'No chart type (cht) in data'
        assert(self.data['cht'] in TYPES), 'Invalid chart type: %s'%self.data['cht']    
        self.data['chd'] = self.encoder.encode(self.dataset, self.maxValue)
        if self.labels:
            self.data['chl'] = '|'.join(self.labels)     
        if self._title:
            self.data['chtt'] = self._title    
        if self.title_style:
            self.data['chts'] = self.title_style
        if self.legends:
            self.data['chdl'] = '|'.join(self.legends)                   
        if self.colors:
            self.data['chco'] = ','.join(self.colors)                
        if self.bars:
            self.data['chbh'] = ','.join(map(str,self.bars))
        if self.lines:
            self.data['chls'] = '|'.join(self.lines) 
        if self.grids:
            self.data['chg'] = ','.join(map(str,self.grids))
        if self.markers:
            self.data['chm'] = '|'.join(self.markers)           
        self.data.update(**self.axes.render())            

    def getData(self):
        """Returns encoded dataset"""
        if 'chd' in self.data:
            return self.data['chd']        
    def checkSize(self,x,y):
        """Make sure the chart size fits the standards"""
        assert(x <= 10**3), 'Width larger than 1000'         
        assert(y <= 10**3), 'Height larger than 1000'        
        assert(x*y <= 3*(10**5)), 'Resolution larger than 300000'         
    def size(self,*args):
        """Set the size of the chart, args are width,height and can be tuple"""
        if len(args) == 2:
            x,y = map(int,args)
        else:
            x,y = map(int,args[0])
        self.checkSize(x,y)
        self.data['chs'] = '%dx%d'%(x,y)  
    def __repr__(self):
        return '<GChart %s %s %s>'%(self._title,self._type,self.dataset)
    def __str__(self):
        """Returns the rendered URL of the chart"""
        self.render()
        params = '&'.join(['%s=%s'%x for x in self.data.items()])
        return self.apiurl + params.replace(' ','+')
           
    def show(self):
        """Shows the chart URL in a webbrowser"""
        webopen(str(self))
    
    def save(self, fname=None):
        """Download the chart from the URL into a filename as a PNG
        
        The filename defaults to the chart title if any"""
        if fname == None:
            if 'chtt' in self.data:
                fname = self.data['chtt']
            elif type(self._title)==type('') and self._title:
                fname = self.data['chtt'] = self._title                
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
        title = self.data.get('chtt','')
        for item in kwargs.items():
            if not item[0] in IMGATTRS:
                raise AttributeError, 'Invalid img tag attribute: %s'%item[0]
            attrs += '%s="%s" '%item
        return '<img alt="%s" title="%s" src="%s" %s>'%(title,title,href,attrs)
