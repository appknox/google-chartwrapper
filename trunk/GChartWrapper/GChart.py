# -*- coding: utf-8 -*-
################################################################################
#  GChartWrapper - v0.7
#  Copyright (C) 2008  Justin Quick <justquick@gmail.com>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License version 3 as published
#  by the Free Software Foundation.
#
#  Thanks to anyone who does anything for this project.
#  If you have even the smallest revision, please email me at above address.
################################################################################
"""
GChartWrapper - Google Chart API Wrapper

The wrapper can render the URL of the Google chart based on your parameters.
With the chart you can render an HTML img tag to insert into webpages on the fly,
show it directly in a webbrowser, or save the chart PNG to disk. New versions
can generate PIL PngImage instances.

Example

    >>> G = GChart('lc',['simpleisbetterthancomplexcomplexisbetterthancomplicated'])
    >>> G.title('The Zen of Python','00cc00',36)
    >>> G.color('00cc00')
    >>> G
    '''http://chart.apis.google.com/chart?
        chd=s:simpleisbetterthancomplexcomplexisbetterthancomplicated
        &chco=00cc00
        &chts=00cc00,36
        &chs=300x150
        &cht=lc
        &chtt=The+Zen+of+Python'''
    >>> G.image() # PIL instance
    <PngImagePlugin.PngImageFile instance at 0xb79fe2ac>
    >>> G.show() # Webbrowser open
    True
    >>> G.save('tmp.png') # Save to disk
    'tmp.png'

See tests.py for unit test and other examples
"""
__all__ = ['Sparkline', 'Map', 'HorizontalBarStack', 'VerticalBarStack', 'QRCode',
     'Line', 'GChart', 'HorizontalBarGroup', 'Scatter', 'Pie3D', 'Pie', 'Meter',
     'Radar', 'VerticalBarGroup', 'LineXY', 'Venn', 'PieC','Pin','Text','Note','Bubble']
__version__ = 0.7
from GChartWrapper.constants import *
from GChartWrapper.constants import _print
from GChartWrapper.encoding import Encoder
from webbrowser import open as webopen
from copy import copy

try:
    from sha import new as new_sha
except ImportError:
    from hashlib import sha1
    def new_sha(astr):
        return sha1(bytes(astr,'utf-8'))

def lookup_color(color):
    color = color.lower()
    if color in COLOR_MAP:
        return COLOR_MAP[color]
    return color

def color_args(args, *indexes):
    args = list(args)
    for i in indexes:
        args[i] = lookup_color(args[i])
    return args

class Dict(object):
    """
    Abstract class for all dictionary operations
    """
    def __init__(self, *args, **kwargs):
        self.data = dict(*args, **kwargs)
    def __repr__(self): return '<GChartWrapper.%s>'%self.__class__.__name__
    def __cmp__(self, dict): return cmp(self.data, dict)
    def __len__(self): return len(self.data)
    def __getitem__(self, key):
        if key in self.data:
            return self.data[key]
        raise KeyError(key)
    def __setitem__(self, key, item): self.data[key] = item
    def __delitem__(self, key): del self.data[key]
    def __contains__(self, key): return key in self.data
    def __iter__(self):
        for key in self.keys(): yield key
    def keys(self): return self.data.keys()
    def items(self): return self.data.items()
    def values(self): return self.data.values()
    def has_key(self, key): return self.data.has_key(key)
    def update(self, **kwargs):
        if kwargs: self.data.update(kwargs)
    def pop(self, key, *args): return self.data.pop(key, *args)
    def popitem(self): return self.data.popitem()

class Axes(Dict):
    """
    Axes attribute dictionary storage

    Use this class via GChart(...).axes
    Methods are taken one at a time, like so:
    
    >>> G.axes.type('xy')
    >>> G.axes.label('Label1') # X Axis
    >>> G.axes.label('Label2') # Y Axis
    """
    def __init__(self, parent):
        self.parent = parent
        self.labels,self.positions,self.ranges,self.styles = [],[],[],[]
        self.data = {}
        Dict.__init__(self)

    def type(self, atype):
        """
        Define the type of axes you wish to use
        atype must be one of x,t,y,r
        call the rest of the axes functions in the corresponding order that you declare the type
        APIPARAM: chxt
        """
        for char in atype:
            assert char in 'xtyr', 'Invalid axes type: %s'%char
        if not ',' in atype:
            atype = ','.join(atype)
        self.data['chxt'] = atype
        return self.parent
     
    def label(self, *args):
        """
        Label each axes one at a time
        args are of the form <label 1>,...,<label n>
        APIPARAM: chxl
        """
        label = '|'.join(map(str,args))
        id = len(self.labels)
        self.labels.append( str('%d:|%s'%(id,label)).replace('None','') )
        return self.parent
        
    def position(self, *args):
        """
        Set the label position of each axis, one at a time
        args are of the form <label position 1>,...,<label position n>
        APIPARAM: chxp
        """
        position = ','.join(map(str,args))
        id = len(self.positions)
        self.positions.append( str('%d,%s'%(id,position)).replace('None','') )
        return self.parent
        
    def range(self, *args):
        """
        Set the range of each axis, one at a time
        args are of the form <start of range>,<end of range>
        APIPARAM: chxr
        """
        self.ranges.append('%d,%s,%s'%(len(self.ranges), args[0], args[1]))
        return self.parent
        
    def style(self, *args):
        """
        Add style to your axis, one at a time
        args are of the form <axis color>,<font size>,<alignment>,<drawing control>,<tick mark color>
        APIPARAM: chxs
        """
        id = str(len(self.styles))
        args = color_args(args, 0)
        self.styles.append(','.join([id]+list(map(str,args))))
        return self.parent

    def render(self):
        """Render the axes data into the dict data"""
        if self.labels:
            self.data['chxl'] = '|'.join(self.labels)
        if self.styles:
            self.data['chxs'] = '|'.join(self.styles)
        if self.positions:
            self.data['chxp'] = '|'.join(self.positions)
        if self.ranges:
            self.data['chxr'] = '|'.join(self.ranges)
        return self.data    
        
class GChart(Dict):
    """Main chart class

    Chart type must be valid for cht parameter
    Dataset can be any python iterable and be multi dimensional
    Kwargs will be put into chart API params if valid"""
    def __init__(self, ctype=None, dataset=[], **kwargs):
        self.lines,self.fills,self.markers,self.scales = [],[],[],[]
        self._geo,self._ld = '',''
        self._dataset = dataset
        self.data = {}
        Dict.__init__(self)
        if ctype:
            self.check_type(ctype)
            self.data['cht'] = ctype
        self._encoding = kwargs.pop('encoding', None)
        self._scale = kwargs.pop('scale', None)
        self.apiurl = kwargs.pop('apiurl', APIURL)
        for k,v in kwargs.items():
            assert k in APIPARAMS, 'Invalid chart parameter: %s'%k
            self.data[k] = v
        self.axes = Axes(self)
        
    ###################
    # Callables
    ###################
    def map(self, geo, country_codes):
        """
        Creates a map of the defined geography with the given country/state codes
        Geography choices are africa, asia, europe, middle_east, south_america, and world
        ISO country codes can be found at http://code.google.com/apis/chart/isocodes.html
        US state codes can be found at http://code.google.com/apis/chart/statecodes.html
        APIPARAMS: chtm & chld
        """
        assert geo in GEO, 'Geograpic area %s not recognized'%geo
        self._geo = geo
        self._ld = country_codes
        return self
        
    def level_data(self, *args):
        """
        Just used in QRCode for the moment
        args are error_correction,margin_size
        APIPARAM: chld
        """
        assert args[0].lower() in 'lmqh', 'Unknown EC level %s'%level
        self.data['chld'] = '%s|%s'%args
        return self
        
    def bar(self, *args):
        """
        For bar charts, specify bar thickness and spacing with the args
        args are <bar width>,<space between bars>,<space between groups>
        bar width can be relative or absolute, see the official doc
        APIPARAM: chbh
        """
        self.data['chbh'] = ','.join(map(str,args))
        return self
        
    def encoding(self, encoding):
        """
        Specifies the encoding to be used for the Encoder
        Must be one of 'simple','text', or 'extended'
        """
        self._encoding = encoding
        return self
        
    def output_encoding(self, encoding):
        """
        Output encoding to use for QRCode encoding
        Must be one of 'Shift_JIS','UTF-8', or 'ISO-8859-1'
        APIPARAM: choe
        """
        assert encoding in ('Shift_JIS','UTF-8','ISO-8859-1'),\
            'Unknown encoding %s'%encoding
        self.data['choe'] = encoding
        return self
        
    def scale(self, *args):
        """
        Scales the data down to the given size
        args must be in the form of <min>,<max>
        will only work with text encoding
        APIPARAM: chds
        """
        self._scale =  ['%s,%s'%args]
        return self
        
    def dataset(self, data):
        """
        Update the chart's dataset, can be two dimensional or contain string data
        """
        self._dataset = data
        return self
        
    def marker(self, *args):
        """
        Defines markers one at a time for your graph
        args are of the form <marker type>,<color>,<data set index>,<data point>,<size>,<priority>
        see the official developers doc for the complete spec
        APIPARAM: chm
        """
        if len(args[0]) == 1:
            assert args[0] in MARKERS, 'Invalid marker type: %s'%args[0]
        assert len(args) <= 6, 'Incorrect arguments %s'%str(args)
        args = color_args(args, 1)
        self.markers.append(','.join(map(str,args)) )
        return self
        
    def line(self, *args):
        """
        Called one at a time for each dataset
        args are of the form <data set n line thickness>,<length of line segment>,<length of blank segment>
        APIPARAM: chls
        """
        self.lines.append(','.join(['%.1f'%x for x in map(float,args)]))
        return self
        
    def fill(self, *args):
        """
        Apply a solid fill to your chart
        args are of the form <fill type>,<fill style>,...
        fill type must be one of c,bg,a
        fill style must be one of s,lg,ls
        the rest of the args refer to the particular style, refer to the official doc
        APIPARAM: chf
        """
        assert args[0] in ('c','bg','a'), 'Fill type must be bg/c/a not %s'%args[0]
        assert args[1] in ('s','lg','ls'), 'Fill style must be s/lg/ls not %s'%args[1]
        if len(args) == 3:
            args = color_args(args, 2)
        else:
            args = color_args(args, 3,5)
        self.fills.append(','.join(map(str,args)))
        return self
        
    def grid(self, *args):
        """
        Apply a grid to your chart
        args are of the form <x axis step size>,<y axis step size>,<length of line segment>,<length of blank segment>
        APIPARAM: chg
        """
        grids =  map(str,map(float,args))
        self.data['chg'] = ','.join(grids).replace('None','')
        return self
        
    def color(self, *args):
        """
        Add a color for each dataset
        args are of the form <color 1>,...<color n>
        APIPARAM: chco
        """
        args = color_args(args, *range(len(args)))
        self.data['chco'] = ','.join(args)
        return self
        
    def type(self, type):
        """
        Set the chart type, either Google API type or regular name
        APIPARAM: cht
        """
        self.data['cht'] = self.check_type(str(type))
        return self
        
    def label(self, *args):
        """
        Add a simple label to your chart
        call each time for each dataset
        APIPARAM: chl
        """
        if self.data['cht'] == 'qr':
            self.data['chl'] = ''.join(map(str,args))
        else:
            self.data['chl'] = '|'.join(map(str,args))
        return self
        
    def legend(self, *args):
        """
        Add a legend to your chart
        call each time for each dataset
        APIPARAM: chdl
        """
        self.data['chdl'] = '|'.join(args)
        return self
        
    def legend_pos(self, pos):
        """
        Define a position for your legend to occupy
        pos must be one of b,t,r,l
        APIPARAM: chdlp
        """
        assert pos in 'btrl', 'Unknown legend position: %s'%pos
        self.data['chdlp'] = str(pos)
        return self
        
    def title(self, title, *args):
        """
        Add a title to your chart
        args are optional style params of the form <color>,<font size>
        APIPARAMS: chtt,chts
        """
        self.data['chtt'] = title
        if args:
            args = color_args(args, 0)
            self.data['chts'] = ','.join(map(str,args))
        return self

    def size(self,*args):
        """
        Set the size of the chart, args are width,height and can be tuple
        APIPARAM: chs
        """
        if len(args) == 2:
            x,y = map(int,args)
        else:
            x,y = map(int,args[0])
        self.check_size(x,y)
        self.data['chs'] = '%dx%d'%(x,y)
        return self

    def margin(self, *args):
        """
        Set the margins of your chart
        args are of the form <left margin>,<right margin>,<top margin>,<bottom margin>[,<legend width>,<legend height>]
        the legend args are optional
        APIPARAM: chma
        """
        if len(args) == 4:
            self.data['chma'] = ','.join(map(str,args))
        elif len(args) == 6:
            self.data['chma'] = ','.join(map(str,args[:4]))+'|'+','.join(map(str,args[4:]))
        else:
            raise ValueError('Margin arguments must be either 4 or 6 items')
        return self
    
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
            assert len(size) == 2, 'Invalid size, must be in the format WxH'
            self.check_size(*map(int,size))
        assert 'cht' in self.data, 'No chart type defined, use type method'
        self.data['cht'] = self.check_type(self.data['cht'])
        if ('any' in dir(self._dataset) and self._dataset.any()) or self._dataset:
            self.data['chd'] = encoder.encode(self._dataset)
        elif not 'choe' in self.data:
            assert 'chd' in self.data, 'You must have a dataset, or use chd'
        if self._scale:
            assert self.data['chd'].startswith('t:'), 'You must use text encoding with chds'
            self.data['chds'] = ','.join(self._scale)
        if self._geo and self._ld:
            self.data['chtm'] = self._geo
            self.data['chld'] = self._ld
        if self.lines:
            self.data['chls'] = '|'.join(self.lines)
        if self.markers:
            self.data['chm'] = '|'.join(self.markers)
        if self.fills:
            self.data['chf'] = '|'.join(self.fills)

    ###################
    # Checks
    ###################
    def check_size(self,x,y):
        """
        Make sure the chart size fits the standards
        """
        assert x <= 1000, 'Width larger than 1,000'
        assert y <= 1000, 'Height larger than 1,000'
        assert x*y <= 300000, 'Resolution larger than 300,000'
        
    def check_type(self, type):
        """Check to see if the type is either in TYPES or fits type name

        Returns proper type
        """
        if type in TYPES:
            return type
        tdict = dict(zip(TYPES,TYPES))
        tdict['line'] = 'lc'
        tdict['bar'] = 'bvs'
        tdict['pie'] = 'p'
        tdict['venn'] = 'v'
        tdict['scater'] = 's'
        assert type in tdict, 'Invalid chart type: %s'%type
        return tdict[type]

    #####################
    # Convience Functions
    #####################     
    def getname(self):
        """
        Gets the name of the chart, if it exists
        """
        return self.data.get('chtt','')

    def getdata(self):
        """
        Returns the decoded dataset from chd param
        """
        #XXX: Why again? not even sure decode works well
        return Encoder(self._encoding).decode(self.data['chd'])

    def _parts(self):
        return ('%s=%s'%(k,QUOTE(v)) for k,v in self.data.items() if v)

    def __str__(self):
        """
        Returns the rendered URL of the chart
        """
        self.render()        
        return self.apiurl + '&'.join(self._parts()).replace(' ','+')

    def url(self):
        """
        Uses str, AND enforces replacing spaces w/ pluses
        """        
        return self.__str__()

    def show(self, *args, **kwargs):
        """
        Shows the chart URL in a webbrowser

        Other arguments passed to webbrowser.open
        """
        return webopen(str(self), *args, **kwargs)

    def save(self, fname=None):
        """
        Download the chart from the URL into a filename as a PNG

        The filename defaults to the chart title (chtt) if any
        """
        if not fname:
            fname = self.getname()
        assert fname != None, 'You must specify a filename to save to'
        if not fname.endswith('.png'):
            fname += '.png'
        try:
            urlretrieve(str(self), fname)
        except:
            raise IOError('Problem saving chart to file: %s'%fname)
        return fname

    def img(self, **kwargs):
        """
        Returns an XHTML <img/> tag of the chart

        kwargs can be other img tag attributes, which are strictly enforced
        uses strict escaping on the url, necessary for proper XHTML
        """       
        safe = 'src="%s" ' % self.url().replace('&','&amp;').replace('<', '&lt;')\
            .replace('>', '&gt;').replace('"', '&quot;').replace( "'", '&#39;')
        for item in kwargs.items():
            if not item[0] in IMGATTRS:
                raise AttributeError('Invalid img tag attribute: %s'%item[0])
            safe += '%s="%s" '%item
        return '<img %s/>'%safe

    def urlopen(self):
        """
        Grabs readable PNG file pointer
        """
        return urlopen(self.__str__())

    def image(self):
        """
        Returns a PngImageFile instance of the chart

        You must have PIL installed for this to work
        """
        try:
            try:
                import Image
            except ImportError:
                from PIL import Image
        except ImportError:
            raise ImportError('You must install PIL to fetch image objects')
        try:
            from cStringIO import StringIO
        except ImportError:
            from StringIO import StringIO
        return Image.open(StringIO(self.urlopen().read()))

    def write(self, fp):
        """
        Writes out PNG image data in chunks to file pointer fp

        fp must support w or wb
        """
        urlfp = self.urlopen().fp
        while 1:
            try:
                fp.write(urlfp.next())
            except StopIteration:
                return

    def checksum(self):
        """
        Returns the SHA1 hexdigest of the chart URL param parts

        good for unittesting...
        """
        self.render()
        items = [(k,self.data[k]) for k in sorted(self.data)]
        return new_sha(str(items)).hexdigest()

# Now a whole mess of convenience classes
# *for those of us who dont speak API*
class Meter(GChart):
    def __init__(self, dataset, **kwargs):
        # we can do this to other charts with preferred settings
        kwargs['encoding'] = 'text'
        GChart.__init__(self, 'gom', dataset, **kwargs)

class QRCode(GChart):
    def __init__(self, content='', **kwargs):
        kwargs['choe'] = 'UTF-8'
        if type(content) in (type(''),):
            kwargs['chl'] = QUOTE(content)
        else:
            kwargs['chl'] = QUOTE(content[0])
        GChart.__init__(self, 'qr', None, **kwargs)

class Line(GChart):
    def __init__(self, dataset, **kwargs):
        GChart.__init__(self, 'lc', dataset, **kwargs)

class LineXY(GChart):
    def __init__(self, dataset, **kwargs):
        GChart.__init__(self, 'lxy', dataset, **kwargs)

class HorizontalBarStack(GChart):
    def __init__(self, dataset, **kwargs):
        GChart.__init__(self, 'bhs', dataset, **kwargs)

class VerticalBarStack(GChart):
    def __init__(self, dataset, **kwargs):
        GChart.__init__(self, 'bvs', dataset, **kwargs)

class HorizontalBarGroup(GChart):
    def __init__(self, dataset, **kwargs):
        GChart.__init__(self, 'bhg', dataset, **kwargs)

class VerticalBarGroup(GChart):
    def __init__(self, dataset, **kwargs):
        GChart.__init__(self, 'bvg', dataset, **kwargs)

class Pie(GChart):
    def __init__(self, dataset, **kwargs):
        GChart.__init__(self, 'p', dataset, **kwargs)

class Pie3D(GChart):
    def __init__(self, dataset, **kwargs):
        GChart.__init__(self, 'p3', dataset, **kwargs)

class Venn(GChart):
    def __init__(self, dataset, **kwargs):
        GChart.__init__(self, 'v', dataset, **kwargs)

class Scatter(GChart):
    def __init__(self, dataset, **kwargs):
        GChart.__init__(self, 's', dataset, **kwargs)

class Sparkline(GChart):
    def __init__(self, dataset, **kwargs):
        GChart.__init__(self, 'ls', dataset, **kwargs)

class Radar(GChart):
    def __init__(self, dataset, **kwargs):
        GChart.__init__(self, 'r', dataset, **kwargs)

class Map(GChart):
    def __init__(self, dataset, **kwargs):
        GChart.__init__(self, 't', dataset, **kwargs)

class PieC(GChart):
    def __init__(self, dataset, **kwargs):
        GChart.__init__(self, 'pc', dataset, **kwargs)

########################################
# Now for something completely different
########################################
class Text(GChart):
    def render(self): pass
    def __init__(self, *args):
        GChart.__init__(self)
        self.data['chst'] = 'd_text_outline'
        args = list(map(str, color_args(args, 0, 3)))
        assert args[2] in 'lrh', 'Invalid text alignment'
        assert args[4] in '_b', 'Invalid font style'
        self.data['chld'] = '|'.join(args)\
            .replace('\r\n','|').replace('\r','|').replace('\n','|').replace(' ','+')

class Pin(GChart):
    def render(self): pass
    def __init__(self, type, *args):
        GChart.__init__(self)
        assert type in PIN_TYPES, 'Invalid type'
        if type == "pin_letter":
            args = color_args(args, 1,2)
        elif type == 'pin_icon':
            args = color_args(args, 1)
            assert args[0] in PIN_ICONS, 'Invalid icon name'
        elif type == 'xpin_letter':
            args = color_args(args, 2,3,4)
            assert args[0] in PIN_SHAPES, 'Invalid pin shape'
            if not args[0].startswith('pin_'):
                args[0] = 'pin_%s'%args[0] 
        elif type == 'xpin_icon':
            args = color_args(args, 2,3)
            assert args[0] in PIN_SHAPES, 'Invalid pin shape'
            if not args[0].startswith('pin_'):
                args[0] = 'pin_%s'%args[0] 
            assert args[1] in PIN_ICONS, 'Invalid icon name'
        elif type == 'spin':
            args = color_args(args, 2)
        self.data['chst'] = 'd_map_%s'%type
        self.data['chld'] = '|'.join(map(str, args))\
            .replace('\r\n','|').replace('\r','|').replace('\n','|').replace(' ','+')
    def shadow(self):
        image = copy(self)
        chsts = self.data['chst'].split('_')
        chsts[-1] = 'shadow'
        image.data['chst'] = '_'.join(chsts)
        return image

class Note(GChart):
    def render(self): pass
    def __init__(self, *args):
        GChart.__init__(self)
        assert args[0] in NOTE_TYPES,'Invalid note type'
        assert args[1] in NOTE_IMAGES,'Invalid note image'
        if args[0].find('note')>-1:
            self.data['chst'] =  'd_f%s'%args[0]
            args = color_args(args, 3)
        else:
            self.data['chst'] = 'd_%s'%args[0]
            assert args[2] in NOTE_WEATHERS,'Invalid weather'
        args = args[1:]
        self.data['chld'] = '|'.join(map(str, args))\
            .replace('\r\n','|').replace('\r','|').replace('\n','|').replace(' ','+')

class Bubble(GChart):
    def render(self): pass
    def __init__(self, type, *args):
        GChart.__init__(self)
        assert type in BUBBLE_TYPES, 'Invalid type'
        if type in ('icon_text_small','icon_text_big'):
            args = color_args(args, 3,4)
            assert args[0] in BUBBLE_SICONS,'Invalid icon type'
        elif type == 'icon_texts_big':
            args = color_args(args, 2,3)
            assert args[0] in BUBBLE_LICONS,'Invalid icon type'
        elif type == 'texts_big':
            args = color_args(args, 1,2)
        self.data['chst'] = 'd_bubble_%s'%type
        self.data['chld'] = '|'.join(map(str, args))\
            .replace('\r\n','|').replace('\r','|').replace('\n','|').replace(' ','+')
    def shadow(self):
        image = copy(self)
        image.data['chst'] = '%s_shadow'%self.data['chst']
        return image
          
if __name__=='__main__':
    from tests import test
    test()
