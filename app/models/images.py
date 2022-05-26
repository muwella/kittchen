from pydantic import BaseModel, HttpUrl
# LOOKUP pydantic UrlStr

# images

# WIP
class Image(BaseModel):
    url: HttpUrl
    name: str