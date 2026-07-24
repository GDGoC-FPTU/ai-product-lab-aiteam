# 02 — Deep-Dive Report (Bài nhóm)

> **Deliverable nhóm (G1–G4 — 40 điểm).** Phân tích sâu bài toán AI mà cả nhóm thống nhất chọn.

---

## 👥 Thông tin nhóm

| | |
|---|---|
| **Tên nhóm** | AI_Team |
| **Mảng kinh doanh** | Xanh SM (GSM) — Vận hành xe điện thời gian thực |
| **Bài toán chọn Deep-Dive** | Trợ lý điều vận sự cố hết pin thực địa (Field-Incident Dispatch Co-pilot) |

| # | Họ và tên | MSSV | Nhiệm vụ chính |
|---|-----------|------|----------------|
| 1 | Kim Mạnh Hưng | 2A202601679 | Prompt prototype (Phase 4 code) |
| 2 | Ong Xuân Sơn | 2A202601327 | Problem Statement & Evaluate |
| 3 | Đinh Lê Quỳnh Phương | 2A202600294 | Future-state & AI Fit |
| 4 | Phùng Văn Linh | 2A202600123 | Workflow mapping (04-diagram) |

---

## 🗳️ Quyết định lựa chọn bài toán

Nhóm quyết định Deep-Dive bài toán **“Xanh SM — Trợ lý điều vận sự cố hết pin thực địa”**.

**Lý do chọn & loại các phương án khác:**
- ✅ **Chọn Xanh SM (sự cố thực địa):** tác động real-time trực tiếp lên doanh thu, tần suất cao (~80 lượt/ngày ở Hà Nội), kiến trúc gọn (LLM Feature), và có ranh giới an toàn đo được để lập trình prototype.
- ❌ **Vinhomes (phản ánh cư dân):** giá trị tốt nhưng rủi ro sai sót liên quan phí quản lý/tranh chấp căn hộ → cần Rule-based router + dữ liệu gán nhãn trước.
- ❌ **Vinmec (discharge summary):** thuộc mảng y tế nhạy cảm, ranh giới an toàn phải cực nghiêm; để lại giai đoạn sau khi đã có quy trình kiểm duyệt lâm sàng.

---

## 🏗️ Phase 3 — DEEP-DIVE

### 3.1. Current-State Workflow Mapping (G1 — 20đ)

> Sơ đồ vẽ tay/vẽ số chi tiết nằm ở file **[04-workflow-diagram.png](04-workflow-diagram.png)**. Dưới đây là bản text đồng bộ với sơ đồ đó.

```text
[Tài xế]                 [Điều phối viên — Dispatcher]                       [Hệ thống]
   │                                                                             │
   │  ① Gọi tổng đài báo hết pin (⏱ 2') ──🔄 Handoff (thoại)──►  Ghi log sự cố   │
   │                                                                             │
   │                     ② Tra vị trí GPS xe trên bản đồ nội bộ (⏱ 2')           │
   │                          │                                                  │
   │                          ▼                                                  │
   │                     ③ Tra dashboard trạm sạc VinFast tìm trụ trống          │
   │                        + đúng cổng sạc theo dòng xe  🔴 (⏱ 5')              │
   │                          │                                                  │
   │                          ▼                                                  │
   │                     ④ Soạn tin nhắn chỉ đường bằng tay,                     │
   │                        gửi qua App tài xế  🔴 (⏱ 5')  ──🔄 Handoff──►  App   │
   │                          │                                                  │
   │                          ▼                                                  │
   │                     ⑤ Gọi xe cứu hộ nếu pin quá thấp (⏱ 1')                 │
   ▼                                                                             │
[Nhận hướng dẫn]                                                                 │

🔴 Bottleneck: Bước ③ (tra trạm) & ④ (soạn tin) — chiếm 10/15 phút, dễ chọn nhầm trạm/cổng sạc.
🔄 Handoff: (a) thoại tài xế→điều phối; (b) tin nhắn điều phối→App tài xế.
⏱ TỔNG THỜI GIAN THỦ CÔNG = 15 phút/lượt.
```

**Con số vận hành (baseline giả định để scoping):**
- ~80 sự cố pin thực địa/ngày tại Hà Nội × 15 phút = **20 giờ-người/ngày** cho riêng khâu này.
- Giờ cao điểm, hàng chờ xử lý tăng → tài xế chờ trung bình 15–25 phút → **~15% cuốc bị bỏ lỡ** trong thời gian xe "chết".

### 3.2. Problem Statement (6-field) & Metrics (G2 — 20đ)

| Field | Nội dung chi tiết |
|---|---|
| **1. Actor / Operator** | Điều phối viên (Dispatcher) tại Trung tâm Điều vận Xanh SM Hà Nội; ca 8 tiếng, cao điểm 7–9h & 17–20h. |
| **2. Current Workflow** | Tài xế gọi báo hết pin → điều phối viên (1) tra GPS xe, (2) mở dashboard trạm sạc VinFast tìm trụ trống đúng cổng sạc theo dòng xe (VF5/VFe34/VF8), (3) gõ tay tin nhắn chỉ đường tiếng Việt gửi qua App, (4) gọi cứu hộ nếu pin quá thấp. 5 bước, hoàn toàn thủ công, dùng bản đồ nội bộ + dashboard + App nhắn tin. Tổng ~15 phút/lượt. |
| **3. Bottleneck** | Bước ③ & ④ (~10 phút): tra trạm sạc trống *phù hợp cổng sạc* và soạn tin hướng dẫn đường đi thân thiện — đây là khâu cần xử lý & sinh ngôn ngữ tự nhiên nhiều nhất, dễ lỗi nhất (chọn nhầm trạm không tương thích cổng sạc). |
| **4. Business Impact** | ~80 lượt/ngày × 15 phút = **20 giờ-người/ngày** lãng phí ở Hà Nội. Thời gian chờ của tài xế kéo dài → rò rỉ ~15% doanh thu cuốc trong lúc xe "chết"; tăng stress tài xế → ảnh hưởng tỉ lệ giữ chân. Nếu nhân rộng toàn quốc, tổn thất tăng theo cấp số. |
| **5. Success Metric** | **(1) Efficiency:** giảm thời gian xử lý sự cố từ **15 phút → dưới 3 phút** (–80%). **(2) Quality:** tỉ lệ hướng dẫn đúng trạm & đúng cổng sạc **≥ 98%**. **(3) Safety:** **0** trường hợp AI đề xuất trạm > 5km khi pin < 5%. **(4) Adoption:** ≥ 90% draft được điều phối viên duyệt & gửi với ≤ 1 lần chỉnh sửa. |
| **6. Operational Boundary** | **ĐƯỢC PHÉP:** gọi API định vị xe, API trạm sạc VinFast trống, DRAFT tin nhắn hướng dẫn (gắn thẻ `[DRAFT_ONLY]`). **TUYỆT ĐỐI KHÔNG:** (a) tự động gửi tin cho tài xế khi chưa có điều phối viên bấm duyệt — bắt buộc **HITL**; (b) đề xuất trạm sạc **sai cổng sạc** với dòng xe; (c) khi pin **< 5%**, không được chỉ tài xế tới trạm cách **> 5km** — phải chuyển sang điều **xe sạc di động (mobile charger)**. Điểm cần duyệt: mọi tin trước khi gửi. |

### 3.3. Future-State Flow & AI Fit (G3 — 10đ)

**AI-Fit Matrix — nhóm chọn `LLM Feature`:**

| Lựa chọn | Phù hợp? | Lý do |
|---|---|---|
| Rule / State-Machine | Một phần | Tốt cho lọc trạm theo cổng sạc & khoảng cách, nhưng *không* sinh được tin nhắn hướng dẫn tiếng Việt tự nhiên → dùng làm lớp kiểm tra an toàn (guardrail). |
| **LLM Feature** ✅ | **Có** | Cần hiểu ngữ cảnh + sinh tin nhắn tiếng Việt thân thiện, trong khi quy trình có cấu trúc cố định → chỉ cần 1 lần gọi LLM có system prompt chặt + HITL. |
| Agentic Loop | Không | Không cần chuỗi hành động tự trị nhiều bước; rủi ro điều phối sai trạm khiến xe cạn pin giữa đường → phải giữ con người ở vòng duyệt. |

**Future-State Flow:**

```text
┌──────────────┐   ┌──────────────────┐   ┌──────────────────┐   ┌──────────────────┐
│ ① Nhận cuộc  │   │ ② 🔵 AI/System   │   │ ③ 🔵 AI draft    │   │ ④ 🟢 Dispatcher  │
│    gọi sự cố │──►│ auto-pull vị trí │──►│ tin [DRAFT_ONLY] │──►│ 1-click DUYỆT    │
│              │   │ + trạm sạc trống │   │ chỉ đường/hướng  │   │ & gửi tài xế     │
│              │   │ (lọc theo cổng)  │   │ dẫn tiếng Việt   │   │ (HITL bắt buộc)  │
└──────────────┘   └──────────────────┘   └──────────────────┘   └──────────────────┘
                              │                                            │
              (Guardrail rule: pin < 5% & trạm > 5km?)                     ▼
                              │                                     [Tài xế nhận tin]
                              ▼ nếu ĐÚNG
                    ⛑️ AI trả JSON:
                    {"action":"dispatch_mobile_charger", ...}
                    → điều xe sạc di động, KHÔNG chỉ trạm xa.

↩️ FALLBACK: Nếu LLM lỗi/timeout/không tự tin → hệ thống hiện cảnh báo, Dispatcher
   quay lại soạn tay như quy trình cũ (degrade an toàn, không chặn nghiệp vụ).

🔵 AI Step   🟢 Human Step (HITL)   ⛑️ Safety branch   ↩️ Fallback
```

**Thời gian kỳ vọng future-state:** ① 2′ + ② ~15s (auto) + ③ ~10s (draft) + ④ ~20s (duyệt) ≈ **dưới 3 phút/lượt**.

---

## 🏁 Phase 5 — EVALUATE (G4 — 10đ)

### AI Readiness Checklist

| # | Tiêu chí | Trạng thái | Ghi chú |
|---|----------|-----------|---------|
| 1 | Có dữ liệu mẫu/logs sạch để test? | ✅ Có | Log sự cố + lịch sử tin nhắn điều phối 6 tháng; API trạm sạc VinFast sẵn có. |
| 2 | Rủi ro AI sai nằm trong tầm kiểm soát (HITL/Fallback)? | ✅ Có | Mọi tin phải điều phối viên duyệt; guardrail pin<5% chặn kịch bản nguy hiểm nhất; có fallback soạn tay. |
| 3 | Stakeholders sẵn sàng đổi quy trình? | 🟡 Một phần | Khối điều vận ủng hộ; cần đào tạo ngắn & thống nhất SLA duyệt draft. |

### Quyết định cuối cùng: ✅ **GO** (scope hẹp)

> **[x] GO** — Bắt đầu xây Prototype với scope hẹp: chỉ sự cố *hết pin* tại *Hà Nội*, chạy song song (shadow) với điều phối viên trong 2 tuần trước khi bật gửi thật.

**Justification (bằng chứng kỹ thuật + chi phí):**

- **Kỹ thuật:** Bài toán có cấu trúc cố định, chỉ cần 1 lần gọi LLM + guardrail rule → độ phức tạp thấp, rủi ro kiểm soát được bằng HITL. Prototype (Phase 4) đã chứng minh 2 ranh giới cốt lõi (thẻ `[DRAFT_ONLY]` và pin < 5% → `dispatch_mobile_charger`) **giữ vững trước 3 adversarial test** (kể cả prompt injection) — xem [starter-code/prompt_prototype.py](starter-code/prompt_prototype.py).
- **Ước lượng chi phí vận hành (LLM):** ~80 lượt/ngày × ~1.5K token/lượt ≈ 120K token/ngày ≈ **3.6M token/tháng**. Với Gemini 2.5 Flash, chi phí token gần như không đáng kể so với **20 giờ-người/ngày** tiết kiệm được → ROI dương rõ ràng ngay ở quy mô Hà Nội. (Nhóm chốt lại đơn giá theo bảng giá hiện hành khi triển khai.)
- **Lợi ích kỳ vọng:** giảm ~80% thời gian xử lý (15′→<3′), thu hồi phần lớn 20 giờ-người/ngày, giảm ~15% rò rỉ doanh thu do xe "chết", cải thiện trải nghiệm tài xế.
- **Điều kiện GO:** giữ scope hẹp; đo baseline 2 tuần; chỉ bật auto-send-after-approval khi tỉ lệ duyệt-không-sửa ≥ 90% và 0 vi phạm guardrail an toàn.

**Rủi ro & giảm thiểu:**

| Rủi ro | Mức | Giảm thiểu |
|---|---|---|
| AI đề xuất trạm sai cổng sạc | Cao | Rule lọc cổng sạc *trước* khi LLM soạn tin; QA đối chiếu. |
| AI chỉ trạm xa khi pin cạn | Nghiêm trọng | Guardrail cứng: pin<5% → `dispatch_mobile_charger`; đã test adversarial. |
| Điều phối viên "duyệt mù" | Trung bình | Thẻ `[DRAFT_ONLY]` + UI bắt buộc xác nhận; audit tỉ lệ chỉnh sửa. |
| LLM lỗi/timeout giờ cao điểm | Trung bình | Fallback soạn tay; timeout ngắn; hàng đợi ưu tiên. |
