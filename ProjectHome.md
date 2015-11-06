## Python Google Chart Wrapper ##

#### Easily create Google charts using Python syntax and data objects. ####

Python wrapper for the [Google Chart API](http://code.google.com/apis/chart/). The wrapper can render the URL of the Google chart, based on your parameters, or it can render an HTML img tag to insert into webpages on the fly. Made for dynamic python websites (Django,Zope,CGI,etc.) that need on the fly chart generation without any extra modules. Works for Python 2 and 3
```
>>> from GChartWrapper import Pie
>>> Pie([5,10]).title('Hello Pie').color('red','lime').label('hello', 'world')
```

**Generates an object that can render/save the chart in many ways. The most useful is display on a website**

![http://chart.apis.google.com/chart?chco=ff0000,00ff00&chd=s:f9&chs=300x150&cht=p3&chl=hello|world&chtt=Hello%20Pie&.png](http://chart.apis.google.com/chart?chco=ff0000,00ff00&chd=s:f9&chs=300x150&cht=p3&chl=hello|world&chtt=Hello%20Pie&.png)

**Simply install the package from [PyPI](http://pypi.python.org/pypi/GChartWrapper/)**
```
$ sudo easy_install -U GChartWrapper
```


### [Demos and Examples](http://justquick.github.com/google-chartwrapper-demos/) ###
### [API](http://justquick.github.com/google-chartwrapper-apidoc/) ###
### WhatsNew ###
### WhoUsesTheWrapper ###
### WrapperFeatures ###
### PilExtension ###
### TemplatingLanguages ###


Any problems/questions/comments send to justquick@gmail.com