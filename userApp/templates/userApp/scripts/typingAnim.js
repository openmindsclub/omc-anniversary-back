
const viewportObserver = new IntersectionObserver((entries, observer) => {
    if (entries[0].isIntersecting) {
        var typed3 = new Typed('#typed3', {
            strings: [`We're celebrating the 15th anniversary of Open Minds club!`],
            typeSpeed: 50,
            backSpeed: 0,
            fadeOut: true,
            showCursor: true,

            cursorChar: " ",
        });
        observer.unobserve(document.querySelector('#typed3'))
    }
})


viewportObserver.observe(document.querySelector('#typed3'));