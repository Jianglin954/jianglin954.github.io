var wechatModal = document.getElementById("WeChatMod");
var wechatBtn = document.querySelectorAll('[id="WeChatBtn"]');
var wechatCloseBtn = document.querySelector(".wechat-modal-close");

for (var i = 0; i < wechatBtn.length; i++) {
  wechatBtn[i].onclick = function () {
    wechatModal.style.display = "block";
  };
}

if (wechatCloseBtn) {
  wechatCloseBtn.onclick = function () {
    wechatModal.style.display = "none";
  };
}

window.onclick = function (event) {
  if (event.target == wechatModal) {
    wechatModal.style.display = "none";
  }
};
