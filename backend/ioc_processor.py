import json
import os

# Mapping of IoC types to pain scores based on the Pyramid of Pain.
IOC_PAIN_SCORES = {
    "hash": 1,             # Trivial
    "ip": 2,               # Easy
    "domain": 3,           # Simple
    "host artifact": 4,    # Annoying
    "network artifact": 5, # Difficult
    "ttp": 6               # Most Painful
}

def process_iocs():
    sample_file = os.path.join('sample_data', 'iocs.json')
    with open(sample_file, 'r') as f:
        iocs = json.load(f)
    
    # Process each IoC, assign a pain score based on its type.
    for ioc in iocs:
        ioc_type = ioc.get("type", "").lower()  # Normalize type.
        pain = IOC_PAIN_SCORES.get(ioc_type, 0)   # Default to 0 if type is unknown.
        ioc["pain_score"] = pain
    return iocs

if __name__ == "__main__":
    processed = process_iocs()
    print(json.dumps(processed, indent=2))
