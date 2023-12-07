from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get('/', tags=["Progreps"])
async def get_all_progreps():
    return ("These are all the Progreps.")

@router.get('/progrep_by_client_id', tags=["Progreps"])
async def get_progrep_by_client_id(client_id: int):
    return("Yeah, this is the ID", client_id)

@router.get('/progrep_by_reservation_id', tags=["Progreps"])
async def get_progrep_by_reservation_id(reservation_id: int):
    return("Yeah, this is the ID", client_id)

@router.post('/progrep', tags=['Progreps'])
async def create_a_progrep():
    return("Iyak, berhasil")

@router.put('/progrep', tags=['Progreps'])
async def update_a_progrep():
    return("Iyak, keganti")

@router.delete('/progrep', tags=['Progreps'])
async def cancel_a_progrep():
    return("Iyak, kehapus")