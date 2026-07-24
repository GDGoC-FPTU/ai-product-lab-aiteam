# Lab 02 - AI Log & Reflection

## Thông tin cá nhân

| Trường | Thông tin |
|---|---|
| Nhóm | AI TEAM |
| Họ và tên | Nguyễn Duy Dũng |
| Mã HV | 2A202601505 |
| Email | dgx3811@gmail.com |

---

# Nhật ký sử dụng AI

## 1. Tôi đã dùng AI để làm gì?

Tôi sử dụng AI như một thought-partner trong quá trình đọc yêu cầu và thực
hiện phần Problem Scan. AI hỗ trợ tôi:

- Đọc slide, README, worksheet và autograder để xác định đúng các file cần
  nộp, phần cá nhân và phần nhóm.
- Brainstorm các pain point vận hành tại Xanh SM, Vinhomes, VinFast,
  Vinpearl và Vinmec theo bốn lenses của worksheet.
- Phản biện từng ý tưởng theo actor, workflow, bottleneck, metric và mức độ
  phù hợp giữa Rule, LLM Feature và Agent.
- Viết ba Quick Problem Cards và bổ sung operational boundary, human review
  cùng fallback cho từng bài toán.
- Kiểm tra cấu trúc file bằng autograder và hỗ trợ quy trình Git trên branch
  cá nhân.

Tôi không sử dụng nguyên kết quả đầu tiên của AI. Tôi đặt câu hỏi lại về
những chỗ chưa rõ, yêu cầu viết lại bằng tiếng Việt có dấu và kiểm tra xem
đâu là nội dung bắt buộc theo rubric.

## 2. AI đã sai hoặc chưa tốt ở điểm nào?

Điểm chưa tốt đáng chú ý nhất là AI đưa ra các con số như thời gian xử lý
10-15 phút, độ chính xác 90% và ngưỡng confidence 0.8 khi chưa có log vận
hành thực tế của doanh nghiệp. Những con số này hữu ích để xây dựng metric
cho bài lab nhưng không thể được trình bày như dữ kiện chính thức.

Ngoài ra, bản nháp đầu tiên được viết bằng tiếng Việt không dấu. Nội dung
vẫn hiểu được nhưng khó đọc và không phù hợp với chất lượng của một báo cáo
nộp chính thức.

AI cũng đề xuất dùng LLM cho một số bước mà rule-based validation phù hợp
hơn. Ví dụ, điều kiện pin dưới 5% và khoảng cách trạm trên 5 km phải là quy
tắc xác định, không nên giao cho LLM tự suy luận.

## 3. Tôi đã sửa như thế nào?

Tôi thực hiện ba điều chỉnh:

1. Gắn từ “ước tính” vào các baseline chưa được kiểm chứng và thêm lưu ý
   rằng nhóm cần xác minh bằng dữ liệu vận hành hoặc phỏng vấn người dùng.
2. Yêu cầu viết lại toàn bộ tài liệu bằng tiếng Việt có dấu và tự đọc lại
   nội dung trước khi commit.
3. Tách kiến trúc thành hai lớp: rule engine bảo vệ các ngưỡng an toàn; LLM
   chỉ tạo nội dung dạng nháp; con người là người phê duyệt hành động cuối
   cùng. Khi thiếu dữ liệu hoặc output không đúng schema, hệ thống phải
   fallback về xử lý thủ công.

## 4. Điều tôi rút ra

AI giúp mở rộng và cấu trúc ý tưởng rất nhanh, nhưng chất lượng đầu ra phụ
thuộc vào việc người dùng có kiểm tra giả định và đặt ranh giới rõ hay
không. Với một bài toán vận hành, metric cần có số để đo thành công, nhưng
mọi con số chưa có nguồn phải được đánh dấu là giả định.

Tôi cũng nhận ra không nên dùng LLM cho mọi quyết định. Các điều kiện cứng,
đặc biệt là điều kiện liên quan đến an toàn, nên được thực thi bằng rule.
LLM phù hợp hơn với việc hiểu ngôn ngữ và tạo bản nháp, còn hành động có
rủi ro phải có human-in-the-loop và fallback.

