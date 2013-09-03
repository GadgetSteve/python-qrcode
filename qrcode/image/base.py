class BaseImage(object):
    """
    Base QRCode image output class.
    """
    kind = None

    def __init__(self, border, width, box_size, *args, **kwargs):
        self.border = border
        self.width = width
        self.box_size = box_size
        self.pixel_size = (self.width + self.border*2) * self.box_size
        self._img = self.new_image(**kwargs)

    def drawrect(self, row, col):
        """
        Draw a single rectangle of the QR code.
        """
        raise NotImplementedError("BaseImage.drawrect")

    def save(self, stream, kind=None):
        """
        Save the image file.
        """
        raise NotImplementedError("BaseImage.save")

    def pixel_box(self, row, col):
        """
        A helper method for pixel-based image generators that specifies the
        four pixel coordinates for a single rect.
        """
        x = (col + self.border) * self.box_size
        y = (row + self.border) * self.box_size
        return [(x, y), (x + self.box_size - 1, y + self.box_size - 1)]

    def new_image(self, **kwargs):
        """
        Build the image class. Subclasses should return the class created.
        """
        return None

    def checked_kind(self, kind):
        """
        Get the image type.

        Subclasses can use this to raise ValueErrors for invalid types.
        """
        if kind is None:
            return self.kind
        return kind
