from fastapi import APIRouter

router = APIRouter(tags=['main'],prefix='/main')

@router.get('/')
def main_path():
    return {'main': 'path'}
