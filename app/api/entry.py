from fastapi import APIRouter, Depends

from app.schemas.entry import EntryCreate, EntryDelete, EntryUpdate
from app.services.entry import EntryService, get_entry_service

router = APIRouter()


@router.post("/entry")
async def create_entry(
    entry_in: EntryCreate, service: EntryService = Depends(get_entry_service)
):
    await service.create_entry(entry_in)
    return "Succesfully created an entry."


@router.get("/entries")
async def read_entries(service: EntryService = Depends(get_entry_service)):
    result = await service.read_entries()

    return result


@router.patch("/entry")
async def update_entry(
    entry_in: EntryUpdate, service: EntryService = Depends(get_entry_service)
):
    await service.update_entry(entry_in)
    return "Successfully updated given entry."


@router.delete("/entry")
async def delete_entry(
    entry_in: EntryDelete, service: EntryService = Depends(get_entry_service)
):
    await service.delete_entry(entry_in)
    return "Successfuly deleted given entry."
