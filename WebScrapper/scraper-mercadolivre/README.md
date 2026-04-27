🛒 Scraper Mercado Livre
Scraper desenvolvido em Python que pesquisa produtos no Mercado Livre e salva os resultados em uma planilha Excel.

 O que o projeto faz
 
Abre o Mercado Livre automaticamente no navegador
Pesquisa um produto definido no código
Coleta nome, preço e URL de cada produto listado
Salva os dados em um arquivo .xlsx
Tecnologias utilizadas
Selenium — automação do navegador
Pandas — manipulação e exportação dos dados
PyAutoGUI — controle de tempo de espera

▶️ Como executar

Clone o repositório
git clone https://github.com/Higor-Car/scraper-mercadolivre.git
cd scraper-mercadolivre
Instale as dependências
pip install selenium pandas pyautogui openpyxl
Execute o script
python scraper.py
O arquivo notebooks.xlsx será gerado na mesma pasta

📁 Estrutura do projeto

scraper-mercadolivre/
│
├── scraper.py        # Script principal
├── notebooks.xlsx    # Resultado gerado após a execução
└── README.md
