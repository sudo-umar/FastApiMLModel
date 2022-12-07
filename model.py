import pandas as pd
from pydantic import BaseModel

class PenguinsFeatureValues(BaseModel):
    bill_length_mm: float
    bill_depth_mm: float
    flipper_length_mm: float
    body_mass_g: float
    species_Adelie: int
    species_Chinstrap:int
    species_Gentoo: int
    island_Biscoe: int
    island_Dream: int
    island_Torgersen:int

    