let number = document.getElementById("phone-number").innerText
console.log(number)
let hashedNumber = number.slice(0,10)
document.getElementById("phone-number").innerText = `${hashedNumber}-XX-XX`
