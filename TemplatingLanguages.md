## [Django](http://docs.djangoproject.com/en/dev/topics/templates/) ##

The wrapper comes with a Django templatetag for easy insertion of charts into your Django templates. Here is an example from the ChartExamples

```
{% load charts %}
{% chart  Line fohmnytenefohmnytene  encoding=simple  %}
    {% size 200 100  %}
    {% axes type xy  %}
    {% axes label April May June  %}
    {% axes label None  50+Kb  %}
{% endchart %}
```

For more information see the DjangoExtension page.

## [Cheetah](http://www.cheetahtemplate.org/) ##

It is very easy to use with Cheetah since it uses native Python import statements. Here is an example from the ChartExamples

```
#from GChartWrapper import Line
#set G = $Line($data)
$G.axes.type('xy')
$G.axes.label('Mar','Apr','May')
$G.axes.label(None,'50+Kb')
$G.color('ff0000')
$G.line(6,5,2)
$G.img()
```

With the new wrapper you can now run this all on **one** line

```
#from GChartWrapper import Line
$Line($data).axes.type('xy').axes.label('Mar','Apr','May').axes.label(None,'50+Kb').color('ff0000').line(6,5,2).img()
```

## [Mako](http://www.makotemplates.org/) ##

To make this work, a separate method had to be added which is a more generic way to construct the charts. Here is an example of usage in mako:

```
<%namespace name="gcw" module="GChartWrapper"/>

${
    gcw.chart('Line',data)\
        .axes.type('xy')\
        .axes.label('Mar','Apr','May')\
        .axes.label(None,'50+Kb')\
        .color('red')\
        .line(6,5,2)\
        .img()
}
```

The generic `chart` method in the module takes its first argument as the name of the chart class you wish to use (ie Line,Pie3D,Meter,etc.). The rest of the arguments and kw arguments are passed into that class

## [Jinja2](http://jinja.pocoo.org/2/) ##

Under development.

## [Genshi](http://genshi.edgewall.org/) ##

Coming soon.

## [Airspeed](http://dev.sanityinc.com/airspeed/) ##

Coming soon.