const markaUrl = '/product-api/add-product-marka/'
const modelUrl = '/product-api/add-product-model/'
const addProductUrl = '/product-api/add-product/'
const categoryUrl = '/product-api/category/'
const cityUrl = '/product-api/city/'
console.log(cityUrl)

const image = []

$(function() {
  // Multiple images preview in browser
  var imagesPreview = function(input, placeToInsertImagePreview) {

      if (input.files) {
        console.log(input.files[0],'goreynolurda')
        image.push(input.files[0])
          var filesAmount = input.files.length;

          for (i = 0; i < filesAmount; i++) {
              var reader = new FileReader();

              reader.onload = function(event) {
                  $($.parseHTML('<img>')).attr('src', event.target.result).addClass( "col-3 mt-3" ).appendTo(placeToInsertImagePreview);
                  
              }

              reader.readAsDataURL(input.files[i]);
          }
      }

  };

  $('#gallery-photo-add').on('change', function() {
      imagesPreview(this, 'div.gallery');
  });
});




for(let i=1980 ; i < 2023 ; i++){
  document.getElementById('buraxilis-illeri').innerHTML+= `<option class="year" value="${i}">${i}</option>`
}

let data = fetch(markaUrl, {
  method: 'GET',
  headers: {
    Accept: 'application/json',
    'Content-Type': 'application/json'
    
  }
})
.then((response) => response.json())
.then((responseJson) => {
    responseJson.forEach(element => {
        
        document.getElementById('masin-markalari').innerHTML +=`<option class="markas"  value="${element.id}">${element.title}</option>` 
    });
    
  // console.log(responseJson);
})
.catch((error) => {
  console.error(error);
});



let cityData = fetch(cityUrl, {
  method: 'GET',
  headers: {
    Accept: 'application/json',
    'Content-Type': 'application/json'
    
  }
})
.then((response) => response.json())
.then((responseJson) => {
    responseJson.forEach(element => {
        
        document.getElementById('detal-city').innerHTML +=`<option class="cities"  value="${element.id}">${element.name}</option>` 
    });
    
  // console.log(responseJson);
})
.catch((error) => {
  console.error(error);
});


const filter_mark = document.getElementById('masin-markalari');

filter_mark.addEventListener("change", e => {
  console.log("taped");
    let option = e.target;
    console.log(option.value);
    marka_id = option.value
    console.log(marka_id);
    let csrf_token = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
    let obj = {
      marka_id
    }
    let data = fetch(modelUrl,{
      method:'POST',
      headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json',
        "X-CSRFToken": csrf_token
      },
      body: JSON.stringify(obj)
      
    })
    .then((response) => response.json())
.then((responseJson) => {
    
  document.getElementById('masin-modelleri').innerHTML = ''
    
    responseJson.forEach(element => {
        document.getElementById('masin-modelleri').innerHTML +=`<option class="models" value="${element.id}">${element.title}</option>` 
        
    });
    
  console.log(responseJson,'evvvvvvvvvvvvvvvvvvvvvv');
})
.catch((error) => {
  console.error(error);
});

})




let categoryData = fetch(categoryUrl, {
    method: 'GET',
    headers: {
      Accept: 'application/json',
      'Content-Type': 'application/json'
      
    }
  })
  .then((response) => response.json())
  .then((responseJson) => {
      responseJson.forEach(element => {
          
          document.getElementById('parent-categories').innerHTML +=`<option class="categories" value="${element.id}">${element.title}</option>` 
      });
      
    // console.log(responseJson);
  })
  .catch((error) => {
    console.error(error);
  });





function categoryApi(obj,select){
    let csrf_token = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
    let data = fetch(categoryUrl,{
        method:'POST',
        headers: {
          Accept: 'application/json',
          'Content-Type': 'application/json',
          "X-CSRFToken": csrf_token
        },
        body: JSON.stringify(obj)
        
      })
      .then((response) => response.json())
  .then((responseJson) => {
        
        if (select ==='parent'){
            document.getElementById('sub-parent-categories').innerHTML = '<option class="sub-cats" value="">Detalın aid olduğu sahə</option>'
            document.getElementById('child-categories').innerHTML = '<option class="sub-cats" value="">Detalı Seçin</option>'
            responseJson["sub_categories"].forEach(element => {
            document.getElementById('sub-parent-categories').innerHTML +=`<option class="sub-cats" value="${element.id}">${element.title}</option>`
            }); 
          }else{
            document.getElementById('child-categories').innerHTML = '<option class="sub-cats" value="">Detalı Seçin</option>'
            responseJson["sub_categories"].forEach(element => {
            document.getElementById('child-categories').innerHTML +=`<option class="sub-cats" value="${element.id}">${element.title}</option>` 
            }); 
          }
          
     
      
    console.log(responseJson,'evvvvvvvvvvvvvvvvvvvvvv');
  })
  .catch((error) => {
    console.error(error);
  });
}


let subcats = document.getElementById("parent-categories")

subcats.addEventListener("change", e => {
    console.log("taped");
      let option = e.target;
      console.log(option.value);
      let category_id = option.value
      let obj = {
        category_id
      }
      let select = 'parent'
      categoryApi(obj,select)
})

let childCats = document.getElementById("sub-parent-categories")

childCats.addEventListener("change", e => {
    console.log("taped");
      let option = e.target;
      console.log(option.value);
      let category_id = option.value
      let obj = {
        category_id
      }
      let select = 'sub-parent'
      categoryApi(obj,select)
})




let models = document.getElementById('masin-modelleri')
let searchBtn = document.getElementById('search')
searchBtn.addEventListener('click',e => {
    e.preventDefault()
    formData = new FormData()
    let marka = document.getElementById('masin-markalari').value
    let model = models.value
    let years = document.getElementById('buraxilis-illeri').value
    let productTitle = document.getElementById('product-title').value
    let banCode = document.getElementById('product-ban').value
    let price = document.getElementById("product-price").value
    let categortID = document.getElementById('child-categories').value
    let city = document.getElementById("detal-city").value
    let isNew = document.getElementById("is-new").value
    let mainImage = document.getElementById("gallery-photo-add").files[0]
    console.log(image,'buduba')
    formData.append('marka_id',marka)
    formData.append('modell_id',model)
    formData.append('year',years)
    formData.append('title',productTitle)
    formData.append('vin_code',banCode)
    formData.append('price',price)
    formData.append('category_id',categortID)
    formData.append('main_image',mainImage)
    formData.append('city',city)
    formData.append("is_new",isNew)
    // formData.append('image',image)
    for (i of image){
      formData.append('image', i);
    }
    // image.forEach(item => {
    //   formData.append('image', item);
    //  });
    console.log(formData)
    let csrf_token = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
    obj ={
      'marka_id' : marka,
      'modell_id' : model,
      'year' : years,
      'title' :productTitle,
      'vin_code' : banCode,
      'price':price,
      'category_id':categortID,
      'main_image':mainImage,
      'city':city,
      'is_new':isNew
    }

    let data = fetch(addProductUrl,{
      method:'POST',
      headers: {
        // 'Content-Type': 'multipart/form-data',
        "X-CSRFToken": csrf_token
      },
      body: formData
      
    })
    .then((response) => response.json())
.then((responseJson) => {
    
    
   console.log(responseJson,'saaa')
   if (responseJson['success']){
     document.getElementById("card").style.display = 'block'
   }
    
  
})
.catch((error) => {
  console.error(error);
});
    
})







// const markaUrl = `http://${window.location.host}/contact-api/main/`

// for(let i=1980 ; i < 2023 ; i++){
//       document.getElementById('buraxilis-illeri').innerHTML+= `<option class="year" value="${i}">${i}</option>`
//     }


// let csrfToken = document.querySelector('[name="csrfmiddlewaretoken"]').getAttribute('value');
// window.addEventListener("load", async function(){
//     let response = await fetch(
//         markaUrl,{
//             method: "GET",
//             headers:{
//                 "Content-Type": "application/json",
//                 'X-CSRFToken': csrfToken
//               }
//         }
//     )
//     let responseData = await response.json()
//     document.getElementById('masin-markalari').innerHTML = '<option class="" value="">Masin markasi</option>'
//     for (marka of responseData){
//         document.getElementById('masin-markalari').innerHTML += `<option class="markas" value="${marka.id}">${marka.title}</option>`
//     }
    
// })
