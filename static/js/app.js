const btn = document.getElementById('contact-button');
console.log(btn);

document.getElementById('contact-button').addEventListener('click', async (e) => {
    e.preventDefault();
    let name = document.getElementById('name').value;
    let phone_number = document.getElementById('number').value
    let csrf_token = document.querySelector('input[name="csrfmiddlewaretoken"]').value;

    let obj = {
        name,
        phone_number
    }

    
    let data = await fetch('/contact-api/contact/', {
        method: 'POST',
        headers: {
            "Content-type": "application/json",
            "X-CSRFToken": csrf_token
        },
        body: JSON.stringify(obj)
    })

    let response = await data.json();
    // console.log(response);
    console.log(response, 'AAAA');
    

    // console.log(name);

    console.log("hey");
})