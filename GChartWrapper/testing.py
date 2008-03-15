from GChartWrapper import GChart
    
class TestClass:
    """Extensive unit tests, more are welcome"""
    all = ('hvz','simple','title','line','multiline','bar','pie','venn','axes','grid','markers','fill','legend')
    
    def simple(self):
        # Instantiate the GChart instance, this is all you will need for making charts
        # GChart(type=None, dataset=None), see the doc for more
        G = GChart()
        # Set the chart type, either Google API type or regular name
        G.type('pie')
        # Update the chart's dataset, can be two dimensional and contain string data
        G.dataset(['hW'])
        # Set the size of the chart, default is 300x150
        G.size(250,100)
        return G
        
    def hvz(self):
        G = GChart('bvg', [[31],[59],[4]])
        G.scale(59)
        G.color('00ff00','ff0000','0000ff')
        G.legend('Goucher(31)','Truman(59)','Kansas(4)')
        G.fill('c','lg',45,'cccccc',0,'000000',1)
        G.fill('bg','s','cccccc')        
        G.size(200,100)
        return G
        
    def title(self):
        # Title using name with optional color and size
        G = GChart('lc',['GurMrabsClgubaolGvzCrgrefOrnhgvshyvforggregunahtyl'])        
        G.title('The Zen of Python','00cc00',36)
        G.color('00cc00')
        return G
        
    def line(self):
        # Add red line 6 thick
        # with 5 line segments with 2 blank segments
        G = GChart('lc',['hX1xPj'])
        G.axes.type('xy')
        G.axes.label('Mar', 'Apr', 'May', 'June', 'July')
        G.axes.label(None, '50+Kb')        
        G.color('ff0000')
        G.line(6,5,2)
        return G

        
    def bar(self):
        # 2 color horizontal bars 10 wide
        # with 5 spacing between bars in group and 10 between groups
        G = GChart('bhg', ['hell','orld'])
        G.color('cc0000', '00aa00') 
        G.bar(10,5,10)   
        return G 
    
    def pie(self):
        # Simple pie chart based on range
        G = GChart('p3', range(1,5))
        G.label('A','B','C','D')
        G.color('00dd00') 
        return G

    def venn(self):
        # Extended venn diagram based on int list, scale the data to the max value
        G = GChart('v', [100,80,60,30,30,30,10])
        return G
 
    def axes(self):
        # Call type first with the chxt
        # then call label and style in order, 
        # label can contain None(s)
        G = GChart('lc',['foobarbaz'])
        G.color('76A4FB') 
        G.axes.type('xyrx')
        G.axes.label('Foo', 'Bar', 'Baz')
        G.axes.label(None, '20K', '60K', '100K')  
        G.axes.label('A', 'B', 'C')  
        G.axes.label(None,'20','40','60','80')      
        G.axes.style('0000dd', 14)
        return G  

    def grid(self):
        # Create dashed line with grid x,y as floats
        # then, just like line, the line and blank segments
        G = GChart('lc',['foobarbaz'])
        G.color('76A4FB')   
        G.line(3,6,3)
        G.grid(20.0,25.0,1,0)
        return G
    
    def markers(self):
        # Mark up some of the data randomly
        G = GChart('lc',['helloWorld'])
        G.marker('c','ff0000',0,3,20)
        G.marker('d','00ff00',0,6,15)    
        G.marker('a','000099',0,4,10)
        G.marker('R','A0BAE9',0,8,0.6)    
        G.marker('r','E5ECF9',0,1,0.25)
        return G
    
   
    
    def markerfill(self):
        # Fill the chart areas with markers
        G = GChart('lc',['99','cefhjkqwrlgYcfgc','QSSVXXdkfZUMRTUQ','HJJMOOUbVPKDHKLH','AA'])
        G.marker('b','76A4FB',0,1,0)
        G.marker('b','224499',1,2,0)
        G.marker('b','FF0000',2,3,0)
        G.marker('B','80C65A',3,4,0)
        return G    

    def fill(self):
        # Fill the chart/background using chf, add axes to show bg 
        G = GChart('lc',['pqokeYONOMEBAKPOQVTXZdecaZcglprqxuux393ztpoonkeggjp'])
        G.color('ff0000')
        G.line(4,3,0)
        G.axes.type('xy') 
        G.axes.label(1,2,3,4,5)
        G.axes.label(None,50,100)
        G.fill('c','lg',45,'ffffff',0,'76A4FB',0.75)
        G.fill('bg','s','EFEFEF')
        return G    


    def legend(self):
        # Add legend to the data set which follows collors
        G = GChart('lc',['FOETHECat','leafgreen','IRON4YOUs'])                                    
        G.color('ff0000','00ff00','0000ff')
        G.legend('Animals','Vegetables','Minerals')
        G.axes.type('y') 
        return G

    def multiline(self):
        # Draw multiple lines with markers on an lxy chart
        G = GChart('lxy', [ 
            [0,30,60,70,90,95,100], # x values
            [20,30,40,50,60,70,80], # y values, etc.
            [10,30,40,45,52],
            [100,90,40,20,10],
            [-1], # domain not found, interpolated
            [5,33,50,55,7],
        ], scale=100) # scale the data to the maximum
        G.color('3072F3','ff0000','00aaaa')
        G.marker('s','FF0000',0,-1,5)
        G.marker('s','0000ff',1,-1,5)
        G.marker('s','00aa00',2,-1,5)   
        G.line(2,4,1)   
        return G
