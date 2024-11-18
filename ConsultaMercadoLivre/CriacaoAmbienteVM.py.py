import subprocess
import os
import sys

def setup_virtualenv(requirements_path='requirements.txt', env_name='venv'):
    # Cria o ambiente virtual
    subprocess.run([sys.executable, "-m", "venv", env_name])
    print(f"Ambiente virtual '{env_name}' criado.")

    # Determina o caminho para o ativador dependendo do sistema operacional
    activate_script = f"{env_name}/bin/activate" if os.name != "nt" else f"{env_name}\\Scripts\\activate"

    # Instala os pacotes do requirements.txt
    try:
        # Executa o pip install no ambiente virtual
        subprocess.run(f"source {activate_script} && pip install -r {requirements_path}", shell=True, check=True)
        print("Bibliotecas instaladas a partir do requirements.txt.")
    except subprocess.CalledProcessError:
        print("Erro ao instalar as bibliotecas. Verifique o arquivo requirements.txt e tente novamente.")

# Caminho para o arquivo requirements.txt (pode ser ajustado se necessário)
requirements_file = '/Users/wagneroliveira/Documents/Jenkins_Python/ConsultaMercadoLivre/requirements.txt'

# Chama a função para configurar o ambiente virtual
setup_virtualenv(requirements_file)
