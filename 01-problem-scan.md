# 01 - Problem Scan

## Thông Tin Cá Nhân

- Họ và tên: Ong Xuân Sơn
- MSSV: 2A202601327
- Nhóm: 

## Phase 1 - SCAN

| # | Subsidiary | Lens | Mô tả ngắn bài toán |
|---|---|---|---|
| 1 | Xanh SM | Time-consuming | Điều phối viên xử lý thủ công sự cố xe điện sắp hết pin giữa ca làm: tra vị trí xe, tìm trạm sạc phù hợp, soạn hướng dẫn cho tài xế. |
| 2 | Vinhomes | Repetitive | Nhân viên CSKH phân loại thủ công phản ánh cư dân trên app Vinhomes Resident như mất nước, hỏng đèn, tiếng ồn, phí dịch vụ, rồi chuyển đến bộ phận phụ trách. |
| 3 | VinFast | Repetitive | Đội vận hành đối chiếu hóa đơn sạc điện của đối tác với log trạm sạc hằng tuần, để phát hiện sai lệch số tiền, thời lượng sạc và mã giao dịch. |
| 4 | Vinmec | Time-consuming | Bác sĩ mất nhiều thời gian tóm tắt hồ sơ xuất viện từ bệnh án điện tử, kết quả xét nghiệm và ghi chú lâm sàng cho từng bệnh nhân. |
| 5 | Vinpearl | Stakeholder Pain | Quản lý khách sạn phải đọc thủ công review từ Booking, Agoda, Google Maps để phát hiện phàn nàn khẩn cấp về phòng, nhân viên, dịch vụ và vệ sinh. |

## Phase 2 - QUICK-ASSESS

### Quick Problem Card #1

- Bài toán: Điều phối viên Xanh SM xử lý sự cố xe điện sắp hết pin giữa ca làm qua nhiều bước thủ công, làm tài xế chờ lâu và xe mất thời gian khai thác.
- Công ty thành viên: Xanh SM
- Actor/Operator đang gặp khó khăn: Điều phối viên trung tâm điều vận và tài xế Xanh SM.
- Workflow thủ công hiện tại:
  1. Tài xế gọi tổng đài báo pin yếu hoặc cần trạm sạc gần nhất.
  2. Điều phối viên tra vị trí GPS xe và mức pin hiện tại trên dashboard.
  3. Điều phối viên tra danh sách trạm sạc gần đó, tính khoảng cách và loại cổng sạc phù hợp.
  4. Điều phối viên soạn tin hướng dẫn đường đi/gửi qua app cho tài xế.
  5. Nếu pin quá thấp, điều phối viên gọi đội cứu hộ hoặc xe sạc pin di động.
- Bước tốn thời gian/lỗi nhất: Bước 3-4, khoảng 10-12 phút/lượt vì phải tra nhiều màn hình và soạn hướng dẫn thủ công.
- AI có thể hỗ trợ ở bước nào: Hỗ trợ bước 3-4 bằng cách tổng hợp vị trí xe, trạm sạc phù hợp, cảnh báo pin thấp và tạo bản nháp tin hướng dẫn.
- Success metric có số: Giảm thời gian xử lý sự cố từ 15 phút xuống dưới 3 phút/lượt; 98% gợi ý đúng loại cổng sạc và khoảng cách an toàn; 100% tin gửi đi cần có điều phối viên duyệt.
- Quick architecture: LLM Feature

### Quick Problem Card #2

- Bài toán: Phản ánh cư dân Vinhomes bị phân loại và điều hướng thủ công, dẫn đến chậm SLA và nhiều ticket bị chuyển sai bộ phận.
- Công ty thành viên: Vinhomes
- Actor/Operator đang gặp khó khăn: Nhân viên CSKH, ban quản lý tòa nhà, cư dân gửi phản ánh.
- Workflow thủ công hiện tại:
  1. Cư dân gửi phản ánh trên app Vinhomes Resident kèm nội dung, ảnh và tòa/căn hộ.
  2. Nhân viên CSKH đọc nội dung và tự gắn nhóm vấn đề.
  3. Nhân viên tra cứu tòa nhà, khu vực, bộ phận phụ trách và mức độ ưu tiên.
  4. Ticket được chuyển sang kỹ thuật, vệ sinh, an ninh, kế toán hoặc ban quản lý.
  5. Nếu phân loại sai, ticket bị đẩy lại và cư dân phải chờ thêm.
- Bước tốn thời gian/lỗi nhất: Bước 2-4, khoảng 8-12 phút/ticket; lỗi phổ biến là chọn sai category hoặc sai bộ phận xử lý.
- AI có thể hỗ trợ ở bước nào: Hỗ trợ đọc nội dung phản ánh, đề xuất category, mức độ ưu tiên, bộ phận phụ trách và draft phản hồi ban đầu cho cư dân.
- Success metric có số: 85% ticket được phân loại trong dưới 30 giây; giảm ticket bị route sai từ 18% xuống dưới 5%; phản hồi ban đầu cho cư dân trong dưới 2 phút.
- Quick architecture: LLM Feature

### Quick Problem Card #3

- Bài toán: Bác sĩ Vinmec mất nhiều thời gian soạn tóm tắt xuất viện, ảnh hưởng đến thời gian làm việc với bệnh nhân và gây quá tải hành chính.
- Công ty thành viên: Vinmec
- Actor/Operator đang gặp khó khăn: Bác sĩ điều trị, điều dưỡng hành chính, bệnh nhân chờ nhận hồ sơ xuất viện.
- Workflow thủ công hiện tại:
  1. Bác sĩ mở bệnh án điện tử, ghi chú lâm sàng, kết quả xét nghiệm và đơn thuốc.
  2. Bác sĩ chọn thông tin quan trọng về chẩn đoán, quá trình điều trị và tình trạng ra viện.
  3. Bác sĩ viết bản tóm tắt xuất viện bằng ngôn ngữ dễ hiểu cho bệnh nhân.
  4. Điều dưỡng/hành chính kiểm tra thông tin cá nhân và in/phát hành hồ sơ.
  5. Nếu thiếu thông tin, hồ sơ quay lại cho bác sĩ sửa.
- Bước tốn thời gian/lỗi nhất: Bước 2-3, khoảng 20-30 phút/bệnh nhân; dễ thiếu kết quả quan trọng hoặc dùng ngôn ngữ quá chuyên môn.
- AI có thể hỗ trợ ở bước nào: Hỗ trợ tạo bản nháp tóm tắt xuất viện từ dữ liệu có sẵn, nhấn mạnh cảnh báo thông tin thiếu và chuyển ngôn ngữ chuyên môn thành dễ hiểu.
- Success metric có số: Giảm thời gian soạn tóm tắt từ 25 phút xuống dưới 8 phút/bệnh nhân; 100% bản tóm tắt phải được bác sĩ duyệt trước khi phát hành; giảm hồ sơ bị trả lại từ 12% xuống dưới 3%.
- Quick architecture: LLM Feature
