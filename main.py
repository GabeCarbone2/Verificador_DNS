import dns.resolver
import dns.exception

print("Verificador de DNS e HTTPS")

dominio = input("Digite um domínio, como example.com: ").strip()

if not dominio:
    print("Você precisa informar um domínio.")
else:
    tipos_registros = ["A", "AAAA"]

    for tipo in tipos_registros:
        try:
            resposta = dns.resolver.resolve(
                dominio,
                tipo,
                lifetime=5,
                search=False
            )
            print(f"Consulta de registro {tipo} realizada com sucesso.")

            for registro in resposta:
                if tipo == "A":
                    print(f"Registro A encontrado: {registro.address}")
                elif tipo == "AAAA":
                    print(f"Registro AAAA encontrado: {registro.address}")

            print(f"TTL: {resposta.rrset.ttl} segundos")

        except dns.resolver.NXDOMAIN:
            print(f"O DNS respondeu que o nome consultado não existe para o tipo {tipo}.")

        except dns.resolver.NoAnswer:
            print(f"O DNS respondeu, mas não retornou registros do tipo {tipo}.")

        except dns.exception.Timeout:
            print(f"Não foi possível obter uma resposta dentro do prazo para o tipo {tipo}.")

        except dns.resolver.NoNameservers as erro:
            print(f"Os servidores DNS consultados não forneceram uma resposta utilizável para o tipo {tipo}.")
            print(f"Detalhes: {erro}")

        except dns.exception.DNSException as erro:
            print(f"Ocorreu outro erro na consulta DNS para o tipo {tipo}: {erro}")
