# 🔍 01 — Problem Scan & Quick Problem Cards (Vin Smart Future)

**Họ và tên:** Quỳnh Phương  
**Mã số sinh viên (MSSV):** SE202601  
**Đơn vị:** Vin Smart Future — AI Product Engineering Lab  

---

## 🔍 Phase 1 — SCAN: Danh sách bài toán vận hành Vingroup

Sử dụng **4 Lenses** (Lặp lại, Tốn thời gian, AI-upgrade, Stakeholder Pain) để quét qua các công ty thành viên Vingroup.

| # | Subsidiary | Lens | Mô tả ngắn bài toán |
|---|------------|------|---------------------|
| 1 | **Xanh SM (GSM)** | Tốn thời gian | Điều phối viên tra cứu vị trí GPS và trụ sạc trống thủ công khi tài xế báo sự cố sắp hết pin trên đường đón khách (mất 15 min/lượt). |
| 2 | **VinFast** | Lặp lại | So khớp và đối chiếu hóa đơn sạc điện hằng tuần giữa dữ liệu viễn thông xe EV và các trạm sạc đối tác nhượng quyền. |
| 3 | **Vinhomes** | AI-upgrade | Phân loại và tự động soạn phản hồi cho khiếu nại cư dân về phí quản lý & tiếng ồn trên App Vinhomes Resident (CSKH phản hồi rập khuôn, tốn 12h xử lý). |
| 4 | **Vinmec** | Pain từ người khác | Bác sĩ mất 20-30 phút/bệnh nhân để tóm tắt hồ sơ y tế xuất viện và kê đơn dặn dò thủ công, gây quá tải giờ cao điểm. |
| 5 | **Vinpearl** | Stakeholder Pain | Khách hàng chờ đợi lâu khi check-in và đổi vé dịch vụ vui chơi VinWonders vào dịp Lễ/Tết do thiếu phân luồng AI linh hoạt. |

---

## 🃏 Phase 2 — QUICK-ASSESS: 3 Quick Problem Cards

### 🃏 QUICK PROBLEM CARD #1

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1                                       │
│                                                             │
│ Bài toán (1 câu): Tài xế Xanh SM báo sự cố sạc pin / hết pin │
│ giữa đường cần điều phối cứu hộ hoặc chỉ đường trạm sạc trống.│
│ Công ty thành viên: [x] Xanh SM (GSM)                       │
│                                                             │
│ Ai đang đau (Actor)? Tài xế (chờ lâu), Dispatcher (quá tải) │
│                                                             │
│ Workflow thủ công hiện tại (5 bước):                        │
│   1. Nhận cuộc gọi sự cố ──> 2. Tra GPS xe ──> 3. Tra trạm sạc  │
│   ──> 4. Soạn SMS chỉ đường ──> 5. Điều xe cứu hộ (nếu cạn pin) │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 3-4 (⏱ 10 phút/lượt)  │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 3-4 (Draft SMS & │
│ tự động lọc trạm sạc phù hợp theo dòng xe VF5/VF8/VFe34).   │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                        │
│ Giảm thời gian xử lý sự cố từ 15 phút ──> dưới 3 phút.      │
│                                                             │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent │
└─────────────────────────────────────────────────────────────┘
```

---

### 🃏 QUICK PROBLEM CARD #2

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2                                       │
│                                                             │
│ Bài toán (1 câu): Phân loại và tự động soạn thảo câu trả lời│
│ phản hồi phản ánh cư dân Vinhomes về vận hành tòa nhà.      │
│ Công ty thành viên: [x] Vinhomes                            │
│                                                             │
│ Ai đang đau (Actor)? Đội ngũ CSKH Ban Quản Lý Vinhomes.     │
│                                                             │
│ Workflow thủ công hiện tại (4 bước):                        │
│   1. Nhận Ticket cư dân ──> 2. Phân loại thủ công phòng ban │
│   ──> 3. Kiểm tra quy định/phí ──> 4. Soạn email trả lời.   │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2-3 (⏱ 30 phút/ticket)│
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2 (Auto Tagging) │
│ và Bước 4 (Draft phản hồi chuẩn văn phong Vinhomes).         │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                        │
│ Giảm SLA phản hồi ticket cư dân từ 12 giờ xuống dưới 1 giờ.  │
│                                                             │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent │
└─────────────────────────────────────────────────────────────┘
```

---

### 🃏 QUICK PROBLEM CARD #3

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3                                       │
│                                                             │
│ Bài toán (1 câu): Tóm tắt tự động hồ sơ bệnh án và lịch sử  │
│ khám chữa bệnh để hỗ trợ bác sĩ Vinmec viết giấy xuất viện. │
│ Công ty thành viên: [x] Vinmec                              │
│                                                             │
│ Ai đang đau (Actor)? Bác sĩ nội trú Vinmec.                 │
│                                                             │
│ Workflow thủ công hiện tại (4 bước):                        │
│   1. Đọc lại toàn bộ EMR ──> 2. Lọc thông tin xét nghiệm   │
│   ──> 3. Tóm tắt quá trình điều trị ──> 4. Soạn dặn dò.     │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 1-3 (⏱ 25 phút/ca)    │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 3 (Tóm tắt EMR   │
│ tự động và trích xuất chỉ số xét nghiệm bất thường).        │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                        │
│ Giảm thời gian chuẩn bị hồ sơ xuất viện từ 25 min ──> 5 min.│
│                                                             │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent │
└─────────────────────────────────────────────────────────────┘
```
