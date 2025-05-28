function carregarTela(event, caminho) {
  if (event) event.preventDefault();
  fetch(`/cadastro/${caminho}/index.html`)
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

function toggleSubmenu(event) {
  event.preventDefault();
  const submenu = event.target.nextElementSibling; 
  if (submenu && submenu.classList.contains('submenu')) {
    if (submenu.style.display === 'none' || submenu.style.display === '') {
      submenu.style.display = 'block';
    } else {
      submenu.style.display = 'none';
    }
  }
}