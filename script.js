// $('.filters ul li').click(function(){
//   $('.filters ul li').removeClass('active');
//   $(this).addClass('active');
  
//   var data = $(this).attr('data-filter');
//   $grid.isotope({
//     filter: data
//   })
// });

// var $grid = $(".grid").isotope({
//   itemSelector: ".all",
//   percentPosition: true,
//   masonry: {
//     columnWidth: ".all"
//   }
// })

// Gallery: https://www.foolishdeveloper.com/2021/09/responsive-filterable-image-gallery.html
// Slideshows: https://codepen.io/imoaazahmed/pen/BwKdQQ

// Enlarge image: https://stackoverflow.com/questions/67815853/how-do-i-make-an-image-full-screen-on-click

// GALLERY FILTERING //
// TODO: support multiple galleries on a page.

// Get the (one) gallery's filter filter-items.
const filterContainer = document.querySelector(".gallery .gallery-filter"),
	galleryItems = document.querySelectorAll(".gallery .filter-item");

// Create event listeners for filter buttons to affect visibility of filtered gallery items.
if (filterContainer != null) {
	filterContainer.addEventListener("click", (event) => {
		if (event.target.classList.contains("filter-button")) {
			// deactivate existing active 'filter-item'
			filterContainer.querySelector(".active").classList.remove("active");
			// activate new 'filter-item'
			event.target.classList.add("active");
			const filterValue = event.target.getAttribute("data-filter");
			galleryItems.forEach((galleryItem) => {
				// Hide all items.
				galleryItem.classList.remove("show");
				galleryItem.classList.add("hide");
				// Show all items that match the filter.
				if (galleryItem.classList.contains(filterValue)/* || filterValue === 'all'*/) {
					galleryItem.classList.remove("hide");
					galleryItem.classList.add("show");
				}
			});
		}
	});
}

// SLIDESHOW SLIDING //
// TODO: support multiple slideshows on a page.

// Get the slides and dots, and track the index.
var slideIndex = 0;
var slides = document.querySelectorAll('.slideshow .slide'),
	dots = document.querySelectorAll('.slideshow .dot');

// Don't do slides stuff if there is no slideshow, or a slideshow but with no images.
if (slides != null) {
	if (slides.length > 0) {
		showSlide(slideIndex);
	}
}

// Clamp slideshow index to min/max values.
function clampSlideshowIndex(index, slideCount) {
	// Prevent index from being out of bounds (1 to slide count).
	var clampedIndex = index;
	if (clampedIndex >= slideCount) {
		clampedIndex = slideCount - 1;
	}
	if (clampedIndex < 0) {
		clampedIndex = 0;
	}

	return clampedIndex;
}

// Display the first image.
function showSlide(index) {
	'use strict';
	
	slideIndex = clampSlideshowIndex(index, slides.length);

	// Fix dots if their count doesn't match that of slides..
	if (slides.length != dots.length) {
		if (slides.length > dots.length) {
			// Add dots.
			for (var i = dots.length; i < slides.length; i++) {
				const dotsContainer = document.querySelector('.slideshow .dots-container');

				var newDotHTML = '\n' + dots[0].outerHTML;
				newDotHTML = newDotHTML.replace('0', `${i}`);
				newDotHTML = newDotHTML.replace(' active', '');

				dotsContainer.innerHTML += newDotHTML;
			}
		} else if (dots.length > slides.length) {
			// Remove dots.
			for (var i = slides.length; i < dots.length; i++) {
				dots[i].style.display = 'none';
			}
		}
		slides = document.querySelectorAll('.slideshow .slide');
		dots = document.querySelectorAll('.slideshow .dot');
	}

	// Change other slides to show/hide;
	for (var i = 0; i < slides.length; i++) {
		slides[i].classList.remove('show');
		slides[i].classList.add('hide');
	}
	slides[slideIndex].classList.remove('hide');
	slides[slideIndex].classList.add('show');

	// Remove active class from other dots.
	for (var i = 0; i < dots.length; i++) {
		dots[i].classList.remove('active');
	}
	dots[slideIndex].classList.add('active');

	// Do a check. If there's only 1 slide, remove the slideshow control elements.
	if (slides.length <= 1) {
		var slideshowControls = document.querySelector('.slideshow .previous, .slideshow .next, .slideshow .dots-container');
		slideshowControls.parentNode.removeChild(slideshowControls);
	}
}
	
// Next or previous slide.
function incrementSlideshowIndex(increment) {
	'use strict';
	slideIndex += increment;
	showSlide(slideIndex);
}

// Slide selecting using dots.
function setSlideshowIndex(index) {
	'use strict';
	slideIndex = clampSlideshowIndex(index, slides.length);
	showSlide(slideIndex);
}