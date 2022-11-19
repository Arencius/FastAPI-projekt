import io
from fastapi import File, APIRouter
from fastapi.responses import StreamingResponse
from PIL import Image, ImageOps


image_inversion_router = APIRouter()


@image_inversion_router.post('/picture/invert')
def invert_image(image: bytes = File()):
    image = Image.open(io.BytesIO(image))

    inverted_image = ImageOps.invert(image)
    response_image = io.BytesIO()
    inverted_image.save(response_image, "JPEG")
    response_image.seek(0)

    return StreamingResponse(response_image, media_type="image/jpeg")