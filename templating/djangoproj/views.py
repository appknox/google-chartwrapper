from django.shortcuts import render_to_response

def example(request):
    return render_to_response('example.html',{
        'venndata': [100,80,60,30,30,30,10],
        'piedata':[60,40],
        'bhgdata':['el','or'],
        'qrstr':'''To the human eye QR Codes look like hieroglyphics, 
            but they can be read by any device that has 
            the appropriate software installed.'''
        })