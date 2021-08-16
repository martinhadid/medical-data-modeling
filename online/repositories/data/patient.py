from dataclasses import dataclass
from datetime import datetime
from typing import List


@dataclass(frozen=True)
class Patient:
    patient_id: str
    timestamp: List[datetime]
    measurement_x: List[float]
    measurement_y: List[float]
    measurement_z: List[float]
