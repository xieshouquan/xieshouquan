var cache = window.document.getElementById('code_img');
cache.onclick = function () {
    this.scr = "/consumer/get_code/?rnd=" + Math.random();
};
$('#btn_register').click(function () {
    $.ajax({
        url: '/consumer/Register/',
        type: 'post',
        data: new FormData($('#register_form')[0]),
        cache: false,
        processData: false,
        contentType: false,
        success: function (data) {
            if (data.status == 'fail') {
                $('#my_error').text(data.msg)
            } else if (data.status == 'form_error') {
                $('#my_error').text(data.msg)
            } else if (data.status == 'success') {
                window.location.href = '/consumer/Login/';
            }
        }
    })
});

