
class console:
    def __init__(self):
        self.countInput = 0
        
    def getNumInput(self):
        res = self.countInput
        self.countInput += 1
        return res
def h1_physical_exam6243898d6ea8b2b541485859(var1):

    result = []
    consoleInput = console()
    def input(*args):
        return var1.split('~')[consoleInput.getNumInput()]
    
    x0 = input ()

    

    v0 = input ()

    

    a = input ()

    

    t = input ()

    

    

    

    _float_x0_posicion = float(x0)

    

    _float_v0_posicion = float(v0)/3.6

    

    _float_a_posicion = float(a)

    

    _float_t_posicion = float(t)

    

    

    

    

    

    _float_x0_velocidad = float(x0)/1000

    

    _float_v0_velocidad = float(v0)

    

    _float_a_velocidad = float(a)/3600

    

    _float_t_velocidad = float(t)*3.6

    

    

    

    

    

    _operacion_posicion = (_float_x0_posicion) + (_float_v0_posicion*_float_t_posicion) + (0.5*_float_a_posicion*(_float_t_posicion*_float_t_posicion)) 

    

    _round_operacion_posicion = f"{_operacion_posicion:.2f}" 

    

    

    

    

    

    _operacion_velocidad = (_float_v0_velocidad) + (_float_a_velocidad *(_float_t_velocidad*_float_t_velocidad))

    

    _round_operacion_velocidad = f"{_operacion_velocidad:.3f}" 

    

    

    

    

    

    result.append ("La posición final es de " + _round_operacion_posicion + " m" + " y la velocidad es de " + _round_operacion_velocidad +" km/h" )

    return result
    

    

    

import unittest
class MyTestCase(unittest.TestCase):
    
    def test_a(self):
        a = h1_physical_exam6243898d6ea8b2b541485859("15~3.2~0~0")
        self.assertEqual(" ".join([str(x).replace("\n", " ") for x in a]), "La posición final es de 15.00 m y la velocidad es de 3.200 km/h")
    def test_b(self):
        b = h1_physical_exam6243898d6ea8b2b541485859("21.1~40~0.1~60")
        self.assertEqual(" ".join([str(x).replace("\n", " ") for x in b]), "La posición final es de 867.77 m y la velocidad es de 61.600 km/h")
    def test_c(self):
        c = h1_physical_exam6243898d6ea8b2b541485859("47~6~5e-2~147")
        self.assertEqual(" ".join([str(x).replace("\n", " ") for x in c]), "La posición final es de 832.23 m y la velocidad es de 32.460 km/h")
    def test_d(self):
        d = h1_physical_exam6243898d6ea8b2b541485859("0.00528742155242945~2169.707420564302~894.9724724177361~50.91834484696929")
        self.assertEqual(" ".join([str(x).replace("\n", " ") for x in d]), "La posición final es de 1190875.96 m y la velocidad es de 166223.569 km/h")
    def test_e(self):
        e = h1_physical_exam6243898d6ea8b2b541485859("14.117827845103875~3.0357790988487388~-2978.051158957227~-140.24943181467472")
        self.assertEqual(" ".join([str(x).replace("\n", " ") for x in e]), "La posición final es de -29289093.05 m y la velocidad es de 1503614.974 km/h")
    def test_f(self):
        f = h1_physical_exam6243898d6ea8b2b541485859("0~0~0~0")
        self.assertEqual(" ".join([str(x).replace("\n", " ") for x in f]), "La posición final es de 0.00 m y la velocidad es de 0.000 km/h")
    def test_g(self):
        g = h1_physical_exam6243898d6ea8b2b541485859("0~3.6~0~1")
        self.assertEqual(" ".join([str(x).replace("\n", " ") for x in g]), "La posición final es de 1.00 m y la velocidad es de 3.600 km/h")
    def test_h(self):
        h = h1_physical_exam6243898d6ea8b2b541485859("0~0~0.277777777~1")
        self.assertEqual(" ".join([str(x).replace("\n", " ") for x in h]), "La posición final es de 0.14 m y la velocidad es de 1.000 km/h")
    def test_i(self):
        i = h1_physical_exam6243898d6ea8b2b541485859("1~0~0~0")
        self.assertEqual(" ".join([str(x).replace("\n", " ") for x in i]), "La posición final es de 1.00 m y la velocidad es de 0.000 km/h")
    def test_j(self):
        j = h1_physical_exam6243898d6ea8b2b541485859("0~1~0~0")
        self.assertEqual(" ".join([str(x).replace("\n", " ") for x in j]), "La posición final es de 0.00 m y la velocidad es de 1.000 km/h")