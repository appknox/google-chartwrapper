#!/usr/bin/env python
from GChartWrapper.testing import TestClass
from GChartWrapper.constants import _print
import os
import sys
from inspect import getsource
import unittest

Test = TestClass()

ordering = ('simple', 'financial', 'bar_text', 'concentric_pie', 'margins', 
'min_max', 'text', 'letter_pin', 'icon_pin', 'adv_icon_pin', 'adv_letter_pin',
'text_pin', 'sticky_note', 'thought_note', 'weather_note', 'small_bubble_icon',
'large_bubble_icon', 'large_bubble_icon_texts', 'large_bubble_texts','qr_code', 
'legend', 'bar', 'pie', 'guide_granularity_20',  
'guide_granularity_40', 'guide_granularity_80', 'guide_radar', 'hvz', 
'guide_sparkline',  'venn', 'fill', 'guide_line_lc', 'title', 'axes', 
'markers',  'line', 'multiline', 'axes_position', 'jacobian',  'numpy', 
'guide_meter', 'guide_intro',    'guide_map',  'grid', 'legend2','guide_bhs',
'guide_bvs', 'guide_bvs_scale', 'guide_bvg', 'guide_bhg', 'guide_chbh_clipped',
'guide_chbh_size','currency_bar','czech_and_unicode','tick_marks')


class ChartsTest(unittest.TestCase):
    def test_charts(self):
        for test,checksum in Test.all.items():
            calcsum = getattr(Test,test)().checksum()
            self.assertEqual(calcsum, checksum, 'Bad checksum for %s'%test)

def test():
    arg = sys.argv[-1].lower()
    if not arg in ('save','wiki','img','url','show','tags','unit'):
        arg = 'url'

    if arg == 'save':
        if not os.path.isdir('tests'):
            os.mkdir('tests')
        for test in Test.all:
            getattr(Test,test)().save(os.path.join(os.getcwd(),'tests',test))

    elif arg == 'unit':
        suite = unittest.TestLoader().loadTestsFromTestCase(ChartsTest)
        unittest.TextTestRunner(verbosity=2).run(suite)

    elif arg == 'wiki':
        links = []
        for n,test in enumerate(ordering):
            testobj = getattr(Test,test)
            G = testobj()
            title = test.title().replace('_','-')
            _print('----')
            links.append(title)
            _print('=== %s ==='%title)
            _print('{{{') #'{{{\n#!python'
            _print( '\n'.join(map(lambda x: x[8:], getsource(testobj).splitlines()[1:-1])) )
            _print('}}}')
            #print '{{{\n#!html'
            _print('%s&.png'%G) #G.img()
            #print '}}}'
            _print()
        for link in links:
            _print('  * [http://code.google.com/p/google-chartwrapper/wiki/ChartExamples#%s %s]'%(link,link))
    elif arg == 'tags':
        _print("""{% load charts %} <table><tr>
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
{% endchart %} </td></tr>""")
        for test in Test.all:
#            if test in ('multiline','axes_position','venn','guide_meter'): continue
            _print('<tr><th>%s</th><td>'%test.title().replace('_','-'))
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
            _print(src,'</td><td><pre>',src.replace('{','&#123;').replace('}','&#125;'),'</pre></td></tr>')
        _print('</table>')
    elif arg == 'img':
        for test in Test.all:
            _print(test,'\t',getattr(Test,test)().img())
            _print()

    elif arg == 'url':
        for test in ordering:
            _print(test,'\t',getattr(Test,test)())
            _print()



    elif arg == 'show':
        for test in Test.all:
            getattr(Test,test)().show()

if __name__=='__main__':
    test()


