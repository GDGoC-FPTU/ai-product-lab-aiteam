"""Generate 04-workflow-diagram.png: Current-State Workflow (Vinmec - nhac tai kham/uong thuoc)."""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

steps = [
    {
        "title": "1. Loc danh sach benh nhan",
        "detail": "He thong HIS loc benh nhan\nman tinh den han tai kham/thuoc",
        "time": "~1 phut/lot",
        "bottleneck": False,
    },
    {
        "title": "2. Tra phac do dieu tri",
        "detail": "NV tong dai tra cuu phac do\ndieu tri rieng cua tung benh nhan",
        "time": "~4 phut/BN",
        "bottleneck": True,
    },
    {
        "title": "3. Goi dien nhac lich/thuoc",
        "detail": "NV goi dien thoai thu cong\nnhac lich tai kham / uong thuoc",
        "time": "~5 phut/BN",
        "bottleneck": True,
    },
    {
        "title": "4. Ghi chu ket qua",
        "detail": "NV ghi chu ket qua cuoc goi\nvao ho so benh an (HIS)",
        "time": "~1 phut/BN",
        "bottleneck": False,
    },
]

handoffs = [
    "[HANDOFF]\nHe thong -> NV",
    "[HANDOFF]\nNV -> Benh nhan",
    "[HANDOFF]\nNV -> He thong",
]

fig, ax = plt.subplots(figsize=(15, 6))
ax.set_xlim(0, 15)
ax.set_ylim(0, 6)
ax.axis("off")

ax.text(7.5, 5.6, "CURRENT-STATE WORKFLOW — Nhac tai kham & uong thuoc cho benh nhan man tinh (Vinmec)",
        ha="center", va="center", fontsize=14, fontweight="bold")

box_w, box_h = 2.8, 2.4
gap = 0.85
start_x = 0.6
y = 2.2

centers = []
for i, step in enumerate(steps):
    x = start_x + i * (box_w + gap)
    centers.append(x + box_w / 2)
    face = "#ffe0e0" if step["bottleneck"] else "#e8f0fe"
    edge = "#d33" if step["bottleneck"] else "#3366cc"
    box = FancyBboxPatch((x, y), box_w, box_h,
                          boxstyle="round,pad=0.05,rounding_size=0.12",
                          linewidth=2.2, edgecolor=edge, facecolor=face)
    ax.add_patch(box)

    ax.text(x + box_w / 2, y + box_h - 0.35, step["title"],
            ha="center", va="top", fontsize=10.5, fontweight="bold", wrap=True)
    ax.text(x + box_w / 2, y + box_h / 2 - 0.15, step["detail"],
            ha="center", va="center", fontsize=9)
    ax.text(x + box_w / 2, y + 0.3, f"TIME: {step['time']}",
            ha="center", va="center", fontsize=9.5, fontweight="bold")

    if step["bottleneck"]:
        ax.text(x + box_w / 2, y + box_h + 0.32, "● BOTTLENECK",
                ha="center", va="center", fontsize=9.5, fontweight="bold", color="#d33")

# Arrows + handoff labels between boxes
for i in range(len(steps) - 1):
    x_start = start_x + i * (box_w + gap) + box_w
    x_end = x_start + gap
    arrow = FancyArrowPatch((x_start, y + box_h / 2), (x_end, y + box_h / 2),
                             arrowstyle="-|>", mutation_scale=20, linewidth=2, color="#444")
    ax.add_patch(arrow)
    ax.text((x_start + x_end) / 2, y - 0.3, handoffs[i],
            ha="center", va="top", fontsize=8, color="#555", style="italic")

ax.text(7.5, 0.55, "TONG CONG = ~11 phut / benh nhan  |  ● Bottleneck: buoc 2 & 3 (tra phac do + goi dien thu cong)",
        ha="center", va="center", fontsize=11.5, fontweight="bold",
        bbox=dict(boxstyle="round,pad=0.4", facecolor="#fff3cd", edgecolor="#d9a441"))

plt.tight_layout()
plt.savefig("04-workflow-diagram.png", dpi=200, bbox_inches="tight")
print("Saved 04-workflow-diagram.png")
