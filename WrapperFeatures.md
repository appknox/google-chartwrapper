## [GoogleCharts](http://code.google.com/apis/chart/) and the GChart Wrapper ##

#### Customizable charts can be generated using the [Google Chart API](http://code.google.com/apis/chart/). The GChart Wrapper allows python access to the parameters of constructing the charts and displaying the URLs generated. ####

### Constructing ###
```
class GChart(UserDict)
    """Main chart class
    
    chart type must be valid for cht parameter
    dataset can be any python iterable
    kwargs will be put into chart params if valid"""
    def __init__(self, ctype, dataset, **kwargs):
```
**The chart takes any iterable python data type and does the encoding for you**
```
# Datasets 
>>> dataset = (1, 2, 3)
# Also 2 dimensional
>>> dataset = [[3,4], [5,6], [7,8]]
```
**Initialize the chart with a valid type (see API reference) and dataset**
```
# 3D Piechart
>>> GChart('p3', dataset)
<GChart  p3 (1, 2, 3)>

# Encoding (simple/text/extended)
>>> G = GChart('p3', dataset, encoding='text')

# maxValue (for encoding values)
>>> G = GChart('p3', dataset, maxValue=100)

# Size
>>> G = GChart('p3', dataset, size=(300,150))

# OR directly pass in API parameters
>>> G = GChart('p3', dataset, chtt='My Cool Chart', chl='A|B|C')
```

### Rendering ###
**As the chart URL itself using str**
```
>>> str(G)
'http://chart.apis.google.com/chart?...'
```

**As an HTML img tag, kw arguments can be valid tag attributes**
```
>>> G.img(height=500,id="chart")
'<img alt="" title="" src="http://chart.apis.google.com/chart?..." id="chart" height="500" >'
```

**Grab a GChart object from an existing Google chart url**
```
>>> G = GChart.fromurl('http://chart.apis.google.com/chart?ch...')
<GChart instance at...>
```
### Viewing ###
**Save chart to file as PNG image, returns filename**
```
>>> G.save('May')
'May.png'
```

**Show URL directly in default web browser**
```
>>> G.show()
```

### Chaining ###

**One of the new features involves chaining the methods together. For example, you could write this**
```
>>> G = Pie3D(range(1,5))
>>> G.label('A','B','C','D')
>>> G.color('00dd00')
>>> print G
```

**But you would probably much rather write this**

```
>>> print Pie3D(range(1,5)).label('A','B','C','D').color('00dd00')
```

**The wrapper returns a copy of itself at each link in the chain, so combining methods onto one line is really easy and saves time and space**