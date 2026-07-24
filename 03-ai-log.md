# 03 — AI Log & Reflection (Cá nhân)

**Họ và tên:** Nguyễn Thế Khải
**Công cụ AI sử dụng:** Claude (Claude Code)

---

## 1. AI giúp gì?

Trong buổi lab, mình dùng Claude làm thought-partner xuyên suốt các phase:
- **Phase 1-2 (Scan & Quick Cards):** Nhờ Claude brainstorm và diễn đạt lại 5 bài toán vận hành thực tế ở các công ty thành viên Vingroup theo đúng 4 lenses (Lặp lại, Tốn thời gian, AI-upgrade, Stakeholder Pain), sau đó dựng thành 4 Quick Problem Cards có cấu trúc rõ ràng (Actor, workflow, bottleneck, metric, kiến trúc đề xuất).
- **Phase 3 (Deep-Dive):** Nhờ Claude điền Problem Statement 6-field cho bài toán được chọn (nhắc tái khám/uống thuốc tại Vinmec), phân loại AI-Fit (LLM Feature vs Rule vs Agentic Loop) và dựng Future-State Flow dạng text-diagram có đánh dấu AI Step / Human-in-the-loop / Fallback.
- **Phase 5 (Evaluate):** Nhờ Claude đối chiếu AI Readiness Checklist với nội dung đã có để đưa ra quyết định GO/NOT YET/NO-GO kèm lý giải.
- **Hỗ trợ kỹ thuật:** Viết script Python (`extras/gen_workflow_diagram.py`) dùng matplotlib để dựng sơ đồ workflow hiện tại thành file `04-workflow-diagram.png`, và hỗ trợ các thao tác git (tạo file, commit, push).

## 2. AI sai gì?

- Ở lần đầu tạo `04-workflow-diagram.png`, Claude dùng các ký tự emoji (⏱, 🔴, 🔄) trực tiếp trong hình vẽ matplotlib. Font mặc định (DejaVu Sans) không hỗ trợ các glyph này nên khi render ra ảnh, chúng bị thay bằng các ô vuông trống (tofu box) — một lỗi kỹ thuật khá tinh vi vì code chạy không báo lỗi, chỉ cảnh báo "Glyph missing" và ảnh vẫn được xuất ra, dễ bị bỏ qua nếu không xem lại ảnh.
- Về mặt nội dung, Claude tự đề xuất quyết định "NOT YET" ở Phase 5 dựa trên suy luận hợp lý (thiếu baseline dữ liệu, chưa khảo sát stakeholder), nhưng đây là một giả định — thực tế nhóm chưa có bằng chứng cụ thể để khẳng định điều này đúng 100%, cần nhóm xác nhận lại dựa trên tình hình thực tế khi làm việc với Vinmec.

## 3. Sửa đổi ra sao?

- Với lỗi glyph: mình yêu cầu Claude đọc lại ảnh đã xuất ra (dùng tool đọc ảnh) để tự phát hiện lỗi hiển thị, sau đó thay toàn bộ emoji bằng nhãn text thuần (`BOTTLENECK`, `[HANDOFF]`, `TIME:`) — vừa tránh lỗi font, vừa đảm bảo ảnh in ra rõ ràng, dễ đọc khi nộp bài.
- Với quyết định Phase 5: mình giữ nguyên phần lý giải AI đưa ra như một bản nháp hợp lý, nhưng ghi chú rõ để cả nhóm review lại và điều chỉnh quyết định GO/NOT YET/NO-GO dựa trên dữ liệu/khảo sát thực tế thay vì chỉ dựa vào suy luận của AI.
- Nhìn chung, bài học rút ra là: AI hỗ trợ tốt việc cấu trúc hóa thông tin và tăng tốc độ soạn thảo, nhưng những quyết định mang tính đánh giá thực tế (business judgment) cần con người xác minh lại bằng chứng, không nên chấp nhận nguyên văn.
