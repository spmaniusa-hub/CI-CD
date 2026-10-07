/**
 * Mani Subramanian — Portfolio Interactions
 * Features: Dark/Light Theme, Responsive Navigation, Skill Filtering,
 * Animated Metrics, Form Validation, Live Timezone Clock.
 */

document.addEventListener('DOMContentLoaded', () => {
  // 1. Theme Toggle
  const themeToggle = document.getElementById('themeToggle');
  const htmlRoot = document.documentElement;

  // Retrieve saved theme or system preference
  const savedTheme = localStorage.getItem('mani_theme');
  if (savedTheme) {
    htmlRoot.setAttribute('data-theme', savedTheme);
  } else if (window.matchMedia && window.matchMedia('(prefers-color-scheme: light)').matches) {
    htmlRoot.setAttribute('data-theme', 'light');
  }

  if (themeToggle) {
    themeToggle.addEventListener('click', () => {
      const currentTheme = htmlRoot.getAttribute('data-theme') || 'dark';
      const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
      htmlRoot.setAttribute('data-theme', newTheme);
      localStorage.setItem('mani_theme', newTheme);
    });
  }

  // 2. Mobile Menu Toggle
  const mobileMenuBtn = document.getElementById('mobileMenuBtn');
  const navMenu = document.getElementById('navMenu');

  if (mobileMenuBtn && navMenu) {
    mobileMenuBtn.addEventListener('click', () => {
      const isExpanded = mobileMenuBtn.getAttribute('aria-expanded') === 'true';
      mobileMenuBtn.setAttribute('aria-expanded', !isExpanded);
      navMenu.classList.toggle('open');
    });

    // Close menu when a navigation link is clicked
    document.querySelectorAll('.nav-link').forEach(link => {
      link.addEventListener('click', () => {
        navMenu.classList.remove('open');
        mobileMenuBtn.setAttribute('aria-expanded', 'false');
      });
    });
  }

  // 3. Active Nav Link on Scroll (Intersection Observer)
  const sections = document.querySelectorAll('section[id]');
  const navLinks = document.querySelectorAll('.nav-link');

  const observerOptions = {
    root: null,
    rootMargin: '-20% 0px -70% 0px',
    threshold: 0
  };

  const navObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const id = entry.target.getAttribute('id');
        navLinks.forEach(link => {
          if (link.getAttribute('href') === `#${id}`) {
            link.classList.add('active');
          } else {
            link.classList.remove('active');
          }
        });
      }
    });
  }, observerOptions);

  sections.forEach(sec => navObserver.observe(sec));

  // 4. Skills Matrix Filtering
  const filterPills = document.querySelectorAll('.filter-pill');
  const skillTiles = document.querySelectorAll('.skill-tile');

  filterPills.forEach(pill => {
    pill.addEventListener('click', () => {
      filterPills.forEach(p => p.classList.remove('active'));
      pill.classList.add('active');

      const filterValue = pill.getAttribute('data-filter');

      skillTiles.forEach(tile => {
        const category = tile.getAttribute('data-category');
        if (filterValue === 'all' || category === filterValue) {
          tile.style.display = 'flex';
          tile.style.opacity = '1';
        } else {
          tile.style.display = 'none';
          tile.style.opacity = '0';
        }
      });
    });
  });

  // 5. Contact Form Validation and Simulation
  const contactForm = document.getElementById('contactForm');
  const formStatus = document.getElementById('formStatus');
  const submitBtn = document.getElementById('submitBtn');

  if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();

      const nameInput = document.getElementById('userName');
      const emailInput = document.getElementById('userEmail');
      const messageInput = document.getElementById('userMessage');

      const nameError = document.getElementById('nameError');
      const emailError = document.getElementById('emailError');
      const messageError = document.getElementById('messageError');

      // Reset errors
      nameError.textContent = '';
      emailError.textContent = '';
      messageError.textContent = '';
      formStatus.className = 'form-status';
      formStatus.style.display = 'none';

      let isValid = true;

      if (!nameInput.value.trim()) {
        nameError.textContent = 'Please enter your name.';
        isValid = false;
      }

      const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!emailInput.value.trim() || !emailPattern.test(emailInput.value.trim())) {
        emailError.textContent = 'Please enter a valid email address.';
        isValid = false;
      }

      if (!messageInput.value.trim()) {
        messageError.textContent = 'Please include a brief message.';
        isValid = false;
      }

      if (!isValid) return;

      // Simulate sending
      submitBtn.disabled = true;
      submitBtn.innerHTML = `<span>Transmitting...</span>`;

      setTimeout(() => {
        formStatus.className = 'form-status success';
        formStatus.textContent = 'Thank you! Your message has been received. Mani will be in touch shortly.';
        formStatus.style.display = 'block';

        contactForm.reset();
        submitBtn.disabled = false;
        submitBtn.innerHTML = `
          <span>Transmit Message</span>
          <svg viewBox="0 0 24 24" width="18" height="18" stroke="currentColor" stroke-width="2" fill="none"><line x1="22" y1="2" x2="11" y2="13"></line><polygon points="22 2 15 22 11 13 2 9 22 2"></polygon></svg>
        `;
      }, 900);
    });
  }

  // 6. Live SF Bay Area (Pacific Time) Clock
  const localTimeDisplay = document.getElementById('localTimeDisplay');
  function updatePacificTime() {
    if (!localTimeDisplay) return;
    try {
      const now = new Date();
      const options = {
        timeZone: 'America/Los_Angeles',
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit',
        hour12: true,
        timeZoneName: 'short'
      };
      const formattedTime = new Intl.DateTimeFormat('en-US', options).format(now);
      localTimeDisplay.textContent = `${formattedTime} (SF Bay Area)`;
    } catch (e) {
      localTimeDisplay.textContent = 'Pacific Time (US/Pacific)';
    }
  }

  updatePacificTime();
  setInterval(updatePacificTime, 1000);

  // 7. Footer Current Year
  const currentYearSpan = document.getElementById('currentYear');
  if (currentYearSpan) {
    currentYearSpan.textContent = new Date().getFullYear();
  }
});
