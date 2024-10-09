
$(".form_button-show").bind("click", function(e){
    const target = document.querySelector(".form_button-show");
    target.classList.toggle("active");
    target.nextElementSibling.classList.toggle("active");
});