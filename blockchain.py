from bloco import Bloco


class Blockchain:
    def __init__(self):
        self.chain = []
        self.transacoes_inconfirmadas = []
        self.genesis_bloco()

    def genesis_bloco(self):
        transacoes = []
        genesis_bloco = Bloco(transacoes, "0")
        genesis_bloco.gerar_hash()
        self.chain.append(genesis_bloco)

    def add_bloco(self, transacoes):
        hash_anterior = (self.chain[len(self.chain) - 1]).hash
        new_bloco = Bloco(transacoes, hash_anterior)
        new_bloco.gerar_hash()
        # prova = prova_de_trabalho(bloco)
        self.chain.append(new_bloco)

    def print_blocos(self):
        for i in range(len(self.chain)):
            atual_bloco = self.chain[i]
            print("bloco {} {}".format(i, atual_bloco))
            atual_bloco.print_contents()

    def validar_chain(self):
        for i in range(1, len(self.chain)):
            atual = self.chain[i]
            anterior = self.chain[i - 1]
            if atual.hash != atual.gerar_hash():
                print("Hash atual não equivale ao hash gerado")
                return False
            if atual.hash_anterior != anterior.gerar_hash():
                print("Bloco anterior não alterado")
                return False
        return True

    def prova_de_trabalho(self, bloco, dificuldade=2):
        prova = bloco.gerar_hash()
        while prova[:2] != "0" * dificuldade:
            bloco.nonce += 1
            prova = bloco.gerar_hash()
        bloco.nonce = 0
        return prova
