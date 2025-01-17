# 🤖 Automação em Python: Login e Cadastro de Produtos 🛠️  

Este projeto é o meu primeiro passo no mundo da automação! 🚀 Ele utiliza Python para:  

1. 🔍 **Pesquisar no Google**: Automatiza a busca pelo sistema.  
2. 🔑 **Login Automatizado**: Preenche as credenciais e faz login automaticamente.  
3. 🛒 **Cadastro de Produtos**: Lê uma base de dados e cadastra automaticamente os produtos no sistema, sem precisar cadastrar um por um!  

---

## 🛠️ Tecnologias Utilizadas  

- **Python** 🐍  
- **Bibliotecas**:  
  - `pyautogui` para automação de cliques e teclas. 🖱️⌨️  
  - `time` para controle de tempo entre ações. ⏳  
  - `pandas` para leitura e manipulação de bases de dados. 📊  

---

## 📋 Pré-requisitos  

1. **Instale o Python** 🐍:  
   Certifique-se de ter o Python 3.8 ou superior instalado em sua máquina.  
   Você pode baixar [aqui](https://www.python.org/downloads/).  

2. **Instale as bibliotecas necessárias**:  
   Execute o comando abaixo para instalar as dependências:  
   ```bash
   pip install pyautogui pandas
   ```  

3. **Prepare a base de dados**:  
   - O script usa um arquivo `.csv` como base de dados para os produtos.  
   - Certifique-se de ter um arquivo similar ao exemplo utilizado
---

### 4. O que acontece:  
- O script irá:  
  1. Abrir o navegador e buscar o sistema no Google.  
  2. Realizar o login automaticamente (você pode configurar suas credenciais no código).  
  3. Cadastrar cada produto da base de dados no sistema, usando `pyautogui` para automação de cliques e preenchimento de campos.  

---

## 📝 Aprendizados  

- Automação de tarefas repetitivas com `pyautogui`.  
- Controle de tempo e espera usando `time.sleep()`.  
- Manipulação de arquivos CSV com `pandas`.  

---

## ⚠️ Observações  

1. **Configuração de Resolução**:  
   - O `pyautogui` funciona com base nas coordenadas de tela. Certifique-se de ajustar as coordenadas no código para a sua resolução.  

2. **Teste Antes de Rodar em Produção**:  
   - Verifique as coordenadas e os tempos configurados para evitar cliques em locais incorretos.  

---

## 📬 Contato  

Se tiver dúvidas ou sugestões, sinta-se à vontade para entrar em contato comigo:  
📧 [Meu Email](liyelaguiar57@gmail.com)  

💖 Obrigada por visitar meu repositório! Espero que este projeto possa inspirar ou ajudar de alguma forma. 🚀✨  
