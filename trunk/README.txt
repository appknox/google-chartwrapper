################################################################################
#  GChartWrapper - v0.9
#  Copyright (C) 2009  Justin Quick <justquick@gmail.com>
#
#  This program is free software. See attached LICENSE.txt for more info
################################################################################

GChartWrapper - Google Chart API Wrapper

The wrapper can render the URL of the Google chart based on your parameters.
With the chart you can render an HTML img tag to insert into webpages on the fly, 
show it directly in a webbrowser, or save the chart PNG to disk.

################################################################################

Changelog:
-- 0.9 --
Switched to New BSD License


-- 0.8 --
Reverse functionality
	>>> G = GChart.fromurl('http://chart.apis.google.com/chart?ch...')
	<GChartWrapper.GChart instance at...>
Chaining fixes
Restuctured Axes functions
Centralized and added unittests
Enhanced unicode support
Demos pages w/ source code

-- 0.7 --
Full py3k compliance
Color name lookup from the css names: http://www.w3schools.com/css/css_colornames.asp
	>>> G = Pie3D(range(1,5))
	>>> G.color('green')
New charts Note,Text,Pin,Bubble
Updated Django templatetags to allow context inclusion and new charts
Added some more templating examples

-- 0.6 --
The wrapper now supports chaining
	The old way:
	>>> G = Pie3D(range(1,5))
	>>> G.label('A','B','C','D')
	>>> G.color('00dd00')
	>>> print G
The new way with chaining
	>>> print Pie3D(range(1,5)).label('A','B','C','D').color('00dd00')
New chart PieC for concentric pie charts

################################################################################


Doc TOC:
    1.1 General
        1.2 Constructing
        1.3 Rendering and Viewing
    2.1 Django extension
        2.2 Static data
        2.3 Dynamic data
	3.1 Other Templating Langs
    4.1 Test framework
    5.1 API documentation

1.1 General 

Customizable charts can be generated using the Google Chart API available
at http://code.google.com/apis/chart/. The GChart Wrapper allows Pythonic access
to the parameters of constructing the charts and displaying the URLs generated.

1.2 Constructing 

class GChart(Dict):
    """Main chart class

    Chart type must be valid for cht parameter
    Dataset can be any python iterable and be multi dimensional
    Kwargs will be put into chart API params if valid"""
    def __init__(self, ctype=None, dataset=[], **kwargs):

The chart takes any iterable python data type (now including numpy arrays)
and does the encoding for you

    # Datasets 
    >>> dataset = (1, 2, 3)
    # Also 2 dimensional
    >>> dataset = [[3,4], [5,6], [7,8]]

Initialize the chart with a valid type (see API reference) and dataset

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


1.3 Rendering and Viewing 

The wrapper has many useful ways to take the URL of your chart and output it 
into different formats like...

    # As the chart URL itself using __str__
    >>> str(G)
    'http://chart.apis.google.com/chart?...'


    # As an HTML <img> tag, kw arguments can be valid tag attributes
    >>> G.img(height=500,id="chart")
    '<img alt="" title="" src="http://chart.apis.google.com/chart?..." id="chart" height="500" >'


    # Save chart to a file as PNG image, returns filename
    >>> G.save('my-cool-chart')
    'my-cool-chart.png'

    # Now fetch the PngImageFile using the PIL module for manipulation
    >>> G.image()
    <PngImagePlugin.PngImageFile instance at 0xb795ee4c>

    # Now that you have the image instance, the world is your oyster
    # Try saving image as JPEG,GIF,etc.
    >>> G.image().save('my-cool-chart.jpg','JPEG')

    # Show URL directly in default web browser
    >>> G.show()



2.1 Django Extension 

Newer versions of the wrapper contain templatetags for generating charts in
Django templates. This allows for dynamic insertion of data for viewing on any
web application. Install the module first using `python setup.py install` then 
place 'GChartWrapper.charts' in your INSTALLED_APPS and then you are ready to go.
Just include the '{% load charts %}' tag in your templates before making charts.
In the templating folder there is a folder called djangoproj which is an example
Django project to get you started.

2.2 Static data

Then try out some static data in your templates

{% chart Line GurMrabsClgubaolGvzCrgrefOrnhgvshyvforggregunahtyl  %}
    {% title 'The Zen of Python' 00cc00 36 %}
    {% color 00cc00 %}
{% endchart %} 
Or try a bubble
{% bubble icon_text_big snack bb $2.99 ffbb00 black as img %}

2.3 Dynamic data

The module supports dynamic insertion of any variable within the context like so

# View code
def example(request):
    return render_to_response('example.html',{'dataset':range(50)})
    
# example.html template code    
{% chart Line dataset  %}
    {% color 00cc00 %}
{% endchart %} 

Look to example.html in the djangoproj for more detailed examples

3.1 Other Templating Languages

Other examples of using the chartwrapper in templating languages
Currently under development

	Cheetah - done
	Mako - done
	Jinja2 - working, gonna b rough
	Genshi?
	Airspeed?
	More to come...

4.1 Test framework

The module also comes with a test framework with sample charts available in
GChartWrapper/testing.py. The tests are executed through GChartWrapper/tests.py

Usage

    $ python tests.py [<mode>]

Where mode is one of the following:

    unit - Runs unit test cases for all charts to see if checksums match
    save - Saves images of all charts in 'tests' folder
    demo - Creates html demo pages (needs pygments)
    url - Prints urls of all charts [default]

5.1 API Documentation 

The Epydoc API information is generated in HTML format and available in the 
docs folder under index.html