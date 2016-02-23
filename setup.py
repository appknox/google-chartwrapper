from distutils.core import setup

CLASSIFIERS = (
    'Development Status :: 5 - Production/Stable',
    'Environment :: Console',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'Intended Audience :: Science/Research',
    'Intended Audience :: System Administrators',
    ('License :: OSI Approved ::'
        ' GNU Library or Lesser General Public License (LGPL)'),
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.3',
    'Programming Language :: Python :: 2.4',
    'Programming Language :: Python :: 2.5',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.0',
    'Programming Language :: Python :: 3.1',
    'Programming Language :: Python :: 3.5',
    'Topic :: Artistic Software',
    'Topic :: Internet :: WWW/HTTP',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ('Topic :: Internet :: WWW/HTTP :: Dynamic Content ::'
        ' CGI Tools/Libraries'),
    'Topic :: Multimedia',
    'Topic :: Multimedia :: Graphics',
    'Topic :: Scientific/Engineering :: Visualization',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Utilities',
)

setup(
    name='ak-gchartwrapper',
    version='0.9.1',
    description='Python Google Chart Wrapper',
    long_description=open("README.txt").read(),
    author="Justin Quick",
    author_email='justquick@gmail.com',
    url='https://github.com/appknox/google-chartwrapper',
    platforms=["Windows", "Linux", "Solaris", "Mac OS-X", "Unix"],
    classifiers=CLASSIFIERS,
    package_dir={'GChartWrapper': 'GChartWrapper'},
    packages=[
        'GChartWrapper', 'GChartWrapper.charts',
        'GChartWrapper.charts.templatetags'],
)
