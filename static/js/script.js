document.addEventListener("DOMContentLoaded", function() {
    let burger = document.querySelector(".header__burger");
    burger.addEventListener("click", function(event) {
      burger.classList.toggle("active");
      document.querySelector(".header__menu").classList.toggle("active");
      document.querySelector("body").classList.toggle("lock");
    });
  });
