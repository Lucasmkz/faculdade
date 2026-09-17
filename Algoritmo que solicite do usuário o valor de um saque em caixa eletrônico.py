<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <!-- Item 4: Título e Ícone da Aba (Favicon) -->
  <title>Projeto Prático</title>
  <link rel="icon" href="img/favicon.ico" type="image/x-icon">
  
  <!-- Item 3: Arquivo CSS externo -->
  <link rel="stylesheet" href="css/styles.css">
</head>
<body>

  <!-- Item 5: Barra de Navegação Centralizada com Hover -->
  <nav class="navbar">
    <ul>
      <li><a href="#inicio">Início</a></li>
      <li><a href="#sobre">Sobre</a></li>
      <li><a href="#tabela">Tabela</a></li>
      <li><a href="#contato">Contato</a></li>
    </ul>
  </nav>

  <!-- Item 6: Barra Horizontal em 100% da Largura -->
  <div class="full-width-bar"></div>

  <!-- Container Principal das Seções -->
  <main class="container">

    <!-- Item 7: Cabeçalho Descolado da Janela e Centralizado (2 Colunas) -->
    <header class="header-section">
      <div class="col-left">
        <h1>Título Principal</h1>
        <h3>Subtítulo da Seção</h3>
        <p>Este é um parágrafo descritivo do cabeçalho da página.</p>
        <a href="#" class="btn">Saiba Mais</a>
      </div>
      <div class="col-right">
        <img src="img/logo.png" alt="Imagem do Cabeçalho">
      </div>
    </header>

    <!-- Item 8: Cartões Descolados (3 Colunas) -->
    <section class="cards-section">
      <div class="card">
        <h3>Cartão 1</h3>
        <img src="img/logo.png" alt="Card 1">
        <p>Descrição do primeiro cartão com detalhes.</p>
        <a href="#">Link 1</a>
      </div>
      <div class="card">
        <h3>Cartão 2</h3>
        <img src="img/logo.png" alt="Card 2">
        <p>Descrição do segundo cartão com detalhes.</p>
        <a href="#">Link 2</a>
      </div>
      <div class="card">
        <h3>Cartão 3</h3>
        <img src="img/logo.png" alt="Card 3">
        <p>Descrição do terceiro cartão com detalhes.</p>
        <a href="#">Link 3</a>
      </div>
    </section>

    <!-- Item 9: Tabela com Fundo 100% da Largura e Matriz 4x5 -->
    <section class="table-section">
      <div class="table-container">
        <h2>Tabela de Dados</h2>
        <table>
          <thead>
            <tr>
              <th>Cabeçalho 1</th>
              <th>Cabeçalho 2</th>
              <th>Cabeçalho 3</th>
              <th>Cabeçalho 4</th>
              <th>Cabeçalho 5</th>
            </tr>
          </thead>
          <tbody>
            <tr><td>Dado 1.1</td><td>Dado 1.2</td><td>Dado 1.3</td><td>Dado 1.4</td><td>Dado 1.5</td></tr>
            <tr><td>Dado 2.1</td><td>Dado 2.2</td><td>Dado 2.3</td><td>Dado 2.4</td><td>Dado 2.5</td></tr>
            <tr><td>Dado 3.1</td><td>Dado 3.2</td><td>Dado 3.3</td><td>Dado 3.4</td><td>Dado 3.5</td></tr>
            <tr><td>Dado 4.1</td><td>Dado 4.2</td><td>Dado 4.3</td><td>Dado 4.4</td><td>Dado 4.5</td></tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- Item 10: Formulário Descolado, Centralizado e Largura 25% -->
    <section class="form-section">
      <div class="form-container">
        <h2>Fale Conosco</h2>
        <p>Preencha os campos abaixo para entrar em contato.</p>
        <form id="contactForm">
          <label for="nome">Nome:</label>
          <input type="text" id="nome" name="nome" required>

          <label for="email">E-mail:</label>
          <input type="email" id="email" name="email" required>

          <label for="mensagem">Mensagem:</label>
          <textarea id="mensagem" name="mensagem" rows="4" required></textarea>

          <button type="submit">Enviar</button>
        </form>
      </div>
    </section>

  </main>

  <!-- Item 3: Arquivo JS externo -->
  <script src="js/script.js"></script>
</body>
</html>


* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: Arial, sans-serif;
  background-color: #f4f4f9;
  color: #333;
}

/* Item 5: Barra de Navegação Centralizada com Hover */
.navbar {
  background-color: #2c3e50;
  display: flex;
  justify-content: center;
  padding: 15px 0;
}

.navbar ul {
  display: flex;
  list-style: none;
  gap: 20px;
}

.navbar a {
  color: #fff;
  text-decoration: none;
  padding: 8px 16px;
  transition: background-color 0.3s;
}

.navbar a:hover {
  background-color: #34495e;
  border-radius: 4px;
}

/* Item 6: Barra Horizontal em 100% da Largura da Tela */
.full-width-bar {
  width: 100%;
  height: 8px;
  background-color: #e74c3c;
}

/* Container para descolar elementos da borda da janela */
.container {
  max-width: 1100px;
  margin: 30px auto;
  padding: 0 20px;
}

/* Item 7: Cabeçalho Descolado (2 Colunas) */
.header-section {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #fff;
  padding: 30px;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  margin-bottom: 30px;
}

.col-left {
  flex: 1;
  padding-right: 20px;
}

.col-left h1 { margin-bottom: 10px; }
.col-left h3 { margin-bottom: 10px; color: #7f8c8d; }
.col-left p { margin-bottom: 15px; }
.col-left a.btn {
  display: inline-block;
  padding: 10px 15px;
  background-color: #3498db;
  color: #fff;
  text-decoration: none;
  border-radius: 4px;
}

.col-right {
  flex: 1;
  text-align: center;
}

.col-right img {
  max-width: 100%;
  height: auto;
}

/* Item 8: Cartões em 3 Colunas com Hover */
.cards-section {
  display: flex;
  gap: 20px;
  margin-bottom: 30px;
}

.card {
  flex: 1;
  background-color: #fff;
  padding: 20px;
  border-radius: 8px;
  text-align: center;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s, box-shadow 0.3s;
}

.card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 12px rgba(0, 0, 0, 0.15);
}

.card img {
  max-width: 80px;
  margin: 15px 0;
}

.card p { margin-bottom: 15px; }
.card a { color: #3498db; text-decoration: none; font-weight: bold; }

/* Item 9: Tabela com Fundo 100% */
.table-section {
  width: 100%;
  background-color: #ecf0f1;
  padding: 20px;
  border-radius: 8px;
  margin-bottom: 30px;
}

.table-container h2 {
  margin-bottom: 15px;
  text-align: center;
}

table {
  width: 100%;
  border-collapse: collapse;
  background-color: #fff;
}

th, td {
  border: 1px solid #ddd;
  padding: 12px;
  text-align: center;
}

th {
  background-color: #2980b9;
  color: white;
}

/* Item 10: Formulário 25% da Área de Conteúdo e Centralizado */
.form-section {
  display: flex;
  justify-content: center;
  margin-bottom: 30px;
}

.form-container {
  width: 25%;
  min-width: 280px;
  background-color: #fff;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.form-container h2 { margin-bottom: 10px; }
.form-container p { margin-bottom: 15px; font-size: 0.9em; }

form {
  display: flex;
  flex-direction: column;
}

label {
  margin-top: 10px;
  margin-bottom: 5px;
  font-weight: bold;
}

input, textarea {
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

button {
  margin-top: 15px;
  padding: 10px;
  background-color: #27ae60;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-weight: bold;
}

button:hover {
  background-color: #219150;
}

