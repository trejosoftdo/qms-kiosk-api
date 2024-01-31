from pydantic import BaseModel

class CreateServiceTurnPayload(BaseModel):
    customerName: str

class CommonHeaders(BaseModel):
    authorization: str
    application: str

class CreateServiceTurnRequest(BaseModel):
    serviceId: int
    headers: CommonHeaders
    payload: CreateServiceTurnPayload

class CreateServiceTurnResponse(BaseModel):
    id: int
    customerName: str
    ticketNumber: str
    peopleInQueue: int
