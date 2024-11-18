pipeline {
    agent any

    // Configuração do agendamento
    triggers {
        cron('0 8 * * 1-5')
    }

    environment {
        // Define o caminho para o log historico 
        LOG_FILE = '/Users/wagneroliveira/Documents/Jenkins_Python/ConsultaMercadoLivre/automacao.log'
        SCRIPT_FILE = '/Users/wagneroliveira/Documents/Jenkins_Python/ConsultaMercadoLivre/Consulta_MercadoLivre.py'
        REQUIREMENTS_FILE = '/Users/wagneroliveira/Documents/Jenkins_Python/ConsultaMercadoLivre/requirements.txt'
    }

    stages {
        stage('Preparar Ambiente') {
            steps {
                echo "Instalando dependências..."
                sh '''
                    python3 -m venv venv
                    source venv/bin/activate
                    pip install --upgrade pip
                    pip install -r ${REQUIREMENTS_FILE}
                '''
            }
        }

        stage('Automação em Andamento') {
            steps {
                echo "Em andamento..."
                script {
                    try {
                        sh '''
                            source venv/bin/activate
                            python ${SCRIPT_FILE}
                        '''
                    } catch (Exception e) {
                        echo "Erro ao executar o script: ${e}"
                        error("Falha no script")
                    }
                }
            }
        }

        stage('Salvando Log de execução') {
            steps {
                echo "Arquivando logs de execução..."
                archiveArtifacts artifacts: "${LOG_FILE}", allowEmptyArchive: true
            }
        }

        stage('Resultados') {
            steps {
                echo "Processo concluído. Verifique os logs para detalhes de execução e erros, se houver."
            }
        }
    }

    post {
        always {
            echo 'Resetando Workspace'
            deleteDir() // Limpa o workspace após a execução
        }
        failure {
            echo 'Execução falhou. Verifique os logs para mais detalhes.'
        }
    }
}
