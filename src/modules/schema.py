from pydantic import BaseModel, Field
import json
from pathlib import Path
from typing import Dict, List


class Compound(BaseModel):
    Name: str = Field(description="The name of the molecule or compound (e.g., \"Linoleic acid\", \"γ-Tocopherol\").")
    Species: str = Field(description="The full Latin name of the plant species where the compound is found (e.g., Aronia melanocarpa L, Ribes nigrum L, Rosa canina L).")
    Organisms: str = Field(description="The biological part under investigation (e.g., \"seeds\").")
    Amount_of_Molecule: str = Field(description=" The reported quantity of the compound, along with its measurement unit (e.g., \"71.2 g/kg oil\", \"36.9 mg/kg\").")

class CompoundList(BaseModel):
    compounds: List[Compound] = Field(description="List of compounds extracted from the paper.", default=[])
