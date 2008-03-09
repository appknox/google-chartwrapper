alphanum = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
class Encoder:
    """Data encoder that handles simple,text, and extended encodings
    
    Based on javascript encoding algorithm"""
    def __init__(self, encoding, maxValue=None):        
        self.maxValue = maxValue
        assert(encoding in ('simple','text','extended')),\
            'Unknown encoding: %s'%encoding    
        self.encoding = encoding
        if encoding == 'simple':
            self.char = ','
            self.coding = alphanum
            self._encode = self.simple
        elif self.encoding == 'text':
            self.char = '|'             
            self._encode = self.text    
        elif encoding == 'extended':
            self.char = ','
            self.coding = alphanum + '-.'
            self._encode = self.extended     

    def encode(self,dataset,maxValue=None):
        """Encode wrapper for a dataset with maximum value
        
        Datasets can be two dimensional
        Strings are ignored as ordinal encoding"""
        if maxValue == None:
            if self.maxValue:
                maxValue = self.maxValue
        code = self.encoding[0]+':'
        if type(dataset[0])==type([]):              
            data = self.char.join([self._encode(data, maxValue) for data in dataset])
        else:
            data = self._encode(dataset, maxValue)
        return code + data            
        
    def simple(self,valueArray,maxValue):                       
        if type(valueArray[0]) == type(''):  
            return ','.join(valueArray)        
        if maxValue == None:
            maxValue = max(valueArray)
        chartData = []         
        for currentValue in valueArray:
            if currentValue != None and currentValue >= 0:
                n = round(61 * float(currentValue) / float(maxValue))
                chartData.append(self.coding[int(n)])
            else:
                chartData.append('_')   
        return ''.join(chartData)            
    def extended(self,valueArray,maxValue):
        #XXX: alot about this doesnt seem right, not well tested
        chartData = ''
        if maxValue == None:
            maxValue = max(valueArray)        
        for currentValue in valueArray:
            if currentValue != None and currentValue >= 0:
                chartData += self.coding[int(float(currentValue)/64)]
                chartData += self.coding[currentValue%64]
            else:
                chartData += '__'   
        return chartData
    def text(self,valueArray,junk):
        chartData = []
        for currentValue in valueArray:            
            if currentValue != None and (0 <= currentValue <= 100):
                chartData.append('%.1f'%currentValue)
            else:
                chartData.append('-1')                
        return ','.join(chartData)
