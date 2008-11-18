#!/usr/bin/env python
"""
GChartWrapper - Google Chart API Wrapper

Unit test platform

    Run this application from the command line for various testing modes.

    Usage

        $ python tests.py [<mode>]

    Where mode is one of the following:

        unit - Runs unit test cases for all charts to see if checksums match
        save - Saves images of all charts in 'tests' folder
        wiki - Creates GoogleCode compatable wiki markup of test src and img
        img - Prints html img tags for all charts
        url - Prints urls of all charts
        show - Opens all charts in tabs in a web browser
        tags - Prints Django template src of all charts
"""
from testing import TestClass
import os
import sys
from inspect import getsource

def test():
    arg = sys.argv[-1].lower()
    if not arg in ('save','wiki','img','url','show','tags','unit'):
        arg = 'url'

    Test = TestClass()

    if arg == 'save':
        if not os.path.isdir('tests'):
            os.mkdir('tests')
        for test in Test.all:
            getattr(Test,test)().save(os.path.join(os.getcwd(),'tests',test))

    elif arg == 'unit':
        import unittest
        class ChartsTest(unittest.TestCase):
            def testcharts(self):
                for test,checksum in Test.all.items():
                    self.assertEqual(getattr(Test,test)().checksum(), checksum)
        suite = unittest.TestLoader().loadTestsFromTestCase(ChartsTest)
        unittest.TextTestRunner(verbosity=2).run(suite)

    elif arg == 'wiki':
        print '#labels Featured,Phase-Implementation,Phase-Deploy'
        print '== Chart examples adapted from the Google examples taken from the wrapper module unit tests =='
        for n,test in enumerate(Test.all):
            testobj = getattr(Test,test)
            G = testobj()
            print '----'
            print '=== %s ==='%test.title().replace('_','-')
            print '{{{'
            print '\n'.join(map(lambda x: x[8:], getsource(testobj).splitlines()[1:-1]))
            print '}}}'
            print '%s&.png'%G
            print
            if n == 0:
                print "*The rest of the examples use the convenience classes for each kind of chart which are one of either `HorizontalBarGroup, HorizontalBarStack, Line, LineXY, Sparkline, Meter, Map, Radar, QRCode, Pie, Pie3D, Scatter, Venn, VerticalBarGroup, or VerticalBarStack`*"
    elif arg == 'tags':
        print """{% load charts %} <table><tr>
        <th> Advanced </th><td>
{%  chart lc 4.0 93.0 42.0 48.8 70.0 99.0  encoding=text %}
    {% scale 4 100 %}
    {%  axes type xy  %}
    {%  axes label Mar  Apr  May  June  July   %}
    {%  axes label None  50+K   %}
    {%  color ff0000   %}
    {%  line 6 5 2   %}
        {% img alt=DataScaling height=400 id=img title=DataSaling %}
    {%  size 400 200   %}
{% endchart %} </td></tr>"""
        for test in Test.all:
#            if test in ('multiline','axes_position','venn','guide_meter'): continue
            print '<tr><th>%s</th><td>'%test.title().replace('_','-')
            src = []
            for l in map(lambda x: x.strip(), getsource(getattr(Test,test)).splitlines()[1:-1]):
                if l.startswith('#') or not l.strip():
                    continue
                elif l.startswith('G ='):
                    l = 'chart '+l.split('(')[0].split('G =')[1] +' ' + '('.join(l.split('(')[1:])

                rmlst = ['G.',']','[',"'"] # __setattr__
                splst = ["','",'(',')',','] # __call__
                for s in splst:
                    l = l.replace(s,' ')
                for r in rmlst:
                    l = l.replace(r,'')
                l = l.replace('axes.','axes ')
                if l.find('encoding')==0:
                    l = l.replace('=',' ')
                src.append('{% '+l+' %}')
            src.append('{% endchart %}')
            src = '\n'.join(src)
            print src,'</td><td><pre>',src.replace('{','&#123;').replace('}','&#125;'),'</pre></td></tr>'
        print '</table>'
    elif arg == 'img':
        for test in Test.all:
            print test,'\t',getattr(Test,test)().img()
            print

    elif arg == 'url':
        for test in Test.all:
            print test,'\t',getattr(Test,test)()
            print

    elif arg == 'show':
        for test in Test.all:
            getattr(Test,test)().show()

if __name__=='__main__':
    test()

