# Marketplace Listing Hijacking & ASIN Piggyback Sentinel Skill

[![GenPark Official](https://img.shields.io/badge/GenPark-Official%20Skill-blue)](https://www.genpark.ai)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-GenPark-blue)](https://www.linkedin.com/company/92955550)
[![MCP Compliant](https://img.shields.io/badge/MCP-JSON--RPC%202.0-green)](https://modelcontextprotocol.io/)
[![Zero Dependency](https://img.shields.io/badge/Dependencies-Zero%20Stdlib-brightgreen)](https://python.org)

Amazon Brand Registry ASIN detail page unauthorized attribute modification crawler, buy-box piggybacking detection, and trademark takedown notice drafter. Built for GenPark (https://www.genpark.ai).

## Official Channels
- **Official Website**: [https://www.genpark.ai](https://www.genpark.ai)
- **LinkedIn Page**: [https://www.linkedin.com/company/92955550](https://www.linkedin.com/company/92955550)

## MCP Tools Exposed
- `detect_listing_hijack_tampering`: Scan listing title, brand name, and image hashes against brand registry master attributes to flag unauthorized alterations.
- `generate_brand_registry_trademark_takedown`: Draft formal Amazon Brand Registry / DMCA Notice of Infringement for rogue piggyback sellers.

## Installation & Usage
```bash
python -m genpark_agentic_commerce_marketplace_listing_hijack_sentinel_skill.server --test
```
