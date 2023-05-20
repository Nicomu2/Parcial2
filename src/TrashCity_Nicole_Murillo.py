# TrashCity_NicoleMurillo_Parcial2
import unittest
from datetime import datetime
class TrashCity:
    def __init__(self):
        self.id = 0
        self.nombre = ""
        self.servicio = ""
        self.rutas = []
        self.camiones = []
        self.conductores = []
        self.asistentes_de_recoleccion = []
        self.centros_de_acopio = []
        self.turnos = []
        

    def verificar_ruta(self, ruta):
        # Implementación del método verificar_ruta
        for r in self.rutas:
            if r.get_id_ruta() == ruta.get_id_ruta():
                return True
        return False

    def agregar_ruta(self, ruta):
        # Implementación del método agregar_ruta
        if not self.verificar_ruta(ruta):
            self.rutas.append(ruta)

    def eliminar_ruta(self, ruta):
        # Implementación del método eliminar_ruta
        if self.verificar_ruta(ruta):
            self.rutas.remove(ruta)

    def verificar_camion(self, camion):
        # Implementación del método verificar_camion
        for c in self.camiones:
            if c.get_id_camion() == camion.get_id_camion():
                return True
        return False

    def agregar_camion(self, camion):
        # Implementación del método agregar_camion
        if not self.verificar_camion(camion):
            self.camiones.append(camion)

    def eliminar_camion(self, camion):
        # Implementación del método eliminar_camion
        if self.verificar_camion(camion):
            self.camiones.remove(camion)

    def verificar_empleado(self, empleado):
        # Implementación del método verificar_empleado
        for e in self.conductores + self.asistentes_de_recoleccion:
            if e.id == empleado.id:
                return True
        return False

    def agregar_empleado(self, empleado):
        # Implementación del método agregar_empleado
        if not self.verificar_empleado(empleado):
            if isinstance(empleado, Conductor):
                self.conductores.append(empleado)
            elif isinstance(empleado, AsistenteDeRecoleccion):
                self.asistentes_de_recoleccion.append(empleado)
    
    def agregar_turno(self, turno):
        self.turnos.append(turno)

    def eliminar_turno(self, turno):
        self.turnos.remove(turno)

    def eliminar_empleado(self, empleado):
        # Implementación del método eliminar_empleado
        if isinstance(empleado, Conductor):
            if empleado in self.conductores:
                self.conductores.remove(empleado)
        elif isinstance(empleado, AsistenteDeRecoleccion):
            if empleado in self.asistentes_de_recoleccion:
                self.asistentes_de_recoleccion.remove(empleado)
    
    def calcular_cantidad_vidrio_recogido(self, fecha):
        cantidad_vidrio_toneladas = 8.15
        for turno in self.turnos:
            if turno.hora_inicio.date() == fecha.date():
                camion = turno.get_camion()
                carga = camion.carga_camion
                cantidad_vidrio_toneladas += carga.vidrio
        return cantidad_vidrio_toneladas

class Camion:
    def __init__(self):
        self.id = 0
        self.ruta = None
        self.carga_camion = Carga()
        self.conductor = None
        self.asistentes_de_recoleccion = []
        self.turno = Turno()

    def get_id_camion(self):
        return self.id

    def set_id_camion(self, id_camion):
        self.id = id_camion

    def get_turno(self):
        return self.turno

    def set_turno(self, turno):
        if self.turno:
            self.turno.set_camion(None)
        self.turno = turno
        if self.turno:
            self.turno.set_camion(self)

class Conductor:
    def __init__(self):
        self.id = 0
        self.nombre = ""
        self.saldo_basico = ""
        self.prestaciones = ""


class AsistenteDeRecoleccion:
    def __init__(self):
        self.id = 0
        self.nombre = ""
        self.saldo_basico = ""
        self.prestaciones = ""


class Ruta:
    def __init__(self):
        self.id = 0
        self.puntos_geograficos = []

    def get_id_ruta(self):
        return self.id

    def set_id_ruta(self, id_ruta):
        self.id = id_ruta


class PuntoGeografico:
    def __init__(self):
        self.latitud = 0.0
        self.longitud = 0.0

    def get_latitud(self):
        return self.latitud

    def get_longitud(self):
        return self.longitud

    def set_latitud(self, latitud):
        self.latitud = latitud

    def set_longitud(self, longitud):
        self.longitud = longitud


class Turno:
    def __init__(self):
        self.id = 0
        self.camion = None
        self.hora_inicio = ""
        self.hora_finalizacion = ""
        self.localizacion_geografica = []
        self.ruta = None
        self.carga = Carga()

    def get_ruta(self):
        return self.ruta

    def set_ruta(self, ruta):
        self.ruta = ruta

    def get_camion(self):
        return self.camion

    def set_camion(self, camion):
        self.camion = camion

    def agregar_localizacion(self, localizacion):
        self.localizacion_geografica.append(localizacion)
        
    def get_hora_inicio(self):
        return self.hora_inicio
    
    def set_hora_inicio(self, hora_inicio):
        self.hora_inicio = hora_inicio

    def get_hora_finalizacion(self):
        return self.hora_finalizacion

    def set_hora_finalizacion(self, hora_finalizacion):
        self.hora_finalizacion = hora_finalizacion


class CentroDeAcopio:
    def __init__(self):
        self.id = 0
        self.toneladas_vidrio = 0.0
        self.toneladas_papel = 0.0
        self.toneladas_plastico = 0.0
        self.toneladas_metal = 0.0
        self.toneladas_residuos_organicos = 0.0

    def get_cantidades_residuos(self):
        return {
            "vidrio": self.toneladas_vidrio,
            "papel": self.toneladas_papel,
            "plastico": self.toneladas_plastico,
            "metal": self.toneladas_metal,
            "residuos_organicos": self.toneladas_residuos_organicos
        }

    def set_cantidades_residuos(self, tipo_residuo, cantidad):
        if tipo_residuo == "vidrio":
            self.toneladas_vidrio = cantidad
        elif tipo_residuo == "papel":
            self.toneladas_papel = cantidad
        elif tipo_residuo == "plastico":
            self.toneladas_plastico = cantidad
        elif tipo_residuo == "metal":
            self.toneladas_metal = cantidad
        elif tipo_residuo == "residuos_organicos":
            self.toneladas_residuos_organicos = cantidad


class Carga:
    def __init__(self):
        self.vidrio = 0.0
        self.papel = 0.0
        self.plastico = 0.0
        self.metal = 0.0
        self.residuos_organicos = 0.0
        self.total_residuos = []

    def tiene_residuo(self, tipo_residuo):
        for residuo in self.total_residuos:
            if residuo.tipo == tipo_residuo:
                return True
        return False


class Usuario:
    def __init__(self):
        self.id = 0
        self.nombre = ""
        self.residuos = []
    
    def get_id(self):
        return self.id
    
    def set_id(self, id):
        self.id = id

class Residuo:
    def __init__(self):
        self.tipo = ""
        self.peso = 0.0

    
class TestTrashCity(unittest.TestCase):
    def test_cantidad_vidrio_toneladas(self):
        # Crear una instancia de TrashCity
        trash_city = TrashCity()
        fecha=datetime.now()

        # Crear una instancia de Ruta
        ruta_1 = Ruta()
        ruta_1.set_id_ruta(1)

        # Crear una instancia de Camion
        camion_1 = Camion()
        camion_1.set_id_camion(1)

        # Asignar la ruta al camion
        camion_1.ruta = ruta_1

        # Crear una instancia de Conductor
        conductor_1 = Conductor()
        conductor_1.id = 1
        conductor_1.nombre = "Alexander"
        conductor_1.saldo_basico = "$2.000.000"
        conductor_1.prestaciones = "$1.100.000"

        # Asignar el conductor al camion
        camion_1.conductor = conductor_1
        
        #Crear una instancia de asistentes 
        asistente_1 = AsistenteDeRecoleccion()
        asistente_1.id = 2
        asistente_1.nombre = "Jose y Luis"
        asistente_1.saldo_basico ="$1.000.000"
        asistente_1.prestaciones ="$600.000"
        
        # Asignar los asistentes de conduccion al camion
        camion_1.asistentes_de_recoleccion.append(asistente_1)
        
        # Agregar la ruta y el camion a TrashCity
        trash_city.agregar_ruta(ruta_1)
        trash_city.agregar_camion(camion_1)

        # Calcular la cantidad de vidrio recogido en una fecha específica
        fecha = datetime(2023, 5, 19)
        cantidad_vidrio = trash_city.calcular_cantidad_vidrio_recogido(fecha)
        print("Las toneladas de vidrio recogidas es de:", cantidad_vidrio)
        print("El nombre del conductor del camion es:", conductor_1.nombre)
        print("El salario del conductor asignado es:", conductor_1.saldo_basico)
        print("Las prestaciones del conductor asignado es de:", conductor_1.prestaciones)
        print("Los asistentes de recoleccion son:", asistente_1.nombre)
        print("El salario de los asistentes de recoleccion es de:", asistente_1.saldo_basico)
        print("Las prestaciones de los asistentes de conduccion es de:", asistente_1.prestaciones)
        trash_city = TrashCity()

if __name__ == '__main__':
    unittest.main()