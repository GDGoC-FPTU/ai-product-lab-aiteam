# 01 - Problem Scan

## Thông Tin Cá Nhân

- Họ và tên: Ong Xuân Sơn
- MSSV: 2A202601327
- Nhóm: AITEAM

---

## Phase 1 - SCAN: Bảng Quét Cơ Hội

| # | Công ty thành viên | Lens | Mô tả ngắn bài toán thực tế |
|---|---|---|---|
| 1 | Xanh SM | Tốn thời gian | Điều phối viên xử lý thủ công sự cố xe điện sắp hết pin trong ca làm: nghe tài xế báo sự cố, tra vị trí GPS, kiểm tra mức pin, tìm trạm sạc phù hợp và soạn hướng dẫn gửi lại cho tài xế. |
| 2 | Vinhomes | Lặp lại | Nhân viên CSKH phải đọc và phân loại thủ công hàng trăm phản ánh cư dân mỗi ngày trên app Vinhomes Resident như mất nước, hỏng đèn, tiếng ồn, phí dịch vụ, an ninh và vệ sinh. |
| 3 | VinFast | Lặp lại | Nhân viên vận hành phải đối chiếu hóa đơn sạc điện từ đối tác với log trạm sạc hằng tuần để phát hiện sai lệch về mã giao dịch, thời lượng sạc, số tiền và biển số xe. |
| 4 | Vinmec | Tốn thời gian | Bác sĩ mất nhiều thời gian soạn tóm tắt hồ sơ xuất viện từ bệnh án điện tử, ghi chú lâm sàng, kết quả xét nghiệm và đơn thuốc cho từng bệnh nhân. |
| 5 | Vinpearl | Stakeholder Pain | Quản lý khách sạn phải đọc thủ công review từ Booking, Agoda và Google Maps để phát hiện các phàn nàn khẩn cấp về phòng bẩn, thái độ nhân viên, đồ ăn hoặc dịch vụ chậm. |
| 6 | VinFast | AI-upgrade | Khách hàng mô tả lỗi xe bằng tiếng Việt tự nhiên như "xe kêu cụp cụp ở bánh trước" hoặc "màn hình bị đơ"; hệ thống hiện tại khó phân loại nhanh nhóm lỗi kỹ thuật ban đầu. |

---

## Phase 2 - QUICK-ASSESS: 3 Quick Problem Cards

### Quick Problem Card #1 - Xanh SM Xử Lý Sự Cố Xe Điện Sắp Hết Pin

**Tên bài toán:** Điều phối viên Xanh SM mất nhiều thời gian xử lý sự cố xe điện sắp hết pin giữa ca làm.

**Công ty thành viên:** Xanh SM

**Actor/Operator đang gặp khó khăn:** Điều phối viên trung tâm điều vận Xanh SM và tài xế đang vận hành xe điện trên đường.

**Sơ đồ quy trình thủ công hiện tại:**

```text
1. Tài xế gọi tổng đài báo pin yếu hoặc cần hỗ trợ sạc
   -> 2. Điều phối viên tra vị trí GPS và mức pin hiện tại của xe
   -> 3. Điều phối viên kiểm tra danh sách trạm sạc gần nhất, loại cổng sạc và tình trạng trụ trống
   -> 4. Điều phối viên tự soạn tin nhắn hướng dẫn đường đi cho tài xế
   -> 5. Nếu pin quá thấp, điều phối viên liên hệ đội cứu hộ hoặc xe sạc pin di động
```

**Bước tốn thời gian/gây lỗi nhiều nhất:** Bước 3 và bước 4, mất khoảng 10-12 phút/lượt. Điều phối viên phải tra nhiều màn hình khác nhau, dễ chọn nhầm trạm xa, nhầm loại cổng sạc hoặc soạn hướng dẫn chưa đủ rõ cho tài xế.

**Bước AI có thể tham gia giải quyết:** AI hỗ trợ ở bước 3 và bước 4 bằng cách tổng hợp vị trí xe, mức pin, loại xe, danh sách trạm sạc phù hợp, rồi tạo bản nháp tin nhắn hướng dẫn cho tài xế. Nếu pin dưới ngưỡng an toàn, AI đề xuất phương án gọi xe sạc pin di động thay vì cố gắng chỉ đường đến trạm xa.

**Metric đo thành công có số cụ thể:**

- Giảm thời gian xử lý sự cố từ 15 phút xuống dưới 3 phút/lượt.
- 98% gợi ý đúng trạm sạc theo khoảng cách, loại cổng sạc và mức pin.
- 100% tin nhắn gửi cho tài xế phải được điều phối viên duyệt trước khi gửi.

**Đề xuất kiến trúc sơ bộ:** LLM Feature

---

### Quick Problem Card #2 - Vinhomes Phân Loại Và Điều Hướng Phản Ánh Cư Dân

**Tên bài toán:** Nhân viên CSKH Vinhomes phân loại phản ánh cư dân thủ công, làm chậm SLA và dễ chuyển sai bộ phận xử lý.

**Công ty thành viên:** Vinhomes

**Actor/Operator đang gặp khó khăn:** Nhân viên CSKH, ban quản lý tòa nhà và cư dân gửi phản ánh qua app.

**Sơ đồ quy trình thủ công hiện tại:**

```text
1. Cư dân gửi phản ánh trên app Vinhomes Resident kèm nội dung, ảnh, tòa và căn hộ
   -> 2. Nhân viên CSKH đọc từng phản ánh và tự xác định nhóm vấn đề
   -> 3. Nhân viên tra cứu tòa nhà, khu vực, bộ phận phụ trách và mức độ ưu tiên
   -> 4. Ticket được chuyển sang kỹ thuật, vệ sinh, an ninh, kế toán hoặc ban quản lý
   -> 5. Nếu phân loại sai, ticket bị trả lại và cư dân phải chờ thêm
```

**Bước tốn thời gian/gây lỗi nhiều nhất:** Bước 2 đến bước 4, mất khoảng 8-12 phút/ticket. Lỗi thường gặp là chọn sai category, đánh giá sai mức độ khẩn cấp hoặc chuyển ticket đến nhầm bộ phận.

**Bước AI có thể tham gia giải quyết:** AI hỗ trợ đọc nội dung phản ánh, trích xuất địa điểm, phân loại category, đề xuất mức độ ưu tiên, đề xuất bộ phận xử lý và tạo bản nháp phản hồi ban đầu cho cư dân.

**Metric đo thành công có số cụ thể:**

- 85% ticket được phân loại trong dưới 30 giây.
- Giảm tỷ lệ ticket bị route sai từ 18% xuống dưới 5%.
- 90% phản ánh có phản hồi ban đầu trong dưới 2 phút.

**Đề xuất kiến trúc sơ bộ:** LLM Feature

---

### Quick Problem Card #3 - Vinmec Soạn Tóm Tắt Hồ Sơ Xuất Viện

**Tên bài toán:** Bác sĩ Vinmec mất nhiều thời gian soạn tóm tắt hồ sơ xuất viện cho bệnh nhân.

**Công ty thành viên:** Vinmec

**Actor/Operator đang gặp khó khăn:** Bác sĩ điều trị, điều dưỡng hành chính và bệnh nhân đang chờ nhận hồ sơ xuất viện.

**Sơ đồ quy trình thủ công hiện tại:**

```text
1. Bác sĩ mở bệnh án điện tử, ghi chú lâm sàng, kết quả xét nghiệm và đơn thuốc
   -> 2. Bác sĩ chọn thông tin quan trọng về chẩn đoán, quá trình điều trị và tình trạng ra viện
   -> 3. Bác sĩ viết bản tóm tắt xuất viện bằng ngôn ngữ dễ hiểu cho bệnh nhân
   -> 4. Điều dưỡng/hành chính kiểm tra thông tin cá nhân và in hồ sơ
   -> 5. Nếu thiếu thông tin, hồ sơ quay lại cho bác sĩ sửa
```

**Bước tốn thời gian/gây lỗi nhiều nhất:** Bước 2 và bước 3, mất khoảng 20-30 phút/bệnh nhân. Bác sĩ dễ bỏ sót thông tin quan trọng hoặc viết nội dung quá chuyên môn khiến bệnh nhân khó hiểu.

**Bước AI có thể tham gia giải quyết:** AI hỗ trợ tạo bản nháp tóm tắt xuất viện từ dữ liệu có sẵn, nhấn mạnh các thông tin còn thiếu, chuẩn hóa cấu trúc bản tóm tắt và chuyển ngôn ngữ chuyên môn thành dễ hiểu hơn cho bệnh nhân.

**Metric đo thành công có số cụ thể:**

- Giảm thời gian soạn tóm tắt từ 25 phút xuống dưới 8 phút/bệnh nhân.
- Giảm tỷ lệ hồ sơ bị trả lại do thiếu thông tin từ 12% xuống dưới 3%.
- 100% bản tóm tắt phải được bác sĩ duyệt trước khi phát hành.

**Đề xuất kiến trúc sơ bộ:** LLM Feature

