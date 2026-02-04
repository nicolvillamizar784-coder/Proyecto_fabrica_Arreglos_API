class Base_datos_empleados:
    def _init_(self):
        #este es un array
        self.db_empleados_lista = []
        
    def guardar_empleado(self, obj_empleado):
        self.db_empleados_lista.append(obj_empleado)
        return True

    def extender_varios_empleados(self, varios_obj):
        self.db_empleados_lista.extend(varios_obj)
        
    def imprimir_info(self):
        for i in range(len(self.db_empleados_lista)):
            print(self.db_empleados_lista[i].ver_info_empleado())