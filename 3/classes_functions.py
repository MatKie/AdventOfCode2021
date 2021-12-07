import numpy as np

class BinaryArray(object):
    '''
    Class to split a list/array of binary strings into
    an array where each row is a binary number and the
    column holds the bit at the respective position (
    counting from the back).
    '''
    def __init__(self, binary_strings):
        # Check what the highest bit number is
        self.max_length = max([len(Ai) for Ai in binary_strings])
        self.binary_array = self.create_array(binary_strings)
        self.dominant_binary = self.find_dominant_binary()
    
    def create_array(self, binary_strings):
        '''
        Create the array and fill the values in
        '''
        nrows = len(binary_strings)
        ncols = self.max_length
        binary_array = np.zeros((nrows, ncols))
        
        for i, string in enumerate(binary_strings):
            # In case there are strings of different size.. 
            diff_bits = self.max_length - len(string)
            string = ['0']*diff_bits + list(string)
            binary_array[i, :] = [int(char) for char in string]
            
        return binary_array
            
    def find_dominant_binary(self):
        '''
        Take the column wise average to find the
        most common digit at that position. If it's 
        above 0.5 there were more 1's and vice versa.
        '''
        averages = self.binary_array.mean(axis=0)
        rounded_averages = averages.round()
               
        return rounded_averages
        
    
class BinaryConverter(object):
    '''
    Simple binary converter taking a binary number
    in the format of a row of a BinaryArray.binary_array.
    '''
    def __init__(self, binary_array):
        self.decimal = self.get_decimal(binary_array)
        
    def get_decimal(self, binary_array):
        '''
        Most simple converter I could think of.
        '''
        decimal = 0
        for i, item in enumerate(binary_array[::-1]):
            decimal += np.power(2,i)*item
        return int(decimal)
            
def invert(A):
    '''
    Invert a binary number, put a 1 where a zero was
    and vice versa
    '''
    B = np.array([0 if item == 1 else 1 for item in A])
    return B       