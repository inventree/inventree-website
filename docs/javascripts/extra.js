/* Mount image carousels (see the 'gallery' macro in main.py).
 * 'document$' fires on every page load, including instant navigation. */
document$.subscribe(function () {
	document.querySelectorAll('.splide.iv-gallery').forEach(function (element) {
		new Splide(element, {
			type: 'loop',
			perMove: 1,
			perPage: parseInt(element.dataset.perPage || '1', 10),
			breakpoints: { 720: { perPage: 1 } },
			autoplay: true,
			pagination: false,
		}).mount();
	});
});
