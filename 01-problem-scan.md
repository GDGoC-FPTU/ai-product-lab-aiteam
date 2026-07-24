# Phase 1 & 2 - Problem Scan and Quick Assessment


## Phase 1 - SCAN

| # | Subsidiary | Lens | Mo ta ngan bai toan |
|---|---|---|---|
| 1 | Vinhomes | Stakeholder Pain, Time-consuming | Phan anh khan cap cua cu dan nhu ket thang may, chap dien, mat nuoc bi mo ta bang ngon ngu tu do, nen nhan vien truc phai doc, danh gia muc do va chuyen tung ticket den dung bo phan. |
| 2 | Vinpearl | Stakeholder Pain, AI-upgrade | Review tieu cuc tren nhieu kenh bi phat hien cham; quan ly khong nhan ra som cac van de nhu phong ban, mat an toan thuc pham hoac thai do phuc vu de xu ly khi khach van dang luu tru. |
| 3 | VinFast | AI-upgrade, Time-consuming | Co van dich vu phai doc mo ta tieng Viet tu do cua khach hang, hoi lai nhieu lan va tu chon nhom ky thuat truoc khi dat lich kiem tra xe. |
| 4 | Xanh SM | Repetitive, Stakeholder Pain | Ghi chu va cuoc goi huy chuyen phai duoc nghe/doc thu cong de phan loai ly do, khien doi van hanh cham nhan ra diem don sai, tai xe tu choi hoac thoi gian cho qua lau. |
| 5 | VinUni | Repetitive, Time-consuming | Giang vien phai doc log autograder va viet lai phan hoi cho nhung loi lap lai, trong khi sinh vien can huong dan de hieu loi thay vi chi nhan ket qua pass/fail. |

## Tieu chi shortlist

Nhom cham moi bai toan theo thang 1-5:

| Tieu chi | Trong so |
|---|---:|
| Noi dau cua stakeholder ro va xay ra thuong xuyen | 30% |
| Co the mo ta current-state workflow va bottleneck | 20% |
| Co metric dinh luong de danh gia | 20% |
| Co the tao du lieu mau va prototype trong buoi lab | 20% |
| Ruil ro AI sai co the kiem soat bang HITL/fallback | 10% |

### Ket qua shortlist so bo

| Bai toan | Pain | Workflow | Metric | Prototype | Safety | Diem quy doi |
|---|---:|---:|---:|---:|---:|---:|
| Vinhomes - Phan loai phan anh khan cap | 5 | 5 | 5 | 5 | 4 | 4.9/5 |
| Vinpearl - Canh bao review nghiem trong | 4 | 4 | 4 | 5 | 4 | 4.2/5 |
| VinFast - Triage mo ta loi xe | 5 | 4 | 4 | 4 | 2 | 4.1/5 |
| Xanh SM - Phan tich huy chuyen | 4 | 4 | 4 | 3 | 5 | 3.9/5 |
| VinUni - Draft phan hoi autograder | 3 | 5 | 4 | 5 | 5 | 4.2/5 |

## Phase 2 - QUICK-ASSESS

## Quick Problem Card #1 - De xuat chon

**Bai toan (1 cau):** Ho tro nhan vien truc Vinhomes phan loai, danh gia muc
do khan cap va draft noi dung chuyen xu ly cho phan anh cua cu dan.

**Cong ty thanh vien:** Vinhomes

**Ai dang dau (Actor)?**

- Cu dan dang gap su co nhung khong biet lien he bo phan nao.
- Nhan vien truc CSKH/Ban quan ly phai doc tung phan anh va tu quyet dinh uu tien.
- Doi ky thuat nhan ticket cham hoac thieu thong tin quan trong.

**Workflow thu cong hien tai:**

1. Cu dan gui noi dung tu do qua app/hotline.
2. Nhan vien truc doc, hoi lai toa/can ho va tinh trang su co.
3. Nhan vien tu danh gia muc do va chon bo phan phu trach.
4. Ticket duoc chuyen cho ky thuat/an ninh/ve sinh.
5. Bo phan xu ly lien he lai cu dan neu ticket thieu thong tin.

**Bottleneck:** Buoc 2-3, uoc tinh 5-8 phut/ticket. Ticket viet mo ho co the
bi chuyen sai bo phan hoac khong duoc nhan la khan cap.

**AI ho tro o dau?** AI trich xuat loai su co, dia diem, muc do khan, thong
tin con thieu; sau do draft nhan phan loai va bo phan tiep nhan. Nhan vien
van la nguoi phe duyet.

**Metric thanh cong (baseline can xac minh):**

- Giam thoi gian triage trung vi tu 6 phut xuong duoi 90 giay/ticket.
- It nhat 90% ticket duoc de xuat dung bo phan tren bo test da gan nhan.
- Recall cua nhom su co khan cap dat it nhat 95%.
- 100% ticket nguy hiem co canh bao va bat buoc con nguoi phe duyet.

**Quick Architecture:** LLM Feature + rule an toan + Human-in-the-loop.

**Operational boundary so bo:**

- AI chi duoc draft nhan va goi y tuyen xu ly, khong tu dong dong ticket.
- AI khong tu dua ra huong dan ky thuat ve dien, chay no, y te hay cuu ho.
- Cac tu khoa nguy hiem nhu "khoi", "chay", "mui gas", "ket thang may",
  "bat tinh" phai kich hoat rule uu tien P0 va chuyen ngay cho nguoi truc.
- Neu do tin cay thap hoac thieu toa/can ho, he thong phai yeu cau bo sung
  thong tin, khong duoc tu suy dien.

## Quick Problem Card #2

**Bai toan (1 cau):** Phat hien va tom tat review Vinpearl co dau hieu nghiem
trong de quan ly phan hoi khi khach van con dang luu tru.

**Cong ty thanh vien:** Vinpearl

**Ai dang dau (Actor)?** Khach dang gap trai nghiem xau; Guest Relations va
Duty Manager phai theo doi nhieu kenh review.

**Workflow thu cong hien tai:**

1. Nhan vien mo tung kenh review.
2. Doc va loc review tieu cuc.
3. Xac dinh co so, phong, chu de va muc do nghiem trong.
4. Gui noi dung cho quan ly phu trach.
5. Quan ly draft phan hoi va giao bo phan xu ly.

**Bottleneck:** Buoc 1-3, uoc tinh 8-12 phut/review va co nguy co bo sot review
ngoai gio lam viec.

**AI ho tro o dau?** Phan loai chu de, tom tat van de, phat hien dau hieu khan
cap va draft phan hoi noi bo.

**Metric thanh cong (baseline can xac minh):**

- 90% review tieu cuc duoc phan loai trong duoi 2 phut ke tu khi nhan du lieu.
- Recall it nhat 95% voi review lien quan an toan, ve sinh va suc khoe.
- Giam thoi gian tong hop thu cong tu 10 phut xuong duoi 2 phut/review.

**Quick Architecture:** LLM Feature; Rule cho tu khoa nghiem trong.

## Quick Problem Card #3

**Bai toan (1 cau):** Draft phan hoi de hieu tu log autograder de sinh vien
biet vi sao code sai va buoc tiep theo can kiem tra gi.

**Cong ty thanh vien:** VinUni

**Ai dang dau (Actor)?** Sinh vien chi nhan log ky thuat kho hieu; tro giang
lap lai viec giai thich cung mot nhom loi.

**Workflow thu cong hien tai:**

1. Sinh vien nop bai va autograder chay test.
2. Sinh vien nhan stack trace/ket qua pass-fail.
3. Sinh vien gui cau hoi cho tro giang.
4. Tro giang doc code va log.
5. Tro giang viet goi y sua loi.

**Bottleneck:** Buoc 3-5, uoc tinh 10-15 phut/yeu cau vao gio cao diem.

**AI ho tro o dau?** Tom tat log, phan loai loi va draft goi y theo kieu
Socratic, khong dua dap an hoan chinh.

**Metric thanh cong (baseline can xac minh):**

- Draft phan hoi duoc tao trong duoi 20 giay.
- It nhat 85% phan hoi duoc tro giang danh gia la dung nhom loi va huu ich.
- 100% phan hoi khong tiet lo solution/reference answer.

**Quick Architecture:** LLM Feature + bo loc noi dung + Human-in-the-loop.

## De xuat quyet dinh

Chon **Quick Problem Card #1 - Phan loai phan anh khan cap Vinhomes** de
Deep-Dive va lam prompt prototype.

Ly do:

1. Cham vao pain point truc tiep: trong luc cu dan dang lo lang vi su co,
   viec bi hoi lai nhieu lan hoac chuyen sai bo phan lam giam niem tin.
2. AI co loi the that su voi ngon ngu tu do, tieng Viet khong dau, viet tat
   va noi dung mo ho; rule-based don thuan kho bao phu het cach dien dat.
3. Pham vi prototype vua suc: input la noi dung ticket, output JSON gom
   category, priority, missing_fields, target_team va draft_summary.
4. Ruil ro co the kiem soat bang rule uu tien, HITL va fallback ve quy trinh
   thu cong.
5. Du lieu test co the tao gia lap ma khong can truy cap du lieu ca nhan that.

## Ke hoach khao sat nhanh truoc khi Deep-Dive

1. Phong van 2-3 nguoi tung gui phan anh tai khu dan cu ve thoi gian cho,
   so lan bi hoi lai va ket qua chuyen xu ly.
2. Phong van gia lap/role-play voi 1 nguoi dong vai nhan vien truc de ve lai
   quy trinh va xac dinh thong tin bat buoc cua moi ticket.
3. Tao bo 30 ticket gia lap: 10 thong thuong, 10 khan cap, 5 mo ho va 5 prompt
   co tinh du AI bo qua quy tac.
4. Gan nhan thu cong category, priority va target_team de lam ground truth.
5. Chay prototype, lap confusion matrix va ghi lai false negative o nhom khan
   cap; neu recall P0 duoi 95% thi quyet dinh NOT YET.
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
