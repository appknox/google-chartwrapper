#!/usr/bin/env python
"""
GChartWrapper - Google Chart API Wrapper

Unit test platform

    Run this application from the command line for various testing modes.
    
    Usage
    
        $ python tests.py [<mode>]
        
    Where mode is one of the following:
    
        save - Saves images of all charts in 'tests' folder
        wiki - Creates GoogleCode compatable wiki markup of test src and img
        img - Prints html img tags for all charts
        url - Prints urls of all charts
        show - Opens all charts in tabs in a web browser
        tags - Prints Django template src of all charts
"""
from GChartWrapper.testing import TestClass
import os,sys
from inspect import getsource
        
def test():        
    arg = sys.argv[-1].lower()
    if not arg in ('save','wiki','img','url','show','tags'):
        arg = 'url'
       
    Test = TestClass()

    if arg == 'save':  
        if not os.path.isdir('tests'):
            os.mkdir('tests')  
        for test in Test.all:
            getattr(Test,test)().save(os.path.join(os.getcwd(),'tests',test))

    elif arg == 'wiki':
        print '== Chart examples adapted from the Google examples taken from the wrapper module unit tests =='
        for n,test in enumerate(Test.all):
            testobj = getattr(Test,test)
            G = testobj()
            print '=== %s ==='%test.title()
            print '{{{'
            print '\n'.join(map(lambda x: x.strip(), getsource(testobj).splitlines()[1:-1]))
            print '}}}'
            print '%s&.png'%G
            print
            if n == 0:
                print """=== Attention! ===
*The rest of the examples use the convenience classes for each kind of bar chart which are one of either 
`HorizontalBarGroup, HorizontalBarStack, Line, LineXY, Sparkline, Meter, Map, Radar, Pie, Pie3D, Scatter, Venn, VerticalBarGroup, or VerticalBarStack`*
                """
    elif arg == 'tags':
        for test in Test.all:
            print '<p>',test
            for l in map(lambda x: x.strip(), getsource(getattr(Test,test)).splitlines()[1:-1]):
                if l.startswith('#'):
                    continue
                elif l.startswith('G = GChart('):
                    l = 'chart '+l[12:-1]

                rmlst = ['G.',']','[',"'"]
                splst = ["','",'(',')',',']
                for s in splst:
                    l = l.replace(s,' ')
                for r in rmlst:
                    l = l.replace(r,'')
                l = l.replace('axes.','axes ')
                print '{% ',l,' %}'
            print '{% endchart %} </p>'          
            print

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
        
