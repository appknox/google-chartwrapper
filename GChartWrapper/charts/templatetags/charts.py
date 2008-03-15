from djangogchart.charts.models import Chart
from django.template import Library,Node
from GChartWrapper.constants import APIPARAMS
register = Library()

class Image(Node):
    def __init__(self, obj):
        self.obj = obj
    def render(self, context): 
        cobj = context[self.obj] 
        if hasattr(cobj,'img'):
            return cobj.img()
        return Chart.objects.get(pk = cobj.id).img(align='center')

def img(parser, token):
    """
    {% img <chart_id> %}
    """    
    return Image(token.contents.split()[1])

register.tag('img', img)


TITLE = {
    'chbh':'Bar width and spacing',
    'chco':'Colors',
    'chd':'Datasets',
    'chdl':'Legend labels',
    'chf':'Fill',
    'chg':'Gridlines',
    'chl':'Labels',
    'chls':'Lines and thickness',
    'chm':'Markers',
    'chs':'Size',
    'cht':'Type',
    'chts':'Title style',
    'chtt':'Title',
    'chxl':'Axes labels',
    'chxp':'Axes position',
    'chxr':'Axes range',
    'chxs':'Axes style',
    'chxt':'Axes type',
}
HELP = {
    'chbh':'&lt;bar width in pixels&gt;,<br />&lt;optional space between bars in a group&gt;,<br />&lt;optional space between groups&gt;',
    'chco':'&lt;color1&gt;,...,&lt;colorn&gt;',
    'chd':'&lt;encoding&gt;:&lt;chart data string&gt;',
    'chdl':'&lt;first data set label&gt;|&lt;n data set label&gt;',
    'chf':'&lt;bg or c&gt;&lt;type of fill&gt;',
    'chg':'&lt;x axis step size&gt;,<br />  &lt;y axis step size&gt;,<br />  &lt;length of line segment&gt;,<br />  &lt;length of blank segment&gt;',
    'chl':'&lt;label 1 value&gt;|<br>  ...<br>  &lt;label n value&gt;',
    'chls':' &lt;data set 1 line thickness&gt;,&lt;length of line segment&gt;,&lt;length of blank segment&gt;|<br />...</br>   &lt;data set n line thickness&gt;,&lt;length of line segment&gt;,&lt;length of blank segment&gt;<br />',
    'chm':'&lt;r or R&gt;,&lt;color&gt;,&lt;any value&gt;,&lt;start point&gt;,&lt;end point&gt;|<br />  ...<br />  &lt;r or R&gt;,&lt;color&gt;,&lt;any value&gt;,&lt;start point&gt;,&lt;end point&gt;',
    'chs':'&lt;width in pixels&gt;x&lt;height in pixels&gt',
    'cht':'&lt;chart type&gt;',
    'chts':'&lt;color&gt;,&lt;fontsize&gt;',
    'chtt':'&lt;chart title&gt;',
    'chxl':' &lt;axis index&gt;:|&lt;label 1&gt;|&lt;label n&gt;|<br />  ...<br />  &lt;axis index&gt;:|&lt;label 1&gt;|&lt;label n&gt;',
    'chxp':' &lt;axis index&gt;,&lt;label 1 position&gt;,&lt;label n position&gt;|<br>...<br>  &lt;axis index&gt;,&lt;label 1 position&gt;,&lt;label n position&gt;',
    'chxr':'  &lt;axis index&gt;,&lt;start of range&gt;,&lt;end of range&gt;|<br>  ...<br>  &lt;axis index&gt;,&lt;start of range&gt;,&lt;end of range&gt;',
    'chxs':'&lt;axis index&gt;,&lt;color&gt;,&lt;font size&gt;,&lt;alignment&gt;|<br>  ...<br>  &lt;axis index&gt;,&lt;color&gt;,&lt;font size&gt;,&lt;alignment&gt;',
    'chxt':' &lt;axis 1&gt;,... &lt;axis n&gt;',
}
class Form(Node):
    def __init__(self, obj, action=''):
        self.obj = obj
        self.action = action
    def render(self, context):        
        cid = context[self.obj].id
        out = """<form action="%s" method="POST">
     <input type="submit" name="save_chart" value="Save"><table><tr><td valign="top">
     <b>Python dataset</b><br><textarea name="data" cols="30" rows="15"></textarea>
     <br><b>Scale</b><br><input type="text" name="scale" value="%s">
     </td><td valign="top">\n"""%(self.action,'\n'.join(context['cmds']))
        data = Chart.objects.get(pk = cid).G().data
        params = list(APIPARAMS)
        for param in params:
            value = data.get(param,'')
            if param in ('chf','chxr'):
                out += '</td><td valign="top">'
            out += '<b><a href="javascript:setVisible(\'%s\');">%s</a></b><br><input type="text" name="%s" value="%s"><div id="%s" style="visibility: hidden; position: absolute;"><code>%s</code></div><br><br>\n'%\
                (param,TITLE[param],param,value,param,HELP[param])                
        return out + '</td></tr></table></form>'
def form(parser, token):
    """
    {% form <chart_id> %}
    """    
    return Form(*token.contents.split()[1:])

register.tag('form', form)


