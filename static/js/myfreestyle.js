
$(document).ready(function () {
    var input_box = $('#search_box');//输入框
    var ul_ = $('ul.list');//待选列表
    var btn_ = $('#search_button');//按钮
    var p= $('#explain');//解释文本框

    //输入框信息改变时
    input_box.on('input propertychange', function() {
        p.hide();
        var kw_ = $.trim(input_box.val());
        if(kw_){
            $.get("/search/?kw="+kw_, function (data, status) {
                    if (status == 'success' && data!='false') {
                        //alert(data);
                        var json = JSON.parse(data);
                        //alert(json);
                        ul_.empty();
                        if(json.length > 0){
                            $.each(json, function(i,item){
                                var li_=$('<li><a href="#">'+item['words']+'</a></li>').appendTo(ul_);
                            });
                        }
                        ul_.show();
                    } else {
                        ul_.empty();
                        $('<li><a href="#">'+'没有这个词'+'</a></li>').appendTo(ul_);
                        ul_.show();
                    }
                });
        }else{
            ul_.hide();
        }
    });
    //输入框失去焦点后 隐藏待选列表
    input_box.blur(function(){
        ul_.hide();
    });
    //输入框获得焦点, 如果有内容就显示待选列表
    input_box.on('focus click',(function(){
        if(input_box.val()=='没有这个词'){
            input_box.val('');
        }
        input_box.val()?ul_.show():ul_.hide();
    }));
    //待选列表鼠标滑入划出
    ul_.on('mouseenter','li',(function(){
        $(this).css("background-color","#999999");
        $('#input_box').val($(this).text());//鼠标滑到那个待选词就把这个词放在输入框
    }));
    ul_.on('mouseleave','li',(function(){
        $(this).css("background-color","#ffffff");
    }));

    //点击查询按钮
    btn_.on('click',function(){
        var kw_ = $.trim(input_box.val());
        if(kw_){
            $.get("/match/?kw="+kw_, function (data, status) {
                    if (status == 'success' && data!='false') {
                        var json = JSON.parse(data);
                        p.empty();
                        p.text(json[0]['fields']['explain']);
                        p.show();
                    } else {
                        p.empty();
                        p.text('没有解释');
                        p.show();
                    }
                });
        }else{
            p.empty();
            p.text('请输入词语!');
            p.show();
        }
    });

});