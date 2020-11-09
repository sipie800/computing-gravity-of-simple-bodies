from ctypes import cdll,c_double,c_int

G=6.672E-3
    
sub=cdll.LoadLibrary(r'libgravity_forward.dll')
g_=sub.gravity_sphere
g_.argtypes=[c_double,c_double,c_double,c_double,c_double,c_double,c_double,c_int]
g_.restype=c_double

from g_type import g_type

def g_sph(x,y,z,xo,yo,zo,ro,g_cp):
    return g_(x,y,z,xo,yo,zo,ro,g_type[g_cp])
