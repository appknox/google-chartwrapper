# PIL Interaction #
The wrapper now supports the [Python Imaging Library](http://www.pythonware.com/products/pil/). Now you can create a chart and fetch the PIL image instance of that chart to display or manipulate however you please. The GChart.image method now returns a [PngImageFile](http://www.pythonware.com/library/pil/handbook/format-png.htm) instance of the chart. You must install the [Python Imaging Library](http://www.pythonware.com/products/pil/) to use these features. The PIL has other image manipulation features like image blending and filtering which can be found in the [PIL Handbook](http://www.pythonware.com/library/pil/handbook/image.htm)

## API ##

The Python API extends the GChart main class, but can be used for any subtype.

```

# Create a simple Google-O-Meter with a label
>>> G = Meter(70).label('Hello').size(225,125)
>>> str(G)
'http://chart.apis.google.com/chart?chl=Hello&chs=225x125&cht=gom&chd=t:70.0'

# Now fetch the PngImageFile
>>> G.image()
<PngImagePlugin.PngImageFile instance at 0xb795ee4c>

# Now that you have the image instance, the world is your oyster
# Try saving image as JPEG,GIF,etc.
>>> G.image().save('google-o-meter.jpg','JPEG')
```

## Advanced Usage ##

The following example takes a chart image and overlays the Google Code logo on top of it as a watermark. You could easily use your own graphics to create a custom overlay.

```
import Image, ImageEnhance
from GChartWrapper import Pie3D

# Main image from chart
image = Pie3D( [1,2,3,4] ).label('A','B','C','D').color('00dd00').image()

# Image to overlay as watermark
# http://www.gstatic.com/codesite/ph/images/code_sm.png
mark = Image.open("code_sm.png")

# Set position and opacity of overlay
position,opacity = (150, 100), 0.2
# Convert to RGBA if needed
mark = mark.convert('RGBA')

# Get alpha layer and lower brightness 
alpha = mark.split()[3]
alpha = ImageEnhance.Brightness(alpha).enhance(opacity)
mark.putalpha(alpha)

# Create new image of the watermark
layer = Image.new('RGBA', image.size, (0,0,0,0))
layer.paste(mark, position)

# Composite the watermark with the chart image
Image.composite(layer, image, layer).show()
```