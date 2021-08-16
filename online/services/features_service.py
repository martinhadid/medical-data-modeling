from typing import List, Optional

import numpy as np
from scipy.stats import linregress


def _get_statistical_measurements(measurement: List[float]) -> (float, float, float):
    return np.std(a=measurement), np.mean(a=measurement), np.median(a=measurement)


def _get_linear_regression(measurement: List[float]) -> (float, float):
    slope, _, r_value, _, _ = linregress(x=range(len(measurement)), y=measurement)
    return slope, r_value


def _get_quadratic_regression(measurement: List[float]) -> Optional[float, float]:
    try:
        x = range(len(measurement))
        a, b, _ = np.polyfit(x=x, y=measurement, deg=2)
        return a, b
    except Exception:
        return None, None


def get_patient_features(measurement_x: List[float],
                         measurement_y: List[float],
                         measurement_z: List[float]) -> dict:

    x_std, x_mean, x_median = _get_statistical_measurements(measurement=measurement_x)
    y_std, y_mean, y_median = _get_statistical_measurements(measurement=measurement_y)
    z_std, z_mean, z_median = _get_statistical_measurements(measurement=measurement_z)

    x_slope, x_r_value = _get_linear_regression(measurement=measurement_x)
    y_slope, y_r_value = _get_linear_regression(measurement=measurement_y)
    z_slope, z_r_value = _get_linear_regression(measurement=measurement_z)

    x_a_quad, x_b_quad = _get_quadratic_regression(measurement=measurement_x)
    y_a_quad, y_b_quad = _get_quadratic_regression(measurement=measurement_y)
    z_a_quad, z_b_quad = _get_quadratic_regression(measurement=measurement_z)

    return {
        "x_std": x_std,
        "x_mean": x_mean,
        "x_median": x_median,
        "y_std": y_std,
        "y_mean": y_mean,
        "y_median": y_median,
        "z_std": z_std,
        "z_mean": z_mean,
        "z_median": z_median,
        "x_slope": x_slope,
        "x_r_value": x_r_value,
        "y_slope": y_slope,
        "y_r_value": y_r_value,
        "z_slope": z_slope,
        "z_r_value": z_r_value,
        "x_a_quad": x_a_quad,
        "x_b_quad": x_b_quad,
        "y_a_quad": y_a_quad,
        "y_b_quad": y_b_quad,
        "z_a_quad": z_a_quad,
        "z_b_quad": z_b_quad,
    }
