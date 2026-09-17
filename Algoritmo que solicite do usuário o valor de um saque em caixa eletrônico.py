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
