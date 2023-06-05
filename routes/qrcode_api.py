import io
import traceback
import typing

import cv2
import fastapi
import numpy
import qrcode

from .types import Colors, ErrorCorrection, Formats

ext = fastapi.APIRouter(
    prefix="/qrcode", default_response_class=fastapi.responses.StreamingResponse
)


@ext.get(
    "/data",
    responses={
        200: {
            "description": "Returns a QR code image based on what format user gives.",
            "content": {
                "image/*": {},
            },
        },
        500: {
            "description": "Internal server error.",
            "content": {
                "application/json": {"example": {"error": "Internal server error."}}
            },
        },
    },
)
async def data(
    data: typing.Union[str, bytes],
    format: Formats = Formats.PNG,
    version: int = 1,
    error_correction: ErrorCorrection = ErrorCorrection.L,
    box_size: int = 10,
    border: int = 4,
    fit: bool = True,
    optimize: int = 20,
    front_color: typing.Union[Colors, str] = "black",
    back_color: typing.Union[Colors, str] = "white",
):
    """
    Returns a QR code image based on what format user gives.  
    Data can be either a string or bytes. (You must encode bytes yourself before passing it to this endpoint.)  
    For front color/back color, you can either pass a string (Will be validated. Explaination below.) or a Colors enum.  
    ### Validating strings:
    Front color/back color must be a valid color name. (See: https://pillow.readthedocs.io/en/stable/reference/ImageColor.html#color-names)  
    Or you can pass a hex color code. (See: https://pillow.readthedocs.io/en/stable/reference/ImageColor.html#color-names)  
    Or you can pass a RGB color code. (Ex: 255,255,255)  
    Or you can pass a HSL color function. (Ex: hsl(0,100%,50%))  
    Or you can pass a HSV color function. (Ex: hsv(0,100%,100%))  
    Or you can pass a RGB color function. (Ex: rgb(255,255,255))  
    Or you can pass an enum provided.  
    """

    try:
        qr = qrcode.QRCode(
            version=version,
            error_correction=error_correction.value,
            border=border,
            box_size=box_size,
        )
        qr.add_data(data, optimize=optimize)
        qr.make(fit=fit)
        bytes_image = io.BytesIO()
        qr.make_image(fill_color=front_color, back_color=back_color).save(
            bytes_image, format=format.value
        )
        return fastapi.responses.StreamingResponse(
            io.BytesIO(bytes_image.getvalue()),
            media_type=f"image/{format.value}",
            status_code=200,
        )
    except Exception as e:
        traceback.print_exc()
        return fastapi.responses.JSONResponse(
            status_code=500, content={"error": str(e)}
        )


@ext.post(
    "/read",
    responses={
        200: {
            "description": "Returns the data from the QR code image.",
            "content": {
                "text/plain": {},
                "application/octet-stream": {},
            },
        },
        500: {
            "description": "Internal server error.",
            "content": {
                "application/json": {"example": {"error": "Internal server error."}}
            },
        },
    },
)
async def read(qr_pic: fastapi.UploadFile):
    """
    Accepts a QR code image and returns the data from the QR code image.
    """
    try:
        img = cv2.imdecode(
            numpy.fromstring(await qr_pic.read(), numpy.uint8), cv2.IMREAD_UNCHANGED
        )
        detector = cv2.QRCodeDetector()
        data, _, _ = detector.detectAndDecode(img)
        return fastapi.responses.PlainTextResponse(data, status_code=200)
    except Exception as e:
        traceback.print_exc()
        return fastapi.responses.JSONResponse(
            status_code=500, content={"error": str(e)}
        )
