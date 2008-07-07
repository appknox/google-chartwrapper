from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from GChartWrapper.charts.models import Chart
from chartproject.charts import interp




def chart(request):
    return render_to_response('charts/chart.html',{
        'ds1':[[10, 50, 60, 80, 40],[50, 60, 100, 40, 20]],
        'ds2':[ [77,66,15,0,31,48,100,77],[20,36,100,2,0,100] ],
        'mycolor': '0000ff',
        'myval':10,
        'val': 'print "HelloWorld"',
        'mydata':[
            [0,30,60,70,90,95,100], # x values
            [20,30,40,50,60,70,80], # y values, etc.
            [10,30,40,45,52],
            [100,90,40,20,10],
            ['-1'], # domain not found, interpolated (strings avoid datascaling)
            [5,33,50,55,7],
        ]})




    
def edit(request, cid=None):
    if cid:
        chart = get_object_or_404(Chart, pk=cid)  
    else:
        chart = Chart(
            name = 'blank_chart',
           data = '1,2,3,4,5',
          chart_instructions = """
chart Line dataset1 encoding=text
size 300 300 
scale 0 5
endchart"""
        )
        chart.save()
    data = ''
    scale = ''
    ns = {}
    if 'save_chart' in request.POST:
        ds,chartimg = interp(request.POST['data'], request.POST['inst']) 
        ns['inst'] = request.POST['inst']
        ns['data'] = '\r\n'.join([','.join(map(str, d)) for d in ds.values()])
        ns['chartimg'] =  chartimg
        chart.data = request.POST['data']
        chart.chart_instructions = ns['inst']
        chart.save()    
        return HttpResponse('<a href="/view/%d/">%s</a>'%(chart.id,ns['chartimg']))
    else:
        ns['data'] = chart.data
        ns['inst'] = chart.chart_instructions
        ds,ns['chartimg'] = interp(chart.data, chart.chart_instructions)
    ns['chart'] = chart       
    return render_to_response('charts/edit.html',ns)
    
def view(request, cid):
    chart = get_object_or_404(Chart,pk=cid)
    ds,chartimg = interp(chart.data, chart.chart_instructions) 
    return HttpResponse(chartimg)    
