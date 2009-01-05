import GChartWrapper

def chart(context, chart=None, *args, **kwargs):
    if chart and chart in dir(GChartWrapper):
        return getattr(GChartWrapper, chart)(*args, **kwargs)
    return GChartWrapper.GChart(*args, **kwargs)