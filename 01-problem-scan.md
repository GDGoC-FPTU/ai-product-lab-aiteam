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
