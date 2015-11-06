# Whats New #

## v0.8 ##

Reverse functionality
```
>>> G = GChart.fromurl('http://chart.apis.google.com/chart?ch...')
<GChartWrapper.GChart instance at...>
```

Restuctured Axes functions. You must declare indexes, axes is callable
```
# Old Way
>>> G.axes.type('xy')
>>> G.axes.label('Mar','Apr','May')
>>> G.axes.label(None,'50+Kb')

# New Way
>>> G.axes('xy')
>>> G.axes.label(0, 'Mar','Apr','May')
>>> G.axes.label(1, None,'50+Kb')
```

Centralized and added unittests.

Enhanced unicode support.

Demos pages w/ source code available at [chartograpy.net](http://www.chartography.net/media/google-chartwrapper-demo/).

Chaining fixes

## v0.7 ##
Full [PY3K](http://www.python.org/dev/peps/pep-3000/) compliance

Finally up at the [PYPI](http://pypi.python.org/pypi?name=GChartWrapper&:action=display)

Color name lookup from the css names: http://www.w3schools.com/css/css_colornames.asp
```
>>> G = Pie3D(range(1,5))
>>> G.color('green')
```
![http://chart.apis.google.com/chart?chs=300x150&chco=008000&cht=p3&chd=t:1.0,2.0,3.0,4.0&.png](http://chart.apis.google.com/chart?chs=300x150&chco=008000&cht=p3&chd=t:1.0,2.0,3.0,4.0&.png)

New charts Note,Text,Pin,Bubble. See ChartExamples for usage

Updated Django templatetags to allow context inclusion and new charts. See DjangoExtension for usage

Added some more templating examples. See DjangoExtension and TemplatingLanguages for usage

## v0.6 ##
The wrapper now supports chaining commands together. Here is an example of the old syntax
```
>>> G = Pie3D(range(1,5))
>>> G.label('A','B','C','D')
>>> G.color('00dd00')
>>> print G
```
Now you can combine the commands into one line
```
>>> print Pie3D(range(1,5)).label('A','B','C','D').color('00dd00')
```
This saves lots of time when using them in templates. You can now use the wrapper for multiple TemplatingLanguages