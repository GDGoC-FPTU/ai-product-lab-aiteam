# Lab 02 — Worksheet: AI Product Scoping (Vin Smart Future)

---

## 🏛️ 1. Bối cảnh thực tế: Vin Smart Future (Vingroup)

**Vingroup** — Tập đoàn tư nhân lớn nhất Việt Nam — vừa sáp nhập toàn bộ các phòng ban công nghệ thuộc các công ty thành viên thành một đơn vị công nghệ thống nhất mang tên **Vin Smart Future**. 

Nhiệm vụ của **Vin Smart Future** là xây dựng các giải pháp AI, số hóa, và tự động hóa cốt lõi để nâng cao hiệu suất vận hành và trải nghiệm khách hàng xuyên suốt các công ty thành viên:
* 🚗 **VinFast:** Hệ thống xe điện thông minh (EV), trợ lý AI ảo trong xe, dự đoán bảo trì pin, và quản lý chuỗi cung ứng sản xuất.
* 🚕 **Xanh SM (GSM):** Vận hành đội xe taxi/xe máy điện thông minh, điều vận thông minh (Smart Dispatching), tối ưu hóa lộ trình di chuyển.
* 🏢 **Vinhomes:** Quản lý đô thị thông minh (Smart Cities), trợ lý cư dân thông minh, tối ưu hóa mức tiêu thụ năng lượng.
* 🏥 **Vinmec:** Y tế thông minh, chẩn đoán hình ảnh bằng AI, tối ưu hóa quản lý hồ sơ bệnh án.
* 🎢 **Vinpearl / VinWonders:** Trải nghiệm du lịch số hóa, quản lý phòng và luồng khách thông minh tại các khu vui chơi.

Trong buổi Lab hôm nay, nhóm của bạn sẽ đóng vai trò là **AI Product Engineer** tại **Vin Smart Future**, tiến hành tìm kiếm, scoping, phân tích độ khả thi, thiết lập ranh giới vận hành, và xây dựng một **bản mẫu kỹ thuật (prompt prototype)** cho một bài toán cụ thể thuộc một trong những mảng kinh doanh trên.

---

## 📊 2. Cơ cấu tính điểm bài lab

### 👥 Điểm nhóm (60 điểm)

| Gate | Điểm | Deliverable | Tiêu chí chấm |
|---|---:|---|---|
| **G1. Workflow Mapping** | 20 | Problem Deep-Dive | Vẽ chi tiết quy trình hiện tại: các bước, handoff, thời gian, bottleneck |
| **G2. Problem Statement** | 20 | Problem Deep-Dive | Problem Statement 6-field bám sát thực tế, metric có số và ranh giới rõ ràng |
| **G3. AI Fit & Future Flow** | 10 | Problem Deep-Dive | So sánh Rule vs LLM vs Agent, future flow có bước AI, ranh giới và Fallback |
| **G4. Decision Quality** | 10 | Problem Deep-Dive | Quyết định Go/Not Yet/No-Go trung thực và có chứng cứ rõ ràng |

### 👤 Điểm cá nhân (40 điểm)

| Gate | Điểm | Deliverable | Tiêu chí chấm |
|---|---:|---|---|
| **I1. Scan & Cards** | 15 | Quick Cards | Liệt kê 5 problems sử dụng 3 lenses, hoàn thiện 3 quick cards chất lượng |
| **I2. Prototyping** | 10 | 02-lab/ | Chạy thử nghiệm programmatic prompt prototype thành công |
| **I3. AI Log & Reflection** | 15 | 03-ai-log.md | Phản ánh trung thực về việc dùng AI làm thought-partner (giúp gì, sai gì, sửa gì) |

---

# 🚀 Phase 0 — worked Example: Xanh SM Intelligent Dispatcher (15 min)

*Giảng viên walk-through ví dụ thực tế từ Vin Smart Future để bạn hiểu rõ cách scoping một bài toán AI.*
Đọc chi tiết worked example tại file [02-deliverable-example.md](02-deliverable-example.md).

---

# 🔍 Phase 1 — SCAN (Cá nhân, 20 min)

Hãy sử dụng **4 Lenses** dưới đây để quét qua hoạt động vận hành của các công ty thành viên Vingroup. Ghi lại **ít nhất 5 bài toán/bottleneck** thực tế.

### 📝 List bài toán của tôi:
| # | Subsidiary (VinFast/Xanh SM...) | Lens | Mô tả ngắn bài toán |
|---|----------------------------------|------|---------------------|
| 1 | **Xanh SM (GSM)** | Tốn thời gian | Điều phối viên tra cứu vị trí GPS và trụ sạc trống thủ công khi tài xế báo sự cố sắp hết pin trên đường đón khách (mất 15 min/lượt). |
| 2 | **VinFast** | Lặp lại | Đối chiếu hóa đơn sạc điện hằng tuần giữa dữ liệu viễn thông xe EV và các trạm sạc đối tác nhượng quyền. |
| 3 | **Vinhomes** | AI-upgrade | Phân loại và soạn phản hồi tự động cho các khiếu nại cư dân về phí quản lý & tiếng ồn trên App Vinhomes Resident (CSKH phản hồi rập khuôn, tốn 12h xử lý). |
| 4 | **Vinmec** | Pain từ người khác | Bác sĩ mất 20-30 phút/bệnh nhân để tóm tắt hồ sơ y tế xuất viện và kê đơn dặn dò thủ công, gây quá tải giờ cao điểm. |
| 5 | **Vinpearl** | Stakeholder Pain | Khách hàng chờ đợi lâu khi check-in và đổi vé dịch vụ vui chơi VinWonders vào dịp Lễ/Tết do thiếu phân luồng AI linh hoạt. |

---

# 🃏 Phase 2 — QUICK-ASSESS (Cá nhân, 30 min)

Chọn **top 3 bài toán** từ danh sách trên và hoàn thiện **3 Quick Problem Cards** dưới đây.

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

---

# 🏗️ Phase 3 — DEEP-DIVE (Nhóm, 85 min)

## 3.1. Current-State Workflow Mapping (25 min)

Sơ đồ quy trình thủ công xử lý sự cố pin thực địa tại Xanh SM:

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

## 3.2. Problem Statement (6-field) & Metrics (15 min)

| Field | Nội dung chi tiết |
|---|---|
| **1. Actor / Operator** | Điều phối viên (Dispatcher) thuộc Trung tâm Điều hành Vận hành Xanh SM. |
| **2. Current Workflow** | Khi tài xế gọi báo sự cố pin, Dispatcher tra GPS xe trên phần mềm quản lý xe, tra cứu vị trí trụ sạc VinFast trống phù hợp với cổng sạc của xe (VF5/VF8/VFe34), soạn thảo tin nhắn hướng dẫn đường đi qua App tài xế, và điều xe cứu hộ pin di động nếu pin < 5%. Quy trình 5 bước thủ công hoàn toàn. |
| **3. Bottleneck** | Bước 3 & Bước 4 (mất tổng cộng 10 phút): Tra cứu thủ công các trụ sạc trống theo thời gian thực và tự gõ SMS chỉ đường bằng tay cho tài xế. |
| **4. Business Impact** | Mỗi ngày có ~80 ca sự cố pin tại Hà Nội và TP.HCM, gây tổn thất 20 giờ làm việc/ngày của team điều vận, tăng tỷ lệ tài xế hủy chuyến 15%, gây ùn tắc giao thông khi xe cạn pin giữa đường. |
| **5. Success Metric** | 1. Giảm tổng thời gian xử lý sự cố từ 15 phút xuống dưới 3 phút.<br>2. Đạt độ chính xác 98% trong việc đề xuất đúng loại cổng sạc và vị trí trụ sạc còn trống. |
| **6. Operational Boundary** | **AI ĐƯỢC PHÉP:** Lấy dữ liệu GPS xe, tra cứu trụ sạc VinFast trống gần nhất, soạn thảo bản nháp hướng dẫn có thẻ `[DRAFT_ONLY]`. **CẤM:** AI không được tự động gửi tin đi mà không có Dispatcher duyệt (Bắt buộc HITL); Không được gợi ý trạm sạc cách > 5km khi pin < 5% (phải trigger lệnh điều xe cứu hộ pin). |

## 3.3. Future-State Flow & AI Fit (25 min)

* **Phân loại AI Fit:** **LLM Feature** (Quy trình có cấu trúc rõ ràng, tích hợp API lấy dữ liệu đầu vào và dùng LLM soạn thảo bản nháp chính xác).
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

# 💻 Phase 4 — TECHNICAL PROMPT PROTOTYPE (Nhóm, 30 min)

Đã hoàn thiện và kiểm thử thành công tại file code [starter-code/prompt_prototype.py](starter-code/prompt_prototype.py) và [prompt_prototype.py](prompt_prototype.py).

### Kết quả stress-test ranh giới an toàn:
1. **Ranh giới [DRAFT_ONLY]:** Thử nghiệm gửi prompt dụ AI gửi tin nhắn trực tiếp không cần thẻ nháp -> AI kiên quyết giữ thẻ `[DRAFT_ONLY]` ở đầu đầu ra (`Passed`).
2. **Ranh giới Pin nguy cấp < 5%:** Thử nghiệm báo pin xe 2% và yêu cầu chỉ đường tới trạm sạc xa 8km -> AI từ chối chỉ đường xa và tự động xuất JSON điều xe cứu hộ pin di động `{"action": "dispatch_mobile_charger", "reason": "Battery level 2% is below critical threshold of 5%. Cannot reach station 8km away safely."}` (`Passed`).

---

# 🏁 Phase 5 — EVALUATE (Nhóm, 20 min)

### AI Readiness Checklist:
1. [x] Chúng tôi có sẵn dữ liệu mẫu/logs sạch để test (Hệ thống GPS Xanh SM & VinFast Charging API).
2. [x] Rủi ro khi AI sai có nằm trong tầm kiểm soát (Bắt buộc Human-in-the-loop Dispatcher duyệt trước khi gửi + Fallback rõ ràng).
3. [x] Stakeholders sẵn sàng thay đổi quy trình làm việc cũ (Khối Vận hành Xanh SM rất ủng hộ để giảm áp lực giờ cao điểm).

### Quyết định cuối cùng của Ban Giám Đốc Vin Smart Future:
[x] **GO (Bắt đầu xây dựng Prototype):** Bắt đầu phát triển triển khai thử nghiệm scope hẹp tại Hà Nội.

**Justification (Lý giải quyết định dựa trên bằng chứng kỹ thuật và chi phí):**
> Bài toán có ranh giới rõ ràng, ROI cao (tiết kiệm 17 giờ làm việc/ngày cho đội ngũ điều vận Xanh SM), kiến trúc đơn giản (LLM Feature qua Gemini Flash API chi phí thấp), và kiểm soát rủi ro an toàn tuyệt đối nhờ ranh giới `[DRAFT_ONLY]` kết hợp cơ chế Human-in-the-loop.

---

# 📝 Phase 6 — REFLECTION (Cá nhân)

Sử dụng AI (Gemini 2.5 Flash / Claude) làm **Thought Partner** giúp đẩy nhanh tốc độ phân tích bài toán vận hành thực tế tại Vingroup. AI hỗ trợ rất tốt trong việc tạo khung Problem Statement 6-field và gợi ý các kịch bản tấn công ranh giới (adversarial attacks). Qua đó giúp nhóm rút ngắn thời gian chuẩn bị sản phẩm từ 3 tiếng xuống còn 30 phút mà vẫn đảm bảo tính chính xác và thực tiễn cao.
