$(document).ready(function () {
    /*登录按钮 click 事件*/
    $(".btn1-l").click(function () {
        window.location.href = 'consumer/login/'
    });

    /*注册按钮 click 事件*/
    $(".btn1-r").click(function () {
        window.location.href='consumer/Register/'
    });

    /*切换城市 click 事件*/
    $(".dianji-qh").click(function () {
        $(".select-city").show();
    });
    $(".close-select-city").click(function () {
        $(".select-city").hide();
    });
    $(".sl-city-con dd a").click(function () {
        var dqm = $(this).text();
        $(".dqm").text(dqm);
        $(".select-city").hide();
    });

//轮播图
    var tu = 0;
    var spend = 1000;
    /*点击  右侧*/
    $(".bnr-right").click(function () {
        dsq();
    });
    /*点击  左侧*/
    $(".bnr-left").click(function () {
        tu--;
        if (tu < 0) {
            tu = 4;
            $(".banner ul").css("left", -6000);
        }
        $(".banner ul").animate({"left": -tu * 1200}, spend);
    });
    /*定时器 开启*/
    var time = setInterval(dsq, 2000);

    function dsq() {
        tu++;
        if (tu > 5) {
            tu = 1;
            $(".banner ul").css("left", 0);
        }
        $(".banner ul").animate({"left": -tu * 1200}, spend);
    }

    $(".banner").hover(function () {
        clearInterval(time);
    }, function () {
        clearInterval(time);
        time = setInterval(dsq, 2000);
    });
//轮播图 END
});
