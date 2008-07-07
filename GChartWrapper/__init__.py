################################################################################
#  GChartWrapper - v0.4
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

See tests.py for unit test and other examples
"""
# Import the important stuff like the basic GChart class
from GChart import GChart

# Now a whole mess of convenience classes
# *for those of us who dont speak API*
class Meter(GChart):
    def __init__(self, dataset, **kwargs):
        # we can do this to other charts with preferred settings
        kwargs['encoding'] = 'text'
        GChart.__init__(self, 'gom', dataset, **kwargs)
        
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

class QRCode(GChart):
    def __init__(self, dataset=None, **kwargs):
        GChart.__init__(self, 'qr', dataset, **kwargs)    
