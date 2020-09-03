###########################################################################
#
#  Copyright 2020 Google LLC
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
###########################################################################

accountActiveAdSummary_Schema = [
  {
    "description": "",
    "name": "accountId",
    "type": "INT64",
    "mode": "NULLABLE"
  },
  {
    "description": "",
    "name": "activeAds",
    "type": "INT64",
    "mode": "NULLABLE"
  },
  {
    "description": "ACTIVE_ADS_TIER_100K, ACTIVE_ADS_TIER_1M, ACTIVE_ADS_TIER_200K, ACTIVE_ADS_TIER_300K, ACTIVE_ADS_TIER_40K, ACTIVE_ADS_TIER_500K, ACTIVE_ADS_TIER_750K, ACTIVE_ADS_TIER_75K",
    "name": "activeAdsLimitTier",
    "type": "STRING",
    "mode": "NULLABLE"
  },
  {
    "description": "",
    "name": "availableAds",
    "type": "INT64",
    "mode": "NULLABLE"
  },
  {
    "description": "",
    "name": "kind",
    "type": "STRING",
    "mode": "NULLABLE"
  }
]
