FROM alpine:latest

LABEL maintainer="Rukchad Wongprayoon <timelessnesses@timelessnesses.me>"
LABEL version="0.1.0"
LABEL description="timelessnesses.api.qrbarpy is a QR code/Barcode generator/reader API."
LABEL repository="https://github.com/timelessnesses/qrbarpy"
LABEL homepage="https://github.com/timelessnesses/qrbarpy"


WORKDIR /app
COPY . /app

# FOR THE LOVE OF GOD RELEASE ALPINE BUILDS WITH MUSL
# libzbar for pyzbar

RUN apk add --virtual .build gcc musl-dev g++ ninja cmake python3-dev && apk add libzbar libuv py3-opencv python3 py3-pip && python3 -m pip install --upgrade pip && pip install -v fastapi uvicorn[standard] qrcode[pil] python-barcode[images] python-multipart pyzbar orjson && apk del .build && rm -rf "$(pip cache dir)"/*
EXPOSE 8000/tcp
EXPOSE 8000/udp
CMD ["python3","-m","uvicorn", "main:app", "--host","0.0.0.0"]
