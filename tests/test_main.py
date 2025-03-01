import pytest

from app.services.enrichment import Enrichment


@pytest.mark.asyncio
async def test_enrich_data():
    enrich_obj = Enrichment()
    patient_data = [
        {
            "chromosome": "chr7",
            "position": "112280",
            "ref": "C",
            "alt": "C"
        },
        {
            "chromosome": "chr8",
            "position": "112280",
            "ref": "C",
            "alt": "C"
        }
    ]
    enrichment_data = [
        {
            "chromosome": "chr8",
            "position": "112280",
            "ref": "C",
            "alt": "C",
            "info": "info2"
        }
    ]

    # Await the async method
    res = await enrich_obj.enrich_data(patient_data=patient_data, enrichment_data=enrichment_data)

    assert res == [
        {
            "chromosome": "chr7",
            "position": "112280",
            "ref": "C",
            "alt": "C",
            "info": None
        },
        {
            "chromosome": "chr8",
            "position": "112280",
            "ref": "C",
            "alt": "C",
            "info": "info2"
        }
    ]
