import requests
import os
import json

# — CONFIGURE —
HA_URL    = "http://localhost:8123"    # Or replace with your host/IP
TOKEN     = "YOUR_LONG_LIVED_ACCESS_TOKEN" # Replace with your Home Assistant long-lived access token
HEADERS   = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type":  "application/json",
}

def call_service(domain: str, service: str, data: dict):
    """Call a Home Assistant service (e.g. light.turn_on)."""
    url = f"{HA_URL}/api/services/{domain}/{service}"
    resp = requests.post(url, headers=HEADERS, json=data)
    resp.raise_for_status()
    return resp.json()

def get_state(entity_id: str):
    """Fetch the current state of an entity."""
    url = f"{HA_URL}/api/states/{entity_id}"
    resp = requests.get(url, headers=HEADERS)
    resp.raise_for_status()
    return resp.json()
    
if __name__ == "__main__":
    
    switch  = "switch.sonoff_s26r2zb"
    # toggle switch
    call_service("switch", "toggle", {"entity_id": switch})
    print(f"Requested {switch} to toggle")