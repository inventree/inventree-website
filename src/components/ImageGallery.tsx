import { Splide, SplideSlide } from '@splidejs/react-splide';

// Default theme
import '@splidejs/react-splide/css';


type GalleryImage = {
    src: string;
    alt?: string;
    title?: string;
};

export default function ImageGallery({
    images,
    title,
}: {
    images: GalleryImage[];
    title?: string;
}) {

    return (
        <Splide aria-label={title ?? "Image Gallery"}>
            {images.map((image, idx) => (
                <SplideSlide key={idx}>
                    <img src={image.src} alt={image.alt} title={image.title} />
                </SplideSlide>
            ))}
        </Splide>
    );
}