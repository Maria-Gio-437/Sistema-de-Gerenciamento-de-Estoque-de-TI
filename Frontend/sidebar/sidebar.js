function toggleSubmenu() {
  document.getElementById("cadastros-submenu").classList.toggle("show");
}

function carregarTela(event, caminho) {
  if (event) event.preventDefault();
  fetch(`../cadastro/${caminho}/index.html`)
    .then(res => res.text())
    .then(html => {
      const container = document.getElementById("conteudo");
      if (container) {
        container.innerHTML = html;
      }
    })
    .catch(() => {
      document.getElementById("conteudo").innerHTML = "<p>Erro ao carregar a tela.</p>";
    });
}
