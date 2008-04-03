from GChartWrapper import *

class TestClass:
    """Extensive unit tests, more are welcome"""
    all = ('simple','title','line','multiline','bar','pie','venn','axes','grid','markers','fill','legend','hvz',
           'guide_intro', 'guide_granularity_20', 'guide_granularity_40', 'guide_granularity_80',
           'guide_line_lc', 'guide_line_lxy', 'guide_sparkline',
           'axes_position')
    
    def simple(self):
        # Instantiate the GChart instance, this is all you will need for making charts
        # GChart(type=None, dataset=None), see the doc for more
        G = GChart()
        # Set the chart type, either Google API type or regular name
        G.type('pie')
        # Update the chart's dataset, can be two dimensional and contain string data
        G.dataset( 'helloworld' )
        # Set the size of the chart, default is 300x150
        G.size(250,100)
        return G
        
    def hvz(self):
        # Make a vertical bar group and scale it to the max
        G = VerticalBarGroup( [[31],[59],[4]] )
        G.scale(59)
        G.color('00ff00','ff0000','0000ff')
        G.legend('Goucher(31)','Truman(59)','Kansas(4)')
        G.fill('c','lg',45,'cccccc',0,'000000',1)
        G.fill('bg','s','cccccc')        
        G.size(200,100)
        return G
        
    def title(self):
        # Title using name with optional color and size
        G = Line( ['GurMrabsClgubaolGvzCrgrefOrnhgvshyvforggregunahtyl'] )
        G.title('The Zen of Python','00cc00',36)
        G.color('00cc00')
        return G
        
    def line(self):
        # Add red line 6 thick
        # with 5 line segments with 2 blank segments
        G = Line( ['hX1xPj'] )
        G.axes.type('xy')
        G.axes.label('Mar', 'Apr', 'May', 'June', 'July')
        G.axes.label(None, '50+Kb')        
        G.color('ff0000')
        G.line(6,5,2)
        return G

        
    def bar(self):
        # 2 color horizontal bars 10 wide
        # with 5 spacing between bars in group and 10 between groups
        G = HorizontalBarGroup( ['hell','orld'] )
        G.color('cc0000', '00aa00') 
        G.bar(10,5,10)   
        return G 
    
    def pie(self):
        # Simple pie chart based on range
        G = Pie3D( [1,2,3,4] )
        G.label('A','B','C','D')
        G.color('00dd00') 
        return G

    def venn(self):
        # Extended venn diagram based on int list, scale the data to the max value
        G = Venn( [100,80,60,30,30,30,10] )
        return G
 
    def axes(self):
        # Call type first with the chxt
        # then call label and style in order, 
        # label can contain None(s)
        G = Line( ['foobarbaz'] )
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
        G = Line( ['foobarbaz'] )
        G.color('76A4FB')   
        G.line(3,6,3)
        G.grid(20.0,25.0,1,0)
        return G
    
    def markers(self):
        # Mark up some of the data randomly
        G = Line( ['helloWorld'] )
        G.marker('c','ff0000',0,3,20)
        G.marker('d','00ff00',0,6,15)    
        G.marker('a','000099',0,4,10)
        G.marker('R','A0BAE9',0,8,0.6)    
        G.marker('r','E5ECF9',0,1,0.25)
        return G     
    
    def markerfill(self):
        # Fill the chart areas with markers
        G = Line( ['99','cefhjkqwrlgYcfgc','QSSVXXdkfZUMRTUQ','HJJMOOUbVPKDHKLH','AA'] )
        G.marker('b','76A4FB',0,1,0)
        G.marker('b','224499',1,2,0)
        G.marker('b','FF0000',2,3,0)
        G.marker('B','80C65A',3,4,0)
        return G    

    def fill(self):
        # Fill the chart/background using chf, add axes to show bg 
        G = Line( ['pqokeYONOMEBAKPOQVTXZdecaZcglprqxuux393ztpoonkeggjp'] )
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
        G = Line( ['FOETHECat','leafgreen','IRON4YOUs'] )  
        G.color('ff0000','00ff00','0000ff')
        G.legend('Animals','Vegetables','Minerals')
        G.axes.type('y') 
        return G

    def multiline(self):
        # Draw multiple lines with markers on an lxy chart
        G = LineXY( [ 
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

    # Examples from the Google Chart API Developer's Guide
    # http://code.google.com/apis/chart/

    def guide_intro(self):
        G = Pie3D([60,40], encoding='text')
        G.size(250,100)
        G.label('Hello', 'World')
        return G

    def guide_granularity_20(self):
        G = Line('fohmnytenefohmnytene', encoding='simple')
        G.size(200,100)
        G.axes.type('xy')
        G.axes.label('April','May','June')
        G.axes.label(None, '50+Kb')
        return G        

    def guide_granularity_40(self):
        G = Line('frothsmzndyoteepngenfrothsmzndyoteepngen', encoding='simple')
        G.size(200,100)
        G.axes.type('xy')
        G.axes.label('April','May','June')
        G.axes.label(None, '50+Kb')
        return G

    def guide_granularity_80(self):
        G = Line('formostthisamazingdayfortheleapinggreenlformostthisamazingdayfortheleapinggreenl', encoding='simple')
        G.size(200,100)
        G.axes.type('xy')
        G.axes.label('April','May','June')
        G.axes.label(None, '50+Kb')
        return G
    
    # http://code.google.com/apis/chart/#line_charts
    def guide_line_lc(self):
        G = Line('fooZaroo', encoding='simple')
        G.size(200,100)
        return G

    # http://code.google.com/apis/chart/#line_charts
    def guide_line_lxy(self):
        # same as the multiline test
        return self.multiline()
        
    # http://code.google.com/apis/chart/#sparkline
    def guide_sparkline(self):
        G = Sparkline([27,25,25,25,25,27,100,31,25,36,25,25,39,25,31,25,25,25,26,26,25,25,28,25,25,100,28,27,31,25,27,27,29,25,27,26,26,25,26,26,35,33,34,25,26,25,36,25,26,37,33,33,37,37,39,25,25,25,25], encoding='text')
        G.color('0077CC')
        G.size(100,20)
        G.marker('B', 'E6F2FA',0,0,0)
        G.line(1,0,0);
        return G

    # this test case isn't working correctly - need to investigate a bit more
    def axes_position(self):
        data = [ [10, 13, 16, 25, 26, 39, 54, 60, 66, 74, 94, 104, 139, 156, 160, 164, 166, 185, 187, 202, 208, 213], 
                 [2914, 3617, 3454, 3390, 3484, 3319, 2372, 2388, 2749, 2381, 2333, 2320, 2261, 1346, 1278, 1174, 1275, 1392, 1373, 2525, 1376, 2334] ]

        # positions between 0 and 100
        axis = [ [0, 13, 28, 42, 56, 71, 84, 100],
                 ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'] ]
        
        # don't do integer arithmetic
        min_value = float(min(data[1]))
        max_value = float(max(data[1]))
        last_value = float(data[1][-1])
        
        G = LineXY(data)
        G.color('76A4FB')
        G.marker('o', '0077CC',0,-1,5)
        G.marker('r', 'E6F2FA',0,(min_value/max_value),1.0) # 0 to 1.0
        G.axes.type("xyr")    
        G.axes.label(*axis[1])
        G.axes.position(*axis[0])
        G.axes.label('%d'%min_value, '%d'%max_value)    
        G.axes.position(int(100*min_value/max_value),100) # 0 to 100
        G.axes.label('%d'%last_value)
        G.axes.position(int(100*last_value/max_value)) # 0 to 100
        return G
        

    
