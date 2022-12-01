window.onload = function () {
	let slideIndex = 1;
	showSlides(slideIndex);
	updateGalleryFilters();
}

// SLIDESHOW
// TODO: Support more than one slideshow on a page.

let slideIndex = 1;
showSlides();

function changeSlide(n) {
	slideIndex += n;
	showSlides();
}

function setSlide(n) {
	slideIndex = n;
	showSlides();
}

function showSlides() {
	// Change slide.
	let slides = document.querySelectorAll('.slideshow .slides .slide');
	if (slides != null) {
		if (slideIndex > slides.length) {
			slideIndex = 1;
		}
		if (slideIndex < 1) {
			slideIndex = slides.length;
		}
		for (let i = 0; i < slides.length; i++) {
			slides[i].style.display = "none";
		}
		slides[slideIndex - 1].style.display = "block";
	}

	// Update dots.
	let dots = document.querySelectorAll('.slideshow .dots .dot');
	if (dots != null) {
		for (let i = 0; i < dots.length; i++) {
			dots[i].className = dots[i].className.replace(" active", "");
		}
		dots[slideIndex - 1].className += " active";
	}

	// Update numbers.
	let number = document.querySelector('.slideshow .overlay .number');
	if (number != null) {
		number.innerHTML = slideIndex + " / " + slides.length;
	}

	// Show/hide next/previous buttons.
	let previous = document.querySelector('.slideshow .overlay .previous');
	if (previous != null) {
		if (slideIndex == 1) {
			previous.style.display = "none";
		} else {
			previous.style.display = "block";
		}
	}
	let next = document.querySelector('.slideshow .overlay .next');
	if (next != null) {
		if (slideIndex == slides.length) {
			next.style.display = "none";
		} else {
			next.style.display = "block";
		}
	}
}

// MODAL

let modal = document.querySelector('#modal');
let modalContent = document.querySelector('#modal #modal-content');

// Click image to open modal.
function openModal(image) {
	modal.style.pointerEvents = "auto";
	modal.style.opacity = "1";
	modalContent.src = image.src;
	modalContent.alt = image.alt;
}

// Modal close button.
function closeModal() {
	modal.style.pointerEvents = "none";
	modal.style.opacity = "0";
}

// Click a modal's image again to open it in a new tab.
function openImage(image) {
	var newWindow = window.open(image.src);
}

// GALLERY
// TODO: Support more than one gallery on a page.

function toggleGalleryFilter(filter) {
	// Toggle filter button (active).
	if (filter.classList.contains('active')) {
		filter.classList.remove('active');
	} else {
		filter.className += " active";
	}

	updateGalleryFilters();
}

let galleryFilters = document.querySelectorAll('#gallery-filters .filter');
let allFilter = document.querySelector('#gallery-filters .filter.all');

function updateGalleryFilters() {
	// Get the filter tag IDs.
	let activeGalleryTagIds = [];
	for (let i = 0; i < galleryFilters.length; i++) {
		if (galleryFilters[i].classList.contains('active')) {
			let tagId = galleryFilters[i].getAttribute('data-filter')
			activeGalleryTagIds.push(tagId);
		}
	}

	// Show all gallery items if no tags are selected.
	if (activeGalleryTagIds.length == 0) {
		allFilter.classList.add('active');
		activeGalleryTagIds.push('all');
	}

	// Show/hide gallery items based on filter tag IDs.
	let galleryItems = document.querySelectorAll('#gallery-items .gallery-item');
	for (let i = 0; i < galleryItems.length; i++) {
		let galleryItem = galleryItems[i];
		galleryItem.classList.add('show');
		for (let j = 0; j < activeGalleryTagIds.length; j++) {
			let filterTagId = activeGalleryTagIds[j];
			if (!galleryItem.getAttribute('data-filter').includes(filterTagId)) {
				galleryItem.classList.remove('show');
				break;
			}
		}
	}
}

// Gallery image lazy loading (use <img loading="lazy"> instead).
/*
(function () {
	let images = document.querySelectorAll('#gallery-items .gallery-item img[data-src]');
	let index = 0;
	
	let lazyLoad = function () {
		if (index >= images.length) {
			return;
		}
		let image = images[index];
		if ((this.scrollY + this.innerHeight) > image.offsetTop) {
			let src = image.getAttribute('data-src');
			console.log('Loaded: ' + src);
			image.src = src;
			image.addEventListener('load', function () {
				// image.removeAttribute('data-src');
			});
			index += 1;
			lazyLoad();
		} else {
			image.src = "";
			console.log('Unoaded: ' + image.getAttribute('data-src'));
		}
	};

	let init = function () {
		window.addEventListener('scroll', lazyLoad);
		lazyLoad();
	};
	return init();
})();
*/