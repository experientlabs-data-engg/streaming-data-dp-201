import random
import uuid
import json
import datetime
from faker import Faker

fake = Faker()

# Constants
WIN_RATE = 0.0015  # 0.1-0.2%
DUPLICATE_RATE = 0.001  # 0.1%
MISSING_FIELD_RATE = 0.05  # 5%
NUM_LOGS = 10000


def generate_page_view_id(counter):
    return f"pv_{counter}"


def generate_impression_id(counter):
    return f"imp_{counter}"


def generate_adtech_log(counter):
    page_view_id = generate_page_view_id(counter)
    impression_id = generate_impression_id(counter)
    timestamp = datetime.datetime.now().isoformat()

    site_url = fake.url()
    ad_position = random.choice(["header", "footer", "sidebar", "navbar", "inline"])
    device_type = random.choices(["Mobile", "Desktop", "Tablet", "SmartTV"], weights=[50, 30, 15, 5])[0]
    os_version = random.choice(["Android 12", "Android 13", "iOS 16", "Windows 11", "macOS 14", "Linux 6.0"])

    vendor_list = random.sample([fake.domain_name() for _ in range(100)], k=random.randint(5, 10))
    purposes = random.sample(range(1, 10), k=random.randint(2, 5))
    legit_interests = random.sample(range(1, 5), k=random.randint(1, 3))

    has_win = random.random() < WIN_RATE
    click_data = fake.url() if random.random() > MISSING_FIELD_RATE else None

    ad_creative = None
    win_reason = None
    if has_win:
        ad_creative = {
            "creative_id": str(uuid.uuid4()),
            "brand": fake.company(),
            "category": random.choice(["Technology", "Automotive", "Fashion", "Food", "Health"]),
            "click_url": fake.url()
        }
    else:
        win_reason = random.choice(["brand_safety", "invalid_format", "policy_violation", "bid_too_low"])

    log = {
        "page_view_id": page_view_id,
        "impression_id": impression_id,
        "timestamp": timestamp,
        "site_url": site_url,
        "ad_position": ad_position,
        "device": {
            "type": device_type,
            "os_version": os_version
        },
        "gdpr": {
            "vendors": vendor_list,
            "purposes": purposes,
            "legitimate_interests": legit_interests
        },
        "click_data": click_data,
        "has_win": has_win,
        "win_reason": win_reason,
        "ad_creative": ad_creative
    }

    return log

if __name__ == '__main__':
    # Generate Logs
    logs = []
    log_counter = 1
    for _ in range(NUM_LOGS):
        log = generate_adtech_log(log_counter)
        logs.append(log)
        log_counter += 1

        # Inject duplicates randomly
        if random.random() < DUPLICATE_RATE:
            logs.append(log)

    # Save logs to a file
    with open("synthetic_adtech_logs.json", "w") as f:
        json.dump(logs, f, indent=4)

    print(f"Generated {len(logs)} logs with realistic distributions.")
