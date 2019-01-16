import datetime
from hashlib import sha256


# Dados alterados para transações

class Bloco:
    def __init__(self, transacoes, hash_anterior):
        self.carimbo_de_hora = datetime.datetime.now()
        self.transacoes = transacoes
        self.hash_anterior = hash_anterior
        self.nonce = 0
        self.hash = self.gerar_hash()

    def gerar_hash(self):
        bloco_header = str(self.carimbo_de_hora) + str(self.transacoes) + str(self.hash_anterior) + str(self.nonce)
        bloco_hash = sha256(bloco_header.encode())
        return bloco_hash.hexdigest()

    def print_conteudo(self):
        print("Carimbo de hora:", self.carimbo_de_hora)
        print("Transacoes:", self.transacoes)
        print("Hash atual:", self.gerar_hash())
        print("Hash anterior:", self.hash_anterior)
