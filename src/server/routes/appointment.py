from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get('/', tags=["Appointments"])
async def get_all_appointments():
    return ("These are all the Appointments.")

@router.get('/appointment_by_client_id', tags=["Appointments"])
async def get_appointment_by_client_id(client_id: int):
    return("Yeah, this is the ID", client_id)

@router.post('/appointment', tags=['Appointments'])
async def make_an_appointment():
    return("Iyak, berhasil")

@router.put('/appointment', tags=['Appointments'])
async def update_an_appointment():
    return("Iyak, keganti")

@router.delete('/appointment', tags=['Appointments'])
async def cancel_an_appointment():
    return("Iyak, kehapus")