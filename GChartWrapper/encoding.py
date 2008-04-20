class Encoder:
    """Data encoder that handles simple,text, and extended encodings
    
    Based on javascript encoding algorithm and pygooglecharts"""
    def __init__(self, encoding=None): 
        self.encoding = 'extended'
        if encoding:
            assert(encoding in ('simple','text','extended')),\
            'Unknown encoding: %s'%encoding        
            self.encoding = encoding          
        coding = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
        ecoding = coding + '-.'
        if self.encoding == 'simple':
           self.coding =  coding
           self.max_value =  61
           self.char = ','
           self.dchar = ''
           self.none = '_'                
           self.value = lambda x: coding[x]            
        elif self.encoding == 'text':
           self.coding = ''
           self.max_value =  100
           self.none = '-1'
           self.char = '|'
           self.dchar = ','
           self.value = lambda x: '%.1f'%x                          
        elif self.encoding == 'extended':
           self.coding =  ecoding
           self.max_value =  4095
           self.none =  '__'
           self.dchar = ''
           self.char = ','         
           self.value = lambda x: '%s%s'% \
                (ecoding[int(float(x)/64)], ecoding[x%64])
    
    def scalevalue(self, value):
        if self.scale and type(self.scale) == type(()):
            lower,upper = self.scale
        elif self.scale:
            lower,upper = 0,float(self.scale)
        else:
            lower,upper = 0,self.max_value
        scaled = int(round(float(value - lower) * self.max_value / upper))
        return min(scaled, self.max_value)

    def encode(self,  *args, **kwargs):
        """Encode wrapper for a dataset with maximum value
        
        Datasets can be one or two dimensional
        Strings are ignored as ordinal encoding"""
        if type(args[0]) == type(''):
            return self.encode([args[0]],**kwargs)
        elif type(args[0]) in (type(0), type(0.0), type(0L)):
            return self.encode([[args[0]]],**kwargs)
        if len(args)>1:
            dataset = args
        else:
            dataset = args[0]  
        typemap = map(type,dataset)
        code = self.encoding[0]+':'
        if type('') in typemap:  
            return code + ','.join(map(str,dataset))
        self.scale = None      
        if 'scale' in kwargs:
            self.scale = kwargs['scale']                 
        if type([]) in typemap:  
            data = self.char.join([self.encodedata(data) for data in dataset]) 
        elif len(dataset) == 1:
            data = self.encodedata(dataset[0])                                  
        else:            
            data = self.encodedata(dataset)        
        return code + data            

    def encodedata(self, data):
        sub_data = []
        enc_size = len(self.coding)
        for value in data: 
            if value in (None,'None'):
                sub_data.append(self.none)
            elif value >= 0:
                try:
                    sub_data.append(self.value(self.scalevalue(value)))
                except ValueError:
                    raise ValueError, 'cannot encode value: %s' % value                         
        return self.dchar.join(sub_data)

    def decode(self, astr):
        e = astr[0]
        dec_data = []
        for data in astr[2:].split(self.char):
            sub_data = []
            if e == 't':
                for value in data.split(','):
                    sub_data.append(float(value))
            elif e == 'e':
                flag = 0
                index = self.coding.index
                for i in range(len(data)):
                    if not flag:
                        this,next = index(data[i]),index(data[i+1])
                        flag = 1
                        sub_data.append((64 * this) + next)  
                    else: flag = 0
            elif e == 's':                        
                for value in data:
                    sub_data.append(self.coding.index(value))
            dec_data.append(sub_data)                    
        return dec_data

def test():
    
    for q,a,d in [
        ('simple','s:Ab9',[0,27,61]),
        ('text','t:0.0,10.0,100.0',[0,10,100]),
        ('extended','e:AH-HAA..',[7,3975,0,4095])
        ]:
        E = Encoder(q)
        data = [d]
        test = E.encode(data)
        print test
        assert(E.decode(test) == data)    
        assert(a == test)
    
   
if __name__=='__main__': test()    
    

