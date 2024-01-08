const container = document.getElementById('container')
const aTag = document.querySelectorAll('a')

container.style.backgroundColor = '#1f2023'
aTag.forEach((a) => a.style.color = 'white')

   const container = document.getElementById('container')
   container.style.backgroundColor = '#1f2023'


const style = document.createElement('style');
style.innerHTML = `
    a, b, strong, span, p {
        color: white;
    },
    #container{
        background-color: #1f2023
    }`
document.body.appendChild(style);

   console.log(123123)