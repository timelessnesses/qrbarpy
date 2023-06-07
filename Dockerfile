
FROM alpine:latest

LABEL maintainer="Rukchad Wongprayoon <timelessnesses@timelessnesses.me>"
LABEL version="0.1.0"
LABEL description="timelessnesses.api.qrbarpy is a QR code/Barcode generator/reader API."
LABEL repository="https://github.com/timelessnesses/qrbarpy"
LABEL homepage="https://github.com/timelessnesses/qrbarpy"

WORKDIR /app

# Install necessary packages
RUN apk add --no-cache \
    gcc \
    musl-dev \
    g++ \
    ninja \
    cmake \
    python3-dev \
    libzbar \
    yaml-dev \
    py3-opencv \
    python3 \
    py3-pip \
 && python3 -m pip install --upgrade pip \
 && pip install --no-cache-dir --upgrade fastapi uvicorn[standard] uvloop qrcode[pil] python-barcode[image] python-multipart pyzbar orjson \
 && apk del gcc musl-dev g++ ninja cmake python3-dev yaml-dev \
 && rm -rf /var/cache/apk/*

EXPOSE 8000/tcp
EXPOSE 8000/udp

COPY . /app

CMD ["python3", "-m", "uvicorn", "main:app", "--host", "0.0.0.0"]
