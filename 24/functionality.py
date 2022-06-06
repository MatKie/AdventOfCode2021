import numpy as np

class ALU(object)
    '''
    Arithmetic logic unit

    Takes the instructions and keeps track of the states
    of variables
    '''
    def __init__(self):
        self.states = {'x': 0, 'y': 0, 'z': 0, 'w': 0}
        self.methods = {
                        'add': np.add(), 'mul': np.multiply(), 
                        'div': np.floor_divide(), 'mod': np.mod(), 
                        'eql': int(np.equal()), 'inp': self._input()
                       }
        
    def do_instruction(self, instr):
        method, var, value = instr.split()
        value = int(value)
        self.states[var] = self.methods.get(method)(self.states[var], value)

    def _input(self, old_var, value):
        return value


def monad(serial_number, instructions):
    '''
    MOdel Number Automatic Detector program
    
    takes a serial number and a set of instructions. Inputs the serial
    number digits at the respective time during the instructions and feeds
    this to the ALU
    '''
    pass
