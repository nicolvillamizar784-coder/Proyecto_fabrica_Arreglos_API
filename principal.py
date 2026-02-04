from Base_datos_empleados import Base_datos_empleados
from Empleado_modelo import Empleado_modelo


#creo la base de datos de empleados
obj_db_empleado_lista = Base_datos_empleados()
#creo el objeto que voy a guardar
obj_empleado1 = Empleado_modelo("Juan", "Perez", "123456789")
obj_empleado2 = Empleado_modelo("Ana", "Gomez", "987654321")


#creo una lista para guardar masivamente
lista_nuevos_empleados = [obj_empleado2, obj_empleado1]

#llamo al metodo para guardar el empleado
obj_db_empleado_lista.guardar_empleado(obj_empleado1)
obj_db_empleado_lista.guardar_empleado(obj_empleado2)

obj_db_empleado_lista.extender_varios_empleados(lista_nuevos_empleados)

#limpiar toda la lista de empleados
obj_db_empleado_lista.imprimir_info()