# -*- coding: utf-8 -*-
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
        'simple':'a6de27c4891b513efe669892f7d5304edd276427',
        'guide_granularity_20':'1422b8f665d8c206ae51e7d081e3efd5be8c64df',
        'pie':'1c70efb85226bece67add6857821931612a516b4',
        'guide_granularity_40':'b9a0e223679091a974261d0b0ff76a7f1a6f87bf',
        'guide_radar':'3232689307ee877de97d33afb775305a1d9955b6',
        'hvz':'428121b69154fe7ca6bfc91871496c6a22ea05f0',
        'guide_sparkline':'22398cd8e290ba82498d71e4670f44c8afc4d31f',
        'guide_bhg':'1abfbaaf0149a45b70de594740cf1dcc8dec0ec9',
        'venn':'63bd278cc8b8abbb2cae317747a6ea79c5a1b708',
        'fill':'d48ed4917a79fefca53ac3fd109fe470b0b3bcb9',
        'guide_line_lc':'b0a0446b4fba55b6b48c23cd1487817d17a7ac3d',
        'title':'85827823968a1ffe961d6fbcf42f6b47513c7f50',
        'axes':'1c24dc0218665a18320d8eb33a5f81f60dd91614',
        'qr_code':'f3dc533977a3befb2f33492ac3702503d18eb23a',
        'markers':'22afa45a6221c316ebb847b40595c0586632b23a',
        'guide_granularity_80':'0a000350f0930cc317b679e7df94cf79da77890c',
        'axes_position':'92b8655c2e16ef388f95abf8ad163605f1f2a1d2',
        'jacobian':'a0a605bc6e0245c3d7fe1fdf990cdd9fc141eb2e',
        'multiline':'8c4ecb646cd40ccd763df727d078914659b7bebc',
        'numpy':'066457dee12063d00ee66aaf505140cfa6b37116',
        'guide_meter':'9da7847582350804ec74a7020a4f19e7e12c59e4',
        'guide_chbh_clipped':'2fe51239ba12dfd1f999013135f8ea2dd15564f1',
        'guide_intro':'7d63dfcc9f4737a89ae3a6a000774276699c67ae',
        'guide_bvg':'bdb6f34c97c3c66e5f958a2d5dc1475106460db5',
        'guide_bhs':'c13b6773dda91a53d206de5c79912026de94e221',
        'guide_map':'fb42ac6ba7e7003c7e742b18942f6b45cf3e29f0',
        'guide_bvs':'da3c89c7e9230694b1b78b81ace3322eec6550ba',
        'grid':'528bded06db202224dda42e42530bfd76c649a1d',
        'bar':'b1438c5ef7579fb1c57004caed58d455ef2f3edf',
        'line':'4ac346c115818b8c1367ec22c73d1c68173c32a3',
        'guide_chbh_size':'1f9a99247fababae18542de7adf21bd15c7cf8f8',
        'legend':'e6051b655c8e7af150c987cadf5a284b816c06fb',
        'legend2':'ef9de98d1e12b07e401b554619a7c2c4271287c6',
        'guide_bvs_scale':'473384e7062cf537ba4f9fea69b6d1c52a1855a4',
        'concentric_pie':'d47836a02b6fcc6c5b78b568302c5fa1f9cb3777',
        'min_max':'879321cb524abb91b24f528276fa0c380c503bf3',
        'margins':'58e5e287ca916f6cf50232ff3a4e643d3bff7276',
        'financial':'59d8b5548eca7a7587f2362c022d701228f99a11',
        'bar_text':'99cac384e1742a9235754fb1d5290a539a0f5962',
        'text':'74838e7b743af07cb88cb54bbd0c8200d6f2bb21',
        'letter_pin':'613e8f6aeaa2a2d79903a0daabf9525e7713adcf',
        'icon_pin':'5be1841e81c136f16d4273a2b03ee4cc4c40adfc',
        'adv_icon_pin':'3be6f1d46d32a0c9faccdacd9176e72a647dc598',
        'adv_letter_pin':'9f74ffdddebbfd00c1c058e25a1d1a15f9ab9e9a',
        'text_pin':'b8df4be52ff8ec1a11e07f6f2821f548f235cdd8',
        'sticky_note':'6186850ddc39a2c84c885c1e5db55b32fb690e93',
        'thought_note':'cca0f17a7cabdd92ed80cad2e0f1a12d2ef27987',
        'weather_note':'0a6e3d9448abcf41acd5c04f9b7536c03625e0a8',
        'small_bubble_icon':'474a085ed5f733554efebad29e2aacec8139541d',
        'large_bubble_icon':'93cd245cbed44e636e11f15b54d3603ae5b1bc6f',
        'large_bubble_icon_texts':'f1e27f937873a363d1e489ac32a6e6c0c7b06c8e',
        'large_bubble_texts':'8595b68e8293db1810a4317325cbbd14eae0a824',
    }

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
        G.bar(10)
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

    def numpy(self):
        # Test to see whether numpy arrays work correctly
        # Must have numpy installed to do this test correctly
        data = [10,20,30,40,50,60,70,80,90]
        try:
            from numpy import array
            data = array(data)
        except ImportError:
            print 'Warning: numpy must be installed to do this test correctly'        
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
        G.marker('F','0000FF',0,'1:4',20)
        G.size(200,125)
        return G
        
    def bar_text(self):
        # Using text markers in a bar chart
        G = HorizontalBarGroup([[40,60],[50,30]], encoding='text')
        G.size(200,125)
        G.marker('tApril mobile hits','000000',0,0,13)
        G.marker('tMay mobile hits','000000',0,1,13,-1)
        G.marker('tApril desktop hits','000000',1,0,13)
        G.marker('tMay desktop hits', '000000',1,1,13)
        G.color('FF9900','FFCC33')
        return G
        
    def margins(self):
        G = Line(['Uf9a','a3fG'], encoding='simple')
        G.size(250,100)
        G.label(1,2,3,4)
        G.fill('bg','s','e0e0e0')
        G.color('000000','0000FF')
        G.margin(20,20,20,30,80,20)
        G.legend('Temp','Sales')
        return G
        
    def min_max(self):
        G = Line('mHMza', encoding='simple')
        G.color('008000')
        G.line(2.0,4.0,1.0)
        G.size(200,140)
        G.axes.type('x')
        G.axes.label(None,'t',None,'F',None)
        G.marker('tMin','0000FF',0,1,10)
        G.marker('fMax','FF0000',0,3,15)
        G.margin(0,0,30,0)
        return G
    
    def text(self):
        text = '''
        1600 Ampitheatre Parkway
        Mountain View, CA
        (650)+253-0000
        '''
        G = Text('darkred',16,'h','red','b',text)
        return G
        
    def letter_pin(self):
        G = LetterPin('A','red','black')
        return G

    def icon_pin(self):
        G = IconPin('home','yellow')
        return G

    def adv_letter_pin(self):
        G = AdvLetterPin('star','A','aqua','black','red')
        return G

    def adv_icon_pin(self):
        G = AdvIconPin('star','home','aqua','red')
        return G

    def text_pin(self):
        G = TextPin(1.2,30,'FFFF88',10,'_','Foo\nBar')
        return G
        
    def sticky_note(self):
        G = Note('note_title','pinned_c',1,'darkgreen','l',"Joe's\nToday 2-for-1 !\n555-1234")
        return G

    def thought_note(self):
        G = Note('note','thought',1,'navy','h',"wouldn't it be\ngreat to eat\nat Joe's?")
        return G

    def weather_note(self):
        G = Note('weather','taped_y','sunny','Barcelona','max 25°','min 15°')
        return G
        
    def small_bubble_icon(self):
        G = SBubbleIcon('petrol','bb','$3/gal','khaki','black')
        return G

    def large_bubble_icon(self):
        G = LBubbleIcon('snack','bb','$2.99','ffbb00','black')
        return G   

    def large_bubble_icon_texts(self):
        G = LBubbleIconTexts('petrol','bb','khaki','black','LoCost Fuel\n$3.05/gal unleaded\n$2.10/gal diesel')
        return G

    def large_bubble_texts(self):
        G = LBubbleTexts('bb','teal','khaki',"Joe\'s Restaurant\n123 Long St\n92745 Mountain View")
        return G