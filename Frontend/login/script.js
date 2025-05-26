document.getElementById('login-form').addEventListener('submit', function (e) {
  e.preventDefault();

  const email = document.getElementById('email').value;
  const senha = document.getElementById('senha').value;

  // Exemplo de login fixo (troque por chamada ao backend, se necessário)
  if (email === 'admin@site.com' && senha === '123456') {
    alert('Login bem-sucedido!');
    // Redireciona para outra página
    window.location.href = 'home.html';
  } else {
    alert('E-mail ou senha inválidos.');
  }
});
