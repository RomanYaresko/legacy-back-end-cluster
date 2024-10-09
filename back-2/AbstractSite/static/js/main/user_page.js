$(".ajax_button_give").bind("click", function(e){
    e.preventDefault();
    var url_bas = $(this).attr("href");
    $.ajax({
        url: url_bas,
        type: "get",
        success: function(response) {
            if ("error" in response)
            {
                alert(response["error"])
            }
            else
            {
                $(".money").text(response["cost"]+" F")
            }
        },
    });
    return false;
});
$(".ajax_button_like").bind("click", function(e){
    e.preventDefault();
    var url_bas = $(this).attr("href");
    $.ajax({
        url: url_bas,
        type: "get",
        success: function(response) {
            if ("error" in response)
            {
                alert(response["error"])
            }
            else
            {
                $("."+response["figure"]+" span").text("Likes: "+response["likes"])
            }
        },
    });
    return false;
});