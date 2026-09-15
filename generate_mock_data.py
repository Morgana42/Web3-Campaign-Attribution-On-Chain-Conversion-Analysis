import pandas as pd
import random
import uuid
import time

# Configuration parameters
num_users = 50
campaigns = ['cbwallet', 'bestprice', 'mev']
sources = ['ClientX', 'hypelab', 'slise']
mediums = ['paid_display', 'organic_social']
target_contract = '0xEXAMPLE9bD2B4ADddBc894D8697F5170800EAdeC'
base_url = 'https://app.example-dapp.xyz'

# Generate unique identifiers for mock users
user_ids = [uuid.uuid4().hex for _ in range(num_users)]
twitter_ids = [str(random.randint(1000000000, 9999999999)) for _ in range(num_users)]
addresses = [f"0x{random.getrandbits(160):040x}" for _ in range(num_users)]

# 1. Mapping: Twitter ID to Wallet Address
mapping_df = pd.DataFrame({
    'twitter_id': twitter_ids,
    'address': addresses
})
mapping_df.to_csv('mock_address_twitter_id_mapping.csv', index=False)

# 2. Campaigns: Daily activity data
campaign_data = []
for camp in campaigns:
    for src in sources:
        campaign_data.append({
            'campaign_id': str(uuid.uuid4()),
            'utm_campaign': camp,
            'utm_source': src,
            'utm_medium': random.choice(mediums)
        })
        
campaigns_df = pd.DataFrame(campaign_data)
campaigns_df.to_csv('mock_campaigns_daily_activity.csv', index=False)

# 3. Events: User interactions on the platform
events_data = []
event_names = ['sign_in', 'Purchase Click', 'PageView', 'swap_executed']

# Simulate an average of 3 events per user
for i in range(num_users * 3):
    user = random.choice(user_ids)
    t_id = random.choice(twitter_ids)
    camp = random.choice(campaigns)
    src = random.choice(sources)
    
    # Build target URL including UTM parameters
    url = f"{base_url}/trade?twitterid={t_id}&utm_campaign={camp}&utm_source={src}&utm_medium=paid_display"
    
    events_data.append({
        'user_id': user,
        'event_time': int(time.time()) - random.randint(1000, 100000),
        'event_name': random.choice(event_names),
        'full_url': url
    })

events_df = pd.DataFrame(events_data).sort_values(by='event_time')
events_df.to_csv('mock_events.csv', index=False)

# 4. Transactions: On-chain activity
transactions_data = []

# Assume a ~30% on-chain conversion rate
converted_users = random.sample(addresses, int(num_users * 0.3))

for addr in converted_users:
    transactions_data.append({
        'From': addr,
        'To': target_contract,
        'amount': round(random.uniform(0.1, 5.0), 4)
    })

transactions_df = pd.DataFrame(transactions_data)
transactions_df.to_csv('mock_transactions.csv', index=False)

print("Mock data files created successfully.")