import random
import json
from faker import Faker
from datetime import datetime

from click_flow.archive.pv_random_data_generator import generate_system_metrics, generate_page_view_request, \
    generate_video_attributes, generate_dimension

fake = Faker()

# Constants
VENDOR_SET = [random.randint(10000, 99999) for _ in range(100)]  # Set of 100 vendor IDs
AD_POSITIONS = ["header", "footer", "sidebar", "navbar", "content", "popup"]
DEVICE_TYPES = ["Mobile", "Desktop", "Tablet", "SmartTV"]
OS_VERSIONS = {
    "Mobile": {
        "iOS": ["16.0.0", "16.1.0", "16.2.0", "16.3.0", "16.4.1", "16.5.2"],
        "Android": ["12.0.0", "12.1.0", "13.0.0", "13.1.0", "14.0.0", "14.1.0"]
    },
    "Desktop": {
        "Windows": ["10.0.0", "10.1.0", "11.0.0", "11.1.0", "11.2.0"],
        "MacOSX": ["10.15.0", "10.15.1", "11.0.0", "11.1.0", "12.0.0", "12.1.0", "13.0.0", "13.1.0"]
    },
    "Tablet": {
        "iOS": ["16.0.0", "16.1.0", "16.2.0", "16.3.0", "16.4.1"],
        "Android": ["12.0.0", "12.1.0", "13.0.0", "13.1.0"]
    },
    "SmartTV": {
        "Tizen": ["5.0.0", "5.1.0", "6.0.0", "6.1.0"],
        "WebOS": ["4.0.0", "4.1.0", "5.0.0", "5.1.0"]
    }
}
BROWSERS = ["Safari", "Chrome", "Firefox", "Edge", "Opera"]
CREATIVE_REJECTION_REASONS = ["brand_safety", "invalid_format", "policy_violation"]

# Sequential ID Counters
page_view_id_counter = 1000
impression_id_counter = 1000
creative_id_counter = 1000

# Helper Functions
def generate_vendors():
    return random.sample(VENDOR_SET, random.randint(5, 10))

def generate_purposes():
    return random.sample(range(1, 10), random.randint(2, 5))

def generate_legitimate_interests():
    return random.sample(range(1, 10), random.randint(1, 3))

def generate_supply_chain_identifiers():
    urls = [fake.url() for _ in range(random.randint(1, 3))]
    urls.append("https://google.com")
    return urls

def generate_device_classification():
    device_type = random.choice(DEVICE_TYPES)
    os_versions = OS_VERSIONS[device_type]
    os_name = random.choice(list(os_versions.keys()))
    os_version = random.choice(os_versions[os_name])
    os_major, os_minor, os_patch = os_version.split(".")
    return {
        "browser": random.choice(BROWSERS),
        "browser_version": f"{random.randint(10, 20)}.0",
        "device_type": device_type,
        "modelCode": random.choice(["iPhone", "Samsung", "iPad", "MacBook", "WindowsPC"]),
        "model_family": {
            "manufacturer": random.choice(["Apple", "Samsung", "Google", "Microsoft"]),
            "model_name": random.choice(["iPhone 14", "Galaxy S22", "Pixel 7", "Surface Pro"])
        },
        "os_major_Version": int(os_major),
        "os_minor_version": int(os_minor),
        "os_patch_version": int(os_patch),
        "os_version": os_version,
        "platform": os_name,
        "resolution_height": random.choice([600, 720, 1080, 1440]),
        "resolution_width": random.choice([800, 1280, 1920, 2560])
    }

def generate_creative(is_win=False):
    global creative_id_counter
    creative_id_counter += 1
    creative = {
        "creativeId": creative_id_counter,
        "advertiserId": random.randint(1000, 9999),
        "cost": round(random.uniform(0.1, 10.0), 2) if is_win else 0,
        "bidType": random.choice(["CPC", "CPM", "CPV", "CPP"]),
        "learning": random.choice([True, False]),
        "categoryId": random.randint(1, 100),
        "eCpm": round(random.uniform(0.1, 10.0), 2) if is_win else 0,
        "ctr": round(random.uniform(0.01, 0.99), 2) if is_win else 0,
        "productRecommendationStrategyId": random.randint(1, 100),
        "productIds": [fake.uuid4() for _ in range(random.randint(1, 3))],
        "adomain": fake.domain_name(),
        "advertiser_cost": round(random.uniform(0.1, 10.0), 2) if is_win else 0,
        "rtbSeat": fake.uuid4(),
        "creativeIndex": random.randint(1, 10),
        "empLineItemId": fake.uuid4(),
        "empAdvertiserId": fake.uuid4(),
        "empOrderId": fake.uuid4(),
        "empEnvironmentId": fake.uuid4(),
        "empAdUnitId": fake.uuid4(),
        "empTopLevelAdUnitId": fake.uuid4(),
        "audienceTargetingOverrideSegmentId": random.randint(1, 100),
        "empCreativeId": fake.uuid4(),
        "partner_creative_id": fake.uuid4(),
        "chosenCreativesize": generate_dimension(),
        "empSiteId": fake.uuid4(),
        "realtime_audience_segments": [random.randint(1, 100) for _ in range(random.randint(1, 3))],
        "useBillableEvent": random.choice([True, False]),
        "viewability": round(random.uniform(0.1, 1.0), 2) if is_win else 0,
        "playRate": round(random.uniform(0.1, 1.0), 2) if is_win else 0,
        "bidder_id": random.randint(1, 100),
        "exchange_cost": round(random.uniform(0.1, 10.0), 2) if is_win else 0,
        "gross_exchange_cost": round(random.uniform(0.1, 10.0), 2) if is_win else 0,
        "internal_vpaid_tracking_enabled": random.choice([True, False]),
        "business_rule_experiment_entry_id": random.randint(1, 100),
        "bidder_margin_override": round(random.uniform(0.1, 10.0), 2) if is_win else 0,
        "play_rate_prediction_model_category_id": random.randint(1, 100),
        "default_margin": round(random.uniform(0.1, 10.0), 2) if is_win else 0,
        "margin_type": random.choice(["DEFAULT", "ZERO", "DEAL", "BUSINESS_RULE_EXPERIMENT", "BIDDER", "DSP_SEAT", "BIDDER_PUBLISHER", "UP_BID", "PUBLISHER_FLOOR_MARGIN_OVERRIDE"]),
        "realtime_audience_segment_run_ids": [random.randint(1, 100) for _ in range(random.randint(1, 3))],
        "play_rate_prediction_model_run_id": random.randint(1, 100),
        "external_ids": {
            "line_item_id": fake.uuid4(),
            "advertiser_id": fake.uuid4(),
            "order_id": fake.uuid4(),
            "creative_id": fake.uuid4(),
            "environment_id": fake.uuid4(),
            "ad_unit_id": fake.uuid4(),
            "top_level_ad_unit_id": fake.uuid4(),
            "site_id": fake.uuid4(),
            "campaign_id": fake.uuid4(),
            "publisher_id": fake.uuid4(),
            "app_id": fake.uuid4(),
            "domain": fake.domain_name(),
            "sub_domain": fake.domain_name(),
            "site_url": fake.url(),
            "insertion_order_id": fake.uuid4(),
            "ad_id": fake.uuid4(),
            "placement_id": fake.uuid4(),
            "deal_id": fake.uuid4(),
            "ad_size": fake.word(),
            "site_category": fake.word()
        },
        "partner_advertiser_name": fake.company(),
        "partner_agency_name": fake.company(),
        "partner_agency_id": fake.uuid4(),
        "format_optimization_experiment_detailid": random.randint(1, 100),
        "format_optimization_experiment_feature_set_priority_id": random.randint(1, 100),
        "format_optimization_status": random.choice(["NOT_APPLICABLE", "SUCCESS", "NO_RULES_MATCHED", "NO_VALID_FORMAT_FOUND", "NOT_ENABLED"]),
        "ds_research_info": fake.sentence(),
        "iab_categories": [fake.word() for _ in range(random.randint(1, 3))],
        "audience_targeting_sample_rate": round(random.uniform(0.1, 1.0), 2),
        "ctv_qr_code_config_id": random.randint(1, 100),
        "bid_internal_auction_price": round(random.uniform(0.1, 10.0), 2) if is_win else 0,
        "advertiser_auction_macro_price": round(random.uniform(0.1, 10.0), 2) if is_win else 0,
        "exchange_post_auction_discount_id": random.randint(1, 100),
        "applicable_margin": round(random.uniform(0.1, 10.0), 2) if is_win else 0,
        "cost_holdback": [{
            "id": random.randint(1, 100),
            "type": fake.word(),
            "value": round(random.uniform(0.1, 10.0), 2)
        } for _ in range(random.randint(1, 3))],
        "floor_traffic_group_detail_id": random.randint(1, 100),
        "floor_experiment_group_id": random.randint(1, 100),
        "floor_experiment_id": random.randint(1, 100),
        "floor_experiment_detail_id": random.randint(1, 100),
        "floor_status": random.choice(["FLOOR_NOT_APPLICABLE", "FLOOR_SUCCESS", "INVALID_FLOOR_EXPERIMENT", "NO_EXPERIMENT_RULES_MATCHED", "PUBLISHER_DISALLOWS_SMART_FLOORS", "PLACEMENT_PUB_FLOOR_MARGIN_OVERRIDE", "AD_SERVER_DISALLOWS_SMART_FLOORS", "DEAL_DISALLOWS_SMART_FLOORS"]),
        "creative_config_collection_element_ids": [random.randint(1, 100) for _ in range(random.randint(1, 3))],
        "creative_format_config_collection_element_ids": [random.randint(1, 100) for _ in range(random.randint(1, 3))],
        "has_matched_user": random.choice([True, False]),
        "nformats_traffic_group_detail_id": random.randint(1, 100),
        "nformats_experiment_group_id": random.randint(1, 100),
        "nformats_experiment_id": random.randint(1, 100),
        "nformats_experiment_detail_id": random.randint(1, 100),
        "nformats_creative_status": random.choice(["NFORMAT_CREATIVE_NOT_APPLICABLE", "NFORMAT_CREATIVE_NOT_ENABLED", "NFORMAT_CREATIVE_SUCCESS", "NFORMAT_CREATIVE_CONFIG_ELEMENTS_DUPLICATE_ERROR", "NFORMAT_CREATIVE_CONFIG_ELEMENTS_INVALID", "NFORMAT_CREATIVE_EXPERIMENT_INVALID", "NFORMAT_CREATIVE_EXPERIMENT_NO_RULES_MATCHED"]),
        "nformats_format_status": random.choice(["NFORMAT_FORMAT_NOT_APPLICABLE", "NFORMAT_FORMAT_NOT_ENABLED", "NFORMAT_FORMAT_SUCCESS", "NFORMAT_FORMAT_CONFIG_ELEMENTS_DUPLICATE_ERROR", "NFORMAT_FORMAT_CONFIG_ELEMENTS_INVALID", "NFORMAT_FORMAT_EXPERIMENT_INVALID", "NFORMAT_FORMAT_EXPERIMENT_NO_RULES_MATCHED", "NFORMAT_FORMAT_CONFIG_ELEMENTS_COLLIDE_WITH_CREATIVE_ELEMENTS"]),
        "floor_experiment_group_allocation_traffic_allocation_percent": round(random.uniform(0.1, 1.0), 2),
        "creative_config_constraint_perumation_id": [random.randint(1, 100) for _ in range(random.randint(1, 3))],
        "creative_format_config_constraint_permutation_id": [random.randint(1, 100) for _ in range(random.randint(1, 3))],
        "noformats_experiment_group_allocation_traffic_allocation_percent": round(random.uniform(0.1, 1.0), 2),
        "adomains": [fake.domain_name() for _ in range(random.randint(1, 3))],
        "has_fraud_sensor_tag": random.choice([True, False]),
        "duration": random.randint(5, 120),
        "deal_floor_traffic_group_detail_id": random.randint(1, 100),
        "deal_floor_experiment_group_id": random.randint(1, 100),
        "deal_floor_experiment_id": random.randint(1, 100),
        "deal_floor_experiment_detail_id": random.randint(1, 100),
        "deal_floor_status": random.choice(["FLOOR_NOT_APPLICABLE", "FLOOR_SUCCESS", "INVALID_FLOOR_EXPERIMENT", "NO_EXPERIMENT_RULES_MATCHED", "PUBLISHER_DISALLOWS_SMART_FLOORS", "PLACEMENT_PUB_FLOOR_MARGIN_OVERRIDE", "AD_SERVER_DISALLOWS_SMART_FLOORS", "DEAL_DISALLOWS_SMART_FLOORS"]),
        "business_rule_experiment_id": random.randint(1, 100),
        "smart_margin_type": random.choice(["MAX_MARGIN_FIXED", "MAX_MARGIN_CAPPED", "SMART_MARGIN_CAPPED", "SMART_MARGIN_UNCAPPED"]),
        "creative_inventory_targeting_id": random.randint(1, 100),
        "creative_format_inventory_targeting_id": random.randint(1, 100),
        "up_bidding_experiment": {
            "id": random.randint(1, 100),
            "dynamic_margin_target_id": random.randint(1, 100),
            "minimum_effective_margin": round(random.uniform(0.1, 10.0), 2),
            "reduced_effective_margin": round(random.uniform(0.1, 10.0), 2),
            "exchange_cost_multiplier": round(random.uniform(0.1, 10.0), 2)
        }
    }
    if not is_win:
        creative["rejection_reason"] = random.choice(CREATIVE_REJECTION_REASONS)
    return creative

def generate_impression(is_win=False):
    global impression_id_counter
    impression_id_counter += 1
    return {
        "impression_id": impression_id_counter,
        "placement_id": fake.uuid4(),
        "originalPlacementId": fake.uuid4(),
        "error_code": fake.word(),
        "rotation_scheme": fake.word(),
        "creative_format_id": random.randint(1, 100),
        "postfix": fake.word(),
        "tag": fake.word(),
        "max_creative_count": random.randint(1, 10),
        "creative_count": random.randint(1, 10),
        "column_count": random.randint(1, 10),
        "control_ab_test_names": [fake.word() for _ in range(random.randint(1, 3))],
        "creatives": [generate_creative(is_win) for _ in range(random.randint(1, 3))],
        "is_licensed_format": random.choice([True, False]),
        "ab_test_names": [fake.word() for _ in range(random.randint(1, 3))],
        "phantom_creatives": [generate_creative(is_win) for _ in range(random.randint(1, 3))],
        "exchange_cost": round(random.uniform(0.1, 10.0), 2) if is_win else 0,
        "gross_exchange_cost": round(random.uniform(0.1, 10.0), 2) if is_win else 0,
        "format_effect_id": random.randint(1, 100),
        "smart_load_distance": random.randint(1, 100),
        "exchangeplacementId": fake.uuid4(),
        "format_test_id": random.randint(1, 100),
        "external_floor": round(random.uniform(0.1, 10.0), 2),
        "acceptable_sizes": [generate_dimension() for _ in range(random.randint(1, 3))],
        "chosenPlacementSize": generate_dimension(),
        "interstitial": random.choice([True, False]),
        "upstream_deal_id": fake.uuid4(),
        "bill_using_visible": random.choice([True, False]),
        "rewarded": random.choice([True, False]),
        "using_cpm_cap": random.choice([True, False]),
        "video_placement_type": random.choice(["UNDEFINED_VIDEO_PLACEMENT", "IN_STREAM_PLACEMENT", "IN_BANNER_PLACEMENT", "IN_ARTICLE_PLACEMENT", "IN_FEED_PLACEMENT", "FLOATING_PLACEMENT"]),
        "request_format": random.choice(["BANNER", "VIDEO", "NATIVE_BANNER", "NATIVE_VIDEO"]),
        "skadn_nonce": fake.uuid4(),
        "upstream_imp_id": fake.uuid4(),
        "gpid": fake.uuid4(),
        "divid": fake.uuid4(),
        "fraud_sensor_tag": random.choice([True, False]),
        "video_attributes": generate_video_attributes(),
        "request_formats": [random.choice(["BANNER", "VIDEO", "NATIVE_BANNER", "NATIVE_VIDEO"]) for _ in range(random.randint(1, 3))],
        "upstream_transaction_id": fake.uuid4(),
        "tagid": fake.uuid4(),
        "dfp_ad_unit_code": fake.uuid4(),
        "has_malvertising_defense_tag": random.choice([True, False]),
        "pod_ad_parent_impression_id": random.randint(1000, 9999)
    }

def generate_page_view_log():
    global page_view_id_counter
    page_view_id_counter += 1
    is_win = random.random() < 0.002  # 0.2% win rate
    site_url = fake.url()
    ad_position = random.choice(AD_POSITIONS)
    return {
        "impressions": [generate_impression(is_win) for _ in range(random.randint(1, 3))],
        "request": generate_page_view_request(),
        "page_view_id": page_view_id_counter,
        "publisher_id": random.randint(1000, 9999),
        "site_id": random.randint(1000, 9999),
        "processed_ms": random.randint(100, 1000),
        "consequent": random.choice([True, False]),
        "force_invalidation": random.choice([True, False]),
        "audience_segments": [random.randint(1, 100) for _ in range(random.randint(1, 3))],
        "kafkaMetaData": {
            "partition_id": random.randint(1, 100),
            "cluster_id": fake.uuid4(),
            "offset": random.randint(1, 1000),
            "timestamp": int(datetime.now().timestamp())
        },
        "mg_invalid_traffic": random.choice([True, False]),
        "mg_prediction_id": fake.uuid4(),
        "mg_reason_code": random.randint(1, 100),
        "mg_response_time": random.randint(100, 1000),
        "cmp": random.choice([True, False]),
        "rtb_throttling_control": random.choice([True, False]),
        "geodata_response_time": random.randint(100, 1000),
        "userdata_response_time": random.randint(100, 1000),
        "external_service_overall_response_time": random.randint(100, 1000),
        "geodata_response_status": random.choice(["SUCCESS", "TIMEOUT", "ERROR", "EMPTY_RESPONSE", "SKIPPED", "NA"]),
        "userdata_response_status": random.choice(["SUCCESS", "TIMEOUT", "ERROR", "EMPTY_RESPONSE", "SKIPPED", "NA"]),
        "user_privacy": {
            "opt_out": random.choice(["TCF", "CCPA", "COOKIE", "IDFA", "GPP"]),
            "consent_string": fake.uuid4(),
            "consent_string_version": random.randint(1, 10),
            "purpose": generate_purposes(),
            "vendors": generate_vendors(),
            "vendors_sample": random.randint(1, 10),
            "ccpa_string": fake.uuid4(),
            "legitimate_interests": generate_legitimate_interests(),
            "special_feature_opt_ins": random.randint(1, 10)
        },
        "supply_source": random.choice(["COP", "PREBID_JS", "PREBID_SERVER", "EBDA", "TAM", "ORTB"]),
        "business_rule_experiment_id": random.randint(1, 100),
        "liverampidl_response_time": random.randint(100, 1000),
        "liveramp_idl_response_status": random.choice(["SUCCESS", "TIMEOUT", "ERROR", "EMPTY_RESPONSE", "SKIPPED", "NA"]),
        "format_optimization_experiment_id": random.randint(1, 100),
        "business_rule_traffic_id": random.randint(1, 100),
        "thirty_three_across_response_time": random.randint(100, 1000),
        "thirty_three_across_response_status": random.choice(["SUCCESS", "TIMEOUT", "ERROR", "EMPTY_RESPONSE", "SKIPPED", "NA"]),
        "extended_id_source": [fake.uuid4() for _ in range(random.randint(1, 3))],
        "rtb_bidfloor_sampling_applied": random.choice([True, False]),
        "floor_traffic_id": random.randint(1, 100),
        "rtb_partner_id": [random.randint(1, 100) for _ in range(random.randint(1, 3))],
        "floor_traffic_allocation_percent": round(random.uniform(0.1, 1.0), 2),
        "nformats_traffic_id": random.randint(1, 100),
        "nformats_traffic_allocation_percent": round(random.uniform(0.1, 1.0), 2),
        "floor_traffic_logging_sample_percent": round(random.uniform(0.1, 1.0), 2),
        "up_bidding_experiment_id": random.randint(0, 100),
        "system_metrics": generate_system_metrics(),
        "pmp_deals_process_time_ms": random.randint(100, 1000),
        "deviceClassification": generate_device_classification(),
        "site_url": site_url,
        "ad_position": ad_position
    }


if __name__ == '__main__':
    # Generate a sample PageViewLog
    page_view_log = generate_page_view_log()

    # Print the generated data as JSON
    print(json.dumps(page_view_log, indent=4))