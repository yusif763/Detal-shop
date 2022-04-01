document.getElementById("id_adress").style.display = "none";
document.getElementById("id_image").style.display = "none"
// document.getElementById("id_image").name = ""
box = document.getElementById("id_is_market")
box.addEventListener('change', (event) => {
    if (event.currentTarget.checked) {
        document.getElementById("id_adress").style.display = "block";
        document.getElementById("id_image").style.display = "block"
        document.getElementById("id_adress").required = true;
        document.getElementById("id_image").required = true
    } else {
        document.getElementById("id_adress").style.display = "none";
        document.getElementById("id_image").style.display = "none"
    }
  })


document.getElementById('id_is_market').style.display = 'none'

function myFunction1() {
    box.checked = true;
    if (box.checked) {
        document.getElementById("id_adress").style.display = "block";
        document.getElementById("id_image").style.display = "block"
        document.getElementById("id_adress").required = true;
        document.getElementById("id_image").required = true
        document.getElementById("register-image").style.display = "block"
    } else {
        document.getElementById("id_adress").style.display = "none";
        document.getElementById("id_image").style.display = "none"
        document.getElementById("register-image").style.display = "none"
    }
}

function myFunction2() {
    box.checked = false;
    if (box.checked) {
        document.getElementById("id_adress").style.display = "block";
        document.getElementById("id_image").style.display = "block"
        document.getElementById("id_adress").required = true;
        document.getElementById("id_image").required = true
        document.getElementById("register-image").style.display = "block"
    } else {
        document.getElementById("id_adress").style.display = "none";
        document.getElementById("id_image").style.display = "none"
        document.getElementById("register-image").style.display = "none"
    }
}