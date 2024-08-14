from typing import List
from langchain.agents import tool

CONTACTS = [{"name": "Bola", "phone": "+2347068288784"}]


@tool("get_all_contacts")
def get_all_contacts(placeholder: str) -> List[dict]:
    """Get contacts."""
    return CONTACTS
