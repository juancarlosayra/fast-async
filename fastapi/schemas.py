from pydantic import BaseModel, ConfigDict


class UserModel(BaseModel):
    id: int
    user_name: str
    
    model_config = ConfigDict(
        from_attributes = True
    )
    
class UserCreateModel(BaseModel):
    user_id: int
    user_name: str
    
    model_config = ConfigDict(
        from_attributes = True,
        json_schema_extra={
            "example":{
                "user_id": "1",
                "user_name": "Sample name"
            }
        }
    )