import colour
import numpy as np

from utils import spec2lab, XYZ2proLab


def computeDEfromSpectra(groundTruth, recovered, cmf,
                         wpSpec, typeDE="CIE2000"):
    """
    Compute deltaE between the recovered and the
    corresponding ground-truth image
    
    Args:
        :param groundTruth: ground truth reference image
            numpy.ndarray (Height x Width x Spectral_Dimension)
        :param recovered: image under evaluation.
            numpy.ndarray (Height x Width x Spectral_Dimension)
        :param cmf: color matching function.
            numpy.ndarray (Spectral_Dimension x 3)
        :param wpSpec: reference white (e.g. D65)
            numpy.ndarray (Spectral_Dimension)
        :param typeDE: deltaE version, can be a string
            ("CIE2000", "CIE1994", or"CIE1976"). Default: "CIE2000"

    Returns:
        deltaE between `recovered` and `groundTruth`
    """
    assert groundTruth.shape == recovered.shape, \
        "Size not match for groundtruth and recovered spectral images"
    assert groundTruth.shape[2] == cmf.shape[0], \
        "Spectral dimension and number of filter must match"
    groundTruth = np.clip(groundTruth.astype("float64"), 0, 1)
    recovered = np.clip(recovered.astype("float64"), 0, 1)
    groundTruth = np.reshape(groundTruth, (-1, groundTruth.shape[2]))
    recovered = np.reshape(recovered, (-1, recovered.shape[2]))
    LABgt = spec2lab(groundTruth, cmf, wpSpec)
    LABrc = spec2lab(recovered, cmf, wpSpec)
    deltaE = np.mean(colour.delta_E(LABgt, LABrc, typeDE))
    return deltaE


def computeProLabEucD(groundTruth, recovered, cmf):
    """
    Compute Euclidean distance in ProLab color space
    between the recovered and the corresponding ground-truth image

    Args:
        :param groundTruth: ground truth reference image.
            numpy.ndarray (Height x Width x Spectral_Dimension)
        :param recovered: image under evaluation.
            numpy.ndarray (Height x Width x Spectral_Dimension)
        :param cmf: color matching function.
            numpy.ndarray (Spatial_Dimension x 3)

    Returns:
        Euclidean error in ProLab color space between `recovered`
            and `groundTruth`
    """
    assert groundTruth.shape == recovered.shape, \
        "Size not match for groundtruth and recovered spectral images"
    h, w, _ = groundTruth.shape
    groundTruth = np.clip(groundTruth.astype("float64"), 0, 1)
    recovered = np.clip(recovered.astype("float64"), 0, 1)
    groundTruth = np.reshape(groundTruth, (-1, groundTruth.shape[2]))
    recovered = np.reshape(recovered, (-1, recovered.shape[2]))

    sumy = np.sum(cmf[:, 1])
    XYZgt = groundTruth @ cmf
    XYZgt /= sumy
    XYZrec = recovered @ cmf
    XYZrec /= sumy

    proLabGT = XYZ2proLab(XYZgt)
    proLabRC = XYZ2proLab(XYZrec)

    l1, a1, b1 = np.split(proLabGT, 3, axis=1)
    l2, a2, b2 = np.split(proLabRC, 3, axis=1)
    dist = np.sqrt((l1 - l2)**2 + (a1 - a2)**2 + (b1 - b2)**2)
    return np.mean(dist)
