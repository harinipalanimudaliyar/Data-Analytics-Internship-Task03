import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# [Step 1] Load your raw website logs
print("Parsing data stream logs...")
df = pd.read_csv('dataset.csv')

# [Step 2] Calculate unique users at each milestone step
view_item = df[df['event_name'] == 'view_item']['user_id'].nunique()
add_to_cart = df[df['event_name'] == 'add_to_cart']['user_id'].nunique()
checkout = df[df['event_name'] == 'begin_checkout']['user_id'].nunique()
purchase = df[df['event_name'] == 'purchase']['user_id'].nunique()

steps = ['1. View Item', '2. Add to Cart', '3. Begin Checkout', '4. Purchase']
counts = [view_item, add_to_cart, checkout, purchase]

# [Step 3] Calculate Real-World Industry Metrics
# Conversion Rate compared to the very first step (Baseline = 100%)
conversion_rates = [(c / counts[0]) * 100 for c in counts]

# Drop-off rate from the immediate previous step
drop_off_rates = [0.0]  # First step has no previous step
for i in range(1, len(counts)):
    drop = ((counts[i-1] - counts[i]) / counts[i-1]) * 100
    drop_off_rates.append(drop)

# [Step 4] Generate the Enterprise Visual Funnel Graph
print("Deploying visual funnel exploration engine...")
fig, ax1 = plt.subplots(figsize=(10, 6))

# Primary Axis: Bar chart for Conversion Percentage
colors = ['#1A237E', '#283593', '#3F51B5', '#7986CB'] # Professional corporate dark blues
bars = ax1.bar(steps, conversion_rates, color=colors, width=0.55, edgecolor='black', alpha=0.9)

# Secondary Axis: Trend line for Step-by-Step Attrition (Drop-off)
ax2 = ax1.twinx()
line = ax2.plot(steps, drop_off_rates, color='#D32F2F', marker='o', linewidth=2, linestyle='--', label='Step Drop-off %')

# Overlay data labels on top of the bars (Showing baseline conversion)
for bar, count in zip(bars, counts):
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2., height + 2,
             f'{height:.1f}%\n({count} Users)', ha='center', va='bottom', fontweight='bold', color='#1A237E', fontsize=10)

# Overlay drop-off leak markers
for i, drop in enumerate(drop_off_rates):
    if i > 0: # Skip the first step
        ax2.text(i, drop + 3, f'-{drop:.1f}% Leak', ha='center', va='bottom', color='#D32F2F', fontweight='bold', fontsize=10)

# Clean up axes styling to look polished
ax1.set_title('GA4 E-commerce Funnel: Conversion Performance & Friction Points', fontsize=13, fontweight='bold', pad=20)
ax1.set_ylabel('Cumulative Conversion Rate (%)', fontsize=11, fontweight='bold', color='#1A237E')
ax2.set_ylabel('Step Attrition Leak Rate (%)', fontsize=11, fontweight='bold', color='#D32F2F')
ax1.set_ylim(0, 120)
ax2.set_ylim(0, 100)
ax1.grid(axis='y', linestyle=':', alpha=0.5)

plt.tight_layout()

# Save the picture file into your local Colab session
plt.savefig('funnel_dropoff_chart.png', dpi=300)
plt.show()

print("\n📊 Pipeline run complete. 'funnel_dropoff_chart.png' has been saved!")
