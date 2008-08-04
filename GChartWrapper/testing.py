"""
GChartWrapper - Google Chart API Wrapper

Unit tests, see tests.py for actually running these
"""
from GChartWrapper import *

class TestClass:
    """
    Extensive unit tests, more are welcome
    
    All methods must be commented and return a GChart instance as the last line.
    """
    # All is dict of (name : checksum) pairs
    all = {
        'axes': '3fcb9723df82a188c047e447e2b199743b00aca2',
        'axes_position': 'a797886c02e0e0ee1468c062df2ea1580ee2c551',
        'bar': 'd595c429605b498d16119e1b085d4db7bd2d65a7',
        'fill': '73116b9306c8fe8f4d9f8c1fa593ceccebac02d0',
        'grid': '4a490e501ac87c5001facc9ae492960edbf9829b',
        'guide_bhg': 'a1e0b86b7f1e974c13d8259119b00bced14bcfd1',
        'guide_bhs': '23267067d1650020971adaa6ef39d3ed2b2f380b',
        'guide_bvg': '1e22a2d40262d44cc72a86f7c6d154088c672a5b',
        'guide_bvs': '405a05b4ea61615d8c41b5e6ecee389a446835e1',
        'guide_bvs_scale': '0a8be59cbe59420a7c0953d83a85be0e2d3a9cd2',
        'guide_chbh_clipped': 'e8560a4d0887091430e1ebcd833dfe9300f2a7f8',
        'guide_chbh_size': '788f22cb06efe959da8668a3a444fe3a3271e4a2',
        'guide_granularity_20': '80009ed49f5d1ca275eb63044c42ff69e3d1713d',
        'guide_granularity_40': '43c4923a966374da72732c495548c21ab81570f5',
        'guide_granularity_80': '7e706185fb5942e7034045bcdba8b400f0890c91',
        'guide_intro': 'f356f143e95842e498b3df6f461a22dbe4d8dd2e',
        'guide_line_lc': '8d9a940c9721af037275cc4aa75ed1e823e7d80a',
        'guide_map': '902aba8398fac9d8701fdaee1bb16e4231445ee0',
        'guide_meter': '8ff5c8c788d7aece26623da767a89fd02d5efe7a',
        'guide_radar': '2b31c0e13524621a8167317d388f1d47df14f891',
        'guide_sparkline': 'e62154b7a0df61d2904f4054375e82abaf9a995b',
        'hvz': 'da5ad186adae230f772df90cbcfcb7aaac9d5080',
        'jacobian': 'c628637eaae14e9a053994871f3039a259d940b9',
        'legend': '223979a48997c5000ea037e143b73fb1db2e66af',
        'legend2': '3ddf9a4efadb4cddd4d6246c03e220b472350a6e',
        'line': 'c8daca4899c882e690635a5343bd9fe7e4f56598',
        'markers': 'a6a03714aeefca7191daf4d9f3f2085dcd4e5924',
        'multiline': '8a2940a0e277907a722a86dd054f1bf6e25b787f',
        'pie': '50731d183a8b377f10377fcc46b33e5f8ec3c9a2',
        'qr_code': 'bc5788f3dea82f76e75ec603f5d451369497689f',
        'simple': '82073d9618e0c17c49f26178d725fae457bc10bc',
        'title': '61fc52176934281eb5560fff2452ab7dd0e0e638',
        'venn': 'c6ecda237b1697ac3dc1257d5b88763a940110b5'
    }

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
        G = VerticalBarGroup( [[31],[59],[4]], encoding='text' )
        G.scale(0,59)
        G.color('00ff00','ff0000','0000ff')
        G.legend('Goucher(31)','Truman(59)','Kansas(4)')
        G.fill('c','lg',45,'cccccc',0,'000000',1)
        G.fill('bg','s','cccccc')        
        G.size(200,100)
        return G

    def qr_code(self):
        # Output a QR code graph that allows 15% restore with 0 margin
        # *Defaults to UTF-8 encoding 
        G = QRCode('''To the human eye QR Codes look like hieroglyphics, 
            but they can be read by any device that has 
            the appropriate software installed.''')
        # or use output_encoding method
        G.output_encoding('UTF-8')
        # level_data(error_correction,margin_size)
        G.level_data('M',0)
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
        # Simple pie chart based on list
        G = Pie3D( [1,2,3,4] )
        G.label('A','B','C','D')
        G.color('00dd00') 
        return G

    def venn(self):
        # Extended venn diagram based on int list, scale the data to the max value
        G = Venn( [100,80,60,30,30,30,10], encoding='text')
        G.scale(0,100)
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
        G = Line( ['helloWorldZZZZ098236561'] )
        G.marker('c','ff0000',0,1,20)
        G.marker('d','80C65A',0,6,15)    
        G.marker('o','FF9900',0,4.0,20.0)
        G.marker('s','3399CC',0,5.0,10.0)
        G.marker('v','BBCCED',0,6.0,1.0)
        G.marker('V','3399CC',0,7.0,1.0)
        G.marker('x','FFCC33',0,8.0,20.0)
        G.marker('h','000000',0,0.30,0.5 )       
        G.marker('a','000099',0,4,10)
        G.marker('R','A0BAE9',0,8,0.6)    
        G.marker('r','E5ECF9',0,1,0.25)
        return G     
        
    def jacobian(self):     
        # from http://toys.jacobian.org/hg/googlecharts/raw-file/tip/docs/examples.html  
        G = Line(['ALAtBmC1EcGYIsLWOXRuVdZhd9ivn4tYzO5b..'],encoding='extended')
        G.size(300,200)
        G.color('cc0000')
        G.fill('c','s','eeeeee')
        G.legend('Sweet')
        return G
    
    def markerfill(self):
        # Fill the chart areas with markers
        G = Line( ['99','cefhjkqwrlgYcfgc',
            'QSSVXXdkfZUMRTUQ','HJJMOOUbVPKDHKLH','AA'] )
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

    def legend2(self):
        # Add a left aligned legend to the chart
        G = Line( ['abcde','FGHIJ','09876'] )  
        G.color('ff0000','00ff00','0000ff')
        G.legend('Animals','Vegetables','Minerals')
        G.legend_pos('l')
        G.axes.type('y') 
        return G

    def multiline(self):
        # Draw multiple lines with markers on an lxy chart
        G = LineXY( [ 
            [0,30,60,70,90,95,100], # x values
            [20,30,40,50,60,70,80], # y values, etc.
            [10,30,40,45,52],
            [100,90,40,20,10],
            ['-1'], # domain not found, interpolated
            [5,33,50,55,7],
        ])
        G.scale(0,100)
        G.color('3072F3','ff0000','00aaaa')
        G.marker('s','FF0000',0,-1,5)
        G.marker('s','0000ff',1,-1,5)
        G.marker('s','00aa00',2,-1,5)   
        G.line(2,4,1)   
        return G

    
    def axes_position(self):
        # multiple axis with label positions specified
        # values between 0 and 100 - use text encoding
        data = [[4.6, 6.0, 7.4, 11.6, 12.0, 14.8, 18.1, 25.1, 
                 27.9, 28.3, 30.6, 34.4, 43.7, 48.3, 57.6, 64.6, 
                 72.5, 74.4, 76.2, 77.2, 86.0, 86.9, 93.9, 96.7, 99.0], 
                [80.5, 100.0, 95.4, 93.7, 96.3, 91.7, 71.5, 63.0, 
                 65.2, 65.5, 66.0, 75.9, 65.8, 64.4, 64.2, 62.5, 37.2, 
                 35.3, 32.4, 35.2, 38.4, 37.9, 69.8, 38.0, 64.5]]
        
        # positions between 0 and 100
        axis = [ [0, 13, 28, 42, 56, 71, 84, 100],
                 ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'] ]
        
        # don't do integer arithmetic
        min_value = float(min(data[1]))
        max_value = float(max(data[1]))
        last_value = float(data[1][-1])
        
        G = LineXY(data, encoding='text')
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
        G = Line('formostthisamazingdayfortheleapinggreenlformostthisamazingdayfortheleapinggreenl',
            encoding='simple')
        G.size(200,100)
        G.axes.type('xy')
        G.axes.label('April','May','June')
        G.axes.label(None, '50+Kb')
        return G
    
    
    def guide_line_lc(self):
        # http://code.google.com/apis/chart/#line_charts
        G = Line('fooZaroo', encoding='simple')
        G.size(200,100)
        return G

        
    
    def guide_sparkline(self):
        # http://code.google.com/apis/chart/#sparkline  
        G = Sparkline([27,25,25,25,25,27,100,31,25,36,25,25,39,
            25,31,25,25,25,26,26,25,25,28,25,25,100,28,27,31,25,
            27,27,29,25,27,26,26,25,26,26,35,33,34,25,26,25,36,25,
            26,37,33,33,37,37,39,25,25,25,25], encoding='text')
        G.color('0077CC')
        G.size(200,40)
        G.marker('B', 'E6F2FA',0,0,0)
        G.line(1,0,0)
        return G

    
    def guide_bhs(self):
        # http://code.google.com/apis/chart/#bar_charts
        G = HorizontalBarStack('ello', encoding='simple')
        G.color('4d89f9')
        G.size(200,125)        
        return G

    def guide_bvs(self):
        G = VerticalBarStack([ [10,50,60,80,40],[50,60,100,40,20] ], encoding='text')
        G.color('4d89f9', 'c6d9fd')
        G.size(200,125)
        return G

    def guide_bvs_scale(self):
        G = VerticalBarStack([ [10,50,60,80,40],[50,60,100,40,20] ], encoding='text')
        G.color('4d89f9', 'c6d9fd')
        G.size(200,125)
        G.scale(0,160)
        return G
        
    def guide_bhg(self):
        G = HorizontalBarGroup(['el','or'], encoding='simple')
        G.color('4d89f9','c6d9fd')
        G.size(200,125)
        return G

    def guide_bvg(self):
        G = VerticalBarGroup(['hello','world'], encoding='simple')
        G.color('4d89f9','c6d9fd')
        G.size(200,125)
        return G

    def guide_chbh_clipped(self):
        G = HorizontalBarStack('hello', encoding='simple')
        G.color('4d89f9')
        G.size(200,125)
        return G

    def guide_chbh_size(self):
        G = HorizontalBarStack('hello', encoding='simple')
        G.color('4d89f9')
        G.size(200,125)
        G.bar_height(10)
        return G

   
    def guide_radar(self):
        # Create a radar chart w/ multiple lines
        G = Radar([ [77,66,15,0,31,48,100,77],[20,36,100,2,0,100] ], encoding='text')  
        G.size(200,200)
        G.color('FF0000','FF9900')
        G.line(2,4,0)
        G.line(2,4,0)        
        G.axes.type('x')
        G.axes.label(0,45,90,135,180,225,270,315)
        G.axes.range(0,360)
        return G
 
    def guide_map(self):
        # Make a map of the US as in the API guide
        G = Map('fSGBDQBQBBAGABCBDAKLCDGFCLBBEBBEPASDKJBDD9BHHEAACAC', encoding='simple')
        G.color('f5f5f5','edf0d4','6c9642','365e24','13390a')
        G.fill('bg','s','eaf7fe')
        G.size(440,220)
        G.map('usa', 'NYPATNWVNVNJNHVAHIVTNMNCNDNELASDDCDEFLWAKSWIORKYMEOHIAIDCTWYUTINILAKTXCOMDMAALMOMNCAOKMIGAAZMTMSSCRIAR')
        return G

    def guide_meter(self):
        # Create a simple Google-O-Meter with a label
        G = Meter(70)
        G.label('Hello')
        G.size(225,125)
        return G


