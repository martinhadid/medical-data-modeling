from dataclasses import dataclass


@dataclass(frozen=True)
class ModelRecord:
    run_id: str
    start_date: str
