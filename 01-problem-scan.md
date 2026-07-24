# Lab 02 - Problem Scan & Quick Problem Cards

## Thông tin cá nhân

| Trường | Thông tin |
|---|---|
| Nhóm | AI TEAM |
| Họ và tên | Nguyễn Duy Dũng |
| Mã HV | 2A202601505 |
| Email | dgx3811@gmail.com |

> **Lưu ý:** Các số liệu trong bài là ước tính phục vụ phân tích. Khi triển
> khai thực tế, nhóm cần xác minh lại bằng dữ liệu vận hành hoặc phỏng vấn
> người dùng.

---

# Phase 1 - SCAN: Quét cơ hội AI

## Danh sách bài toán

| # | Công ty thành viên | Lens | Mô tả ngắn bài toán |
|---:|---|---|---|
| 1 | Xanh SM | Tốn thời gian / Stakeholder Pain | Điều phối viên phải xử lý thủ công tình huống tài xế báo pin yếu: xác minh vị trí, mức pin, trạm sạc phù hợp và soạn hướng dẫn an toàn. |
| 2 | Vinhomes | Lặp lại / AI-upgrade | Nhân viên CSKH đọc, gắn nhãn và chuyển từng phản ánh của cư dân đến đúng bộ phận; nội dung tự do dễ bị gắn sai nhóm hoặc bỏ sót mức độ khẩn cấp. |
| 3 | VinFast | Tốn thời gian / Lặp lại | Cố vấn dịch vụ phải đọc ghi chú, ảnh và lịch sử sửa chữa để chuẩn hóa hồ sơ yêu cầu bảo hành trước khi chuyển bộ phận thẩm định. |
| 4 | Vinpearl / VinWonders | AI-upgrade | Nhân viên tổng hợp thủ công đánh giá đa ngôn ngữ từ nhiều kênh để phát hiện chủ đề khách hàng không hài lòng và gửi cho đơn vị vận hành. |
| 5 | Vinmec | Stakeholder Pain / Tốn thời gian | Nhân viên y tế mất nhiều thời gian tổng hợp thông tin từ hồ sơ để tạo bản nháp tóm tắt xuất viện cho bác sĩ kiểm tra. Sai sót có thể ảnh hưởng đến an toàn người bệnh. |

## Đánh giá sơ bộ

| Bài toán | Giá trị tiềm năng | Độ sẵn sàng dữ liệu | Rủi ro nếu AI sai | Nhận định ban đầu |
|---|---|---|---|---|
| Xanh SM - sự cố pin | Cao, tác động trực tiếp đến thời gian xe dừng chờ | Trung bình: cần GPS, mức pin và dữ liệu trạm sạc | Cao | Phù hợp mô hình lai: rule an toàn + LLM soạn bản nháp + con người duyệt. |
| Vinhomes - phân loại phản ánh | Cao, khối lượng lặp lại lớn | Khá: ticket và lịch sử xử lý thường có cấu trúc | Trung bình | Phù hợp LLM classification, cần ngưỡng tin cậy và fallback. |
| VinFast - hồ sơ bảo hành | Cao, giảm tải cho cố vấn dịch vụ | Trung bình: văn bản, ảnh và lịch sử sửa chữa | Cao | Chỉ nên trích xuất/tóm tắt; không cho AI tự quyết định bảo hành. |
| Vinpearl - tổng hợp đánh giá | Trung bình, hỗ trợ cải thiện dịch vụ | Khá: review dạng văn bản | Thấp | Phù hợp làm pilot vì có thể chạy offline và review theo lô. |
| Vinmec - tóm tắt xuất viện | Cao | Trung bình: dữ liệu nhạy cảm và không đồng nhất | Rất cao | Chưa nên tự động hóa quyết định; bắt buộc bảo mật và bác sĩ phê duyệt. |

---

# Phase 2 - QUICK-ASSESS

## Quick Problem Card 1 - Xanh SM xử lý sự cố pin yếu

| Trường | Nội dung |
|---|---|
| **Bài toán (1 câu)** | Rút ngắn thời gian điều phối khi tài xế Xanh SM báo pin yếu mà vẫn đảm bảo không đưa ra hướng dẫn di chuyển nguy hiểm. |
| **Công ty thành viên** | Xanh SM (GSM) |
| **Actor đang gặp khó khăn** | Điều phối viên là actor chính; tài xế và hành khách là các stakeholder bị ảnh hưởng. |
| **Workflow hiện tại** | 1. Tài xế gọi/nhắn tin báo sự cố → 2. Điều phối viên xác minh biển số, vị trí và mức pin → 3. Tra cứu trạm sạc và khoảng cách → 4. Đánh giá xe có thể đi tiếp hay cần cứu hộ → 5. Soạn hướng dẫn và gửi sau khi xác nhận. |
| **Bottleneck** | Bước 2-4, ước tính 10-15 phút/lượt do phải đối chiếu nhiều nguồn và xử lý dưới áp lực thời gian. |
| **AI hỗ trợ** | LLM tạo bản nháp hướng dẫn từ dữ liệu đã được xác thực; rule engine xử lý ngưỡng pin và khoảng cách. |
| **Success metric** | Giảm thời gian xử lý trung vị từ baseline 15 phút xuống dưới 3 phút; 100% trường hợp pin dưới 5% không được gợi ý trạm xa trên 5 km; 100% tin nhắn gửi đi có điều phối viên phê duyệt. |
| **Quick Architecture** | **LLM Feature kết hợp Rule**. Rule xử lý ranh giới an toàn; LLM chỉ soạn `[DRAFT_ONLY]`; con người quyết định gửi. |

### Ranh giới và fallback

- AI được phép tạo bản nháp tin nhắn và giải thích phương án cho điều phối viên.
- AI không được tự gửi tin, tự điều xe cứu hộ hoặc bỏ qua dữ liệu pin/khoảng cách.
- Nếu pin dưới 5%, hệ thống không hướng dẫn đến trạm xa trên 5 km và phải đề
  xuất lệnh `dispatch_mobile_charger` cho điều phối viên phê duyệt.
- Nếu thiếu GPS, mức pin, tình trạng trạm hoặc độ tin cậy thấp, hệ thống chuyển
  về quy trình thủ công và yêu cầu tài xế cung cấp lại dữ liệu.

---

## Quick Problem Card 2 - Vinhomes phân loại phản ánh cư dân

| Trường | Nội dung |
|---|---|
| **Bài toán (1 câu)** | Tự động đề xuất nhóm nghiệp vụ, mức độ ưu tiên và bộ phận tiếp nhận cho phản ánh của cư dân viết bằng ngôn ngữ tự do. |
| **Công ty thành viên** | Vinhomes |
| **Actor đang gặp khó khăn** | Nhân viên CSKH/trực vận hành; cư dân bị ảnh hưởng khi ticket bị chuyển sai hoặc phản hồi chậm. |
| **Workflow hiện tại** | 1. Cư dân gửi phản ánh → 2. CSKH đọc nội dung và tệp đính kèm → 3. Chọn nhóm và mức ưu tiên → 4. Chuyển đến ban quản lý/kỹ thuật/an ninh/kế toán → 5. Bộ phận nhận kiểm tra và có thể trả lại nếu phân loại sai. |
| **Bottleneck** | Bước 2-4, ước tính 5-8 phút/ticket; nội dung mơ hồ dễ gây chuyển sai bộ phận và xử lý lại. |
| **AI hỗ trợ** | Tóm tắt ticket, đề xuất category/priority/owner và chỉ ra thông tin còn thiếu; không tự động trả lời tranh chấp hoặc cam kết chi phí. |
| **Success metric** | Giảm thời gian phân loại trung vị từ 6 phút xuống dưới 1 phút; độ chính xác top-1 trên tập kiểm thử đạt ít nhất 90%; 100% ticket khẩn cấp được con người review. |
| **Quick Architecture** | **LLM Feature** với taxonomy cố định, structured output, confidence threshold và human review. |

### Ranh giới và fallback

- AI chỉ đưa ra đề xuất, không đóng ticket và không cam kết bồi thường/chi phí.
- Các ticket về an ninh, cháy nổ, y tế, tranh chấp hoặc có confidence dưới 0.8
  phải được chuyển ngay cho nhân viên.
- Nếu output không đúng schema hoặc category không nằm trong taxonomy, hệ
  thống gắn nhãn `needs_manual_triage`.

---

## Quick Problem Card 3 - VinFast chuẩn hóa hồ sơ bảo hành

| Trường | Nội dung |
|---|---|
| **Bài toán (1 câu)** | Hỗ trợ cố vấn dịch vụ trích xuất và chuẩn hóa thông tin từ hồ sơ sửa chữa để tạo bản nháp yêu cầu bảo hành đầy đủ. |
| **Công ty thành viên** | VinFast |
| **Actor đang gặp khó khăn** | Cố vấn dịch vụ và nhân viên thẩm định bảo hành; khách hàng chờ lâu nếu hồ sơ thiếu thông tin. |
| **Workflow hiện tại** | 1. Tiếp nhận mô tả từ khách hàng → 2. Thu thập mã xe, ODO, mã lỗi, ảnh và lịch sử sửa chữa → 3. Đọc và nhập lại vào biểu mẫu → 4. Kiểm tra tính đầy đủ → 5. Chuyển thẩm định hoặc yêu cầu bổ sung. |
| **Bottleneck** | Bước 2-4, ước tính 15-25 phút/hồ sơ; dữ liệu nằm ở nhiều định dạng và dễ nhập thiếu trường. |
| **AI hỗ trợ** | Trích xuất dữ liệu, tóm tắt triệu chứng, đánh dấu bằng chứng còn thiếu và tạo bản nháp có trích dẫn nguồn. |
| **Success metric** | Giảm thời gian chuẩn bị hồ sơ trung vị từ 20 phút xuống dưới 5 phút; trên 95% trường bắt buộc được điền đúng trên tập kiểm thử; 100% quyết định bảo hành do người có thẩm quyền thực hiện. |
| **Quick Architecture** | **LLM Feature** kết hợp validation rule cho trường bắt buộc và định dạng dữ liệu. |

### Ranh giới và fallback

- AI không được tự phê duyệt/từ chối bảo hành, tự suy diễn chi tiết không có
  trong hồ sơ hoặc sửa nội dung bằng chứng gốc.
- Mỗi trường trích xuất phải kèm tham chiếu đến tài liệu/ảnh nguồn.
- Nếu dữ liệu mâu thuẫn, ảnh không đọc được hoặc confidence thấp, hệ thống
  đánh dấu `manual_review_required` thay vì tự điền giá trị.

---

# Xếp hạng để đưa vào thảo luận nhóm

| Hạng | Bài toán | Lý do |
|---:|---|---|
| 1 | Xanh SM - xử lý sự cố pin yếu | Tác động vận hành rõ, metric đo được, có thể stress-test operational boundary bằng prototype của lab. |
| 2 | Vinhomes - phân loại phản ánh | Dữ liệu văn bản phù hợp LLM và rủi ro có thể kiểm soát bằng taxonomy, confidence và HITL. |
| 3 | VinFast - chuẩn hóa hồ sơ bảo hành | Giá trị cao nhưng cần tích hợp nhiều nguồn và kiểm soát chặt việc AI suy diễn sai. |

**Đề xuất cá nhân:** Chọn bài toán **Xanh SM xử lý sự cố pin yếu** để đưa
vào Phase 3. Lý do là phạm vi hẹp, có actor và bottleneck cụ thể, có thể đo
thời gian xử lý và phù hợp trực tiếp với bài stress-test Gemini trong repo.
