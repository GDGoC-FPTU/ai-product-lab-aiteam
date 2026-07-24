# 02 — Deep-Dive Report (Bài nhóm)

> **Tên nhóm:** AI TEAM
>
> **Thành viên (Họ và tên — MSSV):**
> 1. Nguyễn Duy Dũng — 2A202601505
> 2. Kim Mạnh Hưng — 2A202601679
> 3. Nguyễn Thế Khải — 2A202601099
> 4. Phùng Văn Linh — 2A202601992
> 5. Đinh Lê Quỳnh Phương — 2A202601865
> 6. Ong Xuân Sơn — 2A202601327

---

## 🎯 Quyết định lựa chọn
**Bài toán được chọn để Deep-Dive:** Nhắc lịch tái khám và uống thuốc cá nhân hóa cho bệnh nhân mãn tính tại Vinmec.

---

## 🏗️ Phase 3 — DEEP-DIVE

### 3.2. Problem Statement (6-field) & Metrics

| Field | Nội dung chi tiết |
|---|---|
| **1. Actor / Operator** | Nhân viên tổng đài chăm sóc bệnh nhân (Patient Care) tại các bệnh viện Vinmec, phụ trách nhắc lịch tái khám và tuân thủ điều trị cho nhóm bệnh nhân mãn tính (tiểu đường, tim mạch, hậu phẫu...). |
| **2. Current Workflow** | Hằng ngày, NV tổng đài tra danh sách bệnh nhân đến hạn tái khám/uống thuốc từ hệ thống quản lý hồ sơ bệnh án (HIS), tra cứu phác đồ điều trị riêng của từng bệnh nhân, sau đó gọi điện thoại thủ công để nhắc lịch/thuốc và ghi chú lại kết quả cuộc gọi vào hồ sơ. Công cụ sử dụng: hệ thống HIS nội bộ + điện thoại tổng đài. |
| **3. Bottleneck** | Bước tra cứu phác đồ điều trị và gọi điện thủ công cho từng bệnh nhân là chậm nhất và dễ bỏ sót nhất, vì nội dung nhắc cần cá nhân hóa theo phác đồ (không thể dùng kịch bản chung), tốn 6-8 phút/bệnh nhân và phụ thuộc hoàn toàn vào số lượng nhân viên trực tổng đài. |
| **4. Business Impact** | Với số lượng bệnh nhân mãn tính lớn tại mỗi bệnh viện, tổng đài chỉ đủ nhân lực gọi được cho khoảng 60-70% danh sách mỗi ngày, phần còn lại bị trễ hoặc bỏ sót nhắc lịch, kéo theo tỷ lệ tái khám đúng hạn hiện chỉ đạt ~65%, ảnh hưởng đến hiệu quả điều trị và tăng nguy cơ tái nhập viện cấp cứu (chi phí điều trị cao hơn nhiều so với chi phí phòng ngừa). |
| **5. Success Metric** | Giảm số cuộc gọi thủ công bắt buộc từ 100% xuống dưới 30% số ca (70% được xử lý qua nhắc tự động qua app/SMS do AI soạn); tỷ lệ bệnh nhân tái khám đúng hạn tăng từ 65% lên trên 85% trong vòng 3 tháng triển khai. |
| **6. Operational Boundary** | AI được phép: tổng hợp phác đồ điều trị có sẵn trong hồ sơ để soạn nội dung nhắc lịch/thuốc cá nhân hóa, gửi qua kênh tin nhắn/app. AI TUYỆT ĐỐI không được: tự ý thay đổi liều lượng/phác đồ thuốc, đưa ra chẩn đoán hoặc tư vấn y khoa mới, liên hệ trực tiếp với bệnh nhân qua giọng nói AI mà không qua kiểm duyệt nội dung. Điểm cần duyệt: mọi nội dung nhắc lịch liên quan đến thay đổi thuốc/liều lượng phải được bác sĩ/điều dưỡng phụ trách xác nhận trước khi gửi; các ca bệnh nhân không phản hồi sau nhắc tự động phải được chuyển về cho nhân viên tổng đài gọi điện trực tiếp (fallback). |

### 3.3. Future-State Flow & AI Fit

**AI-Fit Matrix:** [ ] Rule / State-Machine  [x] LLM Feature  [ ] Agentic Loop

> Bài toán cần soạn nội dung nhắc lịch cá nhân hóa theo phác đồ điều trị của từng bệnh nhân (ngôn ngữ tự nhiên, không thể liệt kê hết bằng rule cứng), nhưng phạm vi tác vụ đơn giản, không cần AI tự quyết định chuỗi hành động nhiều bước → phù hợp **LLM Feature** hơn là Agentic Loop; đồng thời không thể chỉ dùng Rule/State-Machine vì nội dung nhắc cần diễn đạt tự nhiên và linh hoạt theo từng phác đồ.

**Future-State Flow** (mô tả bước bằng text-diagram, đánh dấu rõ):
* 🔵 **AI Step:** Tác vụ LLM xử lý.
* 🟢 **Human Step (HITL):** Bước con người phê duyệt/review.
* ↩️ **Fallback:** Kế hoạch dự phòng khi LLM trả về kết quả lỗi hoặc không tự tin.

```
1. Hệ thống HIS tự động lọc danh sách bệnh nhân mãn tính đến hạn tái khám/uống thuốc trong ngày.
        │
        ▼
2. 🔵 AI Step: LLM đọc phác đồ điều trị + lịch sử tái khám của từng bệnh nhân,
   soạn nội dung nhắc lịch/thuốc cá nhân hóa (giọng văn thân thiện, đúng thuật ngữ y khoa cơ bản).
        │
        ▼
3. 🟢 Human Step (HITL): Nếu nội dung nhắc có đề cập thay đổi thuốc/liều lượng
   hoặc AI tự đánh giá độ tin cậy thấp → điều dưỡng/bác sĩ phụ trách xem và duyệt trước khi gửi.
   Nếu nội dung chỉ là nhắc lịch thông thường, không đổi thuốc → gửi thẳng (không cần duyệt).
        │
        ▼
4. Hệ thống gửi nhắc lịch qua app/SMS cho bệnh nhân.
        │
        ▼
5. Theo dõi phản hồi/xác nhận của bệnh nhân trong 24h.
        │
        ├──> Bệnh nhân xác nhận/đặt lịch thành công → Kết thúc, cập nhật hồ sơ.
        │
        └──> ↩️ Fallback: Không phản hồi sau 24h, hoặc AI không tự tin khi soạn nội dung
             (VD: phác đồ phức tạp, bệnh nhân có tương tác thuốc đặc biệt)
             → Chuyển ca về hàng đợi cho nhân viên tổng đài gọi điện trực tiếp như quy trình cũ.
```

---

## 🏁 Phase 5 — EVALUATE

### AI Readiness Checklist:
1. [x] Chúng tôi có sẵn dữ liệu mẫu/logs sạch để test? — Có: hệ thống HIS của Vinmec đã lưu trữ phác đồ điều trị và lịch sử tái khám có cấu trúc, đủ để dùng làm input cho LLM và test prototype.
2. [x] Rủi ro khi AI sai có nằm trong tầm kiểm soát (qua HITL hoặc Fallback)? — Có: mọi nội dung liên quan thay đổi thuốc/liều lượng đều qua duyệt của điều dưỡng/bác sĩ (HITL); ca không phản hồi hoặc AI không tự tin sẽ fallback về gọi điện thủ công như quy trình cũ, không có bước nào AI tự quyết định hoàn toàn.
3. [ ] Stakeholders sẵn sàng thay đổi quy trình làm việc cũ? — Chưa chắc chắn: cần họp với đội tổng đài và ban điều dưỡng để xác nhận họ đồng thuận chuyển một phần công việc sang kênh app/SMS tự động, và đào tạo quy trình duyệt nội dung mới trước khi triển khai.

### Quyết định cuối cùng của Ban Giám Đốc Vin Smart Future:
[ ] **GO (Bắt đầu xây dựng Prototype):** Bắt đầu phát triển với scope hẹp.
[x] **NOT YET (Cần tích lũy thêm dữ liệu/xác lập baseline):** Trì hoãn để chuẩn bị thêm.
[ ] **NO-GO (Không khả thi / Rule-based tốt hơn):** Hủy bỏ dự án AI này.

**Justification (Lý giải quyết định dựa trên bằng chứng kỹ thuật và chi phí):**
> Về mặt kỹ thuật, dữ liệu và ranh giới an toàn (HITL + Fallback) đã đủ vững để bắt đầu xây dựng prototype ở quy mô hẹp (2/3 tiêu chí checklist đạt). Tuy nhiên, quyết định là **NOT YET** thay vì GO ngay, vì hai lý do: (1) chưa có baseline định lượng rõ ràng về tỷ lệ tái khám đúng hạn hiện tại theo từng bệnh viện/khoa để đo lường cải thiện sau khi triển khai — cần thu thập số liệu 2-4 tuần trước khi launch; (2) đội tổng đài và ban điều dưỡng — nhóm chịu ảnh hưởng trực tiếp nhất — chưa được khảo sát mức độ sẵn sàng thay đổi quy trình duyệt nội dung, và đây là rủi ro "người dùng không dùng" lớn hơn rủi ro kỹ thuật. Chi phí xây dựng prototype (1 LLM feature đơn giản, không cần agentic loop) thấp, nên việc trì hoãn 2-4 tuần để xác lập baseline và đồng thuận stakeholder là hợp lý hơn là triển khai vội và phải rollback.
