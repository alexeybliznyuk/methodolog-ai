from pydantic import Field, BaseModel


class CourseCreateRequest(BaseModel):
    body: list = Field(...)
    
