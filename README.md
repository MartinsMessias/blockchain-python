# Blockchain
Sistema simples para estudos sobre blockchain | Simple blockchain system

#### Recursos
- Implementação simples, mas completa, de uma blockchain
- Implementação de prova de trabalho.

### Exemplo de uso

```
from blockchain import Blockchain

b1_transacoes = {"sender":"Alice", "receiver": "Bob", "amount":"50"}
b2_transacoes = {"sender": "Bob", "receiver":"Cole", "amount":"25"}
b3_transacoes = {"sender":"Alice", "receiver":"Cole", "amount":"35"}
fk_transacoes = {"sender": "Bob", "receiver":"Cole, Alice", "amount":"25"}

local_blockchain = Blockchain()
local_blockchain.print_blocos()

local_blockchain.add_bloco(b1_transacoes)
local_blockchain.add_bloco(b2_transacoes)
local_blockchain.add_bloco(b3_transacoes)
local_blockchain.print_blocos()
local_blockchain.chain[2].transactions = fk_transacoes
local_blockchain.validar_chain()
```
