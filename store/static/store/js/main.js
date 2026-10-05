function formatCardNumber(input) {
    let value = input.value.replace(/\D/g, '').slice(0, 16);
    let formatted = '';
    for (let i = 0; i < value.length; i++) {
        if (i > 0 && i % 4 === 0) formatted += ' ';
        formatted += value[i];
    }
    input.value = formatted;
    const display = document.getElementById('card-num-preview');
    if (display) display.innerText = formatted ? formatted.padEnd(19, '•') : '•••• •••• •••• ••••';
}

function formatExpiry(input) {
    let value = input.value.replace(/\D/g, '').slice(0, 4);
    if (value.length >= 2) {
        input.value = value.substring(0, 2) + '/' + value.substring(2, 4);
    } else {
        input.value = value;
    }
    const expiryPreview = document.getElementById('card-expiry-preview');
    if (expiryPreview) expiryPreview.innerText = input.value || 'MM/YY';
}

function formatCvv(input) {
    input.value = input.value.replace(/\D/g, '').slice(0, 3);
}

function updateHolderPreview(input) {
    input.value = input.value.replace(/[^a-zA-Z\s]/g, '').toUpperCase();
    const display = document.getElementById('card-holder-preview');
    if (display) display.innerText = input.value || 'YOUR NAME';
}

function openPaymentModal() {
    const modal = document.getElementById('payment-modal');
    if (modal) modal.classList.add('open');
}

function closePaymentModal() {
    const modal = document.getElementById('payment-modal');
    if (modal) modal.classList.remove('open');
}

function processPayment(event) {
    event.preventDefault();
    const btn = document.getElementById('pay-submit-btn');
    const processingText = btn.dataset.processingText || 'Processing...';
    btn.innerText = processingText;
    btn.disabled = true;

    setTimeout(() => {
        document.getElementById('checkout-form').submit();
    }, 1200);
}