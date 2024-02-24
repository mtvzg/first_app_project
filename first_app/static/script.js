function submitForm(action) {
    let form = document.getElementById('authForm');
    if (action === 'login') {
        form.action = "{% url 'login' %}"
    } else if (action === 'register') {
        form.action = "{% url 'registration' %}"
    }
    form.submit();
}

