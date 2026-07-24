# 01 — Problem Scan (Tổng hợp cả nhóm)

> File hợp nhất Phase 1 (SCAN) & Phase 2 (QUICK-ASSESS) của **tất cả thành viên** trong nhóm, tổng hợp từ các branch cá nhân. Mỗi thành viên có một mục riêng bên dưới, giữ nguyên nội dung bài cá nhân đã nộp trên branch của mình.

**Thành viên:** Nguyễn Duy Dũng · Kim Mạnh Hưng · Nguyễn Thế Khải · Phùng Văn Linh · Quỳnh Phương · Ong Xuân Sơn

---

# 👤 Nguyễn Duy Dũng

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

## Phase 1 — SCAN: Quét cơ hội AI

| # | Công ty thành viên | Lens | Mô tả ngắn bài toán |
|---:|---|---|---|
| 1 | Xanh SM | Tốn thời gian / Stakeholder Pain | Điều phối viên phải xử lý thủ công tình huống tài xế báo pin yếu: xác minh vị trí, mức pin, trạm sạc phù hợp và soạn hướng dẫn an toàn. |
| 2 | Vinhomes | Lặp lại / AI-upgrade | Nhân viên CSKH đọc, gắn nhãn và chuyển từng phản ánh của cư dân đến đúng bộ phận; nội dung tự do dễ bị gắn sai nhóm hoặc bỏ sót mức độ khẩn cấp. |
| 3 | VinFast | Tốn thời gian / Lặp lại | Cố vấn dịch vụ phải đọc ghi chú, ảnh và lịch sử sửa chữa để chuẩn hóa hồ sơ yêu cầu bảo hành trước khi chuyển bộ phận thẩm định. |
| 4 | Vinpearl / VinWonders | AI-upgrade | Nhân viên tổng hợp thủ công đánh giá đa ngôn ngữ từ nhiều kênh để phát hiện chủ đề khách hàng không hài lòng và gửi cho đơn vị vận hành. |
| 5 | Vinmec | Stakeholder Pain / Tốn thời gian | Nhân viên y tế mất nhiều thời gian tổng hợp thông tin từ hồ sơ để tạo bản nháp tóm tắt xuất viện cho bác sĩ kiểm tra. Sai sót có thể ảnh hưởng đến an toàn người bệnh. |

### Đánh giá sơ bộ

| Bài toán | Giá trị tiềm năng | Độ sẵn sàng dữ liệu | Rủi ro nếu AI sai | Nhận định ban đầu |
|---|---|---|---|---|
| Xanh SM - sự cố pin | Cao, tác động trực tiếp đến thời gian xe dừng chờ | Trung bình: cần GPS, mức pin và dữ liệu trạm sạc | Cao | Phù hợp mô hình lai: rule an toàn + LLM soạn bản nháp + con người duyệt. |
| Vinhomes - phân loại phản ánh | Cao, khối lượng lặp lại lớn | Khá: ticket và lịch sử xử lý thường có cấu trúc | Trung bình | Phù hợp LLM classification, cần ngưỡng tin cậy và fallback. |
| VinFast - hồ sơ bảo hành | Cao, giảm tải cho cố vấn dịch vụ | Trung bình: văn bản, ảnh và lịch sử sửa chữa | Cao | Chỉ nên trích xuất/tóm tắt; không cho AI tự quyết định bảo hành. |
| Vinpearl - tổng hợp đánh giá | Trung bình, hỗ trợ cải thiện dịch vụ | Khá: review dạng văn bản | Thấp | Phù hợp làm pilot vì có thể chạy offline và review theo lô. |
| Vinmec - tóm tắt xuất viện | Cao | Trung bình: dữ liệu nhạy cảm và không đồng nhất | Rất cao | Chưa nên tự động hóa quyết định; bắt buộc bảo mật và bác sĩ phê duyệt. |

## Phase 2 — QUICK-ASSESS

### Quick Problem Card 1 - Xanh SM xử lý sự cố pin yếu

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

**Ranh giới và fallback:** AI được phép tạo bản nháp tin nhắn và giải thích phương án cho điều phối viên; không được tự gửi tin, tự điều xe cứu hộ hoặc bỏ qua dữ liệu pin/khoảng cách. Nếu pin dưới 5%, hệ thống không hướng dẫn đến trạm xa trên 5 km và phải đề xuất lệnh `dispatch_mobile_charger` cho điều phối viên phê duyệt. Nếu thiếu GPS, mức pin, tình trạng trạm hoặc độ tin cậy thấp, hệ thống chuyển về quy trình thủ công.

### Quick Problem Card 2 - Vinhomes phân loại phản ánh cư dân

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

**Ranh giới và fallback:** AI chỉ đưa ra đề xuất, không đóng ticket và không cam kết bồi thường/chi phí. Ticket về an ninh, cháy nổ, y tế, tranh chấp hoặc confidence dưới 0.8 phải chuyển ngay cho nhân viên. Nếu output sai schema/category, hệ thống gắn nhãn `needs_manual_triage`.

### Quick Problem Card 3 - VinFast chuẩn hóa hồ sơ bảo hành

| Trường | Nội dung |
|---|---|
| **Bài toán (1 câu)** | Hỗ trợ cố vấn dịch vụ trích xuất và chuẩn hóa thông tin từ hồ sơ sửa chữa để tạo bản nháp yêu cầu bảo hành đầy đủ. |
| **Công ty thành viên** | VinFast |
| **Actor đang gặp khó khăn** | Cố vấn dịch vụ và nhân viên thẩm định bảo hành; khách hàng chờ lâu nếu hồ sơ thiếu thông tin. |
| **Workflow hiện tại** | 1. Tiếp nhận mô tả từ khách hàng → 2. Thu thập mã xe, ODO, mã lỗi, ảnh và lịch sử sửa chữa → 3. Đọc và nhập lại vào biểu mẫu → 4. Kiểm tra tính đầy đủ → 5. Chuyển thẩm định hoặc yêu cầu bổ sung. |
| **Bottleneck** | Bước 2-4, ước tính 15-25 phút/hồ sơ; dữ liệu nằm ở nhiều định dạng và dễ nhập thiếu trường. |
| **AI hỗ trợ** | Trích xuất dữ liệu, tóm tắt triệu chứng, đánh dấu bằng chứng còn thiếu và tạo bản nháp có trích dẫn nguồn. |
| **Success metric** | Giảm thời gian chuẩn bị hồ sơ trung vị từ 20 phút xuống dưới 5 phút; trên 95% trường bắt buộc được điền đúng; 100% quyết định bảo hành do người có thẩm quyền thực hiện. |
| **Quick Architecture** | **LLM Feature** kết hợp validation rule cho trường bắt buộc và định dạng dữ liệu. |

**Ranh giới và fallback:** AI không được tự phê duyệt/từ chối bảo hành hay suy diễn chi tiết không có trong hồ sơ. Mỗi trường trích xuất phải kèm tham chiếu tài liệu/ảnh nguồn. Nếu dữ liệu mâu thuẫn hoặc confidence thấp, hệ thống đánh dấu `manual_review_required`.

### Xếp hạng đề xuất

| Hạng | Bài toán | Lý do |
|---:|---|---|
| 1 | Xanh SM - xử lý sự cố pin yếu | Tác động vận hành rõ, metric đo được, phù hợp stress-test operational boundary bằng prototype của lab. |
| 2 | Vinhomes - phân loại phản ánh | Dữ liệu văn bản phù hợp LLM, rủi ro kiểm soát được bằng taxonomy, confidence và HITL. |
| 3 | VinFast - chuẩn hóa hồ sơ bảo hành | Giá trị cao nhưng cần tích hợp nhiều nguồn và kiểm soát chặt việc AI suy diễn sai. |

**Đề xuất cá nhân:** Chọn bài toán **Xanh SM xử lý sự cố pin yếu** để đưa vào Phase 3.

---

# 👤 Kim Mạnh Hưng

> **Người thực hiện:** Kim Mạnh Hưng — MSSV `2A202601679` — Nhóm `AI_Team`

## Bối cảnh quan sát

Quan sát từ khối vận hành thời gian thực của Xanh SM (GSM) — nơi mọi giây trễ quy đổi trực tiếp thành doanh thu mất đi. Qua mô phỏng một ca trực tại Trung tâm Điều vận, điều phối viên bị "ngập" thao tác thủ công ở các sự cố thực địa (hết pin, hỏng xe).

## Phase 1 — SCAN

| # | Subsidiary | Lens | Mô tả ngắn bài toán / bottleneck |
|---|-----------|------|----------------------------------|
| 1 | Xanh SM | Tốn thời gian | Điều phối viên xử lý thủ công sự cố hết pin/hỏng xe thực địa: tra vị trí → tra trạm sạc trống → soạn tin hướng dẫn → gọi cứu hộ (~15 phút/lượt, ~80 lượt/ngày ở Hà Nội). |
| 2 | Xanh SM | Pain từ người khác | Tài xế phàn nàn hệ thống gợi ý điểm đón khách sai vị trí (hẻm nhỏ, toà nhà nhiều cổng) khiến khách chờ lâu, tăng huỷ chuyến. |
| 3 | VinFast | Lặp lại | Đối chiếu hoá đơn sạc điện hằng tuần từ hàng nghìn trụ sạc đối tác với dữ liệu tài chính nội bộ (thủ công, dễ lệch số). |
| 4 | Vinhomes | AI-upgrade | Phân loại & điều hướng phản ánh cư dân trên App Vinhomes Resident (mất nước, hỏng đèn, ồn ào…) đến đúng ban quản lý tòa nhà; hiện phản hồi rập khuôn, trễ tới ~12 giờ. |
| 5 | Vinmec | Tốn thời gian | Bác sĩ soạn tóm tắt hồ sơ xuất viện (discharge summary) từ bệnh án + xét nghiệm, mất 20–30 phút/bệnh nhân, gây quá tải. |
| 6 | Vinpearl | Pain từ người khác | Quét review Booking/Agoda/Google Map để lọc phàn nàn khẩn cấp ("phòng bẩn", "thái độ nhân viên") gửi Manager; hiện làm thủ công, bỏ sót nhiều. |

> **Nhận xét chọn lọc:** Bài #1 (Xanh SM — sự cố thực địa) nổi bật vì tần suất cao & lặp lại, tác động doanh thu real-time rõ ràng, có ranh giới an toàn thú vị để thiết kế (không được điều xe cạn pin đi xa).

## Phase 2 — QUICK-ASSESS

### QUICK PROBLEM CARD #1 — Xanh SM: Trợ lý điều vận sự cố hết pin thực địa

```
Bài toán: Tài xế Xanh SM báo hết pin giữa đường cần được hướng dẫn tới trạm sạc
phù hợp hoặc điều xe sạc cứu hộ.
Công ty thành viên: Xanh SM (GSM)

Ai đang đau (Actor)? Điều phối viên (quá tải giờ cao điểm), Tài xế (chờ lâu, mất cuốc, stress).

Workflow thủ công hiện tại (5 bước):
  1. Nhận cuộc gọi báo sự cố
  → 2. Tra vị trí GPS xe trên bản đồ nội bộ
  → 3. Tra dashboard trạm sạc VinFast tìm trụ trống hợp xe
  → 4. Soạn tin nhắn chỉ đường gửi qua App tài xế
  → 5. Gọi xe cứu hộ nếu pin quá thấp

Bước nào tốn/lỗi nhất? Bước 3-4 (⏱ ~10 phút/lượt)
AI có thể nhảy vào ở bước nào? Bước 3-4 (tự pull vị trí + trạm trống, DRAFT tin
hướng dẫn cho người duyệt).

Metric (có số)? Giảm thời gian xử lý 15 phút ──> dưới 3 phút & tỉ lệ hướng dẫn
đúng trạm/đúng cổng sạc ≥ 98%.

Quick Architecture: LLM Feature (draft + HITL)
```

### QUICK PROBLEM CARD #2 — Vinhomes: Phân loại & điều hướng phản ánh cư dân

```
Bài toán: Tự động phân loại phản ánh cư dân (App Resident) và route đến đúng
ban quản lý tòa nhà, đề xuất mức ưu tiên.
Công ty thành viên: Vinhomes

Ai đang đau (Actor)? Nhân viên CSKH tòa nhà, cư dân chờ lâu.

Workflow thủ công hiện tại (4 bước):
  1. Cư dân gửi phản ánh dạng text tự do
  → 2. CSKH đọc, đoán loại sự cố & tòa/ban phụ trách
  → 3. Chuyển tay (email/nhóm chat) tới bộ phận đúng
  → 4. Soạn phản hồi xác nhận cho cư dân

Bước nào tốn/lỗi nhất? Bước 2-3 (⏱ ~8 phút/lượt, dễ route nhầm ban) → tổng thời
gian phản hồi ~12 giờ.
AI có thể nhảy vào ở bước nào? Bước 2 (phân loại + gán ưu tiên) & Bước 4 (draft
phản hồi mẫu).

Metric (có số)? ≥ 85% phản ánh route đúng ban < 10 giây; giảm thời gian phản
hồi lần đầu từ 12 giờ ──> dưới 1 giờ.

Quick Architecture: LLM Feature + Rule (fallback)
```

### QUICK PROBLEM CARD #3 — Vinmec: Soạn nháp tóm tắt hồ sơ xuất viện

```
Bài toán: Trích xuất thông tin lâm sàng và DRAFT bản tóm tắt xuất viện dễ hiểu
cho bệnh nhân, bác sĩ chỉ review.
Công ty thành viên: Vinmec

Ai đang đau (Actor)? Bác sĩ điều trị (quá tải hành chính).

Workflow thủ công hiện tại (4 bước):
  1. Đọc lại bệnh án điện tử + kết quả xét nghiệm
  → 2. Tổng hợp chẩn đoán, thuốc, dặn dò
  → 3. Gõ tay bản tóm tắt xuất viện
  → 4. Đọc soát & ký duyệt

Bước nào tốn/lỗi nhất? Bước 3 (⏱ 20–30 phút/bệnh nhân)
AI có thể nhảy vào ở bước nào? Bước 3 (DRAFT bản tóm tắt).

Metric (có số)? Giảm thời gian soạn từ 25 phút ──> dưới 8 phút; bác sĩ chỉnh
sửa < 20% nội dung nháp.

Quick Architecture: LLM Feature (HITL bắt buộc — y tế)
```

**Đề cử:** Card #1 (Xanh SM — sự cố hết pin thực địa) vì tác động real-time cao nhất, ranh giới an toàn rõ và đo được (pin < 5% → điều xe sạc di động, không đi trạm xa), kiến trúc gọn (LLM Feature, không cần Agent tự trị).

---

# 👤 Nguyễn Thế Khải

## Phase 1 — SCAN

| # | Subsidiary (VinFast/Xanh SM...) | Lens | Mô tả ngắn bài toán |
|---|----------------------------------|------|---------------------|
| 1 | VinFast | Lặp lại (Repetitive) | Nhân viên bảo hành phải đối chiếu thủ công log lỗi pin từ xe với danh sách mã lỗi chuẩn để xác định có thuộc diện bảo hành hay không, lặp lại hàng trăm lượt/ngày tại các trung tâm dịch vụ. |
| 2 | Xanh SM (GSM) | Stakeholder Pain | Tài xế thường xuyên phàn nàn vì hệ thống điều vận gợi ý điểm đón khách không sát vị trí thực tế (nằm trong hẻm, sai tầng ở TTTM), khiến tài xế phải gọi điện xác nhận lại với khách, kéo dài thời gian chờ. |
| 3 | Vinhomes | Tốn thời gian (Time-consuming) | Nhân viên chăm sóc cư dân phải tự đọc và soạn phản hồi thủ công cho từng đánh giá 1-2 sao trên ứng dụng quản lý cư dân, mỗi phản hồi mất 8-10 phút do phải tra cứu hồ sơ căn hộ liên quan. |
| 4 | Vinmec | AI có thể tốt hơn (AI-upgrade) | Việc sắp xếp lịch hẹn tái khám và nhắc uống thuốc cho bệnh nhân mãn tính hiện dựa vào tổng đài gọi điện thủ công, phản hồi chậm và không cá nhân hóa theo phác đồ điều trị của từng bệnh nhân. |
| 5 | Vinpearl / VinWonders | Lặp lại (Repetitive) | Nhân viên quầy vé phải nhập liệu thủ công thông tin đặt vé nhóm/đoàn từ email hoặc tin nhắn Zalo vào hệ thống bán vé nội bộ, dễ sai sót số lượng và loại vé vào giờ cao điểm. |

## Phase 2 — QUICK-ASSESS

### QUICK PROBLEM CARD #1

```
Bài toán (1 câu): Đối chiếu log lỗi pin xe với danh sách mã lỗi chuẩn để xác định bảo hành.
Công ty thành viên: [x] VinFast  [ ] Xanh SM  [ ] Vinhomes
                     [ ] Vinmec   [ ] Khác (Ghi rõ)________

Ai đang đau (Actor)? Nhân viên kỹ thuật/bảo hành tại trung tâm dịch vụ VinFast

Workflow thủ công hiện tại (3-5 bước):
  1. Xe báo lỗi qua hệ thống chẩn đoán ──> 2. NV tải log lỗi ──>
  3. NV tra cứu thủ công mã lỗi trong bảng quy định bảo hành ──> 4. NV kết luận có/không bảo hành

Bước nào tốn thời gian/lỗi nhất? Bước 3 - tra cứu thủ công (⏱ 12 phút/lượt)
AI có thể nhảy vào hỗ trợ ở bước nào? Bước 3 - tự động đối chiếu log với bảng mã lỗi và đề xuất kết luận

Đo thành công bằng gì (Metric có số)? Giảm thời gian tra cứu từ 12 phút xuống dưới 3 phút/lượt

Quick Architecture: [ ] No AI  [x] Rule  [ ] LLM  [ ] Agent
```

### QUICK PROBLEM CARD #2

```
Bài toán (1 câu): Gợi ý điểm đón khách chính xác hơn cho tài xế Xanh SM.
Công ty thành viên: [ ] VinFast  [x] Xanh SM  [ ] Vinhomes
                     [ ] Vinmec   [ ] Khác (Ghi rõ)________

Ai đang đau (Actor)? Tài xế Xanh SM và khách hàng đặt xe

Workflow thủ công hiện tại (3-5 bước):
  1. Khách đặt xe với địa chỉ text tự do ──> 2. Hệ thống ghim tọa độ GPS gần đúng ──>
  3. Tài xế di chuyển đến điểm ghim ──> 4. Tài xế gọi điện xác nhận vị trí chính xác với khách

Bước nào tốn thời gian/lỗi nhất? Bước 4 - gọi xác nhận (⏱ 3-5 phút/lượt, gây trễ chuyến)
AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2 - LLM phân tích địa chỉ text + ngữ cảnh để đề xuất điểm đón chính xác hơn

Đo thành công bằng gì (Metric có số)? Giảm tỷ lệ phải gọi xác nhận từ 40% xuống dưới 15% số chuyến

Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent
```

### QUICK PROBLEM CARD #3

```
Bài toán (1 câu): Soạn phản hồi tự động cho đánh giá 1-2 sao của cư dân Vinhomes.
Công ty thành viên: [ ] VinFast  [ ] Xanh SM  [x] Vinhomes
                     [ ] Vinmec   [ ] Khác (Ghi rõ)________

Ai đang đau (Actor)? Nhân viên chăm sóc cư dân (CSKH) tại ban quản lý Vinhomes

Workflow thủ công hiện tại (3-5 bước):
  1. Cư dân gửi đánh giá tiêu cực trên app ──> 2. NV đọc và tra hồ sơ căn hộ liên quan ──>
  3. NV soạn phản hồi phù hợp ──> 4. Trưởng ban duyệt trước khi gửi

Bước nào tốn thời gian/lỗi nhất? Bước 2-3 - tra cứu và soạn thảo (⏱ 8-10 phút/lượt)
AI có thể nhảy vào hỗ trợ ở bước nào? Bước 3 - LLM soạn draft phản hồi dựa trên nội dung đánh giá và hồ sơ căn hộ

Đo thành công bằng gì (Metric có số)? Giảm thời gian soạn phản hồi từ 10 phút xuống dưới 2 phút/lượt

Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent
```

### QUICK PROBLEM CARD #4 (Vinmec)

```
Bài toán (1 câu): Nhắc lịch tái khám và uống thuốc cá nhân hóa cho bệnh nhân mãn tính tại Vinmec.
Công ty thành viên: [ ] VinFast  [ ] Xanh SM  [ ] Vinhomes
                     [x] Vinmec   [ ] Khác (Ghi rõ)________

Ai đang đau (Actor)? Nhân viên tổng đài chăm sóc bệnh nhân (Patient Care) tại Vinmec

Workflow thủ công hiện tại (3-5 bước):
  1. NV tra danh sách bệnh nhân mãn tính đến hạn tái khám/uống thuốc ──> 2. NV tra phác đồ điều trị của từng bệnh nhân ──>
  3. NV gọi điện nhắc lịch/thuốc thủ công ──> 4. NV ghi chú lại kết quả cuộc gọi vào hồ sơ

Bước nào tốn thời gian/lỗi nhất? Bước 2-3 - tra phác đồ và gọi điện thủ công (⏱ 6-8 phút/bệnh nhân)
AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2-3 - LLM tổng hợp phác đồ và soạn nội dung nhắc lịch cá nhân hóa, gửi qua tin nhắn/app trước khi cần gọi điện

Đo thành công bằng gì (Metric có số)? Giảm số cuộc gọi thủ công cần thiết từ 100% xuống dưới 30% số ca, tỷ lệ bệnh nhân tái khám đúng hạn tăng từ 65% lên trên 85%

Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent
```

---

# 👤 Phùng Văn Linh

## Phase 1 — SCAN

| # | Subsidiary | Lens | Mô tả ngắn bài toán |
|---|---|---|---|
| 1 | Vinhomes | Stakeholder Pain, Time-consuming | Phản ánh khẩn cấp của cư dân như kẹt thang máy, chập điện, mất nước bị mô tả bằng ngôn ngữ tự do, nên nhân viên trực phải đọc, đánh giá mức độ và chuyển từng ticket đến đúng bộ phận. |
| 2 | Vinpearl | Stakeholder Pain, AI-upgrade | Review tiêu cực trên nhiều kênh bị phát hiện chậm; quản lý không nhận ra sớm các vấn đề như phòng bẩn, mất an toàn thực phẩm hoặc thái độ phục vụ để xử lý khi khách vẫn đang lưu trú. |
| 3 | VinFast | AI-upgrade, Time-consuming | Cố vấn dịch vụ phải đọc mô tả tiếng Việt tự do của khách hàng, hỏi lại nhiều lần và tự chọn nhóm kỹ thuật trước khi đặt lịch kiểm tra xe. |
| 4 | Xanh SM | Repetitive, Stakeholder Pain | Ghi chú và cuộc gọi hủy chuyến phải được nghe/đọc thủ công để phân loại lý do, khiến đội vận hành chậm nhận ra điểm đón sai, tài xế từ chối hoặc thời gian chờ quá lâu. |
| 5 | VinUni | Repetitive, Time-consuming | Giảng viên phải đọc log autograder và viết lại phản hồi cho những lỗi lặp lại, trong khi sinh viên cần hướng dẫn để hiểu lỗi thay vì chỉ nhận kết quả pass/fail. |

### Tiêu chí shortlist

| Tiêu chí | Trọng số |
|---|---:|
| Nỗi đau của stakeholder rõ và xảy ra thường xuyên | 30% |
| Có thể mô tả current-state workflow và bottleneck | 20% |
| Có metric định lượng để đánh giá | 20% |
| Có thể tạo dữ liệu mẫu và prototype trong buổi lab | 20% |
| Rủi ro AI sai có thể kiểm soát bằng HITL/fallback | 10% |

| Bài toán | Pain | Workflow | Metric | Prototype | Safety | Điểm quy đổi |
|---|---:|---:|---:|---:|---:|---:|
| Vinhomes - Phân loại phản ánh khẩn cấp | 5 | 5 | 5 | 5 | 4 | 4.9/5 |
| Vinpearl - Cảnh báo review nghiêm trọng | 4 | 4 | 4 | 5 | 4 | 4.2/5 |
| VinFast - Triage mô tả lỗi xe | 5 | 4 | 4 | 4 | 2 | 4.1/5 |
| Xanh SM - Phân tích hủy chuyến | 4 | 4 | 4 | 3 | 5 | 3.9/5 |
| VinUni - Draft phản hồi autograder | 3 | 5 | 4 | 5 | 5 | 4.2/5 |

## Phase 2 — QUICK-ASSESS

### Quick Problem Card #1 — Đề xuất chọn: Vinhomes phân loại phản ánh khẩn cấp

**Bài toán (1 câu):** Hỗ trợ nhân viên trực Vinhomes phân loại, đánh giá mức độ khẩn cấp và draft nội dung chuyển xử lý cho phản ánh của cư dân.

**Actor:** Cư dân gặp sự cố nhưng không biết liên hệ bộ phận nào; Nhân viên trực CSKH/Ban quản lý phải đọc từng phản ánh và tự quyết định ưu tiên; Đội kỹ thuật nhận ticket chậm hoặc thiếu thông tin quan trọng.

**Workflow thủ công hiện tại:**
1. Cư dân gửi nội dung tự do qua app/hotline.
2. Nhân viên trực đọc, hỏi lại tòa/căn hộ và tình trạng sự cố.
3. Nhân viên tự đánh giá mức độ và chọn bộ phận phụ trách.
4. Ticket được chuyển cho kỹ thuật/an ninh/vệ sinh.
5. Bộ phận xử lý liên hệ lại cư dân nếu ticket thiếu thông tin.

**Bottleneck:** Bước 2-3, ước tính 5-8 phút/ticket. Ticket viết mơ hồ có thể bị chuyển sai bộ phận hoặc không được nhận là khẩn cấp.

**AI hỗ trợ ở đâu?** Trích xuất loại sự cố, địa điểm, mức độ khẩn, thông tin còn thiếu; sau đó draft nhãn phân loại và bộ phận tiếp nhận. Nhân viên vẫn là người phê duyệt.

**Metric thành công (baseline cần xác minh):** Giảm thời gian triage trung vị từ 6 phút xuống dưới 90 giây/ticket; ít nhất 90% ticket được đề xuất đúng bộ phận trên bộ test đã gán nhãn; recall của nhóm sự cố khẩn cấp đạt ít nhất 95%; 100% ticket nguy hiểm có cảnh báo và bắt buộc con người phê duyệt.

**Quick Architecture:** LLM Feature + rule an toàn + Human-in-the-loop.

**Operational boundary sơ bộ:** AI chỉ được draft nhãn và gợi ý tuyến xử lý, không tự động đóng ticket; không tự đưa ra hướng dẫn kỹ thuật về điện, cháy nổ, y tế hay cứu hộ. Các từ khóa nguy hiểm ("khói", "cháy", "mùi gas", "kẹt thang máy", "bất tỉnh") phải kích hoạt rule ưu tiên P0 và chuyển ngay cho người trực. Nếu độ tin cậy thấp hoặc thiếu tòa/căn hộ, hệ thống phải yêu cầu bổ sung thông tin, không được tự suy diễn.

### Quick Problem Card #2 — Vinpearl: Cảnh báo review nghiêm trọng

**Bài toán (1 câu):** Phát hiện và tóm tắt review Vinpearl có dấu hiệu nghiêm trọng để quản lý phản hồi khi khách vẫn còn đang lưu trú.

**Actor:** Khách đang gặp trải nghiệm xấu; Guest Relations và Duty Manager phải theo dõi nhiều kênh review.

**Workflow thủ công hiện tại:** 1. Nhân viên mở từng kênh review → 2. Đọc và lọc review tiêu cực → 3. Xác định cơ sở, phòng, chủ đề và mức độ nghiêm trọng → 4. Gửi nội dung cho quản lý phụ trách → 5. Quản lý draft phản hồi và giao bộ phận xử lý.

**Bottleneck:** Bước 1-3, ước tính 8-12 phút/review và có nguy cơ bỏ sót review ngoài giờ làm việc.

**AI hỗ trợ ở đâu?** Phân loại chủ đề, tóm tắt vấn đề, phát hiện dấu hiệu khẩn cấp và draft phản hồi nội bộ.

**Metric thành công:** 90% review tiêu cực được phân loại trong dưới 2 phút; recall ít nhất 95% với review liên quan an toàn, vệ sinh và sức khỏe; giảm thời gian tổng hợp thủ công từ 10 phút xuống dưới 2 phút/review.

**Quick Architecture:** LLM Feature; Rule cho từ khóa nghiêm trọng.

### Quick Problem Card #3 — VinUni: Draft phản hồi autograder

**Bài toán (1 câu):** Draft phản hồi dễ hiểu từ log autograder để sinh viên biết vì sao code sai và bước tiếp theo cần kiểm tra gì.

**Actor:** Sinh viên chỉ nhận log kỹ thuật khó hiểu; trợ giảng lặp lại việc giải thích cùng một nhóm lỗi.

**Workflow thủ công hiện tại:** 1. Sinh viên nộp bài và autograder chạy test → 2. Sinh viên nhận stack trace/kết quả pass-fail → 3. Sinh viên gửi câu hỏi cho trợ giảng → 4. Trợ giảng đọc code và log → 5. Trợ giảng viết gợi ý sửa lỗi.

**Bottleneck:** Bước 3-5, ước tính 10-15 phút/yêu cầu vào giờ cao điểm.

**AI hỗ trợ ở đâu?** Tóm tắt log, phân loại lỗi và draft gợi ý theo kiểu Socratic, không đưa đáp án hoàn chỉnh.

**Metric thành công:** Draft phản hồi được tạo trong dưới 20 giây; ít nhất 85% phản hồi được trợ giảng đánh giá là đúng nhóm lỗi và hữu ích; 100% phản hồi không tiết lộ solution/reference answer.

**Quick Architecture:** LLM Feature + bộ lọc nội dung + Human-in-the-loop.

**Đề xuất quyết định:** Chọn Quick Problem Card #1 - Phân loại phản ánh khẩn cấp Vinhomes để Deep-Dive, vì AI có lợi thế thật sự với ngôn ngữ tự do/tiếng Việt không dấu/viết tắt, phạm vi prototype vừa sức (input: nội dung ticket, output JSON gồm category, priority, missing_fields, target_team, draft_summary), rủi ro kiểm soát được bằng rule ưu tiên + HITL + fallback.

---

# 👤 Quỳnh Phương

## Phase 1 — SCAN

| # | Subsidiary | Lens | Mô tả ngắn bài toán |
|---|------------|------|---------------------|
| 1 | Xanh SM (GSM) | Tốn thời gian | Điều phối viên tra cứu vị trí GPS và trụ sạc trống thủ công khi tài xế báo sự cố sắp hết pin trên đường đón khách (mất 15 min/lượt). |
| 2 | VinFast | Lặp lại | So khớp và đối chiếu hóa đơn sạc điện hằng tuần giữa dữ liệu viễn thông xe EV và các trạm sạc đối tác nhượng quyền. |
| 3 | Vinhomes | AI-upgrade | Phân loại và tự động soạn phản hồi cho khiếu nại cư dân về phí quản lý & tiếng ồn trên App Vinhomes Resident (CSKH phản hồi rập khuôn, tốn 12h xử lý). |
| 4 | Vinmec | Pain từ người khác | Bác sĩ mất 20-30 phút/bệnh nhân để tóm tắt hồ sơ y tế xuất viện và kê đơn dặn dò thủ công, gây quá tải giờ cao điểm. |
| 5 | Vinpearl | Stakeholder Pain | Khách hàng chờ đợi lâu khi check-in và đổi vé dịch vụ vui chơi VinWonders vào dịp Lễ/Tết do thiếu phân luồng AI linh hoạt. |

## Phase 2 — QUICK-ASSESS

### QUICK PROBLEM CARD #1

```
Bài toán (1 câu): Tài xế Xanh SM báo sự cố sạc pin / hết pin giữa đường cần
điều phối cứu hộ hoặc chỉ đường trạm sạc trống.
Công ty thành viên: Xanh SM (GSM)

Ai đang đau (Actor)? Tài xế (chờ lâu), Dispatcher (quá tải)

Workflow thủ công hiện tại (5 bước):
  1. Nhận cuộc gọi sự cố ──> 2. Tra GPS xe ──> 3. Tra trạm sạc
  ──> 4. Soạn SMS chỉ đường ──> 5. Điều xe cứu hộ (nếu cạn pin)

Bước nào tốn thời gian/lỗi nhất? Bước 3-4 (⏱ 10 phút/lượt)
AI có thể nhảy vào hỗ trợ ở bước nào? Bước 3-4 (Draft SMS & tự động lọc trạm
sạc phù hợp theo dòng xe VF5/VF8/VFe34).

Đo thành công bằng gì (Metric có số)? Giảm thời gian xử lý sự cố từ 15 phút
──> dưới 3 phút.

Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent
```

### QUICK PROBLEM CARD #2

```
Bài toán (1 câu): Phân loại và tự động soạn thảo câu trả lời phản hồi phản
ánh cư dân Vinhomes về vận hành tòa nhà.
Công ty thành viên: Vinhomes

Ai đang đau (Actor)? Đội ngũ CSKH Ban Quản Lý Vinhomes.

Workflow thủ công hiện tại (4 bước):
  1. Nhận Ticket cư dân ──> 2. Phân loại thủ công phòng ban
  ──> 3. Kiểm tra quy định/phí ──> 4. Soạn email trả lời.

Bước nào tốn thời gian/lỗi nhất? Bước 2-3 (⏱ 30 phút/ticket)
AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2 (Auto Tagging) và Bước 4 (Draft
phản hồi chuẩn văn phong Vinhomes).

Đo thành công bằng gì (Metric có số)? Giảm SLA phản hồi ticket cư dân từ 12
giờ xuống dưới 1 giờ.

Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent
```

### QUICK PROBLEM CARD #3

```
Bài toán (1 câu): Tóm tắt tự động hồ sơ bệnh án và lịch sử khám chữa bệnh để
hỗ trợ bác sĩ Vinmec viết giấy xuất viện.
Công ty thành viên: Vinmec

Ai đang đau (Actor)? Bác sĩ nội trú Vinmec.

Workflow thủ công hiện tại (4 bước):
  1. Đọc lại toàn bộ EMR ──> 2. Lọc thông tin xét nghiệm
  ──> 3. Tóm tắt quá trình điều trị ──> 4. Soạn dặn dò.

Bước nào tốn thời gian/lỗi nhất? Bước 1-3 (⏱ 25 phút/ca)
AI có thể nhảy vào hỗ trợ ở bước nào? Bước 3 (Tóm tắt EMR tự động và trích
xuất chỉ số xét nghiệm bất thường).

Đo thành công bằng gì (Metric có số)? Giảm thời gian chuẩn bị hồ sơ xuất viện
từ 25 min ──> 5 min.

Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent
```

---

# 👤 Ong Xuân Sơn

## Thông tin cá nhân

- Họ và tên: Ong Xuân Sơn
- MSSV: 2A202601327

## Phase 1 — SCAN

| # | Subsidiary | Lens | Mô tả ngắn bài toán |
|---|---|---|---|
| 1 | Xanh SM | Time-consuming | Điều phối viên xử lý thủ công sự cố xe điện sắp hết pin giữa ca làm: tra vị trí xe, tìm trạm sạc phù hợp, soạn hướng dẫn cho tài xế. |
| 2 | Vinhomes | Repetitive | Nhân viên CSKH phân loại thủ công phản ánh cư dân trên app Vinhomes Resident như mất nước, hỏng đèn, tiếng ồn, phí dịch vụ, rồi chuyển đến bộ phận phụ trách. |
| 3 | VinFast | Repetitive | Đội vận hành đối chiếu hóa đơn sạc điện của đối tác với log trạm sạc hằng tuần, để phát hiện sai lệch số tiền, thời lượng sạc và mã giao dịch. |
| 4 | Vinmec | Time-consuming | Bác sĩ mất nhiều thời gian tóm tắt hồ sơ xuất viện từ bệnh án điện tử, kết quả xét nghiệm và ghi chú lâm sàng cho từng bệnh nhân. |
| 5 | Vinpearl | Stakeholder Pain | Quản lý khách sạn phải đọc thủ công review từ Booking, Agoda, Google Maps để phát hiện phàn nàn khẩn cấp về phòng, nhân viên, dịch vụ và vệ sinh. |

## Phase 2 — QUICK-ASSESS

### Quick Problem Card #1

- **Bài toán:** Điều phối viên Xanh SM xử lý sự cố xe điện sắp hết pin giữa ca làm qua nhiều bước thủ công, làm tài xế chờ lâu và xe mất thời gian khai thác.
- **Công ty thành viên:** Xanh SM
- **Actor/Operator đang gặp khó khăn:** Điều phối viên trung tâm điều vận và tài xế Xanh SM.
- **Workflow thủ công hiện tại:**
  1. Tài xế gọi tổng đài báo pin yếu hoặc cần trạm sạc gần nhất.
  2. Điều phối viên tra vị trí GPS xe và mức pin hiện tại trên dashboard.
  3. Điều phối viên tra danh sách trạm sạc gần đó, tính khoảng cách và loại cổng sạc phù hợp.
  4. Điều phối viên soạn tin hướng dẫn đường đi/gửi qua app cho tài xế.
  5. Nếu pin quá thấp, điều phối viên gọi đội cứu hộ hoặc xe sạc pin di động.
- **Bước tốn thời gian/lỗi nhất:** Bước 3-4, khoảng 10-12 phút/lượt.
- **AI hỗ trợ ở đâu:** Bước 3-4, tổng hợp vị trí xe, trạm sạc phù hợp, cảnh báo pin thấp và tạo bản nháp tin hướng dẫn.
- **Success metric có số:** Giảm thời gian xử lý sự cố từ 15 phút xuống dưới 3 phút/lượt; 98% gợi ý đúng loại cổng sạc và khoảng cách an toàn; 100% tin gửi đi cần có điều phối viên duyệt.
- **Quick architecture:** LLM Feature

### Quick Problem Card #2

- **Bài toán:** Phản ánh cư dân Vinhomes bị phân loại và điều hướng thủ công, dẫn đến chậm SLA và nhiều ticket bị chuyển sai bộ phận.
- **Công ty thành viên:** Vinhomes
- **Actor/Operator đang gặp khó khăn:** Nhân viên CSKH, ban quản lý tòa nhà, cư dân gửi phản ánh.
- **Workflow thủ công hiện tại:**
  1. Cư dân gửi phản ánh trên app Vinhomes Resident kèm nội dung, ảnh và tòa/căn hộ.
  2. Nhân viên CSKH đọc nội dung và tự gắn nhóm vấn đề.
  3. Nhân viên tra cứu tòa nhà, khu vực, bộ phận phụ trách và mức độ ưu tiên.
  4. Ticket được chuyển sang kỹ thuật, vệ sinh, an ninh, kế toán hoặc ban quản lý.
  5. Nếu phân loại sai, ticket bị đẩy lại và cư dân phải chờ thêm.
- **Bước tốn thời gian/lỗi nhất:** Bước 2-4, khoảng 8-12 phút/ticket.
- **AI hỗ trợ ở đâu:** Đọc nội dung phản ánh, đề xuất category, mức độ ưu tiên, bộ phận phụ trách và draft phản hồi ban đầu cho cư dân.
- **Success metric có số:** 85% ticket được phân loại trong dưới 30 giây; giảm ticket bị route sai từ 18% xuống dưới 5%; phản hồi ban đầu cho cư dân trong dưới 2 phút.
- **Quick architecture:** LLM Feature

### Quick Problem Card #3

- **Bài toán:** Bác sĩ Vinmec mất nhiều thời gian soạn tóm tắt xuất viện, ảnh hưởng đến thời gian làm việc với bệnh nhân và gây quá tải hành chính.
- **Công ty thành viên:** Vinmec
- **Actor/Operator đang gặp khó khăn:** Bác sĩ điều trị, điều dưỡng hành chính, bệnh nhân chờ nhận hồ sơ xuất viện.
- **Workflow thủ công hiện tại:**
  1. Bác sĩ mở bệnh án điện tử, ghi chú lâm sàng, kết quả xét nghiệm và đơn thuốc.
  2. Bác sĩ chọn thông tin quan trọng về chẩn đoán, quá trình điều trị và tình trạng ra viện.
  3. Bác sĩ viết bản tóm tắt xuất viện bằng ngôn ngữ dễ hiểu cho bệnh nhân.
  4. Điều dưỡng/hành chính kiểm tra thông tin cá nhân và in/phát hành hồ sơ.
  5. Nếu thiếu thông tin, hồ sơ quay lại cho bác sĩ sửa.
- **Bước tốn thời gian/lỗi nhất:** Bước 2-3, khoảng 20-30 phút/bệnh nhân.
- **AI hỗ trợ ở đâu:** Tạo bản nháp tóm tắt xuất viện từ dữ liệu có sẵn, nhấn mạnh cảnh báo thông tin thiếu và chuyển ngôn ngữ chuyên môn thành dễ hiểu.
- **Success metric có số:** Giảm thời gian soạn tóm tắt từ 25 phút xuống dưới 8 phút/bệnh nhân; 100% bản tóm tắt phải được bác sĩ duyệt trước khi phát hành; giảm hồ sơ bị trả lại từ 12% xuống dưới 3%.
- **Quick architecture:** LLM Feature
