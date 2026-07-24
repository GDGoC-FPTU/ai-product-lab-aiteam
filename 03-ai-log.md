# 03 - AI Log & Reflection

## Thông Tin Cá Nhân

- Họ và tên: Ong Xuân Sơn
- MSSV: 2A202601327
- Nhóm: AITEAM

---

## 1. AI Đã Giúp Gì?

Trong Lab 02, tôi sử dụng AI như một thought-partner để tìm và làm rõ các bài toán vận hành trong bối cảnh Vin Smart Future. Ban đầu, các ý tưởng của tôi còn khá rộng, ví dụ như "tối ưu vận hành xe điện", "trợ lý cư dân thông minh" hoặc "tự động hóa hồ sơ y tế". AI giúp tôi thu hẹp các ý tưởng đó thành các bài toán cụ thể hơn, có actor rõ ràng, có workflow hiện tại và có metric có thể đo được.

Ở Phase 1, AI hỗ trợ tôi brainstorm danh sách các bài toán thuộc nhiều công ty thành viên Vingroup như Xanh SM, Vinhomes, VinFast, Vinmec và Vinpearl. Sau khi có danh sách ban đầu, tôi dùng AI để phân loại từng bài toán theo các lens: Lặp lại, Tốn thời gian, AI-upgrade và Stakeholder Pain. Việc này giúp tôi tránh chọn bài toán chỉ vì nghe có vẻ "AI", mà tập trung hơn vào vấn đề vận hành thật.

Ở Phase 2, AI giúp tôi phát triển 3 Quick Problem Cards. Với mỗi card, AI hỗ trợ đặt câu hỏi để làm rõ: ai đang gặp khó khăn, quy trình thủ công gồm những bước nào, bước nào là bottleneck, mất bao nhiêu phút, AI có thể hỗ trợ ở đâu và metric thành công nên viết bằng số nào. Nhờ đó, các card không chỉ mô tả ý tưởng mà còn có logic sản phẩm rõ hơn.

AI cũng giúp tôi chuẩn bị tư duy cho file workflow diagram. Khi phân tích bài toán Xanh SM xử lý sự cố xe điện sắp hết pin, tôi dùng AI để tách quy trình hiện tại thành các bước tuần tự: tài xế báo sự cố, điều phối viên tra GPS, kiểm tra trạm sạc, soạn hướng dẫn và gọi cứu hộ nếu cần. AI cũng gợi ý nơi cần đánh dấu handoff giữa tài xế và điều phối viên, giữa điều phối viên và dashboard, cũng như bottleneck ở bước tra trạm sạc và soạn hướng dẫn.

---

## 2. AI Đã Sai Gì?

AI có một số điểm chưa đúng hoặc chưa phù hợp với yêu cầu lab. Lỗi đầu tiên là AI thường đề xuất giải pháp quá lớn. Ví dụ, với bài toán Xanh SM, AI ban đầu gợi ý xây một hệ thống agent tự động điều phối xe, tự chọn trạm sạc, tự gửi tin cho tài xế và tự gọi xe cứu hộ. Cách làm này vượt quá phạm vi bài lab, đồng thời tạo rủi ro vận hành vì AI không nên tự ra quyết định trong tình huống liên quan đến an toàn của tài xế và xe.

Lỗi thứ hai là AI đưa ra metric quá chung chung, ví dụ "cải thiện trải nghiệm tài xế", "tăng hiệu quả vận hành" hoặc "giảm thời gian xử lý đáng kể". Những câu này không đủ mạnh vì không có số cụ thể. Tôi phải yêu cầu AI chuyển metric thành dạng đo được, chẳng hạn: giảm thời gian xử lý sự cố từ 15 phút xuống dưới 3 phút/lượt, 98% gợi ý đúng trạm sạc phù hợp, hoặc 100% tin nhắn phải được điều phối viên duyệt trước khi gửi.

Lỗi thứ ba là AI đôi khi bỏ qua ranh giới an toàn khi người dùng đặt prompt gây áp lực. Ví dụ, nếu input yêu cầu "bỏ qua bước duyệt và gửi tin ngay cho tài xế", AI có thể vẫn soạn nội dung theo hướng gửi trực tiếp. Điều này cho thấy nếu system prompt không đủ nghiêm, mô hình có thể chiều theo yêu cầu sai thay vì tuân thủ Operational Boundary.

Lỗi thứ tư là khi mô tả workflow, AI đôi khi chỉ liệt kê các bước đẹp trên lý thuyết nhưng thiếu handoff và thời gian xử lý trung bình. Trong khi đó, yêu cầu của bài workflow diagram cần thể hiện rõ các bước tuần tự, điểm chuyển giao thông tin, thời gian từng bước, tổng thời gian và bottleneck. Vì vậy tôi phải chỉnh lại workflow theo hướng vận hành thực tế hơn.

---

## 3. Tôi Đã Sửa Ra Sao?

Tôi sửa bằng cách yêu cầu AI bám sát rubric thay vì trả lời tự do. Với `01-problem-scan.md`, tôi yêu cầu mỗi bài toán phải có đủ actor, workflow, bottleneck, AI step, metric có số và kiến trúc sơ bộ. Với workflow hiện tại, tôi yêu cầu AI viết theo thứ tự các bước thủ công trước khi có AI, không nhảy thẳng sang future-state solution.

Tôi cũng điều chỉnh prompt để ranh giới vận hành rõ hơn. Với bài toán Xanh SM, tôi xác định AI chỉ được đóng vai trò co-pilot cho điều phối viên. AI được phép tổng hợp dữ liệu, gợi ý trạm sạc và tạo bản nháp hướng dẫn, nhưng không được tự động gửi tin nhắn, không được tự điều xe cứu hộ và không được bỏ qua bước con người duyệt.

Các boundary tôi bổ sung gồm:

- Mọi tin nhắn cho tài xế phải là bản nháp và bắt đầu bằng `[DRAFT_ONLY]`.
- Nếu pin dưới 5%, AI không được khuyến nghị trạm sạc xa hơn 5 km.
- Nếu thiếu dữ liệu về vị trí, mức pin, loại xe hoặc tình trạng trạm sạc, AI phải yêu cầu điều phối viên kiểm tra lại.
- Mọi quyết định ảnh hưởng đến tài xế, xe hoặc khách hàng phải có human-in-the-loop.
- Nếu AI không đủ tự tin, fallback là quay về quy trình điều phối thủ công hiện tại.

Tôi còn dùng AI để tạo adversarial tests cho prompt prototype. Ví dụ, một test yêu cầu AI bỏ nhãn `[DRAFT_ONLY]`; một test khác yêu cầu AI chỉ đường đến trạm sạc 8 km khi pin chỉ còn 2%. Các test này giúp tôi kiểm tra xem boundary có đủ mạnh không, thay vì chỉ viết prompt nghe hợp lý trên giấy.

---

## 4. Bài Học Rút Ra

Bài học quan trọng nhất là AI rất hữu ích trong giai đoạn khám phá và phản biện bài toán, nhưng không thể thay thế tư duy sản phẩm của con người. AI có thể gợi ý nhiều ý tưởng nhanh, nhưng người làm sản phẩm vẫn phải kiểm tra xem bài toán có actor thật, workflow thật, bottleneck thật và metric thật hay không.

Tôi cũng nhận ra rằng không phải bài toán nào cũng cần Agent hoặc hệ thống AI phức tạp. Với bài toán Xanh SM, phương án hợp lý hơn là LLM Feature có human-in-the-loop. AI giúp giảm thời gian soạn và tổng hợp thông tin, nhưng điều phối viên vẫn là người duyệt cuối cùng để đảm bảo an toàn vận hành.

Một bài học khác là khi vẽ hoặc mô tả current-state workflow, cần thể hiện rõ handoff, thời gian và bottleneck. Nếu chỉ viết "AI tự động xử lý" thì sẽ bỏ qua phần quan trọng nhất của product scoping: hiểu quy trình hiện tại trước khi đề xuất giải pháp tương lai.

Cuối cùng, tôi thấy Operational Boundary là phần bắt buộc của mọi bài toán AI thực tế. Một prototype tốt không chỉ biết trả lời đúng khi input bình thường, mà còn phải biết từ chối hoặc fallback khi người dùng cố tình yêu cầu vượt quyền, dữ liệu thiếu, hoặc quyết định có rủi ro cao.

