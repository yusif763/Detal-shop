const tokenUrl = '/en/contact-api/token/'

const LoginLogic = {
    fetchToken(username, password) {
        fetch(tokenUrl, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                "email": username,
                "password": password
            })
        })
            .then(response => response.json())
            .then(data => {
                if (data.access) {
                    localStorage.setItem('token', data.access);
                }
            })
    }
}


const submit = document.getElementById('login-submit');
const form = document.getElementById("login-form")
submit.onclick = function () {
    const username = document.querySelector('#id_username').value;
    const password = document.querySelector('#id_password').value;
    LoginLogic.fetchToken(username, password);
    setInterval(form.submit(), 3000);
}

