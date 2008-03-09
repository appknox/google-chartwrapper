from distutils.core import setup

setup(
    name='GChartWrapper',
    version='0.1',
    description='Python Google Chart Wrapper',
    long_description="""Python wrapper for the Google Chart API. 
The wrapper can render the URL of the Google chart, based on your parameters, 
or it can render an HTML img tag to insert into webpages on the fly. 
Made for dynamic python websites (Django,Zope,CGI,etc.) that need on the fly 
chart generation without any extra modules. 
The wrapper SHOULD also work with Eastwood the Google Chart API workalike.""",
    author="Justin Quick",
    author_email='justquick@gmail.com',
    url='http://code.google.com/p/google-chartwrapper/',
    packages=['GChartWrapper'],
)
