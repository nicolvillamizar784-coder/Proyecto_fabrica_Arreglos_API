from Base_datos_empleados import Base_datos_empleados
from Empleado_modelo import Empleado_modelo
from diccionario import datos_diccionario

#creo la base de datos de empleados
obj_db_empleado_lista = Base_datos_empleados()
#creo el objeto que voy a guardar
obj_empleado1 = Empleado_modelo("sebastian", "contreras", "123455689")
obj_empleado2 = Empleado_modelo("natalia", "quintero", "9879894321")


#creo una lista para guardar masivamente
lista_nuevos_empleados = [obj_empleado2, obj_empleado1]

#llamo al metodo para guardar el empleado
obj_db_empleado_lista.guardar_empleado(obj_empleado1)
obj_db_empleado_lista.guardar_empleado(obj_empleado2)

obj_db_empleado_lista.extender_varios_empleados(lista_nuevos_empleados)

#limpiar toda la lista de empleados

obj_db_empleado_lista.imprimir_info()
obj_diccionario = datos_diccionario()
info = obj_diccionario.sacar_valores()
print(info)


nuevo_diccionario = {"1093687321": {"nombre":"marcos", "apellido": "rosales", "maquina": ("maquina pinturas",
"maquina hidraulica")}}

obj_diccionario.acttualizar_info(nuevo_diccionario)
obj_diccionario.imprimir_info()
