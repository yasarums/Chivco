from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get('/', tags=["Reservations"])
async def get_all_reservations():
    return ("These are all the reservations.")

@router.get('/reservation_by_client_id', tags=["Reservations"])
async def get_reservation_by_client_id(client_id: int):
    return("Yeah, this is the ID", client_id)

@router.post('/reservation', tags=['Reservations'])
async def book_a_reservation():
    return("Iyak, berhasil")

@router.put('/reservation', tags=['Reservations'])
async def update_a_reservation():
    return("Iyak, keganti")

@router.delete('/reservation', tags=['Reservations'])
async def cancel_a_reservation():
    return("Iyak, kehapus")