const markaUrl = '/main-api/main/'
const modelUrl = '/main-api/main-model/'



for(let i=1980 ; i < 2023 ; i++){
  document.getElementById('buraxilish-filter').innerHTML+= `<option class="year" value="${i}">${i}</option>`
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
    
    document.getElementById('filter-mark').innerHTML = '<option class="" value="">Masin markasi</option>'
    responseJson.forEach(element => {
        
        document.getElementById('filter-mark').innerHTML +=`<option class="markas mr-2" value="${element.slug}">${element.title}</option>` 
    });
    
  // console.log(responseJson);
})
.catch((error) => {
  console.error(error);
});



const filter_mark = document.getElementById('filter-mark');
const filter_model = document.getElementById('filter-model');
filter_model.innerHTML = '<option class="models" value="">Masin modeli</option>'
filter_mark.addEventListener("change", e => {
  filter_model.innerHTML = ''
  filter_model.innerHTML = '<option class="models" value="">Masin modeli</option>'
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
    
  
    
    responseJson.forEach(element => {
        document.getElementById('filter-model').innerHTML +=`<option class="models" value="${element.slug}">${element.title}</option>` 
        
    });

    
  console.log(responseJson,'evvvvvvvvvvvvvvvvvvvvvv');
})
.catch((error) => {
  console.error(error);
});

})

let models = document.getElementById('filter-model')
let searchBtn = document.querySelector('.axtarish')

searchBtn.addEventListener('click',e => {
    let marka = document.getElementById('filter-mark').value
    let model = models.value
    let years = document.getElementById('buraxilish-filter').value
    let searchValue = document.getElementById('search').value
    let banCode = document.getElementById('ban').value
    let csrf_token = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
    localStorage.setItem('csrf',csrf_token)
    console.log(banCode,marka,model,years,searchValue);

  console.log(window.location.href,'saaaaaammmeeekm');
  let url = new URL('https://detalshop.az/main/searched-products/?')

  let search_param = url.searchParams
 
if (marka){

  search_param.set('marka',marka)
}
if (model){

  search_param.set('modell',model)
}
if (years){

  search_param.set('year',years)
}
if (banCode){

  search_param.set('ban_nomresi',banCode)
}
if (searchValue){

  search_param.set('search_value',searchValue)
}


  
  url.search = search_param.toString();
  let new_url = url.toString()
  // if(marka || model || years || banCode || searchValue){

    window.location.href = new_url
  // }
 
})

    


