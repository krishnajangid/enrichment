from fastapi import APIRouter

from app.schemas.schemas import EnrichmentPayload
from app.services.enrichment import Enrichment

router = APIRouter()


@router.post("/enrichment")
async def create_enrichment(
        payload: EnrichmentPayload,
):
    enrich_obj = Enrichment()
    response = await enrich_obj.process(
        patient_data_url=payload.patient_url,
        enrichment_data_url=payload.enrichment_url
    )

    return response
