import random
import json
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_dimension():
    return {
        "width": random.randint(100, 1920),
        "height": random.randint(100, 1080)
    }

def generate_video_attributes():
    return {
        "video_placement_type": random.choice(["UNDEFINED_VIDEO_PLACEMENT", "IN_STREAM_PLACEMENT", "IN_BANNER_PLACEMENT", "IN_ARTICLE_PLACEMENT", "IN_FEED_PLACEMENT", "FLOATING_PLACEMENT"]),
        "video_api": random.choice(["VPAID", "MRAID", "ORMMA", "OMID"]),
        "video_proto": random.choice(["VAST_1_0", "VAST_2_0", "VAST_3_0", "VAST_4_0"]),
        "estimated_player_size_category": random.choice(["EXTRA_SMALL", "SMALL", "MEDIUM", "LARGE"]),
        "skippability": random.choice(["skippable", "nonskippable", "any"]),
        "startDelay": random.choice(["MID_ROLL", "PRE_ROLL", "GENERIC_MID_ROLL", "GENERIC_POST_ROLL"]),
        "min_duration": random.randint(5, 30),
        "max_duration": random.randint(30, 120)
    }

def generate_key_value_pair():
    return {
        "key": fake.word(),
        "value": fake.word()
    }

def generate_user_data_segment():
    return {
        "segtax": random.randint(1, 100),
        "segclass": fake.word(),
        "segment_ids": [random.randint(1, 100) for _ in range(random.randint(1, 5))]
    }

def generate_placement():
    return {
        "placement_id": fake.uuid4(),
        "container_width_dip": random.randint(100, 500),
        "exchangePlacementId": fake.uuid4(),
        "external_floor": round(random.uniform(0.1, 10.0), 2),
        "acceptable_sizes": [generate_dimension() for _ in range(random.randint(1, 3))],
        "interstitial": random.choice([True, False]),
        "upstream_imp_id": fake.uuid4(),
        "rewarded": random.choice([True, False]),
        "request_format": random.choice(["BANNER", "VIDEO", "NATIVE_BANNER", "NATIVE_VIDEO"]),
        "video_placement_type": random.choice(["UNDEFINED_VIDEO_PLACEMENT", "IN_STREAM_PLACEMENT", "IN_BANNER_PLACEMENT", "IN_ARTICLE_PLACEMENT", "IN_FEED_PLACEMENT", "FLOATING_PLACEMENT"]),
        "gpid": fake.uuid4(),
        "divid": fake.uuid4(),
        "video_attributes": generate_video_attributes(),
        "request_formats": [random.choice(["BANNER", "VIDEO", "NATIVE_BANNER", "NATIVE_VIDEO"]) for _ in range(random.randint(1, 3))],
        "request_targeting_error": random.choice([True, False]),
        "error_code": [fake.word() for _ in range(random.randint(1, 3))],
        "idx": random.randint(0, 10),
        "impression_id": random.randint(1000, 9999),
        "postfix": fake.word(),
        "original_placement_id": fake.uuid4(),
        "tagid": fake.uuid4(),
        "dfp_ad_unit_code": fake.uuid4(),
        "ad_position": fake.word(),
        "pod_ad_parent_impression_id": random.randint(1000, 9999)
    }

def generate_app_or_site_content():
    return {
        "episode": random.randint(1, 10),
        "title": fake.sentence(),
        "series": fake.word(),
        "season": fake.word(),
        "lang": fake.language_code(),
        "livestream": random.choice([True, False]),
        "contentCategories": [fake.word() for _ in range(random.randint(1, 3))],
        "genres": [fake.word() for _ in range(random.randint(1, 3))],
        "producerNames": [fake.name() for _ in range(random.randint(1, 3))],
        "channel": fake.word(),
        "network": fake.word()
    }

def generate_upstream_request_properties():
    return {
        "site_id": fake.uuid4(),
        "site_name": fake.company(),
        "site_domain": fake.domain_name(),
        "app_domain": fake.domain_name(),
        "pub_content_categories": [fake.word() for _ in range(random.randint(1, 3))],
        "site_content_categories": [fake.word() for _ in range(random.randint(1, 3))],
        "app_content_categories": [fake.word() for _ in range(random.randint(1, 3))]
    }

def generate_page_view_request():
    return {
        "sdk_type": fake.word(),
        "dnt": random.choice([True, False]),
        "placements": [generate_placement() for _ in range(random.randint(1, 3))],
        "location_type": random.choice(["IP", "WC3", "SDK", "GPS", "USER_DEFINED", "UPSTREAM_IP", "UNKNOWN"]),
        "connection_type": random.choice(["Cellular", "Wifi"]),
        "isp": fake.company(),
        "adserver_start_time": int(datetime.now().timestamp()),
        "page_view_time": int(datetime.now().timestamp()),
        "gmt_hour_offset_time_zone": random.randint(-12, 12),
        "requested_host": fake.domain_name(),
        "request_id": random.randint(1000, 9999),
        "adserver_id": random.randint(1, 100),
        "proxy_id": random.randint(1, 100),
        "locale": fake.locale(),
        "language": fake.language_code(),
        "apple_vendor_id": fake.uuid4(),
        "system_name": fake.word(),
        "system_version": fake.numerify("##.##"),
        "bundle_version_key": fake.uuid4(),
        "device_advertising_id": fake.uuid4(),
        "model": fake.word(),
        "bundle_version": fake.numerify("##.##"),
        "bundle_signature": fake.uuid4(),
        "bundle_identifier": fake.uuid4(),
        "my_App_id": fake.uuid4(),
        "ads_rate": round(random.uniform(0.1, 10.0), 2),
        "sdk_version": fake.numerify("##.##"),
        "device_type": fake.word(),
        "force_invalidation": random.choice([True, False]),
        "is_secure": random.choice([True, False]),
        "is_amp": random.choice([True, False]),
        "environment_id": random.randint(1, 100),
        "placement_width_pixels": random.randint(100, 1920),
        "placement_height_pixels": random.randint(100, 1080),
        "offplatform_user_id": fake.uuid4(),
        "offplatform_source": fake.word(),
        "is_prefetch": random.choice([True, False]),
        "auction_id": fake.uuid4(),
        "macro_1": fake.word(),
        "exchange_auction_id": fake.uuid4(),
        "is_app": random.choice([True, False]),
        "app_name": fake.word(),
        "app_keywords": fake.words(nb=3),
        "app_content_url": fake.url(),
        "dfp_ad_unit_codes": fake.uuid4(),
        "tag_ids": fake.uuid4(),
        "app_store_url": fake.url(),
        "supply_source": random.choice(["COP", "PREBID_JS", "PREBID_SERVER", "EBDA", "TAM", "ORTB"]),
        "tmax": random.randint(100, 1000),
        "omidon": fake.uuid4(),
        "omidpv": fake.uuid4(),
        "placements_exceeding_cap": [fake.uuid4() for _ in range(random.randint(1, 3))],
        "inventory_source": fake.word(),
        "has_liveramp_ats_envelope": random.choice([True, False]),
        "appOrSiteContent": generate_app_or_site_content(),
        "mapped_inventory_verticals": [random.randint(1, 100) for _ in range(random.randint(1, 3))],
        "ad_pod_position": random.randint(1, 10),
        "key_value_pairs": [generate_key_value_pair() for _ in range(random.randint(1, 3))],
        "id5_partner_ids": [fake.uuid4() for _ in range(random.randint(1, 3))],
        "back_filled_id5_partner_ids": [fake.uuid4() for _ in range(random.randint(1, 3))],
        "is_publisher_throttling_control_request": random.choice([True, False]),
        "is_publisher_request_throttled": random.choice([True, False]),
        "upstream_request_properties": generate_upstream_request_properties(),
        "placementByImpressionId": {str(random.randint(1000, 9999)): generate_placement() for _ in range(random.randint(1, 3))},
        "supply_implementation_type": random.choice(["COP", "PREBID_JS", "PREBID_SERVER", "EBDA", "TAM", "ORTB", "VAST_TAGS"]),
        "user_data_segment": [generate_user_data_segment() for _ in range(random.randint(1, 3))],
        "throttled_impression_ids": [random.randint(1000, 9999) for _ in range(random.randint(1, 3))],
        "supply_chain_advertising_system_identifier": [fake.uuid4() for _ in range(random.randint(1, 3))]
    }

def generate_creative():
    return {
        "creativeId": random.randint(1000, 9999),
        "advertiserId": random.randint(1000, 9999),
        "cost": round(random.uniform(0.1, 10.0), 2),
        "bidType": random.choice(["CPC", "CPM", "CPV", "CPP"]),
        "learning": random.choice([True, False]),
        "categoryId": random.randint(1, 100),
        "eCpm": round(random.uniform(0.1, 10.0), 2),
        "ctr": round(random.uniform(0.01, 0.99), 2),
        "productRecommendationStrategyId": random.randint(1, 100),
        "productIds": [fake.uuid4() for _ in range(random.randint(1, 3))],
        "adomain": fake.domain_name(),
        "advertiser_cost": round(random.uniform(0.1, 10.0), 2),
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
        "viewability": round(random.uniform(0.1, 1.0), 2),
        "playRate": round(random.uniform(0.1, 1.0), 2),
        "bidder_id": random.randint(1, 100),
        "exchange_cost": round(random.uniform(0.1, 10.0), 2),
        "gross_exchange_cost": round(random.uniform(0.1, 10.0), 2),
        "internal_vpaid_tracking_enabled": random.choice([True, False]),
        "business_rule_experiment_entry_id": random.randint(1, 100),
        "bidder_margin_override": round(random.uniform(0.1, 10.0), 2),
        "play_rate_prediction_model_category_id": random.randint(1, 100),
        "default_margin": round(random.uniform(0.1, 10.0), 2),
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
        "bid_internal_auction_price": round(random.uniform(0.1, 10.0), 2),
        "advertiser_auction_macro_price": round(random.uniform(0.1, 10.0), 2),
        "exchange_post_auction_discount_id": random.randint(1, 100),
        "applicable_margin": round(random.uniform(0.1, 10.0), 2),
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

def generate_impression():
    return {
        "impression_id": random.randint(1000, 9999),
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
        "creatives": [generate_creative() for _ in range(random.randint(1, 3))],
        "is_licensed_format": random.choice([True, False]),
        "ab_test_names": [fake.word() for _ in range(random.randint(1, 3))],
        "phantom_creatives": [generate_creative() for _ in range(random.randint(1, 3))],
        "exchange_cost": round(random.uniform(0.1, 10.0), 2),
        "gross_exchange_cost": round(random.uniform(0.1, 10.0), 2),
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

def generate_system_metrics():
    return {
        "heap_used_mb": random.randint(100, 1000),
        "heap_used_ratio": round(random.uniform(0.1, 1.0), 2)
    }

def generate_page_view_log():
    return {
        "impressions": [generate_impression() for _ in range(random.randint(1, 3))],
        "request": generate_page_view_request(),
        "page_view_id": random.randint(1000, 9999),
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
            "purpose": random.randint(1, 10),
            "vendors": random.randint(1, 10),
            "vendors_sample": random.randint(1, 10),
            "ccpa_string": fake.uuid4(),
            "legitimate_interests": random.randint(1, 10),
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
        "pmp_deals_process_time_ms": random.randint(100, 1000)
    }


if __name__ == '__main__':
    page_view_log = generate_page_view_log()
    print(json.dumps(page_view_log, indent=4))