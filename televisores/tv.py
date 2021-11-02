class tv:
    _numTV=0
    def __init__(self,marca,estado):
        self._marca=marca
        self._canal=1
        self._precio=500
        self._estado=estado
        self._volumen=1
        self._control=None
        self._numTV+=1
        
    
    def getMarca(self):
        return self._marca
    
    def getControl(self):
        return self._control
    
    def getPrecio(self):
        return self._precio
    
    def getVolumen(self):
        return self._volumen

    def getCanal(self):
        return self._canal
    
    def setMarca(self,n_marca):
        self._marca=n_marca

    def setControl(self,n_control):
        self._control=n_control
    
    def setPrecio(self,n_precio):
        self._precio=n_precio
    
    def setVolumen(self,n_volumen):
        if ((self._estado==True) and (n_volumen>=0 and n_volumen<=7)):
            self._volumen=n_volumen
    def setCanal(self,n_canal):
        if ((self._estado==True) and (n_canal>=1 and n_canal<=120)):
            self._canal=n_canal
    
    @classmethod
    def getNumTV(cls):
        return cls._numTV
    
    @classmethod
    def setNumTV(cls,n_num):
        cls._numTV=n_num

    def turnOn(self):
        self._estado=True
    
    def turnOff(self):
        self._estado=False

    def getEstado(self):
        return self._estado

    def canalUp(self):
        if (self._estado==True):
            if self._canal!=120:
                self._canal+=1
    
    def canalDown(self):
        if (self._estado==True):
            if self._canal!=1:
                self._canal-=1

    def volumenUp(self):
        if (self._estado==True):
            if self._volumen!=7:
                self._volumen+=1
    
    def volumenDown(self):
        if (self._estado==True):
            if self._volumen!=0:
                self._volumen-=1
