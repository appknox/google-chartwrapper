# -*- coding: utf-8 -*-
"""
GChartWrapper - Google Chart API Wrapper

Unit tests, see tests.py for actually running these
"""
from GChartWrapper import *
from GChartWrapper.constants import *

class TestClass:
    """
    Extensive unit tests, more are welcome
    
    All methods must be commented and return a GChart instance as the last line.
    """
    # All is dict of (name : checksum) pairs
    all = {
        'simple':'a6de27c4891b513efe669892f7d5304edd276427', 
        'financial':'ea187e300c593867b2f9c17824da34c5bd9a1bef', 
        'bar_text':'e9028a1ff3a1d42bc1a3dcf51780b0321d5d2c96', 
        'concentric_pie':'d47836a02b6fcc6c5b78b568302c5fa1f9cb3777', 
        'margins':'cfa4d80ae660fa4200d5f70c21ba9bff9d2e240b', 
        'min_max':'62d19b35934e091f6d616d9515f8566e44eef474', 
        'text':'7f10b9de58840d2161aa5f32d4a12d86f772fe92', 
        'letter_pin':'196a01c0923628290c867a77438b22be4e811d41', 
        'icon_pin':'8ac735930b99165d343385fc41958d925a9db931', 
        'adv_icon_pin':'f400bd7857e77cd1ec52f82564db301a18902174', 
        'adv_letter_pin':'64cd43483e19828a63987cb2e6cffcf6eeeac5a5', 
        'text_pin':'2b77242c21c673a4ddce1219ebe4befe9f0c5d03', 
        'sticky_note':'90fe055d338ddfa38b17d6ad94efcfec475ed265', 
        'thought_note':'2720d0512907598f6ed13320d431935dbcb26acd', 
        'small_bubble_icon':'22fcf71930a0dc574cfb305bbec38278dc06cbae', 
        'large_bubble_icon':'f456afa8c7098c57c38fb584c01ebf234b6f5e7c', 
        'large_bubble_icon_texts':'92e5b034421b097d87cc990179f16e65538c2d8a', 
        'large_bubble_texts':'a6687d18fc3264f5938b5c203a968e32e9f954ca', 
        'qr_code':'f0f6cea482cc874beb06b9ca2a689d08bda2285b', 
        'legend':'ffd2fd1e34749569c39d22024ea97bd677e2ca13', 
        'bar':'09ff756b63075bb40e9c97a6fdb5f63f2bbfebf4', 
        'pie':'cc4eae489458948e81474533b422e007a08d92ef', 
        'guide_granularity_20':'d330e4275208e2c5f8affed3e391909f73415907', 
        'guide_granularity_40':'6b9142f87a777ae69484008a57737bbc53096a9d', 
        'guide_granularity_80':'6950bb2691e45ca2698e65c2f1e867c77e8bed37', 
        'guide_radar':'13a21487482f1b341a36bb2d735f97d309b2a47f', 
        'hvz':'5ae5be08294efdb63fa39b5b6c33a8d6423196d6', 
        'guide_sparkline':'e61609da9d1b38b8401249b434bc5150dab9bc77', 
        'venn':'63bd278cc8b8abbb2cae317747a6ea79c5a1b708', 
        'fill':'70add0b67f4f86c2c508a28c3bf5c6aab5775ee9', 
        'guide_line_lc':'b0a0446b4fba55b6b48c23cd1487817d17a7ac3d', 
        'title':'385fcf0b6eeba2aba55302a0f71ed420a2908446', 
        'axes':'e892afdd2cad44f50c9ca3213a2b3b43da9bf34c', 
        'markers':'966a8dbe40048a36b647d344c9a7f379ea136c80', 
        'line':'4e2b17fd477830ae144d50e557c873a76f46deb1', 
        'multiline':'e4281cbc408cf31d551fd3776a890d5b33c7b74d', 
        'axes_position':'3845671d4f57f7232d3837df6f1c73a7f8137059', 
        'jacobian':'4056ac217c6cda014a9dff55011a9a3a702caaf1', 
        'numpy':'066457dee12063d00ee66aaf505140cfa6b37116', 
        'guide_meter':'12657d113593b4a3465ab6d79286b0d849601204', 
        'guide_intro':'bde2d538696e0d598c5359de40e7c92d8efecd16', 
        'guide_map':'5a9068f2689e783749e90b683df1142c89057f03', 
        'grid':'645388ffdbd2bd4f117daa265adfc90baa572f74', 
        'legend2':'e785ef2737453840a0756798fb16160fdf3d28f5', 
        'guide_bhs':'1591e5ea4e8f8886613e73941a10a2c547750e0e', 
        'guide_bvs':'cb2f5344e816f1b1ae2214131f11547ec3f9549a', 
        'guide_bvs_scale':'0f47d77a1aa449b27c90e4b01e8c84a3b3d161d9', 
        'guide_bvg':'35d7126f7ccbf56c30254a1403b15affcb49db4f', 
        'guide_bhg':'ef88b9e73a7a08d16d39d0dd14de9486a8d52a1a', 
        'guide_chbh_clipped':'fe87216a7ce5cc496420de787b52b9eac1c056f9', 
        'guide_chbh_size':'03e1fd7393c87c5c65d88469f557f60e5ca0378b',
        'currency_bar':'ab7245c0c005ee99ee198fd6baab45e68fd6e188', 
        'czech_and_unicode':'3bb3ae7cd462a8fc2724ee52b6ca5bc5f39e908d',
        'tick_marks':'d33a9c7555d75dfadc6446bf5686bf988ccc592b', # NOT RIGHT!
    }
    if PY_VER.startswith('3'):
        # strangeness w/ unicode in py3k
        all['weather_note'] = 'a6e78f827cccdcc15979cd9787deb198e4dc33a6'
    else:
        all['weather_note'] = '7e7e87b94bdd3b8cb1fd208b2d565b58a1bc595e'
        
    def simple(self):
        # Instantiate the GChart instance, this is all you will need for making charts
        # GChart(type=None, dataset=None), see the doc for more
        G = GChart()
        # Set the chart type, either Google API type or regular name
        G.type('pie')
        # Update the chart's dataset, can be two dimensional or contain string data
        G.dataset( 'helloworld' )
        # Set the size of the chart, default is 300x150
        G.size(250,100)
        return G
        
    def hvz(self):
        # Make a vertical bar group and scale it to the max
        G = VerticalBarGroup( [[31],[59],[4]], encoding='text' )
        G.scale(0,59)
        G.color('lime','red','blue')
        G.legend('Goucher(31)','Truman(59)','Kansas(4)')
        G.fill('c','lg',45,'cccccc',0,'black',1)
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
        G.axes.label(0, 'Mar', 'Apr', 'May', 'June', 'July')
        G.axes.label(1, None, '50+Kb')        
        G.color('red')
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
        G.axes.label(0,'Foo', 'Bar', 'Baz')
        G.axes.style(0, '0000dd', 14)
        G.axes.label(1, None, '20K', '60K', '100K')  
        G.axes.label(2, 'A', 'B', 'C')  
        G.axes.label(3, None,'20','40','60','80')      
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
        G.marker('c','red',0,1,20)
        G.marker('d','80C65A',0,6,15)    
        G.marker('o','FF9900',0,4.0,20.0)
        G.marker('s','3399CC',0,5.0,10.0)
        G.marker('v','BBCCED',0,6.0,1.0)
        G.marker('V','3399CC',0,7.0,1.0)
        G.marker('x','FFCC33',0,8.0,20.0)
        G.marker('h','black',0,0.30,0.5 )       
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
        G.marker('b','red',2,3,0)
        G.marker('B','80C65A',3,4,0)
        return G    

    def fill(self):
        # Fill the chart/background using chf, add axes to show bg 
        G = Line( ['pqokeYONOMEBAKPOQVTXZdecaZcglprqxuux393ztpoonkeggjp'] )
        G.color('red')
        G.line(4,3,0)
        G.axes.type('xy') 
        G.axes.label(0, 1,2,3,4,5)
        G.axes.label(1, None,50,100)
        G.fill('c','lg',45,'white',0,'76A4FB',0.75)
        G.fill('bg','s','EFEFEF')
        return G    


    def legend(self):
        # Add legend to the data set which follows collors
        G = Line( ['FOETHECat','leafgreen','IRON4YOUs'] )  
        G.color('red','lime','blue')
        G.legend('Animals','Vegetables','Minerals')
        G.axes.type('y') 
        return G

    def legend2(self):
        # Add a left aligned legend to the chart
        G = Line( ['abcde','FGHIJ','09876'] )  
        G.color('red','lime','blue')
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
        G.color('3072F3','red','00aaaa')
        G.marker('s','red',0,-1,5)
        G.marker('s','blue',1,-1,5)
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
        G.axes.label(0, *axis[1])
        G.axes.position(0, *axis[0])
        G.axes.label(1, '%d'%min_value, '%d'%max_value)    
        G.axes.position(1, int(100*min_value/max_value),100) # 0 to 100
        G.axes.label(2, '%d'%last_value)
        G.axes.position(2, int(100*last_value/max_value)) # 0 to 100
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
        G.axes.label(0, 'April','May','June')
        G.axes.label(1, None, '50+Kb')
        return G        

    def guide_granularity_40(self):
        G = Line('frothsmzndyoteepngenfrothsmzndyoteepngen', encoding='simple')
        G.size(200,100)
        G.axes.type('xy')
        G.axes.label(0, 'April','May','June')
        G.axes.label(1, None, '50+Kb')
        return G

    def guide_granularity_80(self):
        G = Line('formostthisamazingdayfortheleapinggreenlformostthisamazingdayfortheleapinggreenl',
            encoding='simple')
        G.size(200,100)
        G.axes.type('xy')
        G.axes.label(0, 'April','May','June')
        G.axes.label(1, None, '50+Kb')
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
        G.bar(10)
        return G

   
    def guide_radar(self):
        # Create a radar chart w/ multiple lines
        G = Radar([ [77,66,15,0,31,48,100,77],[20,36,100,2,0,100] ], encoding='text')  
        G.size(200,200)
        G.color('red','FF9900')
        G.line(2,4,0)
        G.line(2,4,0)        
        G.axes.type('x')
        G.axes.label(0, 0,45,90,135,180,225,270,315)
        G.axes.range(0, 0,360)
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

    def numpy(self):
        # Test to see whether numpy arrays work correctly
        # Must have numpy installed to do this test correctly
        data = [10,20,30,40,50,60,70,80,90]
        try:
            from numpy import array
            data = array(data)
        except ImportError:
            print('Warning: numpy must be installed to do this test correctly')
        G = Radar(data, encoding='text')
        G.size(200,200)    
        return G

    def concentric_pie(self):
        # Using concentric pie charts
        G = PieC(['Helo','Wrld'], encoding='simple')
        G.size(200,100)
        return G
        
    def financial(self):
        # Fancy markers for financial data
        G = Line([[0,5,10,7,12,6],[35,25,45,47,24,46],[15,40,30,27,39,54],[70,55,63,59,80,60]], encoding='text')
        G.marker('F','blue',0,'1:4',20)
        G.size(200,125)
        return G
        
    def bar_text(self):
        # Using text markers in a bar chart
        G = HorizontalBarGroup([[40,60],[50,30]], encoding='text')
        G.size(200,125)
        G.marker('tApril mobile hits','black',0,0,13)
        G.marker('tMay mobile hits','black',0,1,13,-1)
        G.marker('tApril desktop hits','black',1,0,13)
        G.marker('tMay desktop hits', 'black',1,1,13)
        G.color('FF9900','FFCC33')
        return G
        
    def margins(self):
        G = Line(['Uf9a','a3fG'], encoding='simple')
        G.size(250,100)
        G.label(1,2,3,4)
        G.fill('bg','s','e0e0e0')
        G.color('black','blue')
        G.margin(20,20,20,30,80,20)
        G.legend('Temp','Sales')
        return G
        
    def min_max(self):
        G = Line('mHMza', encoding='simple')
        G.color('008000')
        G.line(2.0,4.0,1.0)
        G.size(200,140)
        G.axes.type('x')
        G.axes.label(0, None,'t',None,'F',None)
        G.marker('tMin','blue',0,1,10)
        G.marker('fMax','red',0,3,15)
        G.margin(0,0,30,0)
        return G
    
    def text(self):
        # Make a text chart label w/ any text you like
        # Google automagically ignores white space and spaces text correctly
        text = '''
        1600 Ampitheatre Parkway
        Mountain View, CA
        (650)+253-0000
        '''
        G = Text('darkred',16,'h','red','b',text)
        return G
        
    def letter_pin(self):
        # Simple map pin w/ a letter/number
        G = Pin('pin_letter','A','red','black')
        return G

    def icon_pin(self):
        # Map pin w/ a certain icon
        G = Pin('pin_icon','home','yellow')
        return G

    def adv_letter_pin(self):
        G = Pin('xpin_letter','star','A','aqua','black','red')
        return G

    def adv_icon_pin(self):
        # Map pin w/ cool icon
        G = Pin('xpin_icon','star','home','aqua','red')
        return G

    def text_pin(self):
        # Straight up map pin w/ following text
        G = Pin('spin',1.2,30,'FFFF88',10,'_','Foo\nBar')
        return G
        
    def sticky_note(self):
        # Note w/ title and text 
        G = Note('note_title','pinned_c',1,'darkgreen','l',"Joe's\nToday 2-for-1 !\n555-1234")
        return G

    def thought_note(self):
        # Thought bubble note
        G = Note('note','thought',1,'navy','h',"wouldn't it be\ngreat to eat\nat Joe's?")
        return G

    def weather_note(self):
        # First example w/ true utf-8 encoding
        G = Note('weather','taped_y','sunny','Barcelona','max 25°','min 15°')
        return G
        
    def small_bubble_icon(self):
        # Small bubble marker
        G = Bubble('icon_text_small','petrol','bb','$3/gal','khaki','black')
        return G

    def large_bubble_icon(self):
        # Larger bubble marker
        G = Bubble('icon_text_big','snack','bb','$2.99','ffbb00','black')
        return G   

    def large_bubble_icon_texts(self):
        # Large bubble marker w/ icon and multiline text
        G = Bubble('icon_texts_big','petrol','bb','khaki','black','LoCost Fuel\n$3.05/gal unleaded\n$2.10/gal diesel')
        return G

    def large_bubble_texts(self):
        # Large bubble marker with just text
        G = Bubble('texts_big','bb','teal','khaki',"Joe\'s Restaurant\n123 Long St\n92745 Mountain View")
        return G
    
    def czech_and_unicode(self):
        # Submitted by anedvedicky
        G = VerticalBarStack( [[10], [20], [30]], encoding = 'text')
        G.color('green','lime','red')
        G.label('šýŽěůčář...')
        G.legend('šýŽěůčář...','∫µ≤','´®†¥¨ˆøπ¬˚≤µ˜')
        return G

    def tick_marks(self):
        G = Line('cEAELFJHHHKUju9uuXUc')
        G.color('76A4FB')
        G.line(2)
        G.axes.type('xyrx')
        G.axes.label(2, 'min','avg','max')
        G.axes.label(3, 'Jan','Feb','Mar')
        G.axes.tick(0,10)
        G.axes.tick(1,-180)
        return G
    
    def currency_bar(self):
        G = VerticalBarStack([43.56,35.62,48.34,57.50,67.30,60.91])
        G.color('blue')
        G.bar(17,15)
        G.marker('N*cEUR1*','black',0,-1,11)
        return G