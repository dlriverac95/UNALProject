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


print ("La posición final es de " + _round_operacion_posicion + " m" + " y la velocidad es de " + _round_operacion_velocidad +" km/h" )

