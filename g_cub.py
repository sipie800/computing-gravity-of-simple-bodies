from ctypes import cdll,c_double,c_int

G=6.672E-3
    
sub=cdll.LoadLibrary(r'libgravity_forward.dll')
g_=sub.gravity_cuboid
g_.argtypes=[c_double,c_double,c_double,c_double,c_double,c_double,c_double,c_double,c_double,c_int]
g_.restype=c_double

from g_type import g_type

def g_cub(x,y,z,x1,x2,y1,y2,z1,z2,g_cp):
    return g_(x,y,z,x1,x2,y1,y2,z1,z2,g_type[g_cp])
