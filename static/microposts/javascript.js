$(function () {
    // 初期表示
    // $('.comment_list').hide();

    // 詳細画面コメントクリック
    $("#comment-dots").on("click", function () {
        $(".comment_list").slideToggle();
    });
});
