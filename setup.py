from distutils.core import setup
import os

packages, data_files = [], []
root_dir = os.path.dirname(__file__)
if root_dir:
    os.chdir(root_dir)

for dirpath, dirnames, filenames in os.walk('GChartWrapper'):
    for i, dirname in enumerate(dirnames):
        if dirname.startswith('.'): del dirnames[i]
    if '__init__.py' in filenames:
        pkg = dirpath.replace(os.path.sep, '.')
        if os.path.altsep:
            pkg = pkg.replace(os.path.altsep, '.')
        packages.append(pkg)
    elif filenames:
        prefix = dirpath[len('GChartWrapper')+1:]
        for f in filenames:
            data_files.append(os.path.join(prefix, f))
         
setup(
    name='GChartWrapper',
    version='0.5',
    description='Python Google Chart Wrapper',
    long_description="""Python wrapper for the Google Chart API. 
The wrapper can render the URL of the Google chart, based on your parameters, 
or it can render an HTML img tag to insert into webpages on the fly. 
Made for dynamic python websites (Django,Zope,CGI,etc.) that need on the fly 
chart generation without any extra modules. Can also grab the PIL Image 
instance of the chart for manipulation""",
    author="Justin Quick",
    author_email='justquick@gmail.com',
    url='http://code.google.com/p/google-chartwrapper/',
      package_dir={'GChartWrapper': 'GChartWrapper'},
      packages=packages,
      package_data={'GChartWrapper': data_files},
)
