from pydantic import BaseModel, Field
import json
from pathlib import Path
from typing import Dict, List


class Compound(BaseModel):
    Name: str = Field(description="The name of the main compound or bioactive molecule studied or quantified.")
    Species: str = Field(description="The scientific name of the plant species from which the compound is extracted.")
    Organisms: str = Field(description="The part of the plant used in the study (e.g., seeds, leaves, roots).")
    Amount_of_Molecule: str = Field(description="The quantity of the compound reported, with units (e.g., mg/kg, g/100g).")

class CompoundList(BaseModel):
    compounds: List[Compound] = Field(description="List of compounds extracted from the paper.", default=[])
