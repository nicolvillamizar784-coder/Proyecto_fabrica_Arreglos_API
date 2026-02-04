from empleado_modelo import Empleado_modelo
from base_datos import Api_BD 
from Api_BD_maquinas import Api_BD_maqinas
  
#codigo principal
objeto_Api = Api_BD()
objeto_Api_maquinas = Api_BD_maqinas()
objeto_Api_maquinas.imprimir_info()
print(objeto_Api_maquinas.buscar_info())
objeto_empleado = Empleado_modelo("Juan","Perez","12345678","555-1234")
objeto_empleado2= Empleado_modelo("Ana","Gomez","87654321","555-5678")
objeto_empleado3= Empleado_modelo("Luis","Martinez","11223344","555-8765")
objeto_Api.guardar_empleado(objeto_empleado)
objeto_Api.guardar_empleado(objeto_empleado2)
objeto_Api.guardar_empleado(objeto_empleado3)
objeto_Api.imprimir_API()