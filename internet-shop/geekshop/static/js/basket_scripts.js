window.onload = function () {
    $('.basket_list').on('click', 'input[type="number"]', function (event) {
        
        $.ajax({
            url: "/basket/edit/" + event.target.name + "/" + event.target.value + "/",   
            success: function (data) {
                $('.basket_list').html(data);
            },
        });
    });   
}