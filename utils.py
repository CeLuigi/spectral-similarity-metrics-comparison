from copy import copy
import numpy as np


def spec2lab(orig_spec, cmf, orig_wp_spectrum):
    """
    Convert spectral image to CIE Lab color space.

    :param orig_spec:
    :param cmf: camera matching function ()
    :param orig_wp_spectrum: 
    """
    def f(t):
        d = 6/29

        case_1 = t > d**3
        case_2 = ~case_1

        out = np.zeros(t.shape)
        out[case_1] = np.cbrt(t[case_1])
        out[case_2] = t[case_2] / (3 * d**2) + 4 / 29

        return out

    spec = copy(orig_spec)

    sum = np.sum(cmf[:, 1] * orig_wp_spectrum.reshape(-1))
    Xw, Yw, Zw = orig_wp_spectrum.reshape(-1) @ cmf
    Xw /= sum
    Yw /= sum
    Zw /= sum

    sumy = np.sum(cmf[:, 1])
    XYZ = spec @ cmf
    XYZ /= sumy

    X, Y, Z = XYZ[:, 0], XYZ[:, 1], XYZ[:, 2]

    Lab = np.zeros((spec.shape[0], 3))
    Lab[:, 0] = 116 *  f(Y / Yw) - 16  # L
    Lab[:, 1] = 500 * (f(X / Xw) - f(Y / Yw))  # a
    Lab[:, 2] = 200 * (f(Y / Yw) - f(Z / Zw))  # b

    return Lab


def XYZ2proLab(xyz):
    """
    Convert from XYZ to ProLab color space

    :param xyz: 
    """
    ill = np.array([0.95047, 1, 1.08883])
    param = np.array([[75.54, 486.66, 167.39, 0],
                      [617.72, -595.45, -22.27, 0],
                      [48.34, 194.94, -243.28, 0],
                      [0.7554, 3.8666, 1.6739, 1]])
    image = False
    if len(xyz.shape) == 3:
        image = True
        h, w, c = xyz.shape
        xyz = np.reshape(xyz, (xyz.shape[0] * xyz.shape[1], xyz.shape[2]))
        assert xyz.shape[1] == ill.shape[0]
    elif len(xyz.shape) == 2:
        assert xyz.shape[1] == ill.shape[0]
    else:
        assert xyz.shape[0] == ill.shape[0]
        xyz = xyz[None]
    xyz /= ill
    ones = np.ones((xyz.shape[0], 1))
    proLabHomog = np.append(xyz, ones, axis=1)
    proLabHomog = proLabHomog@param.transpose()
    if len(proLabHomog.shape) == 1:
        proLabHomog = proLabHomog[None]
    proLab = proLabHomog[:, 0:3] / np.expand_dims(proLabHomog[:, 3], 1)
    if image:
        proLab = np.reshape(proLab, (h, w, c))
    return proLab
