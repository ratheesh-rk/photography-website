// Main JavaScript for website functionality
document.addEventListener('DOMContentLoaded', function() {
    
    // Scroll animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    }, observerOptions);

    // Observe elements for fade-in animation
    const fadeElements = document.querySelectorAll('.service-card, .portfolio-item, .about-text, .about-image, .contact-item');
    fadeElements.forEach(el => {
        el.classList.add('fade-in');
        observer.observe(el);
    });

    // Lazy loading for images
    const images = document.querySelectorAll('img[src]');
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.style.opacity = '1';
                img.style.transform = 'scale(1)';
                imageObserver.unobserve(img);
            }
        });
    });

    images.forEach(img => {
        img.style.opacity = '0';
        img.style.transform = 'scale(0.95)';
        img.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        imageObserver.observe(img);
    });

    // Initialize sections with hidden state
    const sections = document.querySelectorAll('section:not(.hero)');
    sections.forEach(section => {
        section.style.opacity = '0';
        section.style.transform = 'translateY(30px)';
        section.style.transition = 'opacity 0.8s ease, transform 0.8s ease';
    });

    // Smooth reveal animation for sections - using Intersection Observer instead of scroll events
    const sectionObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, {
        threshold: 0.1,
        rootMargin: '0px 0px -100px 0px'
    });

    sections.forEach(section => {
        sectionObserver.observe(section);
    });

    // Portfolio image hover effects
    const portfolioItems = document.querySelectorAll('.portfolio-item');
    portfolioItems.forEach(item => {
        item.addEventListener('mouseenter', function() {
            this.style.transform = 'scale(1.05)';
        });
        
        item.addEventListener('mouseleave', function() {
            this.style.transform = 'scale(1)';
        });
    });

    // Service cards hover effects
    const serviceCards = document.querySelectorAll('.service-card');
    serviceCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-10px)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    });

    // Contact form functionality (if added later)
    const contactForm = document.querySelector('#contact-form');
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            // Add form submission logic here
            console.log('Form submitted');
        });
    }

    // Loading animation
    window.addEventListener('load', function() {
        document.body.classList.add('loaded');
    });

    // Mobile-specific optimizations
    if (window.innerWidth <= 768) {
        // Disable hover effects on mobile
        const hoverElements = document.querySelectorAll('.service-card, .portfolio-item, .contact-item');
        hoverElements.forEach(el => {
            el.style.pointerEvents = 'none';
        });
    }

    // Add loading state to CTA button
    const ctaButton = document.querySelector('.cta-button');
    if (ctaButton) {
        ctaButton.addEventListener('click', function(e) {
            if (this.getAttribute('href') === '#contact') {
                e.preventDefault();
                this.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Loading...';
                setTimeout(() => {
                    this.innerHTML = 'Book Your Session';
                    document.querySelector('#contact').scrollIntoView({
                        behavior: 'smooth'
                    });
                }, 1000);
            }
        });
    }

    // Add CSS for body loading state
    const style = document.createElement('style');
    style.textContent = `
        body.loaded {
            opacity: 1;
        }
        
        body {
            opacity: 0;
            transition: opacity 0.5s ease;
        }
    `;
    document.head.appendChild(style);

    // --- FAB (Floating Action Button) Logic: Updated for base.html ---
    (function() {
        var fab = document.getElementById('floatingActionButton');
        var fabMain = document.getElementById('fabMain');
        var fabOptions = document.getElementById('fabOptions');
        if (!fab || !fabMain || !fabOptions) return;
        fabMain.addEventListener('click', function(e) {
            e.stopPropagation();
            fab.classList.toggle('active');
        });
        fabOptions.addEventListener('click', function(e) {
            e.stopPropagation();
        });
        document.addEventListener('click', function() {
            fab.classList.remove('active');
        });
    })();
}); 