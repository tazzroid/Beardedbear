const btn = document.getElementById("menuBtn");
const nav = document.getElementById("primaryNav");

if (btn && nav) {
  btn.addEventListener("click", () => {
    const open = nav.classList.toggle("is-open");
    btn.setAttribute("aria-expanded", open ? "true" : "false");
  });
}
const words = document.querySelectorAll(".rotate-word");
let currentWord = 0;

setInterval(() => {
  words[currentWord].classList.remove("is-visible");
  currentWord = (currentWord + 1) % words.length;
  words[currentWord].classList.add("is-visible");
}, 2200);
const metaWords = document.querySelectorAll(".meta-word");
let currentMetaWord = 0;

setInterval(() => {
  metaWords[currentMetaWord].classList.remove("is-visible");
  currentMetaWord = (currentMetaWord + 1) % metaWords.length;
  metaWords[currentMetaWord].classList.add("is-visible");
}, 3500);
