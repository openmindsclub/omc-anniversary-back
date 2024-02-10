const text = document.querySelector('.text h3');
text.innerHTML = text.innerText.split('').map(
    (char, i) =>
        `<span style="transform:rotate(${i * 8.3}deg)">${char}</span>`
).join('');


