class Control:
    def __init__(self):
        self._tv=None
    
    def turnOn(self):
        self._tv.turnOn()

    def turnOff(self):
        self._tv.turnOff()

    def canalUp(self):
        self._tv.canalUp()

    def canalDown(self):
        self._tv.canalDown()

    def volumenUp(self):
        self._tv.volumenUp()

    def volumenDown(self):
        self._tv.volumenDown()

    def setCanal(self,n_canal):
        self._tv.setCanal(n_canal)


    def enlazar(self,tele):
        self._tv=tele
        self._tv.setControl(self)
    
    def getTv(self):
        return self._tv

    def setTv(self,n_tv):
        self._tv=n_tv
