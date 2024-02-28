function submitForm(action) {
    let form = document.getElementById('authForm');
    if (action === 'Вход') {
        form.action = "{% url 'log_in' %}"
    } else if (action === 'Регистрация') {
        form.action = "{% url 'registration' %}"
    }
    form.submit();
}

