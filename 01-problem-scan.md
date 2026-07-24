# 01 — Problem Scan (Cá nhân)

> Bài cá nhân — Phase 1 (SCAN) & Phase 2 (QUICK-ASSESS) từ `01-worksheet.md`.

---

## 🔍 Phase 1 — SCAN

### 📝 List bài toán của tôi:

| # | Subsidiary (VinFast/Xanh SM...) | Lens                               | Mô tả ngắn bài toán                                                                                                                                                                                                                                  |
| - | ------------------------------- | ---------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1 | VinFast                         | Lặp lại (Repetitive)             | Nhân viên bảo hành phải đối chiếu thủ công log lỗi pin từ xe với danh sách mã lỗi chuẩn để xác định có thuộc diện bảo hành hay không, lặp lại hàng trăm lượt/ngày tại các trung tâm dịch vụ.                      |
| 2 | Xanh SM (GSM)                   | Stakeholder Pain                   | Tài xế thường xuyên phàn nàn vì hệ thống điều vận gợi ý điểm đón khách không sát vị trí thực tế (nằm trong hẻm, sai tầng ở TTTM), khiến tài xế phải gọi điện xác nhận lại với khách, kéo dài thời gian chờ. |
| 3 | Vinhomes                        | Tốn thời gian (Time-consuming)   | Nhân viên chăm sóc cư dân phải tự đọc và soạn phản hồi thủ công cho từng đánh giá 1-2 sao trên ứng dụng quản lý cư dân, mỗi phản hồi mất 8-10 phút do phải tra cứu hồ sơ căn hộ liên quan.                         |
| 4 | Vinmec                          | AI có thể tốt hơn (AI-upgrade) | Việc sắp xếp lịch hẹn tái khám và nhắc uống thuốc cho bệnh nhân mãn tính hiện dựa vào tổng đài gọi điện thủ công, phản hồi chậm và không cá nhân hóa theo phác đồ điều trị của từng bệnh nhân.                |
| 5 | Vinpearl / VinWonders           | Lặp lại (Repetitive)             | Nhân viên quầy vé phải nhập liệu thủ công thông tin đặt vé nhóm/đoàn từ email hoặc tin nhắn Zalo vào hệ thống bán vé nội bộ, dễ sai sót số lượng và loại vé vào giờ cao điểm.                                       |

---

## 🃏 Phase 2 — QUICK-ASSESS

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
  VD: "Giảm thời gian soạn phản hồi từ 10 min ──> under 2 min"

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
  VD: "Giảm thời gian soạn phản hồi từ 10 min ──> under 2 min"

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
  VD: "Giảm thời gian soạn phản hồi từ 10 min ──> under 2 min"

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
  VD: "Giảm thời gian soạn phản hồi từ 10 min ──> under 2 min"

Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent
```
