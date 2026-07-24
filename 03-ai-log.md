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

## 1. Quá trình tôi thực hiện

Đầu tiên, tôi đối chiếu yêu cầu trong worksheet và README để tách phần cá
nhân khỏi phần nhóm. Ở phần cá nhân, tôi cần quét ít nhất năm bài toán và
chọn ba bài toán để đánh giá nhanh. Tôi tập trung vào các quy trình có thao
tác lặp lại, mất nhiều thời gian hoặc gây khó khăn cho người vận hành.

Từ danh sách ban đầu, tôi giữ lại ba bài toán để phân tích kỹ hơn:

- Xử lý sự cố pin yếu của tài xế Xanh SM.
- Phân loại phản ánh cư dân tại Vinhomes.
- Chuẩn hóa hồ sơ bảo hành tại VinFast.

Tôi chọn ba bài toán này vì đều có actor, quy trình hiện tại và bottleneck
khá rõ. Sau đó, tôi xác định bước nào phù hợp với rule, bước nào có thể dùng
LLM và điểm nào bắt buộc phải có con người phê duyệt.

## 2. Tôi sử dụng AI ở đâu?

Tôi sử dụng AI để tham khảo thêm pain point, kiểm tra xem Quick Problem Card
có thiếu trường nào và gợi ý cách diễn đạt metric rõ ràng hơn. Với phần
prototype, tôi dùng AI để tham khảo cách gọi Gemini SDK và nghĩ thêm các
prompt tấn công vào hai ranh giới an toàn.

AI đóng vai trò hỗ trợ brainstorm và phản biện. Tôi là người đọc lại, đặt
câu hỏi về các giả định, lựa chọn nội dung giữ lại và quyết định bản cuối
cùng đưa vào bài.

## 3. AI trả lời chưa tốt ở điểm nào?

AI từng gợi ý các con số như thời gian xử lý 10-15 phút, độ chính xác 90%
và ngưỡng confidence 0.8 dù chưa có log vận hành thực tế. Nếu dùng nguyên
những con số này, người đọc có thể hiểu nhầm đó là dữ liệu chính thức.

Bản nháp đầu tiên cũng được trình bày bằng tiếng Việt không dấu, khiến tài
liệu khó đọc. Ngoài ra, AI có xu hướng đề xuất LLM cho cả các điều kiện cứng.
Ví dụ, ngưỡng pin dưới 5% và khoảng cách trên 5 km là điều kiện an toàn xác
định, phù hợp với rule hơn là để LLM tự suy luận.

## 4. Tôi đã điều chỉnh như thế nào?

Tôi yêu cầu viết lại tài liệu bằng tiếng Việt có dấu và đánh dấu các số liệu
chưa được kiểm chứng là “ước tính”. Tôi cũng sửa kiến trúc đề xuất theo
hướng:

- Rule engine kiểm tra mức pin và khoảng cách.
- LLM chỉ soạn nội dung có tiền tố `[DRAFT_ONLY]`.
- Điều phối viên là người duyệt trước khi gửi hoặc thực hiện hành động.
- Nếu thiếu dữ liệu hoặc output không đúng định dạng, hệ thống quay về quy
  trình xử lý thủ công.

Khi thử ba prompt tấn công, tôi kiểm tra đầu ra theo đúng hai ranh giới thay
vì chỉ đánh giá câu trả lời có hợp lý về mặt ngôn ngữ hay không. Các trường
hợp pin nguy cấp phải trả về `dispatch_mobile_charger`; trường hợp soạn
hướng dẫn phải giữ `[DRAFT_ONLY]`.

## 5. Bài học rút ra

AI giúp tôi tiết kiệm thời gian khi mở rộng ý tưởng và rà soát cấu trúc,
nhưng không thay thế việc hiểu bài toán và ra quyết định. Người làm bài vẫn
phải kiểm tra nguồn của số liệu, chọn đúng kiến trúc và chịu trách nhiệm về
ranh giới an toàn.

Tôi cũng rút ra rằng không phải bước nào cũng cần LLM. Rule phù hợp với điều
kiện cứng; LLM phù hợp với xử lý ngôn ngữ và tạo bản nháp; các hành động có
rủi ro cần human-in-the-loop và phương án fallback.
