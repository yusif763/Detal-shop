// console.log(window.location.href);
// const filterUrl = 'http://127.0.0.1:8000/main-api/filtered-prod/'

// let url_string = window.location.href
// let url = new URL(url_string);
// let marka = url.searchParams.get("marka_id");
// let model = url.searchParams.get('modell_id');
// let years = url.searchParams.get('year');
// let banCode = url.searchParams.get('vin_code');
// let searchValue = url.searchParams.get('search_value')
// let csrf_token = localStorage.getItem('csrf')


// console.log(marka,model,years,banCode,searchValue);

// let csrf_token = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
    // obj ={
    //   'marka_id' : marka,
    //   'modell_id' : model,
    //   'year' : years,
    //   'search_value' : searchValue,
    //   'ban_code' : banCode
    // }


    // let data = fetch(filterUrl,{
    //     method:'POST',
    //     headers: {
    //       Accept: 'application/json',
    //       'Content-Type': 'application/json',
    //       "X-CSRFToken": csrf_token
    //     },
    //     body: JSON.stringify(obj)
        
    //   })
    //   .then((response) => response.json())
    //   .then((responseJson) => {
    
  
    
    //     responseJson.forEach(element => {
    //         document.getElementById('searched').innerHTML+=`
    //         <div class="card-item col-12 col-md-4 col-lg-4 col-xl-3 col-sm-6">
    //             <div class="incard">
    //                 <i class="fas fa-heart wish"></i>
    //                 <span class='d-none foridinput'>{{i.id}}</span>
    //                 <span class='d-none foridinput'>{{request.user.id}}</span>
                    
    //                 <img src="${element.main_image}" alt="">
    //                 <div class="d-flex">
    //                     <span>satici:</span>
    //                     <span style="color: red;">${element.user_id.username}</span>
    //                 </div>
    //                 <p>${element.title}</p>
    //                 <button>${element.price}</button>
    //             </div>
    //         </div>`
            
    //     });
        
    //   console.log(responseJson,'evvvvvvvvvvvvvvvvvvvvvv');
    // })
    // .catch((error) => {
    //     console.error(error);
    //   });
      
      