import numpy as np
import skimage.exposure
from io import BytesIO
from PIL import Image
from skimage import img_as_float


def adjust_gamma(img, gamma):
    """
    Parameters
    ----------
    img : `PIL.JpegImagePlugin.JpegImageFile`
    """
    # noinspection PyTypeChecker
    X = np.asarray(img, dtype=np.uint8)
    X = img_as_float(X)
    X = skimage.exposure.adjust_gamma(X, gamma=gamma)
    # noinspection PyUnresolvedReferences
    X = (255. * X).astype(np.uint8)
    img_corrected = Image.fromarray(X)
    return img_corrected

def jpg_compress(img, quality):
    """
    Parameters
    ----------
    img : `PIL.JpegImagePlugin.JpegImageFile`
    """
    out = BytesIO()
    img.save(out, format='jpeg', quality=quality)
    img_compressed = Image.open(out)
    return img_compressed
