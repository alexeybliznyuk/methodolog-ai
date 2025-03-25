from fastapi import FastAPI, Request, Response
from pydantic import BaseModel
from service.deepseek_service import DeepSeekService
from schemas.request.request_schemas import CourseCreateRequest

app = FastAPI()

class ApiModel(BaseModel):
    data: dict

@app.post("/structure")
async def structure(request: CourseCreateRequest):
    json_data = request.model_dump()
    service = DeepSeekService()
    response = service.generate_structure(json_data["body"])
    print(json_data["body"])
    return {"data": response}
