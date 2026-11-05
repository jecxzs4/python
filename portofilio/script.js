
// ANIMASI TYPING
const typingElement = document.getElementById("typing");

const words = [
    "Web Developer",
    "PPLG Student",
    "Programmer",
    "Tech Enthusiast"
];

let wordIndex = 0;
let charIndex = 0;
let deleting = false;

function typingEffect() {

    const currentWord = words[wordIndex];

    if (deleting) {
        charIndex--;
    } else {
        charIndex++;
    }

    typingElement.textContent =
        currentWord.substring(0, charIndex);

    let speed = deleting ? 60 : 120;

    if (!deleting && charIndex === currentWord.length) {
        deleting = true;
        speed = 1200;
    }

    else if (deleting && charIndex === 0) {
        deleting = false;
        wordIndex = (wordIndex + 1) % words.length;
        speed = 400;
    }

    setTimeout(typingEffect, speed);
}

typingEffect();


// MOBILE MENU
const menuBtn = document.getElementById("menuBtn");
const navLinks = document.getElementById("navLinks");

menuBtn.addEventListener("click", function() {
    navLinks.classList.toggle("active");
});

// TUTUP MENU SETELAH LINK DIKLIK
document.querySelectorAll(".nav-links a").forEach(link => {
    link.addEventListener("click", function() {
        navLinks.classList.remove("active");
    });
});


// ANIMASI SCROLL
const cards = document.querySelectorAll(
    ".project-card, .skill-card, .about-card"
);

const observer = new IntersectionObserver(entries => {

    entries.forEach(entry => {

        if (entry.isIntersecting) {
            entry.target.style.opacity = "1";
            entry.target.style.transform = "translateY(0)";
        }

    });

}, {
    threshold: 0.15
});

cards.forEach(card => {

    card.style.opacity = "0";
    card.style.transform = "translateY(30px)";
    card.style.transition = "0.7s ease";

    observer.observe(card);

    
// PROJECT MODAL
const projectCards = document.querySelectorAll(".project-card");

const projectModal = document.getElementById("projectModal");
const closeModal = document.getElementById("closeModal");

const modalTitle = document.getElementById("modalTitle");
const modalDescription = document.getElementById("modalDescription");
const modalTech = document.getElementById("modalTech");
const modalLink = document.getElementById("modalLink");

function openProject(card) {

    modalTitle.textContent = card.dataset.title;
    modalDescription.textContent = card.dataset.description;
    modalTech.textContent = card.dataset.tech;

    modalLink.href = card.dataset.link;

    projectModal.classList.add("active");
}

projectCards.forEach(card => {

    card.addEventListener("click", () => {
        openProject(card);
    });

    card.addEventListener("keydown", event => {
        if (event.key === "Enter" || event.key === " ") {
            event.preventDefault();
            openProject(card);
        }
    });

});

closeModal.addEventListener("click", () => {
    projectModal.classList.remove("active");
});

projectModal.addEventListener("click", event => {

    if (event.target === projectModal) {
        projectModal.classList.remove("active");
    }

});

document.addEventListener("keydown", event => {

    if (event.key === "Escape") {
        projectModal.classList.remove("active");
    }

});



});

// PROJECT MODAL
const projectCards = document.querySelectorAll(".project-card");

const projectModal = document.getElementById("projectModal");
const closeModal = document.getElementById("closeModal");

const modalTitle = document.getElementById("modalTitle");
const modalDescription = document.getElementById("modalDescription");
const modalTech = document.getElementById("modalTech");
const modalLink = document.getElementById("modalLink");

function openProject(card) {

    modalTitle.textContent = card.dataset.title;
    modalDescription.textContent = card.dataset.description;
    modalTech.textContent = card.dataset.tech;

    modalLink.href = card.dataset.link;

    projectModal.classList.add("active");
}

projectCards.forEach(card => {

    card.addEventListener("click", () => {
        openProject(card);
    });

    card.addEventListener("keydown", event => {
        if (event.key === "Enter" || event.key === " ") {
            event.preventDefault();
            openProject(card);
        }
    });

});

closeModal.addEventListener("click", () => {
    projectModal.classList.remove("active");
});

projectModal.addEventListener("click", event => {

    if (event.target === projectModal) {
        projectModal.classList.remove("active");
    }

});

document.addEventListener("keydown", event => {

    if (event.key === "Escape") {
        projectModal.classList.remove("active");
    }

});

