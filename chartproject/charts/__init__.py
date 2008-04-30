from django.template import Context,Template
def interp(dataset,insts):
    ds,out = {},['{% load charts %}']
    i = 1
    for l in dataset.splitlines():
        if l.strip():
            try:  l = map(float, l.split(','))
            except:
                try: l = map(int, l.split(','))
                except: l = l.split(',')
            if i in ds:
                ds[i].append(l)
            else:
                ds[i] = [l]
        else:
            i += 1
    for l in insts.splitlines():
        if l.strip():
            out.append('{% '+l.strip()+' %}')
    ns = {}            
    for n,dat in ds.items():
        ns['dataset%d'%n] = dat            
    template = Template('\n'.join(out))
    return ds,template.render(Context(ns))
