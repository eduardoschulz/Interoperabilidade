import numpy as np
from matplotlib.patches import Polygon
import matplotlib.pyplot as plt
import matplotlib as mpl
import json

files = ["../logs/oai/oai/iperf/oai-oaicn",
         "../logs/srsran/oai/iperf/20240304-oai",
         "../logs/oai/open5gs/iperf/oai-open5gs",
         "../logs/srsran/open5gs/iperf/20240320",
         "../logs/oai/free5gc/iperf/20240304-oai-free5gc",
         "../logs/srsran/free5gc/iperf/20240304-free5gc"
]
labels = [
        "OAI CN",
        "Open5GS",
        "Free5GC",
]
rans = [
        "OAI RAN",
        "srsRAN",
        "_OAI",
        "_srsRAN",
        "_OAI",
        "_srsRAN",
]


def conv(x):
    stream = x['streams'][0]
    # rtt comes in micro seconds and we convert it to ms (https://github.com/esnet/iperf/blob/332c31ee6512514c216077407a725b5b958b1582/src/tcp_info.c#L168)
    return float(stream['rtt'])/1_000

def from_iter(x):
    return [conv(t) for t in x['intervals']]

def build(save=True):
    count = len(files)
    total_count = len(labels)
    fig, ax = plt.subplots(1,1)
    fig.supylabel("RTT (ms)", fontsize=16)

    dataset = []
    for i in range(count):
        with open(files[i], "r") as file:
            data = json.load(file)
        dataset.append(list(from_iter(data)))

    colors = ["#7EA16B", "#C3D898"]
    b = ax.boxplot(dataset, labels=rans, medianprops={"color": "#000000"})
    for i in range(len(b['boxes'])):
        box = b['boxes'][i]
        ax.add_patch(Polygon(box.get_xydata(), facecolor=colors[i%2], label=rans[i]))

    x = np.arange(len(labels)) * 2 + 1.5
    ax.set_xticks(x, labels, fontsize=16)
    ax.legend(loc='upper right', ncols=2, fontsize=14)

#fig.tight_layout(pad=0.1)

    fig.set_size_inches(10.4, 4.2)
    plt.tight_layout()
#plt.show()
    if save:
        fig.savefig("figs/rtt.pdf", dpi=100)

if __name__ == "__main__":
    build(False)
    mpl.use('QtAgg') 
    plt.show()
