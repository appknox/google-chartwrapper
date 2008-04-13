from django.http import *
from django.shortcuts import render_to_response
from djangogchart.charts.models import *



def chart(request):
    return render_to_response('charts/chart.html',{
        'mycolor': '0000ff',
        'myval':10,
        'mydata':[
            [0,30,60,70,90,95,100], # x values
            [20,30,40,50,60,70,80], # y values, etc.
            [10,30,40,45,52],
            [100,90,40,20,10],
            [-1], # domain not found, interpolated
            [5,33,50,55,7],
        ]})




def edit(request, cid):
    chart = Chart.objects.get(pk=cid)  
    G = chart.G()     
    data = ''
    scale = ''
    ns = {'chart':chart,'data':data,'scale':scale}
    if 'save_chart' in request.POST:
        keys = request.POST.keys()
        keys.remove('save_chart')
        keys.remove('data')
        keys.remove('scale')
        if request.POST['scale']:
            ns['scale'] = float(request.POST['scale'])
        else:
            ns['scale'] = None
        if request.POST['data']:
            G.data['chd'] = DataEval(request.POST['data'].splitlines())
            keys.remove('chd')
        for k in keys:
            v = request.POST[k]
            if request.POST[k] and v:
                G.data[k] = ns[k] =  str(request.POST[k])
                
        if not 'chs' in keys:
            G.data['chs'] = '300x150'                
        chart.save(G)
    else:        
        for k,v in G.items():
            ns[k] = v
    ns['data'] = G.getdata()       
      #  chart.save(ChartEval(cmds.splitlines())   )
#        return HttpResponseRedirect('/edit/%s/'%cid)
    return render_to_response('charts/edit.html',ns)
    
def view(request, cid):
    return HttpResponse(Chart.objects.get(pk=cid).img())    
