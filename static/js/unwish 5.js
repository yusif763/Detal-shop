let xButtons = document.querySelectorAll('.x-button');

xButtons.forEach(element => {
    element.addEventListener('click', async (e) => { 
        e.preventDefault();
        let csrf_token = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
        
        let product = element.nextElementSibling.innerHTML
        console.log(element , 'fgf')
        
       
        console.log('mgcmgcvnv');
            console.log(product);
            let obj = {
                product
            }
            
            console.log(obj);
            let data = await fetch('/contact-api/wishlist/', {
                method: 'DELETE',
                headers: {
                    "Content-type": "application/json",
                    "X-CSRFToken": csrf_token
                },
                body: JSON.stringify(obj)
            });
        
            // let response = await data.json();
            console.log(data);
            window.location.reload()
            
        });
    });
