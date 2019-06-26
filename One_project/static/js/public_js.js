$(document).ready(function () {
    /*点击显示二维码 */
    $(".erweima").click(function () {
        $(".ewm-tu").toggle();
    });

    /*商品分类快捷 click 事件*/
    $("[kj]").click(function () {
        $("[kj-sh]").toggle();
    });

    $("[mg]").hover(function () {
        $(this).addClass("hover-show-bg");
        var a1 = $(this).attr("mg");
        $("[mg2=" + a1 + "]").show();
    }, function () {
        $(this).removeClass("hover-show-bg");
        var a1 = $(this).attr("mg");
        $("[mg2=" + a1 + "]").hide();
    });

    /*search 切换*/
    $("[ss-search]").click(function () {
        $(this).addClass('current').siblings().removeClass("current");
        var sh = $(this).attr("ss-search");
        $("[ss-search-show=" + sh + "]").show().siblings().hide();
    });
});
