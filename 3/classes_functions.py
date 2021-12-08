import numpy as np

def invert(A):
    '''
    Invert a binary number, put a 1 where a zero was
    and vice versa
    '''
    B = np.array([0 if item == 1 else 1 for item in A])
    return B

class BinaryArray(object):
    '''
    Class to split a list/array of binary strings into
    an array where each row is a binary number and the
    column holds the bit at the respective position (
    counting from the back).
    '''
    def __init__(self, binary_strings, do_invert=False):
        # Check what the highest bit number is
        self.max_length = max([len(Ai) for Ai in binary_strings])
        self.binary_array = self.create_array(binary_strings)
        self.do_invert = do_invert
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
        # numpy annoyingly uses bankers rounding to the nearest even value
        # therefore use nextafter, to push .5 values to 0.5 + a tiny bit and
        # round up
        rounded_averages = np.rint(np.nextafter(averages, averages + np.ones_like(averages)))
        if self.do_invert:
            rounded_averages = invert(rounded_averages)
               
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
            

def find_scrubber_number(BinaryArray):
    '''
    Find the oxygen relevant number, by eliminating all number
    from the array which do not have the same bit at the first,
    second, third.. position until only one number is left.
    '''

    length, nbits = BinaryArray.binary_array.shape
    i = 0
    dominant_binary = BinaryArray.dominant_binary

    while length > 1 and i < nbits:
        BinaryArray.binary_array = BinaryArray.binary_array[np.where(BinaryArray.binary_array[:, i] == dominant_binary[i])[0]]
        
        length = BinaryArray.binary_array.shape[0]    
        dominant_binary = BinaryArray.find_dominant_binary()
        i = i + 1

    result = np.array(BinaryArray.binary_array[0])
    return result
