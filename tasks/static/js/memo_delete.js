document.addEventListener("DOMContentLoaded", function () {
    const btn = document.getElementById("delete-btn");
    const memoId = btn.dataset.memoId;

    btn.addEventListener("click", function () {
        if (confirm("本当に削除しますか？")) {
            fetch(`/memo/${memoId}/delete/`, {
                method: "DELETE",
                headers: {
                    "X-CSRFToken": getCookie("csrftoken")
                }
            })
            .then(response => response.json())
            .then(data => {
                alert(data.message);
                window.location.href = "/memos/";
            });
        }
    });

    function getCookie(name) {
        const cookieValue = document.cookie
            .split('; ')
            .find(row => row.startsWith(name + '='))
            ?.split('=')[1];
        return cookieValue;
    }
});
