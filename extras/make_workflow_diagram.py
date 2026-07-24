"""
Sinh sơ đồ Current-State Workflow cho Lab 02 (Xanh SM — sự cố hết pin thực địa).
Xuất ra: 04-workflow-diagram.png ở thư mục gốc repo.

Chạy:  python extras/make_workflow_diagram.py

Lưu ý sư phạm: Rubric G1 (20đ) ưu tiên bản VẼ TAY của nhóm. File này là bản số hoá
"sạch" để (a) đảm bảo có file hợp lệ cho autograder, (b) làm mẫu tham chiếu. Nhóm nên
chụp/đính kèm bản vẽ tay của mình nếu muốn tối đa điểm phần trình bày.
"""

import os
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

# --- Bảng màu ---
COL_NORMAL = "#E3F2FD"   # xanh nhạt: bước thường
COL_NORMAL_EDGE = "#1565C0"
COL_BOTTLE = "#FDECEA"   # đỏ nhạt: bottleneck
COL_BOTTLE_EDGE = "#C62828"
COL_TEXT = "#0D1B2A"

# (tiêu đề, chi tiết, thời gian, có phải bottleneck?)
STEPS = [
    ("1. Nhận cuộc gọi\nbáo sự cố", "Dispatcher\nIn: điện thoại", "2 phút", False),
    ("2. Tra vị trí\nGPS xe", "Dispatcher\nbản đồ nội bộ", "2 phút", False),
    ("3. Tra trạm sạc trống\n(đúng cổng sạc)", "Dispatcher\ndashboard VinFast", "5 phút", True),
    ("4. Soạn tin nhắn\nchỉ đường (tay)", "Dispatcher\ngửi qua App", "5 phút", True),
    ("5. Gọi xe cứu hộ\n(nếu pin quá thấp)", "Dispatcher\nhotline cứu hộ", "1 phút", False),
]


def build() -> str:
    fig, ax = plt.subplots(figsize=(16.5, 6.2))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 40)
    ax.axis("off")

    # Tiêu đề
    ax.text(
        50, 37.5,
        "Xanh SM — Current-State Workflow: Xử lý sự cố hết pin thực địa",
        ha="center", va="center", fontsize=17, fontweight="bold", color=COL_TEXT,
    )
    ax.text(
        50, 34.3,
        "Actor: Điều phối viên (Dispatcher)   |   Quy trình thủ công 100%",
        ha="center", va="center", fontsize=11, color="#455A64",
    )

    n = len(STEPS)
    box_w, box_h = 15.5, 12.5
    gap = (100 - n * box_w) / (n + 1)
    y = 15

    centers = []
    for i, (title, sub, dur, bottleneck) in enumerate(STEPS):
        x = gap + i * (box_w + gap)
        cx = x + box_w / 2
        centers.append(cx)

        face = COL_BOTTLE if bottleneck else COL_NORMAL
        edge = COL_BOTTLE_EDGE if bottleneck else COL_NORMAL_EDGE

        ax.add_patch(FancyBboxPatch(
            (x, y), box_w, box_h,
            boxstyle="round,pad=0.3,rounding_size=1.2",
            facecolor=face, edgecolor=edge, linewidth=2.2,
        ))
        ax.text(cx, y + box_h - 3.0, title, ha="center", va="center",
                fontsize=11, fontweight="bold", color=COL_TEXT)
        ax.text(cx, y + box_h / 2 - 1.2, sub, ha="center", va="center",
                fontsize=8.5, color="#37474F")
        # nhãn thời gian
        ax.text(cx, y - 2.2, f"Thời gian: {dur}", ha="center", va="center",
                fontsize=10, fontweight="bold",
                color=COL_BOTTLE_EDGE if bottleneck else "#1565C0")
        if bottleneck:
            ax.plot(cx - 5.6, y + box_h + 2.0, marker="o", markersize=10,
                    color=COL_BOTTLE_EDGE)
            ax.text(cx - 4.2, y + box_h + 2.0, "BOTTLENECK", ha="left", va="center",
                    fontsize=9.5, fontweight="bold", color=COL_BOTTLE_EDGE)

    # Mũi tên nối các bước
    for i in range(n - 1):
        x0 = centers[i] + box_w / 2
        x1 = centers[i + 1] - box_w / 2
        # handoff (chuyển giao qua kênh khác) ở bước 1->2 và 4->5
        is_handoff = i in (0, 3)
        ax.add_patch(FancyArrowPatch(
            (x0, y + box_h / 2), (x1, y + box_h / 2),
            arrowstyle="-|>", mutation_scale=22, linewidth=2,
            color="#78909C",
            linestyle="dashed" if is_handoff else "solid",
        ))
        if is_handoff:
            ax.text((x0 + x1) / 2, y + box_h / 2 + 2.1, "Handoff",
                    ha="center", va="center", fontsize=8, color="#546E7A",
                    style="italic")

    # Tổng thời gian
    ax.add_patch(FancyBboxPatch(
        (33, 3.2), 34, 5.2,
        boxstyle="round,pad=0.3,rounding_size=1.2",
        facecolor="#FFF8E1", edgecolor="#F9A825", linewidth=2,
    ))
    ax.text(50, 5.8, "TỔNG THỜI GIAN THỦ CÔNG = 15 phút / lượt",
            ha="center", va="center", fontsize=12.5, fontweight="bold", color="#E65100")

    # Chú thích
    ax.plot(3, 1.4, marker="o", markersize=9, color=COL_BOTTLE_EDGE)
    ax.text(5, 1.4,
            "Bottleneck (bước 3 & 4 chiếm 10/15 phút)      "
            "Handoff = chuyển giao thông tin qua kênh khác (mũi tên nét đứt)",
            ha="left", va="center", fontsize=8.5, color="#607D8B")

    out_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                            "04-workflow-diagram.png")
    fig.savefig(out_path, dpi=150, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    return out_path


if __name__ == "__main__":
    path = build()
    print(f"[OK] Da xuat so do: {path}")
