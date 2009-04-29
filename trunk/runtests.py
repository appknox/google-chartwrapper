from GChartWrapper.tests import *
from inspect import getsource

html = """
<html>
<head>
<title>%(name)s</title>
</head>
<body>
%(img)s
<pre>%(code)s</pre>
</pre>
</body></html>"""
lnks = []
for chart in TestChartTypes.all:
    obj = getattr(TestChartTypes('test_%s'%chart),'test_%s'%chart)
    lines = getsource(obj).splitlines()
    lines[0] = lines[0].replace('(self)','()').replace('def test_','def ')
    del lines[-2]
    w = 175
    if chart.find('pin')>-1: w = 30
    lnks.append('<a href="%s" class="thickbox">%s</a>'%(obj(),obj().img(border=0,width=w)) )
    fo=open('demo/%s.html'%chart,'w')
    fo.write(html%{'code':'\n'.join(lines),'img':obj().img(),'name':chart})
    fo.close()
print '<table>'
for i,x in enumerate(lnks):
    if i == 0:
        print '<tr>'
    if i % 3 == 0:
        print '</tr><tr>'
    print '<td width="25%%">%s</td>'%x