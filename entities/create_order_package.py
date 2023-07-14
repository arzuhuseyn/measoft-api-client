class CreateOrderPackage:
    def __init__(
        self,
        name: str,
        code: str,
        barcode: str,
        message: str,
        weight: float,
        length: float,
        width: float,
        height: float,
    ):
        self.name = name
        self.code = code
        self.barcode = barcode
        self.message = message
        self.weight = weight
        self.length = length
        self.width = width
        self.height = height