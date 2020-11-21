"""
def estatistica(self, dia: str, agencia: str, flag: str) -> dict:
    estatistica: Dict[str, Union[List[str], str, int]] = {}
    if flag != 'detail':
        estatistica[f'{agencia} - {dia}'] = len(self.clientes_atendidos)
    else:
        estatistica['dia'] = dia
        estatistica['agencia'] = agencia
        estatistica['clientes atendidos'] = self.clientes_atendidos
        estatistica['quantidade de clientes atendidos'] = (
            len(self.clientes_atendidos)
        )
    return estatistica
"""
