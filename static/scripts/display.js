window.addEventListener('load', () => {
     setTimeout(() => {
         const lines = document.querySelectorAll('.hidden-line');
         lines.forEach((line, index) => {
             setTimeout(() => {
                 line.classList.add('visible-line')
             ;}, index * 1000);
         });
     }, 500);
});