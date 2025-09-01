// Dark mode functionality
class DarkMode {
    constructor() {
        this.theme = localStorage.getItem('theme') || 'light';
        this.init();
    }

    init() {
        // Set initial theme
        this.setTheme(this.theme);
        
        // Add event listeners
        this.addEventListeners();
        
        // Update navbar background on scroll
        this.handleNavbarScroll();
    }

    setTheme(theme) {
        this.theme = theme;
        document.documentElement.setAttribute('data-theme', theme);
        localStorage.setItem('theme', theme);
        
        // Update navbar background based on theme
        this.updateNavbarBackground();
    }

    toggleTheme() {
        const newTheme = this.theme === 'light' ? 'dark' : 'light';
        this.setTheme(newTheme);
    }

    addEventListeners() {
        // Theme toggle button
        const themeToggle = document.querySelector('.theme-toggle');
        if (themeToggle) {
            themeToggle.addEventListener('click', () => this.toggleTheme());
        }

        // Navbar scroll effect
        window.addEventListener('scroll', () => this.handleNavbarScroll());
    }

    handleNavbarScroll() {
        const nav = document.querySelector('.nav');
        if (!nav) return;

        if (window.scrollY > 100) {
            nav.style.background = this.theme === 'light' 
                ? 'rgba(255, 255, 255, 0.95)' 
                : 'rgba(26, 32, 44, 0.95)';
        } else {
            nav.style.background = this.theme === 'light' 
                ? 'rgba(255, 255, 255, 0.9)' 
                : 'rgba(26, 32, 44, 0.9)';
        }
    }

    updateNavbarBackground() {
        const nav = document.querySelector('.nav');
        if (!nav) return;

        if (window.scrollY > 100) {
            nav.style.background = this.theme === 'light' 
                ? 'rgba(255, 255, 255, 0.95)' 
                : 'rgba(26, 32, 44, 0.95)';
        } else {
            nav.style.background = this.theme === 'light' 
                ? 'rgba(255, 255, 255, 0.9)' 
                : 'rgba(26, 32, 44, 0.9)';
        }
    }
}

// Initialize dark mode when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    new DarkMode();
}); 