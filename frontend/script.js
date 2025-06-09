const form = document.getElementById('loanForm');
const resultDiv = document.getElementById('result');
const loadingDiv = document.getElementById('loading');

form.addEventListener('submit', async (e) => {
    e.preventDefault();
    resultDiv.textContent = '';
    resultDiv.className = 'placeholder';
    loadingDiv.classList.remove('hidden');

    const formData = new FormData(form);
    const data = {};
    formData.forEach((value, key) => data[key] = value);

    try {
        const response = await fetch('http://127.0.0.1:5000/predict', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });
        const res = await response.json();
        loadingDiv.classList.add('hidden');
        if (res.loan_status) {
            resultDiv.textContent = res.loan_status === 'Approved' ? 'Loan Approved' : 'Loan Not Approved';
            resultDiv.className = res.loan_status === 'Approved' ? 'approved' : 'not-approved';
        } else {
            resultDiv.textContent = res.error || 'Error: Could not get prediction. Please try again later.';
            resultDiv.className = 'not-approved';
        }
    } catch (err) {
        loadingDiv.classList.add('hidden');
        resultDiv.textContent = 'Error: Could not get prediction. Please try again later.';
        resultDiv.className = 'not-approved';
    }
});