$(".acc").submit(function(e){
    e.preventDefault();
    var action_url = $(this).attr("action")
    var $that = $(this),
    formData = new FormData($that.get(0));
    $.ajax({
        type: "POST",
        url: action_url,
        data: formData,
        contentType: false,
        processData: false,
        success: function(response){
            if ("error" in response){
                inputs = document.querySelectorAll("input")
                errors = document.querySelectorAll(".input_error")
                for (let index = 0; index < errors.length; index++) {
                    $(errors[index]).html($(errors[index]).html().replace($(errors[index]).text(),''));
                }
                for (let index = 0; index < inputs.length; index++) {
                    inputs[index].classList.remove("invalidate")
                }
                for (let key in response["error"]){
                    document.querySelector('input[name='+key+']').classList.add("invalidate");
                    $('#'+key).text(response["error"][key])
                }
            }
            else if ("invalid_account" in response) {
                document.querySelector('#username_login').classList.remove("invalidate");
                document.querySelector('#username_login').nextElementSibling.innerHTML = " "
                document.querySelector('#username_login').classList.add("invalidate");
                document.querySelector('#username_login').nextElementSibling.innerHTML = response["invalid_account"]
            }
            else if("html" in response){
                $(".figures").prepend(response["html"]);
            }
            else{
                location=response["success_link"];
            }

        }
    })
})

const container = document.querySelector('.form_body')
if (container){
container.addEventListener('click', function(e) {
	const target = e.target;
	if (target.classList.contains('button')) {
        buttons = document.querySelectorAll('.button')
        for (let i = 0; i < buttons.length; i++) {
            buttons[i].classList.remove('active')
        }
        forms = document.querySelectorAll('.form')
        for (let i = 0; i < forms.length; i++) {
            forms[i].classList.remove("active")
        }
        for (let i = 0; i < forms.length; i++) {
            for (let j = 0; j < forms[i].classList.length; j++) {
                for (let k = 0; k < target.classList.length; k++) {
                    if (forms[i].classList[j] == target.classList[k]) {
                        forms[i].classList.toggle('active')
                    }
                }
            }
        }
		target.classList.toggle('active')
	}
})
}
