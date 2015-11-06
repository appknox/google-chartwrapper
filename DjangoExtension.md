### Installation ###

Add the following app to your Django INSTALLED\_APPS in your settings.py file like so:

```
...
INSTALLED_APPS = ('GChartWrapper.charts',...)
...
```

Then you can use the templatetag in any of your templates.

### Templatetage Usage ###
**The module contains a template tags extension that functions like this**
```
{% load charts %}

{% chart Line GurMrabsClgubaolGvzCrgrefOrnhgvshyvforggregunahtyl  %}
    {% title 'The Zen of Python' 00cc00 36 %}
    {% color 00cc00 %}
{% endchart %} 
```
**Which creates and img tag to handle this chart**

![http://chart.apis.google.com/chart?chd=s:GurMrabsClgubaolGvzCrgrefOrnhgvshyvforggregunahtyl&chco=00cc00&chts=00cc00,36&chs=300x150&cht=lc&chtt=The+Zen+of+Python&.png](http://chart.apis.google.com/chart?chd=s:GurMrabsClgubaolGvzCrgrefOrnhgvshyvforggregunahtyl&chco=00cc00&chts=00cc00,36&chs=300x150&cht=lc&chtt=The+Zen+of+Python&.png)

_**NEW**_ **You can also put the GChart instance into the template context and use it like so**

```
{% load charts %}

{% chart Line ... as my_nifty_line_chart  %}
    ...
{% endchart %} 

{{ my_nifty_line_chart }} # URL
{{ my_nifty_line_chart.img }} # XHTML <img/> tag
```

**Even more importantly, with some of the new chart types**

```
{% load charts %}

{% pin pin_letter A red black as pin_a %}

{{ pin_a.img }} # Regular image
{{ pin_a.shadow.img }} # Shadow image
```
![http://chart.apis.google.com/chart?chst=d_map_pin_letter&chld=A|FF0000|000000&.png](http://chart.apis.google.com/chart?chst=d_map_pin_letter&chld=A|FF0000|000000&.png)
![http://chart.apis.google.com/chart?chst=d_map_pin_shadow&chld=A|FF0000|000000&.png](http://chart.apis.google.com/chart?chst=d_map_pin_shadow&chld=A|FF0000|000000&.png)

### More Examples ###

The templating folder in the ExtrasDistribution contains a `djangoproj` subfolder which is a standard Django project to test out the functionality of the templatetags. If you execute `python manage.py runserver` then go to http://localhost:8000/ it will render several charts from the ChartExamples. The template can be found [here](http://code.google.com/p/google-chartwrapper/source/browse/trunk/templating/djangoproj/templates/example.html)