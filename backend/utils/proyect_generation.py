import openseespy.opensees as ops
import opsvis as opsv
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from utils.init_data import *
import tempfile
import io
def BoxSection (d,t):
    A = d*d - (d-2*t)**2
    Iz = d**4/12 - (d-2*t)**4/12
    Iy = Iz
    J = Iz + Iy
    return pd.Series([A, Iz, Iy, J], index=['A', 'Iz', 'Iy', 'J'])

def DefineSection(tag,matTag,d,t, Nfw, Nff,GJ):
    #ops.uniaxialMaterial('Elastic',matTag,E) # Usando materiales uniaxiales elásticos para definir la respuesta esfuerzo-deformación de la fibra.
    ops.uniaxialMaterial('Steel02',matTag,Fy,E,bs,*params,Fy/E,1,Fy/E,1)
    ops.section('Fiber',tag,'-GJ', GJ)
    ops.patch('rect',matTag,Nff,Nff,d/2,d/2,d/2-t,d/2-t)
    ops.patch('rect',matTag,Nff,Nfw,d/2,d/2-t,d/2-t,-d/2 +t)
    ops.patch('rect',matTag,Nff,Nff,d/2-t,-d/2,d/2,-d/2+t)
    ops.patch('rect',matTag,Nff,Nff,-d/2+t,d/2,-d/2,d/2-t)
    ops.patch('rect',matTag,Nff,Nfw,-d/2+t,d/2-t,-d/2,-d/2+t)
    ops.patch('rect',matTag,Nff,Nff,-d/2,-d/2,-d/2+t,-d/2+t)
    ops.patch('rect',matTag,Nfw,Nff,d/2-t,d/2,-d/2+t,d/2-t)
    ops.patch('rect',matTag,Nfw,Nff,d/2-t,-d/2+t,-d/2+t,-d/2)    

def vecxz (ndI,ndJ,y=[0,0,1]):
    coordI = ops.nodeCoord(ndI)
    coordJ = ops.nodeCoord(ndJ)
    
    xaxis = np.subtract(coordJ,coordI)
    xaxis = xaxis/np.linalg.norm(xaxis)
    
    yaxis = y/np.linalg.norm(y)

    if abs(np.dot(xaxis,yaxis)) > 0.99999:
        print(f'Error: x and y axes are parallel for nodes I={ndI} and J={ndJ} and yaxis',y)

    zaxis = np.cross(xaxis,yaxis)
        
    return zaxis


def definition_nodes():
    nodos = [
        [1, -320 * inch, -320 * inch, 0 * inch],
        [2, 320 * inch, -320 * inch, 0 * inch],
        [3, -320 * inch, 320 * inch, 0 * inch],
        [4, 320 * inch, 320 * inch, 0 * inch],
        [5, -288 * inch, -288 * inch, 320 * inch],
        [6, 288 * inch, -288 * inch, 320 * inch],
        [7, -288 * inch, 288 * inch, 320 * inch],
        [8, 288 * inch, 288 * inch, 320 * inch],
        [9, -256 * inch, -256 * inch, 640 * inch],
        [10, 256 * inch, -256 * inch, 640 * inch],
        [11, -256 * inch, 256 * inch, 640 * inch],
        [12, 256 * inch, 256 * inch, 640 * inch],
        [13, -224 * inch, -224 * inch, 960 * inch],
        [14, 224 * inch, -224 * inch, 960 * inch],
        [15, -224 * inch, 224 * inch, 960 * inch],
        [16, 224 * inch, 224 * inch, 960 * inch],
        [17, -192 * inch, -192 * inch, 1280 * inch],
        [18, 192 * inch, -192 * inch, 1280 * inch],
        [19, -192 * inch, 192 * inch, 1280 * inch],
        [20, 192 * inch, 192 * inch, 1280 * inch],
        [21, -160 * inch, -160 * inch, 1600 * inch],
        [22, 160 * inch, -160 * inch, 1600 * inch],
        [23, -160 * inch, 160 * inch, 1600 * inch],
        [24, 160 * inch, 160 * inch, 1600 * inch],
        [25, -160 * inch, -160 * inch, 1920 * inch],
        [26, 160 * inch, -160 * inch, 1920 * inch],
        [27, -160 * inch, 160 * inch, 1920 * inch],
        [28, 160 * inch, 160 * inch, 1920 * inch],
        [30, -160 * inch, -320 * inch, 1600 * inch],
        [31, 160 * inch, -320 * inch, 1600 * inch],
        [32, -320 * inch, -160 * inch, 1600 * inch],
        [33, 320 * inch, -160 * inch, 1600 * inch],
        [34, -320 * inch, 160 * inch, 1600 * inch],
        [35, 320 * inch, 160 * inch, 1600 * inch],
        [36, -160 * inch, 320 * inch, 1600 * inch],
        [37, 160 * inch, 320 * inch, 1600 * inch],
        [40, -160 * inch, -320 * inch, 1920 * inch],
        [41, 160 * inch, -320 * inch, 1920 * inch],
        [42, -320 * inch, -160 * inch, 1920 * inch],
        [43, 320 * inch, -160 * inch, 1920 * inch],
        [44, -320 * inch, 160 * inch, 1920 * inch],
        [45, 320 * inch, 160 * inch, 1920 * inch],
        [46, -160 * inch, 320 * inch, 1920 * inch],
        [47, 160 * inch, 320 * inch, 1920 * inch],

        [51,  (-304 + 0.5) * inch, (-304 + 0.5) * inch, 160 * inch],
        [52,  (304 - 0.5) * inch, (-304 + 0.5) * inch, 160 * inch],
        [53,  (-304 + 0.5) * inch, (304 - 0.5) * inch, 160 * inch],
        [54,  (304 - 0.5) * inch, (304 - 0.5) * inch, 160 * inch],
        
        [61,  (-16 + 0) * inch, (-304 + 1.3) * inch, 160 * inch],
        [62,  (16 + 0) * inch, (-304 + 1.3) * inch, 160 * inch],
        [63,  (-304 + 1.3) * inch, (-16 + 0) * inch, 160 * inch],
        [64,  (-304 + 1.3) * inch, (16 + 0) * inch, 160 * inch],
        [65,  (-16 + 0) * inch, (304 - 1.3) * inch, 160 * inch],
        [66,  (16 + 0) * inch, (304 - 1.3) * inch, 160 * inch],
        [67,  (304 - 1.3) * inch, (16 + 0) * inch, 160 * inch],
        [68,  (304 - 1.3) * inch, (-16 + 0) * inch, 160 * inch]
        
    ]
    # Convertir la lista a un DataFrame de pandas
    df_nodos = pd.DataFrame(nodos, columns=['id_nodos', 'X', 'Y', 'Z'])
    # Mostrar el DataFrame
    return df_nodos

def definition_elements():
    elementos = [
        [1, 1, 51],
        [2, 51, 5],    
        [3, 2, 52],
        [4, 52, 6], 
        [5, 3, 53],
        [6, 53, 7],
        [7, 4, 54],    
        [8, 54, 8],    
        
        [9, 5, 9],
        [10, 6, 10],
        [11, 7, 11],
        [12, 8, 12],
        [13, 9, 13],
        [14, 10, 14],
        [15, 11, 15],
        [16, 12, 16],
        [17, 13, 17],
        [18, 14, 18],
        [19, 15, 19],
        [20, 16, 20],
        [21, 17, 21],
        [22, 18, 22],
        [23, 19, 23],
        [24, 20, 24],
        [25, 21, 25],
        [26, 22, 26],
        [27, 24, 28],
        [28, 23, 27],
        [29, 5, 7],
        [30, 9, 11],
        [31, 13, 15],
        [32, 17, 19],
        [33, 21, 23],
        [34, 25, 27],
        [35, 6, 8],
        [36, 10, 12],
        [37, 14, 16],
        [38, 18, 20],
        [39, 22, 24],
        [40, 26, 28],
        [41, 5, 6],
        [42, 9, 10],
        [43, 13, 14],
        [44, 17, 18],
        [45, 21, 22],
        [46, 25, 26],
        [47, 7, 8],
        [48, 11, 12],
        [49, 15, 16],
        [50, 19, 20],
        [51, 23, 24],
        [52, 27, 28],
        
        [53, 1, 63],    
        [54, 63, 7], 
        
        [55, 5, 11],
        [56, 9, 15],
        [57, 13, 19],
        [58, 17, 23],
        
        [59, 3, 64],
        [60, 64, 5],
        
        [61, 7, 9],
        [62, 11, 13],
        [63, 15, 17],
        [64, 19, 21],
            
        [65, 2, 68],
        [66, 68, 8],    
        
        [67, 6, 12],
        [68, 10, 16],
        [69, 14, 20],
        [70, 18, 24],
        
        [71, 4, 67],
        [72, 67, 6],
        
        [73, 8, 10],
        [74, 12, 14],
        [75, 16, 18],
        [76, 20, 22],
    
        [77, 1, 61],
        [78, 61, 6],    
        
        [79, 5, 10],
        [80, 9, 14],
        [81, 13, 18],
        [82, 17, 22],
        
        [83, 2, 62],
        [84, 62, 5],
        
        [85, 6, 9],
        [86, 10, 13],
        [87, 14, 17],
        [88, 18, 21],
        
        [89, 3, 65],
        [90, 65, 8],    
        
        [91, 7, 12],
        [92, 11, 16],
        [93, 15, 20],
        [94, 19, 24],
        
        [95, 4, 66],
        [96, 66, 7],    
        
        [97, 8, 11],
        [98, 12, 15],
        [99, 16, 19],
        [100, 20, 23],
        [101, 21, 27],
        [102, 23, 25],
        [103, 22, 28],
        [104, 24, 26],
        [105, 21, 26],
        [106, 22, 25],
        [107, 23, 28],
        [108, 24, 27],
        [109, 5, 8],
        [110, 9, 12],
        [111, 13, 16],
        [112, 17, 20],
        [113, 6, 7],
        [114, 10, 11],
        [115, 14, 15],
        [116, 18, 19],
        [117, 30, 40],
        [118, 31, 41],
        [119, 32, 42], 
        [120, 33, 43],
        [121, 34, 44],
        [122, 35, 45],
        [123, 36, 46],
        [124, 37, 47],
        [125, 30, 21],
        [126, 31, 22],
        [127, 23, 36],
        [128, 24, 37],
        [129, 40, 25],
        [130, 41, 26],
        [131, 27, 46],
        [132, 28, 47],
        [133, 32, 21],
        [134, 22, 33],
        [135, 34, 23],
        [136, 24, 35],
        [137, 42, 25],
        [138, 26, 43],
        [139, 44, 27],
        [140, 28, 45],
        [141, 31, 26],
        [142, 22, 41],
        [143, 30, 25],
        [144, 21, 40],
        [145, 24, 47],
        [146, 37, 28],
        [147, 23, 46],
        [148, 36, 27],
        [149, 32, 25],
        [150, 21, 42],
        [151, 22, 43],
        [152, 33, 26],
        [153, 34, 27],
        [154, 23, 44],
        [155, 24, 45],
        [156, 35, 28],  
    ]

    # Convertir la lista en un DataFrame
    df_elementos = pd.DataFrame(elementos, columns=["id_frame", "Nodo_I", "Nodo_J"])


    return df_elementos

def definition_section():
    data = {
    'id_frame': list(range(1, 157)),  # Crear los ID de los elementos desde 1 hasta 144
    'd': [30*inch] * 28 + [14*inch] * 4 + [20*inch] * 2 + [14*inch] * 4 + [20*inch] * 2 + [14*inch] * 4 + 
         [20*inch] * 2 + [14*inch] * 4 + [20*inch] * 2 + [14*inch] * 48 + [20*inch] * 8 + [12*inch] * 8 +
         [20*inch] * 40,  # Definir las longitudes de d de acuerdo con el patrón
    't': [0.625*inch] * 28 + [0.625*inch] * 4 + [0.625*inch] * 2 + [0.625*inch] * 4 + [0.625*inch] * 2 + 
         [0.625*inch] * 4 + [0.625*inch] * 2 + [0.625*inch] * 4 + [0.625*inch] * 2 + [0.625*inch] * 48 + 
         [0.625*inch] * 8 + [0.5*inch] * 8 + [0.625*inch] * 40  # Definir las longitudes de t de acuerdo con el patrón
    }
    df_seccion = pd.DataFrame(data)
    # Aplica la función BoxSection a cada fila del DataFrame
    df_seccion[['A', 'Iz', 'Iy', 'J']] = df_seccion.apply(lambda row: BoxSection(row['d'], row['t']), axis=1)

    return df_seccion


def definition_elements_section():
    df_elementos = definition_elements()
    df_seccion = definition_section()
    df_elementos_seccion = pd.merge(df_elementos,df_seccion,on='id_frame',how='inner')

    nueva_columna_u_vecxz = [[0, 0, 1]] * len(df_elementos_seccion)
    df_elementos_seccion['u_vecxz'] = nueva_columna_u_vecxz

    # Valores de elementos verticales
    elementos_verticales = [25,26,27,28,117,118,119,120,121,122,123,124]

    vecxz_verticales = [0,-1,0]

    def actualizar_nueva_columna(row):
        if row['id_frame'] in elementos_verticales:
            return vecxz_verticales
        return row['u_vecxz']

    df_elementos_seccion['u_vecxz'] = df_elementos_seccion.apply(actualizar_nueva_columna, axis=1)

    return df_elementos_seccion


def definition_values():
    valores1 = list(range(1, 25))                       # Seccion B30x30x0.625 desde el elemento  1 - hasta el elemento 24
    valores2 = list(range(29, 33))                      # Seccion B14x14x0.625 desde el elemento 29 - hasta el elemento 32
    valores3 = list(range(35, 39))                      # Seccion B14x14x0.625 desde el elemento 35 - hasta el elemento 38
    valores4 = list(range(41, 45))                      # Seccion B14x14x0.625 desde el elemento 41 - hasta el elemento 44
    valores5 = list(range(47, 51))                      # Seccion B14x14x0.625 desde el elemento 47 - hasta el elemento 50
    valores6 = list(range(53, 101))                      # Seccion B14x14x0.625 desde el elemento 53 - hasta el elemento 100
    valores7 = list(range(109, 117))                     # Seccion B12x12x0.625 desde el elemento 109 - hasta el elemento 116
    valores = valores1 + valores2 + valores3 + valores4 + valores5 + valores6 + valores7
    return valores


def init_model_structure():
    ops.wipe()
    ops.model('basic','-ndm',3,'-ndf',6)
    df_nodos = definition_nodes()

    for index, row in df_nodos.iterrows():
        id_nodos,x,y,z = row
        ops.node(int(id_nodos),x,y,z)

    # Apoyos de la base de las “mega columnas” articulados
    ops.fix(1,1,1,1,0,0,0)  
    ops.fix(2,1,1,1,0,0,0) 
    ops.fix(3,1,1,1,0,0,0) 
    ops.fix(4,1,1,1,0,0,0)   

    # Asignacion de diafragma rígido en “losa superior e inferior"

    # losa superior
    ops.node(400,0*inch,0*inch,1920*inch); ops.fix(400,0,0,1,1,1,0)
    ops.rigidDiaphragm(3,400,*[25,26,27,28,40,41,42,43,44,45,46,47])

    # losa inferior
    ops.node(300,0*inch,0*inch,1600*inch); ops.fix(300,0,0,1,1,1,0)
    ops.rigidDiaphragm(3,300,*[21,22,23,24,30,31,32,33,34,35,36,37])

def next_model_structure():
    Np=5   #Cuatro puntos Integración de Gauss-Lobatto
    Nfw=4
    Nff=1
    u=1
    v=1
    df_elementos_seccion = definition_elements_section()
    valores = definition_values()
    for index, row in df_elementos_seccion.iterrows():
        id_frame,Nodo_I,Nodo_J,d,t,A,Iz,Iy,J,u_vecxz = row
        zaxis = vecxz(Nodo_I,Nodo_J,u_vecxz)
        transfTag=u
        integrationTag=u
        secTag=u

        #ops.geomTransf('Linear',transfTag,*zaxis)
        ops.geomTransf('Corotational',transfTag,*zaxis) # Se modifica transformacion geometrica de Linear a Corotational

        if  id_frame in valores:
            GJ=G*J
            matTag=v
            DefineSection(secTag,matTag,d,t, Nfw, Nff,GJ)
            v=v+1
        else:
            ops.section('Elastic', secTag, E, A, Iz,Iy,G,J) # Definiendo una sección elástica utilizando las propiedades del material y las propiedades de la seccion

        ops.beamIntegration('Lobatto', integrationTag, secTag, Np) # Integración de Gauss-Lobatto con cuatro puntos
        ops.element('forceBeamColumn', id_frame, Nodo_I,Nodo_J, transfTag, integrationTag) #Definiendo el elemento viga-columna basado en fuerzas (force-based)
        u=u+1

def do_gravity_mass_analytic():
    ops.timeSeries('Constant',1)
    ops.pattern('Plain',1,1)

    for node in range(5, 21):
        ops.load(node, 0.0, 0.0, -W1, 0.0, 0.0, 0.0)
        ops.mass(node,m1,m1,m1,0.0,0.0,0.0)     # Masa simica

    for node in range(21, 25):
        ops.load(node, 0.0, 0.0, -W2, 0.0, 0.0, 0.0)
        ops.mass(node,m2,m2,m2,0.0,0.0,0.0)     # Masa simica

    for node in range(25, 29):
        ops.load(node, 0.0, 0.0, -W3, 0.0, 0.0, 0.0)
        ops.mass(node,m3,m3,m3,0.0,0.0,0.0)     # Masa simica

    for node in range(30, 38):
        ops.load(node, 0.0, 0.0, -W4, 0.0, 0.0, 0.0)
        ops.mass(node,m4,m4,m4,0.0,0.0,0.0)     # Masa simica

    for node in range(40, 48):
        ops.load(node, 0.0, 0.0, -W3, 0.0, 0.0, 0.0)
        ops.mass(node,m3,m3,m3,0.0,0.0,0.0)     # Masa simica

    # Configurar el sistema de análisis estático

    ops.constraints('Transformation')
    ops.numberer('RCM')
    ops.system('BandGeneral')
    ops.algorithm('Linear')
    ops.integrator('LoadControl',1)
    ops.analysis('Static')
    ops.analyze(1)
    ops.reactions()

    


def create_image_stream():
    image_stream = io.BytesIO()
    plt.savefig(image_stream, format='png')
    plt.close()
    image_stream.seek(0)
    return image_stream


def create_model():
    init_model_structure()
    opsv.plot_model()
    image_stream =create_image_stream()
    return image_stream

def create_model_two():
    init_model_structure()
    next_model_structure()
    fig_size=(60, 65)
    opsv.plot_model(fig_wi_he=fig_size,element_labels=0,az_el=(-60,25),local_axes=False)
    image_stream = create_image_stream()
    return image_stream

def create_model_tree():
    init_model_structure()
    next_model_structure()
    do_gravity_mass_analytic()
    opsv.plot_defo(sfac=20,fig_wi_he=(30,60))
    image_stream = create_image_stream()
    return image_stream

def create_model_four():
    
    init_model_structure()
    next_model_structure()
    do_gravity_mass_analytic()
