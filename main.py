import dns.resolver
import socket

print("Verificador de DNS e HTTPS")

dominio = input("Digite um domínio, como example.com: ").strip()

if not dominio:
    print("Você precisa informar um domínio.")
else:
    print(f"Consultando Registros A de: {dominio}")

    try:
        resposta = dns.resolver.resolve(
            dominio,
            "A",
            lifetime=5,
            search=False
        )
        print("Consulta realizada com sucesso.")

        for registro in resposta:
            print(f"Registro A encontrado: {registro.address}")

        print(f"TTL: {resposta.rrset.ttl} segundos")
        
    except dns.resolver.NXDOMAIN:
        print("O DNS respondeu que o nome consultado não existe.")

    except dns.resolver.NoAnswer:
        print("O DNS respondeu, mas não retornou registros do tipo A.")

    except dns.exception.Timeout:
        print("Não foi possível obter uma resposta dentro do prazo.")

    except dns.resolver.NoNameservers as erro:
        print("Os servidores DNS consultados não forneceram uma resposta utilizável.")
        print(f"Detalhes: {erro}")

    except dns.exception.DNSException as erro:
        print(f"Ocorreu outro erro na consulta DNS: {erro}")