# Automação de Cadastro de Produtos  

Este projeto utiliza **Python** e a biblioteca **pyautogui** para automatizar o processo de cadastro de produtos em um sistema web. O script realiza interações com a interface gráfica do usuário (UI), inserindo dados de um arquivo CSV em campos específicos do sistema.

## Pré-requisitos  

Antes de executar o código, verifique se você tem os seguintes requisitos instalados:  
- Python 3.7 ou superior  
- Bibliotecas Python necessárias:  
  - `pyautogui` (automatização da UI)  
  - `pandas` (manipulação de dados)  
  - `openpyxl` (leitura de arquivos Excel, caso necessário)  

Instale as dependências executando:  
```bash
pip install pyautogui pandas openpyxl
```

## Como usar  

1. **Prepare o arquivo CSV**  
   Crie um arquivo chamado `produtos.csv` com as colunas:  
   - `codigo`  
   - `marca`  
   - `tipo`  
   - `categoria`  
   - `preco_unitario`  
   - `custo`  
   - `obs` (opcional)  

   Exemplo de conteúdo do CSV:  
   ```csv
   codigo,marca,tipo,categoria,preco_unitario,custo,obs
   101,MarcaA,ProdutoX,Categoria1,25.00,15.00,"Produto novo"
   102,MarcaB,ProdutoY,Categoria2,50.00,30.00,""
   ```

2. **Configuração do ambiente**  
   - Certifique-se de que o sistema da empresa está acessível no link:  
     `https://dlp.hashtagtreinamentos.com/python/intensivao/login`  
   - Atualize o código com suas credenciais de login.  

3. **Execute o script**  
   Salve o script Python em um arquivo (`automacao_cadastro.py`, por exemplo) e execute no terminal:  
   ```bash
   python automacao_cadastro.py
   ```

4. **Aguarde a conclusão**  
   O script abrirá o navegador, fará login no sistema, buscará os dados no CSV e realizará o cadastro dos produtos.

## Notas importantes  

- **Coordenadas da tela:**  
  Certifique-se de que as coordenadas de clique (x, y) estão ajustadas para o seu monitor. Caso necessário, utilize o seguinte comando para capturar as coordenadas:  
  ```python
  pyautogui.position()
  ```  

- **Segurança:**  
  Evite deixar suas credenciais de login diretamente no código. Considere usar variáveis de ambiente ou ferramentas de gerenciamento de segredos.

- **Tempo de espera:**  
  Se o sistema for mais lento para carregar, aumente os tempos de espera (`time.sleep`) conforme necessário.  

## Melhorias futuras  

- Implementar login automatizado com autenticação segura.  
- Ajustar o script para diferentes resoluções de tela.  
- Adicionar suporte a outros formatos de entrada (como Excel).  

## Contribuição  

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests com melhorias ou correções.

## Contato

Caso tenha dúvidas ou sugestões, entre em contato:

- **E-mail**: lialilinbox@gmail.com
- **GitHub**: https://github.com/liapsps/
