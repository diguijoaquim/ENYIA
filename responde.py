
import requests
class Responder:
    def responder_chat(p):
        if "harley" in p:
            return "Herlay è uma chatbot de inteligencia artificial criado pela a equipa Mtevolution , um grupo mocambicano"
        elif "diqui" in p:
            return "Se esta falar de Dique joaquim , ele é um jovem mocambicano  com um talento muito grande na programacao . Ele è do norte do pais em Niassa tem uma equipa em Maputo e angola"
        elif "danca" and "ouro" in p:
            return "A danca de ouro è um tipo de danca que um Repper Moçambicano ,Lil wayne de moz inventou ,Neste caso nao tenho mais informacoes sobre a danca"
        elif "quem" and "criou" in p:
            return "Fui criado por Diqui joaquim simplesmente ghost404 ,ele é um dos programadores da Mt evolution o grupo fundado por jose em Maputo."
        elif "membros" and "evolution" in p:
            return "Claro, aqui estao os membros da mt evolution.  Jose,Sandino, Dique, Jorge Claro que podem existir outos mas nao tenho acesso a informaçao em tempo real."
        if "kkkk" in p:
            return "Hehehe, fico feliz em saber que tas feliz"
        else:
            API_BASE_URL = "https://afriaconect.onrender.com"
            def connect_to_api(data):
                try:
                    response = requests.post(f"{API_BASE_URL}/backend-api/v2/conversation", json=data)
                    response.raise_for_status()
                    return response.json()
                except requests.exceptions.RequestException as e:
                    print(f"Erro ao conectar à API: {str(e)}")
                    return str(e)
            data = {
    "conversation_id": "12345",  # Substitua pelo ID da conversação desejada
    "jailbreak": "default",  # Substitua pelo tipo de jailbreak desejado
    "meta": {
        "content": {
            "conversation": [
                {
                    "role": "system",
                    "content": "escreva a personalidade aqui" #aqui escreva a personalidade
                }
            ],
            "internet_access": True,
            "parts": [
                {
                    "role": "system",
                    "content": "ola"
                        }
            ]
        }
    }
}
            resposta = connect_to_api(data)
            if resposta:
                return resposta
            else:
                return  resposta+"Temos um problema , aguarde um pouco😌"