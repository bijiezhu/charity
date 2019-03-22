$(document).ready(function() {

  this.querySelectorAll('.modal-button').forEach(function(el) {
    el.addEventListener('click', function() {
      console.log('clicked')
      var target = document.querySelector(el.getAttribute('data-target'));

      target.classList.add('is-active');

      target.querySelector('.modal-close').addEventListener('click',   function() {
          target.classList.remove('is-active');
       });
    });
  });

});
