# Verificador de DNS e HTTPS

Projeto de estudo em Python voltado à automação de diagnósticos de infraestrutura.

Atualmente, consulta registros DNS do tipo A, apresenta os endereços IPv4
retornados e o TTL, com tratamento de erros de resolução.

A verificação de certificados HTTPS está planejada para as próximas etapas.

## Executar no Linux

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python main.py
```
