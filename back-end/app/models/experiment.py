from pydantic import Field, BaseModel
from datetime import datetime
from typing import Optional
from beanie import PydanticObjectId


class Experiment(BaseModel):
    id: PydanticObjectId = Field(default_factory=PydanticObjectId, alias="id")
    name: str = Field(..., description="Experiment title", min_length=1, max_length=40)
    created_at: Optional[datetime] = Field(default_factory=datetime.now)
    # iterations: Optional[List[str]] = []  # TODO: List[Iteration]

    def __repr__(self) -> str:
        return f"<Experiment {self.name}>"

    def __str__(self) -> str:
        return self.name

    def __hash__(self) -> int:
        return hash(self.name)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Experiment):
            return self.id == other.id
        return False

    class Settings:
        name = "experiment"

    class Config:
        schema_extra = {
            "example": {
                "name": "Is the passenger survived?",
                "created_at": datetime.now()
            }
        }