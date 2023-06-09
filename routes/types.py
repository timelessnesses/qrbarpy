import enum

import barcode
import qrcode


class Formats(str, enum.Enum):

    """
    Comprehensive list of picture formats that pillow support writing.
    """

    BLP = "blp"
    BMP = "bmp"
    DDS = "dds"
    DIB = "dib"
    EPS = "eps"
    GIF = "gif"
    ICNS = "icns"
    ICO = "ico"
    IM = "im"
    JPEG = "jpeg"
    JPG = "jpg"
    MSP = "msp"
    PCX = "pcx"
    PNG = "png"
    PPM = "ppm"
    SGI = "sgi"
    SPIDER = "spider"
    TGA = "tga"
    TIFF = "tiff"
    WEBP = "webp"
    XBM = "xbm"
    PALM = "palm"
    PDF = "pdf"
    QOI = "qoi"
    XV = "xv"


class ErrorCorrection(str, enum.Enum):

    """
    Comprehensive list of error correction levels that qrcode supports.
    """

    L = qrcode.ERROR_CORRECT_L
    M = qrcode.ERROR_CORRECT_M
    Q = qrcode.ERROR_CORRECT_Q
    H = qrcode.ERROR_CORRECT_H


class Colors(str, enum.Enum):

    """
    Comprehensive list of colors that pillow supports.
    """

    ALICEBLUE = "aliceblue"
    ANTIQUEWHITE = "antiquewhite"
    AQUA = "aqua"
    AQUAMARINE = "aquamarine"
    AZURE = "azure"
    BEIGE = "beige"
    BISQUE = "bisque"
    BLACK = "black"
    BLANCHEDALMOND = "blanchedalmond"
    BLUE = "blue"
    BLUEVIOLET = "blueviolet"
    BROWN = "brown"
    BURLYWOOD = "burlywood"
    CADETBLUE = "cadetblue"
    CHARTREUSE = "chartreuse"
    CHOCOLATE = "chocolate"
    CORAL = "coral"
    CORNFLOWERBLUE = "cornflowerblue"
    CORNSILK = "cornsilk"
    CRIMSON = "crimson"
    CYAN = "cyan"
    DARKBLUE = "darkblue"
    DARKCYAN = "darkcyan"
    DARKGOLDENROD = "darkgoldenrod"
    DARKGRAY = "darkgray"
    DARKGREEN = "darkgreen"
    DARKGREY = "darkgrey"
    DARKKHAKI = "darkkhaki"
    DARKMAGENTA = "darkmagenta"
    DARKOLIVEGREEN = "darkolivegreen"
    DARKORANGE = "darkorange"
    DARKORCHID = "darkorchid"
    DARKRED = "darkred"
    DARKSALMON = "darksalmon"
    DARKSEAGREEN = "darkseagreen"
    DARKSLATEBLUE = "darkslateblue"
    DARKSLATEGRAY = "darkslategray"
    DARKSLATEGREY = "darkslategrey"
    DARKTURQUOISE = "darkturquoise"
    DARKVIOLET = "darkviolet"
    DEEPPINK = "deeppink"
    DEEPSKYBLUE = "deepskyblue"
    DIMGRAY = "dimgray"
    DIMGREY = "dimgrey"
    DODGERBLUE = "dodgerblue"
    FIREBRICK = "firebrick"
    FLORALWHITE = "floralwhite"
    FORESTGREEN = "forestgreen"
    FUCHSIA = "fuchsia"
    GAINSBORO = "gainsboro"
    GHOSTWHITE = "ghostwhite"
    GOLD = "gold"
    GOLDENROD = "goldenrod"
    GRAY = "gray"
    GREY = "grey"
    GREEN = "green"
    GREENYELLOW = "greenyellow"
    HONEYDEW = "honeydew"
    HOTPINK = "hotpink"
    INDIANRED = "indianred"
    INDIGO = "indigo"
    IVORY = "ivory"
    KHAKI = "khaki"
    LAVENDER = "lavender"
    LAVENDERBLUSH = "lavenderblush"
    LAWNGREEN = "lawngreen"
    LEMONCHIFFON = "lemonchiffon"
    LIGHTBLUE = "lightblue"
    LIGHTCORAL = "lightcoral"
    LIGHTCYAN = "lightcyan"
    LIGHTGOLDENRODYELLOW = "lightgoldenrodyellow"
    LIGHTGREEN = "lightgreen"
    LIGHTGRAY = "lightgray"
    LIGHTGREY = "lightgrey"
    LIGHTPINK = "lightpink"
    LIGHTSALMON = "lightsalmon"
    LIGHTSEAGREEN = "lightseagreen"
    LIGHTSKYBLUE = "lightskyblue"
    LIGHTSLATEGRAY = "lightslategray"
    LIGHTSLATEGREY = "lightslategrey"
    LIGHTSTEELBLUE = "lightsteelblue"
    LIGHTYELLOW = "lightyellow"
    LIME = "lime"
    LIMEGREEN = "limegreen"
    LINEN = "linen"
    MAGENTA = "magenta"
    MAROON = "maroon"
    MEDIUMAQUAMARINE = "mediumaquamarine"
    MEDIUMBLUE = "mediumblue"
    MEDIUMORCHID = "mediumorchid"
    MEDIUMPURPLE = "mediumpurple"
    MEDIUMSEAGREEN = "mediumseagreen"
    MEDIUMSLATEBLUE = "mediumslateblue"
    MEDIUMSPRINGGREEN = "mediumspringgreen"
    MEDIUMTURQUOISE = "mediumturquoise"
    MEDIUMVIOLETRED = "mediumvioletred"
    MIDNIGHTBLUE = "midnightblue"
    MINTCREAM = "mintcream"
    MISTYROSE = "mistyrose"
    MOCCASIN = "moccasin"
    NAVAJOWHITE = "navajowhite"
    NAVY = "navy"
    OLDLACE = "oldlace"
    OLIVE = "olive"
    OLIVEDRAB = "olivedrab"
    ORANGE = "orange"
    ORANGERED = "orangered"
    ORCHID = "orchid"
    PALEGOLDENROD = "palegoldenrod"
    PALEGREEN = "palegreen"
    PALETURQUOISE = "paleturquoise"
    PALEVIOLETRED = "palevioletred"
    PAPAYAWHIP = "papayawhip"
    PEACHPUFF = "peachpuff"
    PERU = "peru"
    PINK = "pink"
    PLUM = "plum"
    POWDERBLUE = "powderblue"
    PURPLE = "purple"
    RED = "red"
    ROSYBROWN = "rosybrown"
    ROYALBLUE = "royalblue"
    SADDLEBROWN = "saddlebrown"
    SALMON = "salmon"
    SANDYBROWN = "sandybrown"
    SEAGREEN = "seagreen"
    SEASHELL = "seashell"
    SIENNA = "sienna"
    SILVER = "silver"
    SKYBLUE = "skyblue"
    SLATEBLUE = "slateblue"
    SLATEGRAY = "slategray"
    SLATEGREY = "slategrey"
    SNOW = "snow"
    SPRINGGREEN = "springgreen"
    STEELBLUE = "steelblue"
    TAN = "tan"
    TEAL = "teal"
    THISTLE = "thistle"
    TOMATO = "tomato"
    TURQUOISE = "turquoise"
    VIOLET = "violet"
    WHEAT = "wheat"
    WHITE = "white"
    WHITESMOKE = "whitesmoke"
    YELLOW = "yellow"
    YELLOWGREEN = "yellowgreen"


class BarcodeFormat(str, enum.Enum):
    CODE39 = "code39"
    CODE128 = "code128"
    PZN7 = "pzn7"
    EAN13 = "ean13"
    EAN8 = "ean8"
    JAN = "jan"
    ISBN13 = "isbn13"
    ISBN10 = "isbn10"
    ISSN = "issn"
    UPC_A = "upc-a"
    EAN14 = "ean14"
    GS1_128 = "gs1-128"

    def convert(self,format: "BarcodeFormat"):
        convertables = {
            "code39": barcode.Code39,
            "code128": barcode.Code128,
            "pzn7": barcode.PZN,
            "ean13": barcode.EAN13,
            "ean8": barcode.EAN8,
            "jan": barcode.JAN,
            "isbn13": barcode.ISBN13,
            "isbn10": barcode.ISBN10,
            "issn": barcode.ISSN,
            "upc-a": barcode.UPCA,
            "ean14": barcode.EAN14,
            "gs1-128": barcode.Gs1_128,
        }
        return convertables[format.value]


class BarcodeOutputSelection(str, enum.Enum):
    PNG = "png"
    JPEG = "jpeg"
