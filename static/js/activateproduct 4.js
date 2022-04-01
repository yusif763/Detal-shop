const ActivateProductLogic = {
    productManager(productId) {
        fetch('/contact-api/activate-product', {
            method: 'POST',
            credentials: 'include',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${localStorage.getItem('token')}`
            },
            body: JSON.stringify({
                'product_id': productId,
            })
        })
            // .then(response => response.json())
            .then(data => {
                getProductManager()
            });
    }
}

function activateProduct(button) {
    const productId = button.getAttribute('data-id')
    ActivateProductLogic.productManager(productId)
}



function getProductManager() {
    fetch('/contact-api/activate-product', {
        method: 'GET',
        credentials: 'include',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${localStorage.getItem('token')}`
        }
    })
        .then(response => response.json())
        .then(data => {
            console.log(data);
            const activateButton = document.getElementsByClassName('activate-button');
            for (let i = 0; i < data.length; i++) {
                activateButton[i].innerHTML = ''
                if (data[i]['is_active'] == false) {
                    activateButton[i].innerHTML = `<button data-id='${data[i]['id']}' class='mt-2 activate' onclick='activateProduct(this)'>Aktiv et</button>`
                } else {
                    activateButton[i].innerHTML = `<button data-id='${data[i]['id']}' class='mt-2 activate' onclick='activateProduct(this)'>Deaktiv et</button>`
                }

            }
        });
}

window.addEventListener('DOMContentLoaded', (event) => {
    getProductManager()
});
