from pydantic import BaseModel


class EnrichmentPayload(BaseModel):
    patient_url: str
    enrichment_url: str
