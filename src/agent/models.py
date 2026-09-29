from pydantic import BaseModel, Field


class JobDescription(BaseModel):
    role_title: str
    company: str | None = None

    experience_min_years: int | None = None
    experience_max_years: int | None = None

    location: list[str] = Field(default_factory=list)

    must_have_skills: list[str] = Field(default_factory=list)
    good_to_have_skills: list[str] = Field(default_factory=list)

    responsibilities: list[str] = Field(default_factory=list)

    education_requirements: list[str] = Field(default_factory=list)

    employment_type: str | None = None

    raw_text: str