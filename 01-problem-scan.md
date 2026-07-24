# 01 — Problem Scan & Quick Cards (Bài cá nhân)

> **Deliverable cá nhân (I1 — 15 điểm).** Thể hiện tư duy tìm & sàng lọc bài toán AI *trước* khi nhóm thảo luận.
>
> **Người thực hiện:** `Kim Mạnh Hưng` — MSSV `2A202601679` — Nhóm `AI_Team
> **Vai trò giả định:** AI Product Engineer tại **Vin Smart Future** (đơn vị công nghệ hợp nhất của Vingroup).


---

## 🏛️ Bối cảnh quan sát của tôi

Tôi tiếp cận bài toán từ khối **vận hành thời gian thực (real-time operations)** của **Xanh SM (GSM)** — nơi mọi giây trễ đều quy đổi trực tiếp thành doanh thu mất đi và trải nghiệm tài xế/khách hàng. Qua mô phỏng một ca trực tại Trung tâm Điều vận, tôi nhận thấy điều phối viên bị "ngập" thao tác thủ công ở các sự cố thực địa (hết pin, hỏng xe), trong khi các mảng khác của Vingroup cũng có những nút thắt xử lý ngôn ngữ tương tự.

---

## 🔍 Phase 1 — SCAN: Bảng quét cơ hội (4 Lenses)

Tôi dùng 4 thấu kính — **Lặp lại**, **Tốn thời gian**, **AI-upgrade**, **Stakeholder Pain** — quét qua vận hành các công ty thành viên.

| # | Subsidiary | Lens | Mô tả ngắn bài toán / bottleneck |
|---|-----------|------|----------------------------------|
| 1 | **Xanh SM** | Tốn thời gian | Điều phối viên xử lý thủ công sự cố hết pin/hỏng xe thực địa: tra vị trí → tra trạm sạc trống → soạn tin hướng dẫn → gọi cứu hộ (~15 phút/lượt, ~80 lượt/ngày ở Hà Nội). |
| 2 | **Xanh SM** | Pain từ người khác | Tài xế phàn nàn hệ thống gợi ý điểm đón khách sai vị trí (hẻm nhỏ, toà nhà nhiều cổng) khiến khách chờ lâu, tăng huỷ chuyến. |
| 3 | **VinFast** | Lặp lại | Đối chiếu hoá đơn sạc điện hằng tuần từ hàng nghìn trụ sạc đối tác với dữ liệu tài chính nội bộ (thủ công, dễ lệch số). |
| 4 | **Vinhomes** | AI-upgrade | Phân loại & điều hướng phản ánh cư dân trên App Vinhomes Resident (mất nước, hỏng đèn, ồn ào…) đến đúng ban quản lý tòa nhà; hiện phản hồi rập khuôn, trễ tới ~12 giờ. |
| 5 | **Vinmec** | Tốn thời gian | Bác sĩ soạn tóm tắt hồ sơ xuất viện (discharge summary) từ bệnh án + xét nghiệm, mất 20–30 phút/bệnh nhân, gây quá tải. |
| 6 | **Vinpearl** | Pain từ người khác | Quét review Booking/Agoda/Google Map để lọc phàn nàn khẩn cấp ("phòng bẩn", "thái độ nhân viên") gửi Manager; hiện làm thủ công, bỏ sót nhiều. |

> **Nhận xét chọn lọc:** Bài **#1 (Xanh SM — sự cố thực địa)** nổi bật vì (a) tần suất cao & lặp lại, (b) tác động doanh thu real-time rõ ràng, (c) có ranh giới an toàn thú vị để thiết kế (không được điều xe cạn pin đi xa). Đây là bài tôi đề cử nhóm chọn Deep-Dive.

---

## 🃏 Phase 2 — QUICK-ASSESS: 3 Quick Problem Cards

Tôi chọn **top 3**: #1 (Xanh SM sự cố thực địa), #4 (Vinhomes phản ánh cư dân), #5 (Vinmec discharge summary).

### 🟩 QUICK PROBLEM CARD #1 — Xanh SM: Trợ lý điều vận sự cố hết pin thực địa

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1                                        │
│                                                             │
│ Bài toán: Tài xế Xanh SM báo hết pin giữa đường cần được    │
│ hướng dẫn tới trạm sạc phù hợp hoặc điều xe sạc cứu hộ.     │
│ Công ty thành viên: [x] Xanh SM (GSM)                       │
│                                                             │
│ Ai đang đau (Actor)? Điều phối viên (quá tải giờ cao điểm), │
│                      Tài xế (chờ lâu, mất cuốc, stress).    │
│                                                             │
│ Workflow thủ công hiện tại (5 bước):                        │
│   1. Nhận cuộc gọi báo sự cố                                │
│   → 2. Tra vị trí GPS xe trên bản đồ nội bộ                 │
│   → 3. Tra dashboard trạm sạc VinFast tìm trụ trống hợp xe  │
│   → 4. Soạn tin nhắn chỉ đường gửi qua App tài xế           │
│   → 5. Gọi xe cứu hộ nếu pin quá thấp                       │
│                                                             │
│ Bước nào tốn/ lỗi nhất? Bước 3–4 (⏱ ~10 phút/lượt)          │
│ AI có thể nhảy vào ở bước nào? Bước 3–4 (tự pull vị trí +   │
│   trạm trống, DRAFT tin hướng dẫn cho người duyệt).        │
│                                                             │
│ Metric (có số)? Giảm thời gian xử lý 15 phút ──> dưới 3 phút│
│   & tỉ lệ hướng dẫn đúng trạm/đúng cổng sạc ≥ 98%.         │
│                                                             │
│ Quick Architecture: [x] LLM Feature (draft + HITL)          │
└─────────────────────────────────────────────────────────────┘
```

### 🟦 QUICK PROBLEM CARD #2 — Vinhomes: Phân loại & điều hướng phản ánh cư dân

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2                                        │
│                                                             │
│ Bài toán: Tự động phân loại phản ánh cư dân (App Resident)  │
│ và route đến đúng ban quản lý tòa nhà, đề xuất mức ưu tiên. │
│ Công ty thành viên: [x] Vinhomes                            │
│                                                             │
│ Ai đang đau (Actor)? Nhân viên CSKH tòa nhà, cư dân chờ lâu.│
│                                                             │
│ Workflow thủ công hiện tại (4 bước):                        │
│   1. Cư dân gửi phản ánh dạng text tự do                   │
│   → 2. CSKH đọc, đoán loại sự cố & tòa/ban phụ trách        │
│   → 3. Chuyển tay (email/nhóm chat) tới bộ phận đúng        │
│   → 4. Soạn phản hồi xác nhận cho cư dân                    │
│                                                             │
│ Bước nào tốn/ lỗi nhất? Bước 2–3 (⏱ ~8 phút/lượt, dễ route │
│   nhầm ban) → tổng thời gian phản hồi ~12 giờ.             │
│ AI có thể nhảy vào ở bước nào? Bước 2 (phân loại + gán ưu   │
│   tiên) & Bước 4 (draft phản hồi mẫu).                     │
│                                                             │
│ Metric (có số)? ≥ 85% phản ánh route đúng ban < 10 giây;    │
│   giảm thời gian phản hồi lần đầu từ 12 giờ ──> dưới 1 giờ. │
│                                                             │
│ Quick Architecture: [x] LLM Feature  [ ] Rule (fallback)    │
└─────────────────────────────────────────────────────────────┘
```

### 🟥 QUICK PROBLEM CARD #3 — Vinmec: Soạn nháp tóm tắt hồ sơ xuất viện

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3                                        │
│                                                             │
│ Bài toán: Trích xuất thông tin lâm sàng và DRAFT bản tóm    │
│ tắt xuất viện dễ hiểu cho bệnh nhân, bác sĩ chỉ review.     │
│ Công ty thành viên: [x] Vinmec                              │
│                                                             │
│ Ai đang đau (Actor)? Bác sĩ điều trị (quá tải hành chính).  │
│                                                             │
│ Workflow thủ công hiện tại (4 bước):                        │
│   1. Đọc lại bệnh án điện tử + kết quả xét nghiệm           │
│   → 2. Tổng hợp chẩn đoán, thuốc, dặn dò                    │
│   → 3. Gõ tay bản tóm tắt xuất viện                         │
│   → 4. Đọc soát & ký duyệt                                  │
│                                                             │
│ Bước nào tốn/ lỗi nhất? Bước 3 (⏱ 20–30 phút/bệnh nhân)     │
│ AI có thể nhảy vào ở bước nào? Bước 3 (DRAFT bản tóm tắt).  │
│                                                             │
│ Metric (có số)? Giảm thời gian soạn từ 25 phút ──> dưới 8   │
│   phút; bác sĩ chỉnh sửa < 20% nội dung nháp.             │
│                                                             │
│ Quick Architecture: [x] LLM Feature (HITL bắt buộc — y tế)  │
└─────────────────────────────────────────────────────────────┘
```

---

## 🗳️ Đề cử của tôi cho nhóm

Tôi đề cử nhóm chọn **Card #1 (Xanh SM — sự cố hết pin thực địa)** để Deep-Dive vì:

- **Tác động real-time** cao nhất: mỗi phút trễ = tài xế không đón khách = rò rỉ doanh thu ngay lập tức.
- **Ranh giới an toàn rõ và đo được**: bắt buộc Human-in-the-loop (điều phối viên duyệt trước khi gửi) và một quy tắc an toàn vật lý hấp dẫn để lập trình — *pin < 5% thì không được điều xe đi trạm xa, phải gọi xe sạc di động*.
- **Kiến trúc gọn (LLM Feature)**, không cần Agent tự trị → rủi ro thấp, dễ đạt GO với scope hẹp.

> Card #2 (Vinhomes) và Card #3 (Vinmec) đều giá trị nhưng rủi ro pháp lý/y tế cao hơn, cần thêm dữ liệu và tầng kiểm duyệt chặt hơn — phù hợp làm giai đoạn sau.
