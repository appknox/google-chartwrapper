from distutils.core import setup

CLASSIFIERS = (
    ('Development Status :: 5 - Production/Stable'),
    ('Environment :: Console'),
    ('Environment :: Web Environment'),
    ('Framework :: Django'),
    #('Framework :: Zope3'),
    #('Framework :: Trac'),
    #('Framework :: TurboGears :: Widgets'),
    #('Framework :: Twisted'),
    ('Intended Audience :: Developers'),
    ('Intended Audience :: Science/Research'),
    ('Intended Audience :: System Administrators'),
    ('License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)'),
    ('Natural Language :: English'),
    ('Operating System :: OS Independent'),
    ('Programming Language :: Python'),
    ('Programming Language :: Python :: 2'),
    ('Programming Language :: Python :: 2.3'),
    ('Programming Language :: Python :: 2.4'),
    ('Programming Language :: Python :: 2.5'),
    ('Programming Language :: Python :: 2.6'),
    ('Programming Language :: Python :: 2.7'),
    ('Programming Language :: Python :: 3'),
    ('Programming Language :: Python :: 3.0'),
    ('Programming Language :: Python :: 3.1'),
    ('Topic :: Artistic Software'),
    ('Topic :: Internet :: WWW/HTTP'),
    ('Topic :: Internet :: WWW/HTTP :: Dynamic Content'),
    ('Topic :: Internet :: WWW/HTTP :: Dynamic Content :: CGI Tools/Libraries'),
    ('Topic :: Multimedia'),
    ('Topic :: Multimedia :: Graphics'),
    ('Topic :: Scientific/Engineering :: Visualization'),
    ('Topic :: Software Development :: Libraries :: Python Modules'),
    ('Topic :: Utilities'),
)

setup(
    name='GChartWrapper',
    version='0.8',
    description='Python Google Chart Wrapper',
    long_description="""Python wrapper for the Google Chart API. 
The wrapper can render the URL of the Google chart, based on your parameters, 
or it can render an HTML img tag to insert into webpages on the fly. 
Made for dynamic python websites (Django,Zope,CGI,etc.) that need on the fly 
chart generation without any extra modules. Can also grab the PIL Image 
instance of the chart for manipulation. Works for Python 2 and 3""",
    author="Justin Quick",
    author_email='justquick@gmail.com',
    url='http://code.google.com/p/google-chartwrapper/',
    download_url='http://google-chartwrapper.googlecode.com/files/GChartWrapper-0.8.tar.gz',
    platforms = ["Windows", "Linux", "Solaris", "Mac OS-X", "Unix"],
    classifiers=CLASSIFIERS,
      package_dir={'GChartWrapper': 'GChartWrapper'},
      packages=['GChartWrapper', 'GChartWrapper.charts', 'GChartWrapper.charts.templatetags'],
)