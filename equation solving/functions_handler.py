from math import sqrt

import numpy as np
from numpy import sin, tan, tanh
from sympy import *
from sympy.core.sympify import converter


class function:
    def __init__(self, function, x_start, x_stop):
        self.function = function
        self.x_start = x_start
        self.x_stop = x_stop

    def get_x(self):
        return np.linspace(self.x_start, self.x_stop)

    def get_y(self):
        return list(map(self.calc, np.linspace(self.x_start, self.x_stop)))

    def calc(self, num):
        return self.function.evalf(subs={x: num})

    def get_text(self):
        return self.text


x=symbols('x')
functions = {
    "0.5*x^5+1.8*x^4-2.2*x^3+0.8*x^2+0.3*x-1.3":
        function(0.5 * x ** 5 + 1.8 * x ** 4 - 2.2 * x ** 3 + 0.8 * x ** 2 + 0.3 * x - 1.3, -1, 1 ),
    "x*sin(x)-1":
        function(x * sin(x) - 1, 0, 2 ),
    "sqrt(x)+sin(5-x^2)^3-1":
        function( sqrt(x) + sin(5 - x ** 2) ** 3 - 1, 0.1, 2),
    "tan(x)+tanh(x)": function(tan(x) + tanh(x), 2.3, 2.4
                               ),
    "x^3-x-4": function(x ** 3 - x - 4, 1, 2
                        ),
    "x^2-5": function( x ** 2 - 5, 2, 3
                      ),
    "x^2-7": function( x ** 2 - 7, 2, 3
                      ),
    "x^3-3*x+2": function(x ** 3 - 3 * x + 2, -3, -1
                          )
}

