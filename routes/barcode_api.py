import io
import traceback
import typing

import barcode
import barcode.writer
import cv2
import fastapi
import numpy
import pyzbar.pyzbar

from .types import BarcodeFormat, BarcodeOutputSelection

ext = fastapi.APIRouter(
    prefix="/barcode", default_response_class=fastapi.responses.StreamingResponse
)


@ext.get(
    "/data",
    responses={
        200: {
            "description": "Returns a Barcode image based on what format user gives.",
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
    data: str,
    format: BarcodeFormat,
    file_type: BarcodeOutputSelection = BarcodeOutputSelection.PNG,
):
    """
    A route for generating a barcode image.
    """
    try:
        img = io.BytesIO()

        barcode_class = format.convert(format)
        print("generate")
        barcode_class(
            data, writer=barcode.writer.ImageWriter(format=file_type.value)
        ).write(img)
        img.seek(0)
        return fastapi.responses.StreamingResponse(
            img, media_type=f"image/{file_type.value}"
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
            "description": "Returns the data(s) from the Barcode image.",
            "content": {
                "application/json": {"example": ["Hello, World!", "Among us."]}
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
async def read(file: fastapi.UploadFile):
    """
    A route for reading a barcode image.
    """
    try:
        img = cv2.imdecode(
            numpy.fromstring(await file.read(), numpy.uint8), cv2.IMREAD_UNCHANGED
        )
        return fastapi.responses.ORJSONResponse(
            content=[i.data.decode("utf-8") for i in pyzbar.pyzbar.decode(img)]
        )
    except Exception as e:
        traceback.print_exc()
        return fastapi.responses.JSONResponse(
            status_code=500, content={"error": str(e)}
        )
