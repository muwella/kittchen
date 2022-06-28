from pydantic import BaseModel, HttpUrl
# LOOKUP pydantic UrlStr

# WIP should import Base (models) instead of pydantic BaseModel (schemas)

# images

class Image(BaseModel):
    url: HttpUrl
    name: str