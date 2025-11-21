// Main JavaScript for SmartX Study

document.addEventListener('DOMContentLoaded', function() {
    // Initialize tooltips and interactive elements
    initializeTooltips();
    initializeAnimations();
    initializeFormEnhancements();
    initializeNotifications();
});

// Tooltip initialization
function initializeTooltips() {
    const tooltipElements = document.querySelectorAll('[data-tooltip]');
    
    tooltipElements.forEach(element => {
        element.addEventListener('mouseenter', showTooltip);
        element.addEventListener('mouseleave', hideTooltip);
    });
}

function showTooltip(event) {
    const element = event.target;
    const tooltipText = element.getAttribute('data-tooltip');
    
    const tooltip = document.createElement('div');
    tooltip.className = 'tooltip absolute z-50 bg-gray-900 text-white text-sm rounded py-1 px-2 pointer-events-none';
    tooltip.textContent = tooltipText;
    
    document.body.appendChild(tooltip);
    
    const rect = element.getBoundingClientRect();
    tooltip.style.left = rect.left + (rect.width / 2) - (tooltip.offsetWidth / 2) + 'px';
    tooltip.style.top = rect.top - tooltip.offsetHeight - 5 + 'px';
    
    element._tooltip = tooltip;
}

function hideTooltip(event) {
    const element = event.target;
    if (element._tooltip) {
        document.body.removeChild(element._tooltip);
        element._tooltip = null;
    }
}

// Animation on scroll
function initializeAnimations() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-fade-in');
            }
        });
    }, observerOptions);
    
    document.querySelectorAll('.animate-on-scroll').forEach(element => {
        observer.observe(element);
    });
}

// Form enhancements
function initializeFormEnhancements() {
    // File upload preview
    const fileInputs = document.querySelectorAll('input[type="file"]');
    
    fileInputs.forEach(input => {
        input.addEventListener('change', function(event) {
            const file = event.target.files[0];
            if (file) {
                showFilePreview(file, input);
            }
        });
    });
    
    // Auto-resize textareas
    const textareas = document.querySelectorAll('textarea');
    textareas.forEach(textarea => {
        textarea.addEventListener('input', autoResizeTextarea);
    });
    
    // Form validation feedback
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(event) {
            if (!validateForm(form)) {
                event.preventDefault();
                showValidationErrors(form);
            }
        });
    });
}

function showFilePreview(file, input) {
    const preview = document.createElement('div');
    preview.className = 'mt-2 text-sm text-gray-600';
    
    const icon = file.type === 'application/pdf' ? 'fas fa-file-pdf' : 'fas fa-file';
    const size = (file.size / (1024 * 1024)).toFixed(2) + ' MB';
    
    preview.innerHTML = `
        <div class="flex items-center">
            <i class="${icon} mr-2 text-red-500"></i>
            <span>${file.name} (${size})</span>
        </div>
    `;
    
    // Remove existing preview
    const existingPreview = input.parentNode.querySelector('.file-preview');
    if (existingPreview) {
        existingPreview.remove();
    }
    
    preview.className += ' file-preview';
    input.parentNode.appendChild(preview);
}

function autoResizeTextarea(event) {
    const textarea = event.target;
    textarea.style.height = 'auto';
    textarea.style.height = textarea.scrollHeight + 'px';
}

function validateForm(form) {
    const requiredFields = form.querySelectorAll('[required]');
    let isValid = true;
    
    requiredFields.forEach(field => {
        if (!field.value.trim()) {
            isValid = false;
            field.classList.add('border-red-500');
        } else {
            field.classList.remove('border-red-500');
        }
    });
    
    return isValid;
}

function showValidationErrors(form) {
    const errorContainer = form.querySelector('.form-errors') || createErrorContainer(form);
    errorContainer.innerHTML = '<p class="text-red-600 text-sm">Please fill in all required fields.</p>';
    errorContainer.scrollIntoView({ behavior: 'smooth', block: 'center' });
}

function createErrorContainer(form) {
    const container = document.createElement('div');
    container.className = 'form-errors bg-red-50 border border-red-200 rounded p-3 mb-4';
    form.insertBefore(container, form.firstChild);
    return container;
}

// Notification system
function initializeNotifications() {
    // Auto-hide alerts
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            hideAlert(alert);
        }, 5000);
        
        // Add close button
        const closeBtn = document.createElement('button');
        closeBtn.innerHTML = '&times;';
        closeBtn.className = 'ml-auto text-lg font-bold hover:opacity-75';
        closeBtn.onclick = () => hideAlert(alert);
        alert.appendChild(closeBtn);
    });
}

function hideAlert(alert) {
    alert.style.opacity = '0';
    alert.style.transform = 'translateX(100%)';
    setTimeout(() => {
        alert.remove();
    }, 300);
}

function showNotification(message, type = 'info') {
    const notification = document.createElement('div');
    notification.className = `toast bg-${getNotificationColor(type)}-100 border border-${getNotificationColor(type)}-200 text-${getNotificationColor(type)}-800 px-4 py-3 rounded shadow-lg`;
    
    notification.innerHTML = `
        <div class="flex items-center">
            <i class="fas fa-${getNotificationIcon(type)} mr-2"></i>
            <span>${message}</span>
            <button class="ml-4 text-lg font-bold hover:opacity-75" onclick="this.parentElement.parentElement.remove()">&times;</button>
        </div>
    `;
    
    document.body.appendChild(notification);
    
    setTimeout(() => {
        notification.remove();
    }, 5000);
}

function getNotificationColor(type) {
    const colors = {
        'success': 'green',
        'error': 'red',
        'warning': 'yellow',
        'info': 'blue'
    };
    return colors[type] || 'blue';
}

function getNotificationIcon(type) {
    const icons = {
        'success': 'check-circle',
        'error': 'exclamation-triangle',
        'warning': 'exclamation-circle',
        'info': 'info-circle'
    };
    return icons[type] || 'info-circle';
}

// Utility functions
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

function throttle(func, limit) {
    let inThrottle;
    return function() {
        const args = arguments;
        const context = this;
        if (!inThrottle) {
            func.apply(context, args);
            inThrottle = true;
            setTimeout(() => inThrottle = false, limit);
        }
    };
}

// Loading states
function showLoading(element) {
    const originalContent = element.innerHTML;
    element.innerHTML = '<i class="fas fa-spinner fa-spin mr-2"></i>Loading...';
    element.disabled = true;
    element.dataset.originalContent = originalContent;
}

function hideLoading(element) {
    element.innerHTML = element.dataset.originalContent || 'Submit';
    element.disabled = false;
    delete element.dataset.originalContent;
}

// Smooth scrolling
function smoothScrollTo(element) {
    element.scrollIntoView({
        behavior: 'smooth',
        block: 'start'
    });
}

// Local storage helpers
function saveToStorage(key, value) {
    try {
        localStorage.setItem(key, JSON.stringify(value));
    } catch (e) {
        console.warn('Could not save to localStorage:', e);
    }
}

function loadFromStorage(key) {
    try {
        const item = localStorage.getItem(key);
        return item ? JSON.parse(item) : null;
    } catch (e) {
        console.warn('Could not load from localStorage:', e);
        return null;
    }
}

// Export functions for use in other scripts
window.SmartXUtils = {
    showNotification,
    showLoading,
    hideLoading,
    smoothScrollTo,
    saveToStorage,
    loadFromStorage,
    debounce,
    throttle
};