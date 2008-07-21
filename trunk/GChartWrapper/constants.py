APIPARAMS = {
    'cht' : "chart-type", 
    'chbh': "horizontal-bar height", 
    'chtt': "title", 
    'chdl': "legend:  <first data set label>|<n data set label>", 
    'chco': "color:  <color1>,..,<colorn> ", 
    'chd': "text-encoding", 
    'chs': "chart-size", 
    'chf': "fill", 
    'chts': "title text-size: chts=<color>,<fontsize> ", 
    'chl': "label chl=<label 1 value>|...<label n value>", 
    'chxt': "axis types chxt=<axis 1>,...<axis n>, choices x,t,y,r ", 
    'chxl': """axis labels  
        chxl=
        <axis index>:|<label 1>|<label n>|
        ...
        <axis index>:|<label 1>|<label n>""", 
    'chg': '''grid 
        chg=
        <x axis step size>,
        <y axis step size>,
        <length of line segment>,
        <length of blank segment>
        ''', 
    'chxr': '''axis range: 
        chxr=
        <axis index>,<start of range>,<end of range>|
        ...
        <axis index>,<start of range>,<end of range>
        ''', 
    'chxs': ''' axis style
        <axis index>,<color>,<font size>,<alignment>|
        ...
        <axis index>,<color>,<font size>,<alignment>        ''', 
    'chls': ''' line-style
        <data set 1 line thickness>,<length of line segment>,<length of blank segment>|
    ...
    <data set n line thickness>,<length of line segment>,<length of blank segment>
            ''', 
        'chm': '''line,sparkline, bar chart line style
    chm=D,<color>,<data set index>,<data point>,<size>,<priority>
    ''', 
        'chxp': '''label positions
    <axis index>,<label 1 position>,<label n position>|
    ...
    <axis index>,<label 1 position>,<label n position>
    ''', 
    'chp': '''zero-line, for bar charts
        <value between 0 and 1 for dataset 1>,
    <value between 0 and 1 for dataset n>
        ''', 
    'chds': '''data-scaling, for text encoding ''', 
    'chdlp': '''legend position''',     
    'choe': '''output encoding ''',     
    'chtm': '''map-type (africa,usa, etc.) ''', 
 'chld': '''level data: countries to be colored, EC level in QR codes ''',
}

MARKERS = ('a', 'c', 'd', 'o', 's', 'v', 'V', 'h', 'x', 'r', 'R', 'b', 'B', 'D')

TYPES = {'qr':'QR codes','bvs': 'Horizontal bar group', 'p3': 'Venn', 'lc': 'Line', 'bhg': 'Vertical bar group', 't': 'Meter', 'p': '3D Pie', 's': 'Radar', 'r': 'Map', 'bvg': 'Pie', 'lxy': 'Horizontal bar stack', 'v': 'Scatter', 'bhs': 'Vertical bar stack', 'gom': 'Sparkline', 'ls': 'Line XY'}

IMGATTRS = ('title','alt','align','border','height','width','ismap','longdesc',
'usemap','id','class','style','lang','xml:lang','onclick','ondblclick','onmousedown',
'onmouseup','onmouseover','onmousemove','onmouseout','onkeypress','onkeydown','onkeyup')

GEO = ('africa','asia','europe','middle_east','south_america','usa','world')

TTAGSATTRS = ('label','title','color','line','grid','bar','marker','fill','legend','axes',
'encoding','scale','size','type','dataset','img','map','bar_height','legend_pos','output_encoding','level_data')

APIURL = 'http://chart.apis.google.com/chart?' 
