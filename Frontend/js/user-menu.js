document.addEventListener('DOMContentLoaded', () => {
  const userIcon = document.getElementById('user-icon');
  const userMenu = document.getElementById('user-menu');
  const logoutBtn = document.getElementById('logout-btn');
  const userEmailDisplay = document.getElementById('user-email');

  if (userIcon) {
    userIcon.addEventListener('click', () => {
      userMenu.classList.toggle('show');
    });
  }

  if (logoutBtn) {
    logoutBtn.addEventListener('click', () => {
      localStorage.removeItem('usuario_logado');
      localStorage.removeItem('usuario_email');
      window.location.href = 'login/index.html';
    });
  }

  // Mostrar o e-mail armazenado (padrão caso não exista)
  const email = localStorage.getItem('usuario_email') || 'admin@site.com';
  userEmailDisplay.textContent = email;
});
