import os
from dotenv import load_dotenv
from cli import inicializar_interface, rodar_menu, error_mensagem
from generator import configurar_cliente

load_dotenv()

def main():
    """
    Função principal que inicia a aplicação.
    """

    inicializar_interface()

    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        
        error_mensagem("GEMINI_API_KEY não encontrada no arquivo .env")
        return
    
    client = configurar_cliente(api_key)

    rodar_menu(client)


if __name__ == "__main__":
    main()