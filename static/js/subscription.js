// Email subscription form handler
(function() {
    'use strict';

    // Initialize when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }

    function init() {
        const form = document.querySelector('.subscription-form');
        if (!form) return;

        form.addEventListener('submit', handleSubmit);
    }

    async function handleSubmit(event) {
        event.preventDefault();

        const form = event.target;
        const emailInput = form.querySelector('input[type="email"]');
        const submitButton = form.querySelector('button[type="submit"]');
        const messageDiv = form.parentElement.querySelector('.subscription-message');

        if (!emailInput || !submitButton || !messageDiv) return;

        const email = emailInput.value.trim();

        // Basic validation
        if (!email) {
            showMessage(messageDiv, 'Please enter your email address.', 'error');
            return;
        }

        if (!isValidEmail(email)) {
            showMessage(messageDiv, 'Please enter a valid email address.', 'error');
            return;
        }

        // Disable form while submitting
        submitButton.disabled = true;
        submitButton.textContent = 'Subscribing...';
        hideMessage(messageDiv);

        try {
            const response = await fetch('/api/subscribe', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ email }),
            });

            const data = await response.json();

            if (data.success) {
                showMessage(messageDiv, data.message, 'success');
                emailInput.value = '';
            } else {
                showMessage(messageDiv, data.message, 'error');
            }
        } catch (error) {
            console.error('Subscription error:', error);
            showMessage(messageDiv, 'Unable to subscribe. Please try again later.', 'error');
        } finally {
            submitButton.disabled = false;
            submitButton.textContent = 'Subscribe';
        }
    }

    function isValidEmail(email) {
        // Basic email validation regex
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailRegex.test(email);
    }

    function showMessage(element, message, type) {
        element.textContent = message;
        element.className = 'subscription-message show ' + type;
    }

    function hideMessage(element) {
        element.classList.remove('show');
    }
})();
