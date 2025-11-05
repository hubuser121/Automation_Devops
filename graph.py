# automation_metrics.py
# Author: Karthik Naik K
# Purpose: Compare DevOps Automation vs Manual Process performance

import matplotlib.pyplot as plt

# Data
metrics = ['Build Time (min)', 'Error Rate (%)', 'Success Rate (%)']
manual = [30, 15, 85]       # Example manual process values
automated = [5, 2, 98]      # Example automated process values

# Create figure
plt.figure(figsize=(10, 6))

# Bar chart comparison
x = range(len(metrics))
plt.bar(x, manual, width=0.35, label='Manual Process', color='tomato')
plt.bar([p + 0.35 for p in x], automated, width=0.35, label='Automated Process', color='seagreen')

# Labels & aesthetics
plt.title('Automation vs Manual Process in DevOps', fontsize=14, weight='bold')
plt.xticks([p + 0.175 for p in x], metrics, rotation=15, fontsize=11)
plt.ylabel('Performance Values', fontsize=12)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.6)

# Save and display
plt.tight_layout()
plt.savefig('automation_performance_comparison.png', dpi=300)
plt.show()

print("✅ Graph generated and saved as 'automation_performance_comparison.png'")
