const hamburger = document.querySelector('.hamburger')
const lines = document.querySelectorAll('.line');
const aside = document.querySelector('aside')

hamburger.addEventListener('click', ()=> {
    lines.forEach(line => {
        line.classList.toggle('active')
    })

    aside.classList.toggle('active')
})