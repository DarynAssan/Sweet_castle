const modal = document.querySelector(".modal");
const modalContent = document.querySelector(".modal__content");
const close = document.querySelector(".modal__close");
const modalImg = document.querySelector(".modal__img");
const productList = document.querySelectorAll(".product__list");
const title = document.querySelector(".detail__title");
const cost = document.querySelector(".detail__price");
const qur = document.querySelector(".detail__description");



productList.forEach((list, index) => {
  const view = list.querySelector(".product__viewBtn");
  const costs = list.querySelector(".detail__prices");
  const qura = list.querySelector(".detail__descriptions");
  const productImg = list.querySelector(".product__img").getAttribute("src");

  view.addEventListener("click", () => {
    modal.classList.add("modal--bg");
    modalContent.classList.add("modal__content--show");
    modalImg.setAttribute("src", productImg);
    title.innerText = view.textContent;
    cost.innerText = costs.textContent;
    qur.innerText = qura.textContent;
  });
});

close.addEventListener("click", () => {
  modal.classList.remove("modal--bg");
  modalContent.classList.remove("modal__content--show");
});

modal.addEventListener("click", () => {
  modal.classList.remove("modal--bg");
  modalContent.classList.remove("modal__content--show");
});
