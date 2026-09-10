class Paciente:
    def _init_(self,rut:str,nombre:str, edad:int, prevision:str):
        self.rut=rut
        self.nombre=nombre
        self.edad=edad
        self.self.prevision=prevision

        @property
        def rut(self)->str:
            return self._rut

        @rut.setter
        def rut(self,rut:str):
            self._rut = rut