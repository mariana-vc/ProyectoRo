No se como funciona esto.


def dict_depth(d, depth=0):
    if not isinstance(d, dict) or not d:
        return depth
    return max(dict_depth(v, depth+1) for k, v in d.iteritems())

dic = {
'status01':{'linea01':{'titulo01':{'descrip01':250}}},
'status02':{'linea02':{'titulo02':{'descrip02':260}}	},
'status03':{'linea03':{'titulo03':{'descrip03':270}}},
'status04':{'linea04':{'titulo04':{'descrip04':280}}},
'status05':{'linea05':{'titulo05':{'descrip05':290}}},
'status06':{'linea06':{'titulo06':{'descrip06':300}}},
'status07':{'linea07':{'titulo07':{'descrip07':310}}},
'status08':{'linea08':{'titulo08':{'descrip08':320}}},
}

print "La señorita flagui"
print "holi 2.0"

print dict_de
pth(dic)

print "hola mundo"




stati = []
for status in dic:
    children = []
    for linea in dic[status]:
        subchildren = []
        for clave in dic[status][linea]:
            subsubchildren = []
            for concepto in dic[status][linea][clave]:
                subsubchildren.append( {'name': concepto,
                                        'size': float(dic[status][linea][clave][concepto])} )
            subchildren.append( {'name': clave,
                                 'children': subsubchildren } )
        children.append( {'name': linea,
                          'children': subchildren} )
    stati.append( {'name': status,
                 'children': children} )
    
proyectos = {'name': 'proyectos',
             'children': stati }


<<<<<<< HEAD

//Este es un estupido comentario

#
#stati = []
#for status in lista:
#    children = []
#    for linea in lista[status]:
#        subchildren = []
#        for clave in lista[status][linea]:
#            subsubchildren = []
#            for concepto in lista[status][linea][clave]:
#                subsubchildren.append( {'name': concepto,
#                                        'size': float(lista[status][linea][clave][concepto])} )
#            subchildren.append( {'name': clave,
#                                 'children': subsubchildren } )
#        children.append( {'name': linea,
#                          'children': subchildren} )
#    stati.append( {'name': status,
#                 'children': children} )
#    
#proyectos = {'name': 'proyectos',
#             'children': stati }
#
#print proyectos
#


La señorita pufi 256 clave de facebook


=======
>>>>>>> 4a93eeb913d6311b14b523bf03cf8916a0bc7c90
