const ActivateProductLogic = {
    productManager(productId) {
        fetch('/main-api/activate-product', {
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
    fetch('/main-api/activate-product', {
        method: 'GET',
        credentials: 'include',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${localStorage.getItem('token')}`
        }
    })
        .then(response => response.json())
        .then(data => {
            products = document.getElementById('products');
            products.innerHTML = '';
            console.log(data);
            for (let i = 0; i < data.length; i++) {
                products.innerHTML += `<div class="card-item col-12 col-md-4 col-lg-4 col-xl-3 col-sm-6">
                    <div class="incard">
                        <i class="fas fa-heart"></i>
                        <div class="d-flex"> 
                        <img style="width:100%;" src="${data[i]['main_image']}" alt="">
                        </div>
                        <div class="d-flex">
                            <span>satici:</span>
                            <span style="color: red;">${data[i]['user']}</span>
                        </div>
                        <p>${data[i]['title']}</p>
                        <button>23</button>
                        <div style="display:flex; alig-items:center; justify-content:center; width:80%;" class="activate-button mb-4">
                        <button data-id='${data[i]['id']}' class='mt-2 activate' onclick='activateProduct(this)'>Aktiv et</button>
                        </div>
                    </div>
                </div>`

            }
        });
}

window.addEventListener('DOMContentLoaded', (event) => {
    getProductManager()
});
