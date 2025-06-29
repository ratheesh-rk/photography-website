// Hero Slider JavaScript
class HeroSlider {
    constructor() {
        this.slides = document.querySelectorAll('.slide');
        this.dots = document.querySelectorAll('.slider-dot');
        this.currentSlide = 0;
        this.slideInterval = null;
        this.autoPlayDelay = 6000; // 6 seconds for better responsiveness
        this.isTransitioning = false;
        this.hasAnimatedContent = false; // Track if content has been animated
        
        this.init();
    }
    
    init() {
        if (this.slides.length === 0) return;
        
        // Ensure proper initial state - reset all slides first
        this.slides.forEach((slide, i) => {
            slide.classList.remove('active', 'prev', 'next');
        });
        
        // Set the first slide as active
        this.slides[0].classList.add('active');
        this.dots[0].classList.add('active');
        this.currentSlide = 0;
        
        this.bindEvents();
        this.startAutoPlay();
        this.updateSlideContent();
    }
    
    bindEvents() {
        // Dot navigation
        this.dots.forEach((dot, index) => {
            dot.addEventListener('click', () => {
                if (!this.isTransitioning) {
                    this.goToSlide(index);
                }
            });
        });
        
        // Keyboard navigation
        document.addEventListener('keydown', (e) => {
            if (!this.isTransitioning) {
                if (e.key === 'ArrowLeft') {
                    this.prevSlide();
                } else if (e.key === 'ArrowRight') {
                    this.nextSlide();
                }
            }
        });
        
        // Touch/swipe support
        let touchStartX = 0;
        let touchEndX = 0;
        let touchStartY = 0;
        let touchEndY = 0;
        
        const hero = document.querySelector('.hero');
        if (hero) {
            hero.addEventListener('touchstart', (e) => {
                touchStartX = e.changedTouches[0].screenX;
                touchStartY = e.changedTouches[0].screenY;
            });
            
            hero.addEventListener('touchend', (e) => {
                if (!this.isTransitioning) {
                    touchEndX = e.changedTouches[0].screenX;
                    touchEndY = e.changedTouches[0].screenY;
                    
                    // Only handle horizontal swipes, ignore vertical scrolling
                    const diffX = Math.abs(touchStartX - touchEndX);
                    const diffY = Math.abs(touchStartY - touchEndY);
                    
                    // Only trigger swipe if horizontal movement is greater than vertical
                    if (diffX > diffY && diffX > 50) {
                        this.handleSwipe(touchStartX, touchEndX);
                    }
                }
            });
            
            // Prevent default touch behavior that might interfere with scrolling
            hero.addEventListener('touchmove', (e) => {
                // Allow vertical scrolling, prevent horizontal scrolling
                const diffX = Math.abs(touchStartX - e.changedTouches[0].screenX);
                const diffY = Math.abs(touchStartY - e.changedTouches[0].screenY);
                
                if (diffX > diffY && diffX > 30) {
                    e.preventDefault();
                }
            }, { passive: false });
        }
        
        // Pause autoplay on hover
        hero.addEventListener('mouseenter', () => {
            this.pauseAutoPlay();
        });
        
        hero.addEventListener('mouseleave', () => {
            this.startAutoPlay();
        });
    }
    
    goToSlide(index) {
        if (index < 0) index = this.slides.length - 1;
        if (index >= this.slides.length) index = 0;
        
        if (index === this.currentSlide || this.isTransitioning) return;
        
        this.isTransitioning = true;
        
        // Determine slide direction
        const direction = index > this.currentSlide ? 1 : -1;
        
        // Store current slide index before changing
        const previousSlide = this.currentSlide;
        
        // Remove active class from current dot
        this.dots[this.currentSlide].classList.remove('active');
        
        // Add active class to new slide FIRST to prevent dark appearance
        this.slides[index].classList.add('active');
        this.dots[index].classList.add('active');
        
        // Add transition classes based on direction to the PREVIOUS slide
        if (direction === 1) {
            this.slides[previousSlide].classList.add('prev');
        } else {
            this.slides[previousSlide].classList.add('next');
        }
        
        // Remove active class from previous slide
        this.slides[previousSlide].classList.remove('active');
        
        this.currentSlide = index;
        this.updateSlideContent();
        
        // Clean up transition classes after animation
        setTimeout(() => {
            this.slides[previousSlide].classList.remove('prev', 'next');
            this.isTransitioning = false;
        }, 2000); // Match CSS transition duration (2s)
    }
    
    nextSlide() {
        this.goToSlide(this.currentSlide + 1);
    }
    
    prevSlide() {
        this.goToSlide(this.currentSlide - 1);
    }
    
    handleSwipe(startX, endX) {
        const swipeThreshold = 80; // Increased threshold for mobile
        const diff = startX - endX;
        
        if (Math.abs(diff) > swipeThreshold) {
            if (diff > 0) {
                // Swipe left - next slide
                this.nextSlide();
            } else {
                // Swipe right - previous slide
                this.prevSlide();
            }
        }
    }
    
    startAutoPlay() {
        this.stopAutoPlay();
        this.slideInterval = setInterval(() => {
            if (!this.isTransitioning) {
                this.nextSlide();
            }
        }, this.autoPlayDelay);
    }
    
    stopAutoPlay() {
        if (this.slideInterval) {
            clearInterval(this.slideInterval);
            this.slideInterval = null;
        }
    }
    
    pauseAutoPlay() {
        this.stopAutoPlay();
    }
    
    updateSlideContent() {
        // Only animate content on the first slide change
        if (!this.hasAnimatedContent) {
            const heroTitle = document.querySelector('.hero-title');
            const heroSubtitle = document.querySelector('.hero-subtitle');
            
            if (heroTitle) {
                heroTitle.style.animation = 'none';
                heroTitle.offsetHeight; // Trigger reflow
                heroTitle.style.animation = 'cinematicTitleIn 1.2s cubic-bezier(0.25, 0.46, 0.45, 0.94) 0.3s forwards';
            }
            
            if (heroSubtitle) {
                heroSubtitle.style.animation = 'none';
                heroSubtitle.offsetHeight; // Trigger reflow
                heroSubtitle.style.animation = 'cinematicSubtitleIn 1.2s cubic-bezier(0.25, 0.46, 0.45, 0.94) 0.6s forwards';
            }
            
            this.hasAnimatedContent = true;
        }
        // For subsequent slides, content stays visible without re-animation
    }
    
    // Public method to manually control slides
    setSlide(index) {
        this.goToSlide(index);
    }
    
    // Public method to change autoplay delay
    setAutoPlayDelay(delay) {
        this.autoPlayDelay = delay;
        this.startAutoPlay();
    }
}

// Initialize slider when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    // Small delay to ensure CSS is fully loaded
    setTimeout(() => {
        new HeroSlider();
    }, 100);
});

// Export for potential external use
window.HeroSlider = HeroSlider; 