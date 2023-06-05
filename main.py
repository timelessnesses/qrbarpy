import fastapi

import routes

app = fastapi.FastAPI(
    title="timelessnesses.api.qrbarpy",
    description="An API for generating QR codes/Barcodes with Python.",
    docs_url="/",
)

app.include_router(routes.qr_code.ext)
app.include_router(routes.barcode_api.ext)
