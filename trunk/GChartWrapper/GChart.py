################################################################################
#  GChartWrapper - v0.5
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
     'Radar', 'VerticalBarGroup', 'LineXY', 'Venn']
__version__ = 0.5

from UserDict import UserDict
import urllib
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
        self.lines,self.fills,self.markers,self.scales = [],[],[],[]
        self.bar_heights,self._geo,self._ld = '','',''
        self._dataset = dataset
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
        self.apiurl = APIURL
        if 'apiurl' in kwargs:
            self.apiurl = kwargs['apiurl']
            del kwargs['apiurl']
        for k,v in kwargs.items():
            assert(k in APIPARAMS), 'Invalid chart parameter: %s'%k
            self.data[k] = v

    def map(self, geo, country_codes):
        assert(geo in GEO), 'Geograpic area %s not recognized'%geo
        self._geo = geo
        self._ld = country_codes

    def level_data(self, *args):
        assert(args[0].lower() in 'lmqh'), 'Unknown EC level %s'%level
        self.data['chld'] = '%s|%s'%args

    def bar_height(self, *heights):
        self.bar_heights = ','.join(map(str,heights))

    def encoding(self, encoding):
        self._encoding = encoding

    def output_encoding(self, encoding):
        assert(encoding in ('Shift_JIS','UTF-8','ISO-8859-1')),\
            'Unknown encoding %s'%encoding
        self.data['choe'] = encoding

    def scale(self, *scale):
        self._scale =  ['%s,%s'%scale]

    def dataset(self, data):
        self._dataset = data

    def marker(self, *args):
        if not args[0].startswith('t'):
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
        if self.data['cht'] == 'qr':
            self.data['chl'] = ''.join(map(urllib.quote,args))
        else:
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
        elif not 'choe' in self.data:
            assert('chd' in self.data), 'You must have a dataset, or use chd'
        if self._scale:
            assert(self.data['chd'].startswith('t:')), 'You must use text encoding with chds'
            self.data['chds'] = ','.join(self._scale)
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


    def check_size(self,x,y):
        """
        Make sure the chart size fits the standards
        """
        assert(x <= 10**3), 'Width larger than 1,000'
        assert(y <= 10**3), 'Height larger than 1,000'
        assert(x*y <= 3*(10**5)), 'Resolution larger than 300,000'

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
        return self.data.get('chtt','')

    def getdata(self):
        """
        Returns the decoded dataset from chd param
        """
        #XXX: Why again? not even sure decode works well
        return Encoder(self._encoding).decode(self.data['chd'])

    def _parts(self):
        return ('%s=%s'%i for i in self.data.items() if i[1])

    def __str__(self):
        """
        Returns the rendered URL of the chart
        """
        self.render()        
        return (self.apiurl + '&'.join(self._parts())).replace(' ','+')

    def url(self):
        """
        Uses str, AND enforces replacing spaces w/ pluses
        """        
        return str(self)

    def show(self, *args, **kwargs):
        """
        Shows the chart URL in a webbrowser

        Other arguments passed to webbrowser.open
        """
        import webbrowser
        return webbrowser.open(str(self), *args, **kwargs)

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
            urllib.urlretrieve(str(self), fname)
        except IOError, e:
            raise IOError, 'Problem saving chart to file: %s'%e
        return fname

    def img(self, **kwargs):
        """
        Returns an XHTML <img/> tag of the chart

        kwargs can be other img tag attributes, which are strictly enforced
        uses strict escaping on the url, necessary for proper XHTML
        """       
        safe = 'src="%s" ' % self.url().replace('&','&amp').replace('<', '&lt;')\
            .replace('>', '&gt;').replace('"', '&quot;').replace( "'", '&#39;')
        for item in kwargs.items():
            if not item[0] in IMGATTRS:
                raise AttributeError, 'Invalid img tag attribute: %s'%item[0]
            safe += '%s="%s" '%item
        return '<img %s/>'%safe

    def urlopen(self):
        """
        Grabs readable PNG file pointer
        """
        return urllib.urlopen(str(self))

    def image(self):
        """
        Returns a PngImageFile instance of the chart

        You must have PIL installed for this to work
        """
        try:
            import Image
        except ImportError:
            raise ImportError, 'You must install PIL to fetch image objects'
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
        Returns the SHA1 hexdigest of the chart PNG image content

        good for unittesting...
        """
        from sha import new
        return new(self.urlopen().read()).hexdigest()

# Now a whole mess of convenience classes
# *for those of us who dont speak API*
class Meter(GChart):
    def __init__(self, dataset, **kwargs):
        # we can do this to other charts with preferred settings
        kwargs['encoding'] = 'text'
        GChart.__init__(self, 'gom', dataset, **kwargs)

# like these guys...
class QRCode(GChart):
    def __init__(self, content='', **kwargs):
        kwargs['choe'] = 'UTF-8'
        kwargs['chl'] = urllib.quote(content)
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

if __name__=='__main__':
    from tests import test
    test()
