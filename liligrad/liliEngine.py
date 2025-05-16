import math


class Scalar:
    _grad :float
    _scalar :float
    _op :str
    
    def __init__(self, _scalar, _nodeEnd=(), _op='',_order={}):
        self._scalar = _scalar
        self._nodeEnd = _nodeEnd
        self._op = _op
        self._grad = 0.0
        self._backprop = lambda: None
        self._order = _order



    def backprop(self):
        self._grad = 1.0
        scalar_list = [val for val in self.order.values()]
        for val in reversed(scalar_list):
            val._backprop()
        
        
    
    



    def __add__(self, other):
        other = other if isinstance(other, Scalar) else Scalar(other)
        ret = Scalar(self._scalar + other._scalar, (self, other), '+')
    
        def _backprop():
            self._grad =+ ret._grad
            other._grad =+ ret._grad
        ret._backprop = _backprop
        return ret 
        
    def __radd__(self, other):
        return self + other
        

    def __sub__(self, other):
        other = other if isinstance(other, Scalar) else Scalar(other)
        ret = Scalar(self._scalar + (-other._scalar), (self, other), '-')
        def _backprop():
            self._grad =+ ret._grad
            other._grad =+ ret._grad
        ret._backprop = _backprop
        return ret  
                
    def __rsub__(self, other):
         self._scalar = other - self._scalar ;return self 

         
    def __mul__(self, other):
        other = other if isinstance(other, Scalar) else Scalar(other)
        ret = Scalar(self._scalar * other._scalar, (self, other), '*')
        def _backprop():
            self._grad =+ other._scalar * ret._grad
            other._grad =+ self._scalar* ret._grad
        ret._backprop = _backprop
        return ret

    def __rmul__(self, other):
        return self * other


    def tanh(self):
        ret = Scalar((math.exp(2 * self._scalar) -1)/(math.exp(2 * self._scalar) +1), (self, ), 'tanh')
        def _backprop():
            self._grad =+ (1 - ret.scalar ** 2) * ret._grad 

        ret._backprop = _backprop
        return ret  


    def exp(self):
        ret = Scalar(math.exp(self._scalar), (self, ), 'exp')
        def _backprop(s):
            self._grad =+ math.exp(self.scalar)
        ret._backprop = _backprop
        return ret

    def __repr__(self):
        return f"Scalar(scalar= {self._scalar}: grad= {self._grad})"


