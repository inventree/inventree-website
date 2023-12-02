
import Zoom from 'react-medium-image-zoom';
import 'react-medium-image-zoom/dist/styles.css';

export default function Thumnbnail({
    src,
    title,
    height="200px",
}: {
    src: string,
    title?: string;
    height?: string;
}) {

    return (
        <Zoom>
            <div className='thumbnail-container'>
                <img src={src} alt={title ?? ""} height={height} />
            </div>
        </Zoom> 
    )
}
