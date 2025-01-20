kN = 1.0
mm = 1.0
sec = 1.0
min = 60*sec

kip = 4.448*kN
inch = 25.4*mm

ft = 12*inch
ksi = kip/inch**2
GPa = kN/mm**2
MPa = 0.001 * (kN/mm**2)

g = 32.2*ft/sec**2


W1 = 18*kip
W2 = 760*kip
W3 = 70*kip
W4 = 260*kip

m4 = W4 / g
m3 = W3 / g
m2 = W2 / g
m1 = W1 / g

E = 200*GPa # (E=29000ksi)
Fy = 317.16*MPa
Fu = 399.90*MPa
Esh = 3998.96*MPa
esh = 0.012
es = Fy / E
eu = 0.16
bs =  (Fu/Fy - 1)/(eu/es - 1)
v = 0.30
G = E/(2*(1+v))

R0 = 20
cR1=0.925
cR2=0.15
params = [R0, cR1, cR2]


