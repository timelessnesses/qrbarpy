# timelessnesses.api.qrbarpy

`qrbarpy` is a Python webserver that generates QR codes and barcodes.

## Installation

### Requirements

1. Python 3.8 or higher
2. poetry (`pip install poetry`)
3. zbar (`apt install libzbar0` for ubuntu/debian. Else look it up for your OS.)

### Install

1. Clone this repository
2. Run `poetry install`
3. Run `poetry run uvicorn qrbarpy.main:app --reload`

## API Usage

All of the documentations/values/possible return types and errors can be found at index.
