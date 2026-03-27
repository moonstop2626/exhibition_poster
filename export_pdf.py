import subprocess
import sys
import os

# ─── Configuration ────────────────────────────────────────────
URL = "https://moonstop2626.github.io/exhibition_poster/exhibition_poster_2.html"
OUTPUT = "P-Tech_Product_Range.pdf"

# Custom size: 2900mm x 1900mm Landscape
PAGE_WIDTH  = 2900  # mm
PAGE_HEIGHT = 1900  # mm
ZOOM        = 1.0   # increase if content is too small (e.g. 1.5)
DPI         = 300   # print quality (300 recommended for large format)

# wkhtmltopdf path — auto-detects Windows or Linux/Mac
WKHTMLTOPDF = (
    r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
    if os.name == "nt"
    else "wkhtmltopdf"
)
# ──────────────────────────────────────────────────────────────

def convert():
    cmd = [
        WKHTMLTOPDF,
        "--page-width",  f"{PAGE_WIDTH}mm",
        "--page-height", f"{PAGE_HEIGHT}mm",
        "--dpi",         str(DPI),
        "--zoom",        str(ZOOM),
        "--orientation", "Landscape",
        "--no-stop-slow-scripts",
        "--javascript-delay", "2000",   # wait 2s for JS to render
        "--load-error-handling", "ignore",
        "--enable-local-file-access",
        "--margin-top",    "0mm",
        "--margin-bottom", "0mm",
        "--margin-left",   "0mm",
        "--margin-right",  "0mm",
        URL,
        OUTPUT
    ]

    print(f"Converting : {URL}")
    print(f"Page size  : {PAGE_WIDTH}mm x {PAGE_HEIGHT}mm (Landscape)")
    print(f"DPI        : {DPI}")
    print(f"Output     : {OUTPUT}")
    print("Please wait...")

    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode == 0:
        print(f"\n✅ Done! PDF saved as: {OUTPUT}")
    else:
        print(f"\n❌ Error:\n{result.stderr}")
        sys.exit(1)

if __name__ == "__main__":
    convert()