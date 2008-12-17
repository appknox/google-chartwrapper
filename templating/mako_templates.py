from mako.template import Template

print Template("""
<%namespace name="gchart" module="GChartWrapper.mako"/>

${gchart.chart('p3',data)}

""").render(data=range(5))


"""

${hw.my_tag()}
"""