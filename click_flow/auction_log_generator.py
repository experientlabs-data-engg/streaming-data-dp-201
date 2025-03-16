import json
import random
from faker import Faker
from datetime import datetime, timedelta

# Initialize Faker
fake = Faker()

# Helper functions
def generate_transaction_summary_key():
    return {
        "bidder_id": random.randint(1, 1000),
        "placement_id": random.randint(1, 1000),
        "available_deals": [random.randint(1, 100) for _ in range(random.randint(1, 5))],
        "status_code": random.randint(200, 500),
        "has_bid": random.choice([True, False]),
        "has_buyer_uid": random.choice([True, False]),
        "country_code": fake.country_code(),
        "platform": fake.word(),
        "device_type": fake.word(),
        "interstitial": random.choice([True, False]),
        "has_daid": random.choice([True, False]),
        "bid_type": random.choice(["CPC", "CPM", "CPV", "CPP"]),
        "is_control_request": random.choice([True, False]),
        "request_format": random.choice(["BANNER", "VIDEO", "NATIVE_BANNER", "NATIVE_VIDEO"]),
        "throttled_deals": [random.randint(1, 100) for _ in range(random.randint(1, 5))],
        "has_criteo_id": random.choice([True, False]),
        "has_liveramp_idl_id": random.choice([True, False]),
        "supply_implementation_type": random.choice(["COP", "PREBID_JS", "PREBID_SERVER", "EBDA", "TAM", "ORTB", "VAST_TAGS"])
    }

def generate_transaction_summary_count():
    return {
        "key": generate_transaction_summary_key(),
        "ad_server_id": random.randint(1, 1000),
        "min_page_view_time": random.randint(1000, 10000),
        "max_page_view_time": random.randint(10000, 20000),
        "count": random.randint(1, 100),
        "request_size_sum": random.randint(1000, 10000)
    }

def generate_bid_response_sample_key():
    return {
        "bidder_id": random.randint(1, 1000),
        "seat_id": fake.uuid4(),
        "partner_creative_id": fake.uuid4()
    }

def generate_bid_response_sample():
    return {
        "key": generate_bid_response_sample_key(),
        "ad_server_id": random.randint(1, 1000),
        "page_view_time": random.randint(1000, 10000),
        "page_view_id": random.randint(1000, 10000),
        "json_response": json.dumps({"response": "sample"}),
        "has_bid": random.choice([True, False])
    }

def generate_request_response_sample():
    return {
        "publisher_id": random.randint(1, 1000),
        "placement_ids": [fake.uuid4() for _ in range(random.randint(1, 5))],
        "ad_server_id": random.randint(1, 1000),
        "page_view_id": random.randint(1000, 10000),
        "page_view_time": random.randint(1000, 10000),
        "country_code": fake.country_code(),
        "platform": fake.word(),
        "device_type": fake.word(),
        "has_buyer_uid": random.choice([True, False]),
        "bidder_id": random.randint(1, 1000),
        "status_code": random.randint(200, 500),
        "response_time_millis": random.randint(100, 1000),
        "json_request": json.dumps({"request": "sample"}),
        "json_response": json.dumps({"response": "sample"}),
        "has_daid": random.choice([True, False]),
        "rtb_partner_id": [random.randint(1, 1000) for _ in range(random.randint(1, 5))],
        "ad_server_metadata": json.dumps({"metadata": "sample"}),
        "extended_id_source": [fake.uuid4() for _ in range(random.randint(1, 5))],
        "creative_config_json": json.dumps({"creative": "sample"}),
        "processing_details_json": json.dumps({"details": "sample"}),
        "request_metadata_json": json.dumps({"metadata": "sample"}),
        "supply_implementation_type": random.choice(["COP", "PREBID_JS", "PREBID_SERVER", "EBDA", "TAM", "ORTB", "VAST_TAGS"]),
        "user_data_segment": [{
            "segtax": random.randint(1, 100),
            "segclass": fake.word(),
            "segment_ids": [random.randint(1, 100) for _ in range(random.randint(1, 5))]
        } for _ in range(random.randint(1, 5))]
    }

def generate_auction_log():
    return {
        "key_info": {
            "ad_server_id": random.randint(1, 1000),
            "auction_id": fake.uuid4(),
            "publisher_id": random.randint(1, 1000),
            "page_view_time": random.randint(1000, 10000),
            "page_view_id": random.randint(1000, 10000),
            "log_id": fake.uuid4(),
            "device": fake.word(),
            "location": fake.word(),
            "referrer": fake.url(),
            "has_daid": random.choice([True, False]),
            "mapped_inventory_verticals": [random.randint(1, 100) for _ in range(random.randint(1, 5))]
        },
        "timestamp": int(datetime.now().timestamp()),
        "winners": [{
            "url": fake.url(),
            "success": random.choice([True, False]),
            "error_msg": fake.sentence(),
            "bidder_id": random.randint(1, 1000),
            "auction_id": fake.uuid4(),
            "seat_id": fake.uuid4(),
            "bid_id": fake.uuid4(),
            "timestamp": int(datetime.now().timestamp()),
            "latency_ms": random.randint(100, 1000),
            "cost": random.uniform(1.0, 100.0),
            "seatBidId": fake.uuid4(),
            "imp_id": fake.uuid4()
        } for _ in range(random.randint(1, 5))],
        "transactions": [{
            "bidderId": random.randint(1, 1000),
            "request": {
                "request_id": fake.uuid4(),
                "buyeruid": fake.uuid4(),
                "imp": [{
                    "impression_id": random.randint(1, 1000),
                    "placement_id": random.randint(1, 1000),
                    "available_deals": [random.randint(1, 100) for _ in range(random.randint(1, 5))],
                    "interstitial": random.choice([True, False]),
                    "request_format": random.choice(["BANNER", "VIDEO", "NATIVE_BANNER", "NATIVE_VIDEO"]),
                    "outgoing_bid_floor": random.uniform(1.0, 100.0),
                    "deals": [{
                        "deal_campaign_id": random.randint(1, 1000),
                        "deal_floor": random.uniform(1.0, 100.0),
                        "floor_traffic_group_detail_id": random.randint(1, 1000),
                        "floor_experiment_group_id": random.randint(1, 1000),
                        "floor_experiment_id": random.randint(1, 1000),
                        "floor_experiment_detailid": random.randint(1, 1000),
                        "floor_status": random.choice(["FLOOR_NOT_APPLICABLE", "FLOOR_SUCCESS", "INVALID_FLOOR_EXPERIMENT", "NO_EXPERIMENT_RULES_MATCHED", "PUBLISHER_DISALLOWS_SMART_FLOORS", "PLACEMENT_PUB_FLOOR_MARGIN_OVERRIDE", "AD_SERVER_DISALLOWS_SMART_FLOORS", "DEAL_DISALLOWS_SMART_FLOORS"]),
                        "bid_floor": random.uniform(1.0, 100.0),
                        "smart_floor": random.uniform(1.0, 100.0),
                        "adjusted_impression_floor": random.uniform(1.0, 100.0)
                    } for _ in range(random.randint(1, 5))],
                    "throttled_deals": [random.randint(1, 1000) for _ in range(random.randint(1, 5))],
                    "eCpm_floor": random.uniform(1.0, 100.0),
                    "viewability": random.uniform(0.0, 1.0),
                    "playRate": random.uniform(0.0, 1.0),
                    "ctr": random.uniform(0.0, 1.0),
                    "external_floor": random.uniform(1.0, 100.0),
                    "floor_traffic_group_detail_id": random.randint(1, 1000),
                    "floor_experiment_group_id": random.randint(1, 1000),
                    "floor_experiment_id": random.randint(1, 1000),
                    "floor_experiment_detailid": random.randint(1, 1000),
                    "video_placement_type": random.choice(["UNDEFINED_VIDEO_PLACEMENT", "IN_STREAM_PLACEMENT", "IN_BANNER_PLACEMENT", "IN_ARTICLE_PLACEMENT", "IN_FEED_PLACEMENT", "FLOATING_PLACEMENT"]),
                    "floor_status": random.choice(["FLOOR_NOT_APPLICABLE", "FLOOR_SUCCESS", "INVALID_FLOOR_EXPERIMENT", "NO_EXPERIMENT_RULES_MATCHED", "PUBLISHER_DISALLOWS_SMART_FLOORS", "PLACEMENT_PUB_FLOOR_MARGIN_OVERRIDE", "AD_SERVER_DISALLOWS_SMART_FLOORS", "DEAL_DISALLOWS_SMART_FLOORS"]),
                    "ecpm_outgoing_bid_floor": random.uniform(1.0, 100.0),
                    "floor_experiment_group_allocation_traffic_allocation_percent": random.uniform(0.0, 100.0),
                    "ad_position": fake.word(),
                    "exchange_cost": random.uniform(1.0, 100.0),
                    "gross_exchange_cost": random.uniform(1.0, 100.0)
                } for _ in range(random.randint(1, 5))],
                "is_controlrequest": random.choice([True, False]),
                "has_buyer_uid": random.choice([True, False])
            },
            "response": {
                "latency_ms": random.randint(100, 1000),
                "error": fake.sentence(),
                "status_code": random.randint(200, 500),
                "bid_results": [{
                    "impression_id": random.randint(1, 1000),
                    "seat_id": fake.uuid4(),
                    "bid_id": fake.uuid4(),
                    "status_code": random.randint(200, 500),
                    "error": fake.sentence(),
                    "bid_type": random.choice(["CPC", "CPM", "CPV", "CPP"]),
                    "bid_floor": random.uniform(1.0, 100.0),
                    "status_codes": [random.randint(200, 500) for _ in range(random.randint(1, 5))],
                    "advertiser_name": fake.company(),
                    "agency_name": fake.company(),
                    "agency_id": fake.uuid4(),
                    "category_overrides": [fake.word() for _ in range(random.randint(1, 5))],
                    "blocking_publisher_control_id": random.randint(1, 1000),
                    "associated_publisher_control_ids": [random.randint(1, 1000) for _ in range(random.randint(1, 5))],
                    "publisher_control_id_for_bid_floor": random.randint(1, 1000),
                    "internal_campaign_id": random.randint(1, 1000),
                    "bundle_id": fake.uuid4(),
                    "business_rule_experiment_entry_id": random.randint(1, 1000),
                    "cost_holdback": [{
                        "id": random.randint(1, 1000),
                        "type": fake.word(),
                        "value": random.uniform(1.0, 100.0)
                    } for _ in range(random.randint(1, 5))],
                    "business_rule_experiment_id": random.randint(1, 1000),
                    "margin_type": fake.word(),
                    "smart_margin_type": random.choice(["MAX_MARGIN_FIXED", "MAX_MARGIN_CAPPED", "SMART_MARGIN_CAPPED", "SMART_MARGIN_UNCAPPED"]),
                    "exchange_cost": random.uniform(1.0, 100.0),
                    "gross_exchange_cost": random.uniform(1.0, 100.0)
                } for _ in range(random.randint(1, 5))],
                "response2_l": json.dumps({"response": "2.1"}),
                "response2_3": json.dumps({"response": "2.3"}),
                "response2_3_Json": json.dumps({"response": "2.3_Json"}),
                "nbr": random.randint(1, 100)
            }
        } for _ in range(random.randint(1, 5))],
        "business_rule_experiment_id": random.randint(1, 1000),
        "business_rule_traffic_id": random.randint(1, 1000),
        "floor_traffic_id": random.randint(1, 1000),
        "floor_traffic_allocation_percent": random.uniform(0.0, 100.0),
        "floor_traffic_logging_sample_percent": random.uniform(0.0, 100.0),
        "throttled_impressions": [{
            "impression_id": random.randint(1, 1000),
            "placement_id": random.randint(1, 1000),
            "interstitial": random.choice([True, False]),
            "is_control_request": random.choice([True, False]),
            "throttled_bidders": [{
                "bidder_id": random.randint(1, 1000),
                "has_buyer_uid": random.choice([True, False]),
                "bid_type": random.choice(["CPC", "CPM", "CPV", "CPP"]),
                "available_deals": [random.randint(1, 1000) for _ in range(random.randint(1, 5))],
                "request_format": random.choice(["BANNER", "VIDEO", "NATIVE_BANNER", "NATIVE_VIDEO"]),
                "status_code": random.randint(200, 500)
            } for _ in range(random.randint(1, 5))]
        } for _ in range(random.randint(1, 5))],
        "supply_implementation_type": random.choice(["COP", "PREBID_JS", "PREBID_SERVER", "EBDA", "TAM", "ORTB", "VAST_TAGS"]),
        "id_test_record": {
            "test_id": fake.uuid4(),
            "test_result": random.choice(["PASS", "FAIL"])
        }
    }

# Continuously generate and print AuctionLog
if __name__ == "__main__":
    while True:
        auction_log = generate_auction_log()
        print(json.dumps(auction_log, indent=2))
        # Sleep for a short interval (e.g., 1 second) before generating the next log
        import time
        time.sleep(1)
