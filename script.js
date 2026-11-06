(() => {
  const toggle = document.querySelector('[data-menu-toggle]');
  const nav = document.querySelector('[data-nav]');
  if (toggle && nav) {
    toggle.addEventListener('click', () => {
      const open = nav.classList.toggle('is-open');
      toggle.setAttribute('aria-expanded', String(open));
      toggle.querySelector('.sr-only').textContent = open ? 'Fechar menu' : 'Abrir menu';
    });
    nav.querySelectorAll('a').forEach((link) => link.addEventListener('click', () => {
      nav.classList.remove('is-open'); toggle.setAttribute('aria-expanded', 'false');
      toggle.querySelector('.sr-only').textContent = 'Abrir menu';
    }));
  }

  const filters = [...document.querySelectorAll('[data-filter]')];
  const cards = [...document.querySelectorAll('[data-category]')];
  filters.forEach((filter) => filter.addEventListener('click', () => {
    const selected = filter.dataset.filter || 'all';
    filters.forEach((item) => {
      const active = item === filter;
      item.classList.toggle('is-active', active);
      item.setAttribute('aria-pressed', String(active));
    });
    cards.forEach((card) => card.classList.toggle('is-hidden', selected !== 'all' && card.dataset.category !== selected));
  }));
})();
