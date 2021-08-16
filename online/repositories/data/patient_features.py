from dataclasses import dataclass


@dataclass(frozen=True)
class PatientFeatures:
    measurement_x_std: float
    measurement_x_mean: float
    measurement_x_median: float

    measurement_y_std: float
    measurement_y_mean: float
    measurement_y_median: float

    measurement_z_std: float
    measurement_z_mean: float
    measurement_z_median: float

    measurement_x_lr_slope: float
    measurement_x_lr_corr: float

    measurement_y_lr_slope: float
    measurement_y_lr_corr: float

    measurement_z_lr_slope: float
    measurement_z_lr_corr: float

    measurement_x_quad_a: float
    measurement_x_quad_b: float

    measurement_y_quad_a: float
    measurement_y_quad_b: float

    measurement_z_quad_a: float
    measurement_z_quad_b: float
