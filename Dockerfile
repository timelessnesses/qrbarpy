FROM python:3.10-alpine

LABEL maintainer="Rukchad Wongprayoon <timelessnesses@timelessnesses.me>"
LABEL version="0.1.0"
LABEL description="timelessnesses.api.qrbarpy is a QR code/Barcode generator/reader API."
LABEL repository="https://github.com/timelessnesses/qrbarpy"
LABEL homepage="https://github.com/timelessnesses/qrbarpy"


WORKDIR /app
COPY . /app

# FOR THE LOVE OF GOD RELEASE ALPINE BUILDS WITH MUSL
# libzbar for pyzbar

RUN apk add --no-cache --virtual .build-deps gcc musl-dev g++ ninja cmake libzbar

RUN pip install -r requirements.txt
RUN apk del .build-deps gcc musl-dev g++ ninja cmake # saving spaces
EXPOSE 8000
CMD ["uvicorn", "main:app"]