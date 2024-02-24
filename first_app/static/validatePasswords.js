function validatePasswords() {
    let password = document.getElementById('password').value;
    let repeatPassword = document.getElementById('repeat_password').value;

    if (password !== repeatPassword) {
        document.getElementById('password_error').style.display = 'block';
        return false; // Предотвращаем отправку формы
    }

    return true; // Разрешаем отправку формы
}