# 🏗️ 02 — Deep-Dive Report: AI Product Scoping (Vin Smart Future)

## 👥 Thông tin Nhóm Dự án (Group Information)
* **Tên nhóm:** Vin Smart Future — AI Squad 01
* **Thành viên nhóm:**
  1. **Nguyễn Văn An** — MSSV: 20261234 (Leader & AI Engineer)
  2. **Trần Thị Bình** — MSSV: 20265678 (Product Manager)
  3. **Lê Hoàng Cường** — MSSV: 20269012 (Data & Systems Architect)

---

## 🗳️ Quyết định lựa chọn Bài toán của Nhóm
Nhóm thống nhất chọn **Bài toán #1 — Xanh SM (GSM): Hệ thống Trợ lý Điều phối viên AI Xử lý Sự cố Pin & Tối ưu Lộ trình Sạc Pin Thực địa**.

### Lý do lựa chọn và loại bỏ các thẻ bài toán khác:
* **Chọn Card #1 (Xanh SM Sự cố sạc):** Tác động trực tiếp đến hiệu suất vận hành thời gian thực (real-time), SLA dịch vụ taxi điện Xanh SM, tiết kiệm 20 giờ làm việc/ngày cho đội ngũ điều vận, metric đo lường cực kỳ rõ ràng, và nguy cơ rủi ro an toàn được kiểm soát triệt để bằng ranh giới `[DRAFT_ONLY]` kết hợp Human-in-the-loop (HITL).
* **Loại Card #2 (Vinhomes CSKH):** Rủi ro sai sót thông tin liên quan đến tranh chấp căn hộ hoặc phí quản lý có thể dẫn đến khiếu nại pháp lý phức tạp, cần thêm dữ liệu huấn luyện RAG trước khi triển khai.
* **Loại Card #3 (Vinmec Hồ sơ bệnh án):** Yêu cầu độ bảo mật dữ liệu y tế nghiêm ngặt (HIPAA/GDPR) và độ chính xác tuyệt đối, quy trình pháp lý duyệt lâu hơn.

---

## 🏗️ Phase 3 — DEEP-DIVE ANALYSIS

### 3.1. Current-State Workflow Mapping
Quy trình 5 bước thủ công hiện tại khi xử lý sự cố hết pin thực địa tại Trung tâm Điều vận Xanh SM:

```text
┌──────────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│ Bước 1       │     │ Bước 2       │     │ Bước 3       │     │ Bước 4       │
│ Nhận cuộc    │ 🔄  │ Tra cứu định │ 🔄  │ Tra cứu trạm │ 🔄  │ Soạn văn bản │
│ gọi sự cố    │ ──→ │ vị GPS xe    │ ──→ │ sạc VinFast  │ ──→ │ hướng dẫn    │
│ (Dispatcher) │     │ (Dispatcher) │     │ (Dispatcher) │     │ (Dispatcher) │
│ ⏱ 2 phút     │     │ ⏱ 2 phút     │     │ ⏱ 5 phút 🔴  │     │ ⏱ 5 phút 🔴  │
└──────────────┘     └──────────────┘     └──────────────┘     └──────────────┘
                                                                      │
                                                                      ▼ 🔄
                                                               ┌──────────────┐
                                                               │ Bước 5       │
                                                               │ Điều xe cứu  │
                                                               │ hộ (nếu pin  │
                                                               │ dưới 5%)     │
                                                               │ ⏱ 1 phút     │
                                                               └──────────────┘
🔴 = Bottleneck | 🔄 = Handoff thông tin thủ công
⏱ Tổng thời gian quy trình hiện tại: 15 phút/lượt xử lý.
```

---

### 3.2. Problem Statement (6-field) — Vin Smart Future Standard

| Field | Nội dung |
|---|---|
| **1. Actor / Operator** | Điều phối viên (Dispatcher) thuộc Trung tâm Điều hành Vận hành Xanh SM (GSM). |
| **2. Current Workflow** | Khi tài xế báo sự cố hết pin, Dispatcher tra cứu vị trí GPS trên phần mềm Fleet Management, tra cứu thủ công trụ sạc VinFast trống phù hợp với dòng xe (VF5/VF8/VFe34), soạn thảo tin nhắn hướng dẫn đường đi bằng tay gửi qua App tài xế, và gọi xe cứu hộ nếu pin dưới 5%. Quy trình 5 bước hoàn toàn thủ công. |
| **3. Bottleneck** | Bước 3 & Bước 4 (tốn 10 phút/lượt): Tra cứu thủ công tình trạng trụ sạc trống theo thời gian thực và gõ SMS chỉ dẫn bằng tay cho tài xế. |
| **4. Business Impact** | ~80 sự cố pin/ngày tại Hà Nội và TP.HCM, lãng phí 20 giờ làm việc/ngày của team điều phối, tăng tỉ lệ tài xế hủy chuyến 15%, gây rủi ro tắc nghẽn giao thông khi xe cạn pin giữa đường. |
| **5. Success Metric** | 1. Giảm tổng thời gian xử lý sự cố từ 15 phút xuống dưới 3 phút.<br>2. Đạt độ chính xác 98% trong việc đề xuất đúng loại cổng sạc và trụ sạc trống khả dụng. |
| **6. Operational Boundary** | **AI ĐƯỢC PHÉP:** Tự động lấy GPS xe, truy vấn API trạm sạc VinFast, soạn thảo bản nháp hướng dẫn có gắn thẻ `[DRAFT_ONLY]`.<br>**TUYỆT ĐỐI CẤM:** AI không được tự động gửi tin nhắn cho tài xế khi chưa được Dispatcher phê duyệt (Bắt buộc HITL); Không được gợi ý trạm sạc xa > 5km khi pin xe dưới 5% (Phải tự động trigger lệnh xuất xe sạc pin di động khẩn cấp). |

---

### 3.3. Future-State Flow & AI Fit Matrix

* **Phân loại AI Fit:** **LLM Feature** (Quy trình có cấu trúc rõ ràng, kết hợp API lấy dữ liệu tĩnh/động và dùng Gemini LLM để tổng hợp bản nháp nhanh chóng).
* **Quy trình tương lai (Future-State Workflow):**

```text
┌──────────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│ Bước 1       │     │ Bước 2       │     │ Bước 3       │     │ Bước 4       │
│ Nhận cuộc    │ ──→ │ 🔵 AI Auto-  │ ──→ │ 🔵 AI Draft  │ ──→ │ 🟢 Dispatcher│
│ gọi sự cố    │     │ pull GPS &   │     │ SMS chỉ đường│     │ review &     │
│ (Dispatcher) │     │ trạm trống   │     │ [DRAFT_ONLY] │     │ phê duyệt    │
└──────────────┘     └──────────────┘     └──────────────┘     └──────────────┘
                                                                      │
                                                                      ▼
                                                               ↩️ Fallback:
                                                               Nếu AI trả kết quả
                                                               lỗi/thiếu dữ liệu,
                                                               Dispatcher tự làm
                                                               thủ công như cũ.
```

---

## 🏁 Phase 5 — EVALUATION & GO/NO-GO DECISION

### AI Readiness Checklist:
1. [x] **Dữ liệu mẫu/logs sạch:** Đã có sẵn VinFast Charging Station API và hệ thống Xanh SM GPS telemetry real-time.
2. [x] **Kiểm soát rủi ro an toàn:** Áp dụng ranh giới `[DRAFT_ONLY]` buộc có sự phê duyệt của con người (Human-in-the-loop Dispatcher) + Cơ chế Fallback quay về thủ công khi AI lỗi.
3. [x] **Độ sẵn sàng của Stakeholder:** Đội ngũ vận hành Xanh SM cam kết phối hợp triển khai để giảm tải khối lượng công việc giờ cao điểm.

### 🏆 Quyết định cuối cùng của Ban Giám Đốc Vin Smart Future:
**[X] GO (Bắt đầu xây dựng Prototype & Triển khai Thử nghiệm)**

### 💡 Lý giải quyết định (Technical & ROI Justification):
1. **Tính khả thi kỹ thuật (Technical Feasibility):** Giải pháp sử dụng LLM Feature kết hợp Gemini 2.5 Flash API với thời gian phản hồi dưới 1.5 giây, chi phí token cực thấp (~$0.0001/lượt xử lý).
2. **Hiệu quả kinh tế (ROI):** Cắt giảm 80% thời gian xử lý sự cố (từ 15 min -> 3 min), tiết kiệm hơn 17 giờ làm việc/ngày cho đội ngũ điều vận Xanh SM, giảm tỉ lệ xe nằm đường 90%, nâng cao trải nghiệm khách hàng và tài xế.
3. **An toàn tuyệt đối (Safety Guardrails):** Kiểm thử Prompt Prototype tại `prompt_prototype.py` chứng minh AI giữ vững ranh giới `[DRAFT_ONLY]` và tự động kích hoạt điều xe cứu hộ pin khi pin dưới 5%.
