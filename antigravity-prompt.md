# 🪄 Prompt cho Antigravity — Trợ lý hoàn thiện Lab 02 (AI Product Scoping)

> **Cách dùng:** Mở repo này trong **Antigravity** (IDE agentic của Google). Copy nguyên khối
> "MASTER PROMPT" bên dưới và dán vào ô chat của Agent. Điền các ô `<...>` trước khi gửi.
>
> Prompt được thiết kế theo cấu trúc **Role → Context → Task → Constraints → Definition of Done**
> để agent hành động có kiểm soát, không bịa và không phá vỡ ranh giới an toàn của bài lab.

---

## 📋 MASTER PROMPT (copy phần trong khung)

```text
# ROLE
Bạn là AI Product Engineer kiêm trợ lý kỹ thuật, giúp nhóm mình hoàn thiện Lab 02
"AI Product Scoping (Vin Smart Future)" trong repo hiện tại. Ưu tiên: đúng rubric,
trung thực số liệu, giữ vững ranh giới an toàn, code chạy được.

# CONTEXT (đọc kỹ các file trong repo trước khi làm)
- README.md — hướng dẫn nộp bài & rubric.
- 01-worksheet.md — 6 Phase của lab.
- 02-deliverable-example.md — bài mẫu "xuất sắc" (chỉ tham chiếu, KHÔNG copy nguyên văn).
- 03-inspiration-kit.md — ngân hàng bài toán gợi ý.
- autograder/autograder.py — bộ chấm tự động (đọc để biết chính xác tiêu chí PASS).
- starter-code/prompt_prototype.py — code prototype cần hoàn thiện.

Bài toán nhóm mình đang chọn: <VD: Xanh SM — trợ lý điều vận sự cố hết pin thực địa>.
Thông tin nhóm: <Tên nhóm>; thành viên: <Họ tên + MSSV của từng người>.

# TASK
1. Kiểm tra 4 file deliverable ở thư mục gốc đã tồn tại và đủ nội dung theo rubric chưa:
   01-problem-scan.md, 02-deep-dive-report.md, 03-ai-log.md, 04-workflow-diagram.(png/jpg/pdf).
2. Rà soát 01/02/03: điền thông tin nhóm, đảm bảo metric CÓ SỐ, có Operational Boundary,
   có HITL + Fallback, và quyết định GO/NOT YET/NO-GO kèm lý giải chi phí.
3. Hoàn thiện starter-code/prompt_prototype.py:
   - SYSTEM_PROMPT chặt, nêu rõ 2 ranh giới: (a) mọi tin nhắn phải bắt đầu bằng [DRAFT_ONLY];
     (b) pin < 5% thì KHÔNG gợi ý trạm > 5km, phải trả JSON {"action":"dispatch_mobile_charger",...}.
   - evaluate_prompt() dùng SDK google-genai, và có fallback offline khi thiếu API key
     để script vẫn chạy được (exit code 0) trên CI không có key.
   - >= 3 adversarial test (gồm 1 prompt-injection) + assertion in ra "Passed"/không in "Failed".
4. Chạy self-check và sửa đến khi PASS:
   python autograder/autograder.py

# CONSTRAINTS (ranh giới bắt buộc — KHÔNG vi phạm)
- KHÔNG hard-code API key vào source (dùng biến môi trường GEMINI_API_KEY/GOOGLE_API_KEY).
- KHÔNG chỉnh sửa file trong autograder/ hay .github/ để "lách điểm".
- KHÔNG bịa số liệu: mọi con số phải ghi rõ là giả định/baseline để scoping.
- KHÔNG copy nguyên văn 02-deliverable-example.md — diễn đạt lại bằng góc nhìn của nhóm.
- Giữ nguyên tắc Problem-First: ưu tiên LLM Feature/Rule đơn giản thay vì Multi-Agent.
- Dòng tổng kết của script KHÔNG in đúng chữ "Passed"/"Failed" để tránh nhiễu bộ đếm autograder.

# DEFINITION OF DONE
- `python autograder/autograder.py` in ra: "[SUCCESS] Tat ca cac check duoc chon deu thanh cong!"
- 9 tiêu chí (4 file + 5 code check) đều PASS.
- Các file .md đã điền tên nhóm + MSSV thật, không còn placeholder <...>.
- Giải thích ngắn gọn cho nhóm: đã thay đổi gì và vì sao.
```

---

## 🎯 Các prompt phụ trợ (dùng khi cần)

**A. Đổi sang bài toán khác (không phải Xanh SM):**
```text
Nhóm mình muốn đổi bài toán Deep-Dive sang: <VD: Vinhomes — phân loại phản ánh cư dân>.
Hãy giữ nguyên cấu trúc rubric nhưng viết lại 01/02/03 cho bài toán mới, và thiết kế lại
2 ranh giới an toàn phù hợp cho prototype (ví dụ: cấm tự đóng ticket khiếu nại phí quản lý,
bắt buộc gắn nhãn [DRAFT_ONLY] cho phản hồi cư dân). Cập nhật adversarial test tương ứng.
Lưu ý: autograder yêu cầu SYSTEM_PROMPT chứa >= 2 trong các từ khoá {draft_only, 5%,
dispatch_mobile_charger} — nếu đổi kịch bản, hãy đọc lại autograder để chỉnh cho khớp.
```

**B. Đóng vai CFO phản biện (Phase 2 stress-test):**
```text
Đây là Quick Problem Card của nhóm: <dán nội dung>. Đóng vai CFO và Trưởng phòng Vận hành
cực kỳ khắt khe, chỉ ra 3 điểm yếu về logic/metric và giải thích vì sao một giải pháp
rule-based có thể tốt hơn AI ở bài này. Sau đó đề xuất cách siết metric cho thuyết phục hơn.
```

**C. Kiểm thử ranh giới an toàn (Phase 4):**
```text
Hãy viết thêm 3 câu tấn công (adversarial) tinh vi nhằm dụ model bỏ thẻ [DRAFT_ONLY] hoặc
chỉ tài xế tới trạm xa khi pin cạn. Với mỗi câu, dự đoán phản hồi đúng và giải thích vì sao
SYSTEM_PROMPT hiện tại chặn được. Nếu chặn chưa chắc, đề xuất câu chữ siết lại system prompt.
```

---

## ⚠️ Nhắc nhở khi dùng bất kỳ AI agent nào (Antigravity/Claude/Gemini)

1. **Đọc trước, sửa sau:** yêu cầu agent đọc `autograder/autograder.py` trước khi sửa code — tiêu chí PASS nằm ở đó.
2. **Kiểm chứng số liệu:** mọi con số agent đưa ra hãy hỏi lại "đây là giả định hay dữ liệu?".
3. **Đừng để agent phá ranh giới:** nếu agent gợi ý sửa autograder hoặc hard-code kết quả để "qua bài", đó là dấu hiệu sai — dừng lại.
4. **Bài cá nhân phải là giọng của bạn:** 01/03 mỗi thành viên tự viết lại; đừng nộp trùng văn.
