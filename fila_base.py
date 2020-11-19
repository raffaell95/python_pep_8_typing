class FilaBase:
    codigo: int = 0
    fila = []
    clientesatendidos = []
    senhaatual: str = ''

    def resetafila(self) -> None:
        if self.codigo >= 100:
            self.codigo = 0
        else:
            self.codigo += 1
