import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

logo = """
                                                             ▄▄                     
▀███▀▀▀███                                                 ▀███                     
  ██    ▀█                                                   ██                     
  ██   █   ▄██▀██▄▀███▄███▀███  ▀███ ▀████████▄█████▄        ██   ▄▄█▀██▀██▀   ▀██▀ 
  ██▀▀██  ██▀   ▀██ ██▀ ▀▀  ██    ██   ██    ██    ██        ██  ▄█▀   ██ ██   ▄█   
  ██   █  ██     ██ ██      ██    ██   ██    ██    ██        ██  ██▀▀▀▀▀▀  ██ ▄█    
  ██      ██▄   ▄██ ██      ██    ██   ██    ██    ██        ██  ██▄    ▄   ███     
▄████▄     ▀█████▀▄████▄    ▀████▀███▄████  ████  ████▄    ▄████▄ ▀█████▀    █      
                                                                                    
                                                                                    
"""

#FORUM CATEGORIES PROGRAMACAO
FORUM_PROGRAMA = """🔥 1. Programação / Desenvolvimento de Software

É o mais procurado no mundo inteiro.
Cursos recomendados:

Análise e Desenvolvimento de Sistemas

Engenharia de Software

Ciência da Computação

O que eles querem que você saiba:

JavaScript/TypeScript

React

Node.js

Python

Banco de dados"""

FORUM_CURSOS_GRATUITOS = """💻 Melhores cursos de programação (Grátis e Pagos) 🚀

🔹 1. DIO.me — Gratuito 🆓
Ótima plataforma para começar, com trilhas bem organizadas e projetos práticos.

🔹 2. Alura — Pago 💰
Cursos completos, didática forte e foco no mercado de trabalho.

🔹 3. Coursera — Pago 💻
Cursos de universidades renomadas com certificados.

🔹 4. Udemy — Pago 🎓
Grande biblioteca de cursos em várias linguagens.

🔹 5. Platforma X — Pago 🎯
Conteúdo focado em desenvolvimento web e mobile.

📌 Observação:
Plataformas online oferecem ótimos cursos tanto gratuitos quanto pagos.
Escolha de acordo com seu nível e objetivos."""

PROTEGER_COOKIES = """**`como proteger cookies temporários`**

**1. Use cookies "HttpOnly"

Isso impede que scripts no navegador (como JavaScript) leiam o cookie.

Apenas o servidor consegue acessar esse cookie.

Exemplo em PHP:**

`setcookie("token", $valorToken, [
    'expires' => time() + 3600,
    'path' => '/',
    'secure' => true,
    'httponly' => true,
    'samesite' => 'Strict'
]);
`

secure → só envia em HTTPS

httponly → impede acesso via JS

samesite → ajuda a evitar ataques CSRF

**2. Criptografia do cookie**

Em vez de colocar dados sensíveis no cookie, coloque um valor criptografado ou token.

No servidor, você decifra para validar a sessão.

Exemplo simples em Python Flask:

`from itsdangerous import URLSafeTimedSerializer

secret_key = "minha_chave_secreta"
serializer = URLSafeTimedSerializer(secret_key)

# Criar cookie
token = serializer.dumps({"user_id": 123})

# Ler cookie
data = serializer.loads(token, max_age=3600)  # Expira em 1h
`

**3. Expiração curta**

Quanto mais curto o tempo de vida, menor o risco de alguém usar o cookie roubado.

**4. Validação de IP ou User-Agent**

No servidor, guarde o IP ou User-Agent da sessão.

Se alguém tentar usar o cookie de outro navegador ou rede, a sessão é invalidada."""

FORUM_ENTRAR_CIBERSEGURANCA = """Perfeito! Então, se você quer entrar no mundo de cibersegurança, é bom ter um caminho bem estruturado. Vou te mostrar um guia organizado, desde fundamentos até práticas avançadas:

1. Fundamentos essenciais

Antes de estudar segurança avançada, você precisa dominar:

Redes: TCP/IP, portas, protocolos (HTTP, HTTPS, DNS, SMTP).

Sistemas operacionais: Linux e Windows.

Programação básica: Python é essencial para scripts de segurança, automação.

Comandos de terminal: Navegação, manipulação de arquivos, logs.

2. Conceitos de segurança

Cookies e sessões: Como funcionam, como são armazenados, vulnerabilidades como XSS.

Autenticação e autorização: Tokens, JWT, OAuth.

Criptografia básica: Hashing (MD5, SHA), criptografia simétrica e assimétrica.

Ataques comuns: Phishing, SQL injection, brute force, MITM (Man in the Middle).

3. Ferramentas de aprendizado prático

Wireshark: Análise de pacotes (educacional).

TryHackMe e Hack The Box: Plataformas práticas de segurança.

Python: Para criar ferramentas de segurança ofensiva ética.

4. Ética e segurança

Nunca teste contas alheias ou sites sem permissão — isso é crime.

Use laboratórios próprios ou simuladores online para praticar.

Aprender segurança ofensiva é sobre proteger sistemas, não prejudicá-los.

5. Próximos passos sugeridos

Aprender Python básico e avançado para automação de tarefas.

Estudar redes com Wireshark.

Montar laboratório local com máquinas virtuais.

Praticar em plataformas como TryHackMe, Hack The Box."""

FORUM_PROXY = """( **COMO CONFIGURAR PROXY NO KALI LINUX**   )

apt-get install proxychains4

sudo nano /etc/proxychains4.conf

random_chain (Ativo)

# defaults set to "tor"
#socks4 127.0.0.1 9050 (Desligado)

(Novo Proxy)
socks5   IP Port
socks5   IP Port
(Etc)

( COMO CONFIGURAR PROXY NO WINDOWS )

ENTRA EM Configurações
VAI A Rede e Internet
É IR EM Proxy

(desativa) Detectar configurações automaticamente

VAI À Usar um servidor de proxy
Configurar

IP do proxy                    Porta

É SALVA

SITE PRA TESTE PROXY :clip: 

Site: https://meuip.com.br/
Site: https://dnsleaktest.com/

sudo apt install tor -y

service tor status
service tor stop"""

FORUM_SSH = """SSH 
-------------------------------------

Linux:

sudo apt install ssh

systemctl status ssh.service

-----------------------------------------------
ssh usuário@IP

(exemplo) ssh admin@192.168.1.100
---------------------------------------------------

Windows:

Use Putty ou OpenSSH

ssh usuário@IP

(exemplo) ssh admin@192.168.1.100"""

#Fim FORUM CATEGORIES PROGRAMACAO

#FORUM CATEGORIES ROTEIROS
FORUM_ROTEIROS = """
📚 Roteiro de Estudos – Metadados
🔹 Nível 1 – Básico (conceito e prática simples)

✔️ O que são metadados (dados sobre dados).
✔️ Tipos de metadados (descritivos, estruturais, administrativos).
✔️ Onde aparecem: imagens, documentos, músicas, vídeos.
✔️ Como ver e remover metadados no Windows e Linux.

👉 Tarefa prática:

Pegue uma foto do celular → veja os metadados no PC → remova e compare.

🔹 Nível 2 – Intermediário (segurança e privacidade)

✔️ Riscos de privacidade (GPS em fotos, autor em documentos).
✔️ Boas práticas antes de compartilhar arquivos.
✔️ Usar ferramentas especializadas como ExifTool.

👉 Tarefa prática:

Baixe um PDF da internet → veja os metadados → descubra quem criou/qual software foi usado.

🔹 Nível 3 – Avançado (uso em investigação e TI)

✔️ Metadados em bancos de dados.
✔️ Metadados em sites (HTML meta tags).
✔️ Metadados em redes (cabeçalhos de pacotes).

👉 Tarefa prática:

Analisar metadados de diferentes tipos de arquivos."""

FORUEM_OQ_SAO_METADADOS = """
O que são metadados?
São basicamente "dados sobre dados". Eles descrevem e dão informações adicionais sobre um arquivo, documento, foto, vídeo ou qualquer outro tipo de dado.

🔎 Exemplos práticos:

Foto no celular: além da imagem em si, ela guarda metadados como a data da foto, modelo da câmera, resolução, localização (se o GPS estiver ativo).

Música/MP3: além do som, o arquivo tem metadados com nome da música, artista, álbum, gênero.

Documento Word/PDF: pode ter autor, data de criação, últimas alterações, versão.

📌 Tipos de metadados

Descritivos → ajudam a identificar (título, autor, palavras-chave).

Estruturais → mostram como os dados estão organizados (páginas de um livro, capítulos de um vídeo).

Administrativos → informações técnicas e de direitos (data de criação, formato, permissões de uso).

⚠️ Por que são importantes?

Ajudam na organização e busca (Google usa metadados para achar páginas certas).

Facilitam compartilhamento e catalogação.

Podem trazer riscos de privacidade (ex.: mandar uma foto com metadados de localização sem querer)."""

FORUM_LIMPAR_METADADOS = """
No Windows

Clique com o botão direito no arquivo → Propriedades.

Vá na aba Detalhes.

Embaixo, clique em Remover Propriedades e Informações Pessoais.

Vai aparecer 2 opções:

Criar uma cópia limpa (sem metadados).

Escolher manualmente quais informações quer apagar (ex.: autor, localização, data).

Salve → pronto, o arquivo vai estar "zerado" de metadados.

🐧 No Linux

No Linux você pode usar ferramentas de terminal:

🔹 Usando exiftool

Instalar:

sudo apt update && sudo apt install libimage-exiftool-perl -y

Para ver metadados:

exiftool arquivo.jpg

Para apagar todos os metadados:

exiftool -all= arquivo.jpg"""

FORUEM_BASE_DE_METADADOS = """
1. Tipos de metadados em arquivos diferentes

Imagens (JPEG, PNG, RAW) → câmera, GPS, data.

Documentos (Word, PDF, Excel) → autor, revisões, comentários, histórico de edição.

Músicas (MP3, FLAC) → álbum, artista, gênero, ano.

Vídeos (MP4, MKV) → codec, resolução, data de gravação.

🛡️ 2. Privacidade

Metadados podem entregar informações pessoais sem você perceber.

Exemplo: Tirar foto em casa e postar → metadados podem revelar coordenadas GPS da sua casa.

Por isso é importante sempre revisar e limpar os metadados antes de compartilhar algo.

⚙️ 3. Ferramentas

ExifTool → extrai e edita metadados.

Mat2 → focado em privacidade e anonimização.

🗂️ 4. Metadados em sistemas

Bancos de dados → usam metadados para descrever tabelas e colunas.

Sites (HTML) → têm metadados nas meta tags que ajudam o Google a indexar.

Arquivos de rede → pacotes de internet têm metadados (cabeçalhos, IP, horários)."""

#Fim FORUM CATEGORIES ROTEIROS

#CATEGORIAS DE FORUMS

#categoria PROGRAMACAO
def programacao_forum():
    print("--- Fórum de Programação / Desenvolvimento de Software ----")
    print("Assuntos disponíveis:")
    print("1 - Guias básicos Programação / Desenvolvimento de Software\n")
    print("2 - Melhores cursos de programação (Grátis e Pagos)\n")
    print("3 - Como proteger cookies temporários\n")
    print("4 - Como entrar na cibersegurança\n")
    print("5 - Como usar proxy no Kali Linux e Windows\n")
    print("6 - Como usar SSH no Linux e Windows\n")

    escolhaspr = input("Qual forum você quer? : ")
    clear()
    if escolhaspr == '1':
        print(FORUM_PROGRAMA)
        input("\nPressione Enter para voltar...")
        clear()
    elif escolhaspr == '2':
        print(FORUM_CURSOS_GRATUITOS)
        input("\nPressione Enter para voltar...")
        clear()
    elif escolhaspr == '3':
        print(PROTEGER_COOKIES)
        input("\nPressione Enter para voltar...")
        clear()
    elif escolhaspr == '4':
        print(FORUM_ENTRAR_CIBERSEGURANCA)
        input("\nPressione Enter para voltar...")
        clear()
    elif escolhaspr == '5':
        print(FORUM_PROXY)
        input("\nPressione Enter para voltar...")
        clear()
    elif escolhaspr == '6':
        print(FORUM_SSH)
        input("\nPressione Enter para voltar...")
        clear()

#categoria ROTEIROS
def roteiros_():
    print("--- Roteiro de Estudos – Metadados ----")
    print("Assuntos disponíveis:")
    print("1 - Guias básicos Roteiro de Estudos – Metadados\n")
    print("2 - O que são metadados?\n")
    print("3 - Como limpar metadados de arquivos\n")
    print("4 - Base de conhecimento sobre metadados\n")

    escolhasr = input("Qual forum você quer? : ")
    clear()
    if escolhasr == '1':
        print(FORUM_ROTEIROS)
        input("\nPressione Enter para voltar...")
        clear()
    elif escolhasr == '2':
        print(FORUEM_OQ_SAO_METADADOS)
        input("\nPressione Enter para voltar...")
        clear()
    elif escolhasr == '3':
        print(FORUM_LIMPAR_METADADOS)
        input("\nPressione Enter para voltar...")
        clear()
    elif escolhasr == '4':
        print(FORUEM_BASE_DE_METADADOS)
        input("\nPressione Enter para voltar...")
        clear()

#fim categorias

def acessar_forum():
    print("--- Acessar o Fórum ---")
    print("Categorias disponíveis:")
    print("1 - Programação / Desenvolvimento de Software")
    print("2 - Roteiro de Estudos – Metadados")
    escolha_categoria = input("Escolha uma categoria: ")
    if escolha_categoria == '1':
        clear()
        programacao_forum()
    elif escolha_categoria == '2':
        clear()
        roteiros_()

while True:
    print(logo)
    print("--- Bem-vindo ao Fórum lev ---------------------------")
    print("1 - Acessar o fórum          |     versão do forum 1.0")
    print("2 - Sair                     |           criado por: ④")
    print("------------------------------------------------------")
    escolhas = input("Escolha uma opção: ")

    clear()

    if escolhas == '1':
        acessar_forum()
    elif escolhas == '2':
        break
    else:
        input("Opção inválida. Pressione Enter para continuar...")
