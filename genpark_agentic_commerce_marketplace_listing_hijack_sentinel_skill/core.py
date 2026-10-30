# -*- coding: utf-8 -*-
"""Marketplace Listing Hijacking Sentinel for GenPark Agentic Commerce."""
import json
from typing import Dict, Any

class MarketplaceListingHijackSentinel:
    @staticmethod
    def detect_listing_hijack_tampering(asin: str, master_brand_name: str, current_page_brand: str, unauthorized_sellers_count: int = 0) -> Dict[str, Any]:
        brand_altered = master_brand_name.strip().lower() != current_page_brand.strip().lower()
        has_piggybackers = unauthorized_sellers_count > 0
        is_compromised = brand_altered or has_piggybackers
        
        return {
            "asin": asin,
            "registered_brand": master_brand_name,
            "scraped_brand": current_page_brand,
            "unauthorized_seller_count": unauthorized_sellers_count,
            "listing_integrity_breached": is_compromised,
            "hijack_severity": "CRITICAL_BRAND_ATTRIBUTE_HIJACK" if brand_altered else ("ROGUE_PIGGYBACK_RESELLERS" if has_piggybackers else "CLEAN_LISTING"),
            "recommended_action": "SUBMIT_IMMEDIATE_BRAND_REGISTRY_INFRACTION" if is_compromised else "ROUTINE_MONITORING"
        }

    @staticmethod
    def generate_brand_registry_trademark_takedown(asin: str, trademark_reg_number: str, violator_merchant_id: str) -> Dict[str, Any]:
        complaint = f"""FORMAL NOTICE OF TRADEMARK INFRINGEMENT & LISTING TAMPERING

To: Amazon Brand Registry Infringement Team
ASIN: {asin}
Merchant ID: {violator_merchant_id}
Registered Trademark Number: {trademark_reg_number}

The seller identified by Merchant ID {violator_merchant_id} is unlawfully piggybacking on our branded ASIN {asin} offering counterfeit or unauthorized reproductions. We have not authorized this distributor to market our registered goods.

We request immediate removal of the infringing merchant from this listing to prevent customer confusion and brand dilution.
"""
        return {
            "asin": asin,
            "violator_id": violator_merchant_id,
            "trademark_registration": trademark_reg_number,
            "takedown_notice_text": complaint,
            "submission_route": "Amazon Brand Registry Report a Violation Tool (RAV)"
        }
