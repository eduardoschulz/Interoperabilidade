import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import json

mpl.use('QtAgg') 
files = ["../logs/oai/oai/iperf/oai-oaicn",
         "../logs/srsran/oai/iperf/20240304-oai",
         "../logs/oai/open5gs/iperf/oai-open5gs",
         "../logs/srsran/open5gs/iperf/20240320",
         "../logs/oai/free5gc/iperf/20240304-oai-free5gc",
         "../logs/srsran/free5gc/iperf/20240304-free5gc"
]
labels = [
        "OAI CN",
        "Open5Gs",
        "Free5Gc",
]

rans = ["OAI", "srsRAN"]

def conv(x):
    return x['end']['sum_sent']['retransmits']

def readfile(file):
    with open(file, "r") as file:
        data = json.load(file)
    return conv(data)


x = np.arange(len(labels))  # the label locations
width = 0.33  # the width of the bars
multiplier = 0

colors = ["#7EA16B", "#C3D898"]
fig, ax = plt.subplots(layout='constrained')

for i in range(len(files)//len(labels)):
    offset = width * multiplier
    index = i
    data = (readfile(files[index]), readfile(files[index+2]), readfile(files[index+4]))
    rects = ax.bar(x + offset, data, width, label=rans[i], color=colors[i])
    ax.bar_label(rects, padding=2)
    multiplier += 1

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Número de pacotes retransmitidos')
ax.set_xticks(x + width/2, labels)
ax.set_ylim(0, 3500)
ax.legend(loc='upper right', ncols=2)

plt.show()
