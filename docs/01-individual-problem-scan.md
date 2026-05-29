# 01 — Individual Problem Scan

## Scan rộng

| # | Lăng kính | Problem quan sát được | Ai đang đau? | Dấu hiệu thật |
|---|---|---|---|---|
| 1 | Tốn thời gian | Trưởng nhóm mất nhiều thời gian tổng hợp tiến độ từ 15 người | Trưởng nhóm | 60–90 phút mỗi lần tổng hợp |
| 2 | Lặp lại | Mỗi tuần phải viết báo cáo sprint/project update thủ công | Trưởng nhóm, PM, quản lý | Lặp lại hằng tuần |
| 3 | Pain từ người khác | Thành viên bị hỏi lại nhiều lần về task đang làm | Developer, Tester, UI/UX, BA | Thông tin update rời rạc |
| 4 | AI có thể tốt hơn | Khó phát hiện task có nguy cơ trễ deadline | Trưởng nhóm, quản lý | Blocker thường bị phát hiện muộn |
| 5 | Tốn thời gian | Phải đọc nhiều tin nhắn để tìm quyết định hoặc cập nhật cũ | Cả nhóm | Mất 10–15 phút/lần tìm |
| 6 | Lặp lại | Trưởng nhóm phải chuẩn bị câu hỏi cho daily/weekly meeting | Trưởng nhóm | Lặp lại theo chu kỳ |
| 7 | Tốn thời gian | Phải kiểm tra GitHub/PR để xác nhận task đã thật sự hoàn thành | Trưởng nhóm, reviewer | Nhiều task báo xong nhưng chưa merge |
| 8 | Pain từ người khác | Quản lý/khách hàng hỏi tiến độ nhưng báo cáo chưa sẵn | Quản lý, khách hàng, trưởng nhóm | Báo cáo dễ bị trễ |
| 9 | AI có thể tốt hơn | Khó gom blocker theo module và mức độ ảnh hưởng | Trưởng nhóm | Blocker nằm rải rác ở nhiều nguồn |
| 10 | Lặp lại | Tạo bản tổng hợp done/doing/blocker mỗi tuần | Trưởng nhóm | Format gần giống nhau mỗi tuần |

## Top 3

| Rank | Problem | Vì sao chọn | Điều còn chưa chắc |
|---|---|---|---|
| 1 | Tổng hợp tiến độ và phát hiện rủi ro của nhóm 15 người | Workflow rõ, impact lớn, đo được thời gian | Cần xác định nguồn dữ liệu nào khả dụng |
| 2 | Phát hiện blocker muộn | Pain thật, ảnh hưởng deadline | Khó đo chính xác nếu không có dữ liệu lịch sử |
| 3 | Viết báo cáo sprint/project update thủ công | Lặp lại, dễ dùng AI draft | Có thể chỉ cần template nếu dữ liệu đã rõ |

## Problem Card #1 — Project Progress & Risk Summary

### Bài toán một câu

Trưởng nhóm phần mềm đang quản lý 15 thành viên mất nhiều thời gian để tổng hợp tiến độ, phát hiện blocker và viết báo cáo vì thông tin nằm rải rác ở Jira/Trello, GitHub và tin nhắn nhóm.

### Actor

Trưởng nhóm phần mềm chịu trách nhiệm quản lý 15 thành viên trong dự án, bao gồm developer, tester, UI/UX và BA.

### Thời điểm / bối cảnh

Hằng ngày trước buổi daily meeting hoặc hằng tuần trước buổi sprint review/project update, trưởng nhóm cần nắm được ai đang làm gì, task nào đã xong, task nào bị trễ, blocker nào cần xử lý và rủi ro nào có thể ảnh hưởng deadline.

### Current workflow

```text
1. Mở Jira/Trello để xem danh sách task
2. Đọc tin nhắn nhóm trên Slack/Teams/Zalo
3. Hỏi từng thành viên về tiến độ nếu thông tin chưa rõ
4. Kiểm tra GitHub commit/pull request/file đã cập nhật
5. Tổng hợp task done/doing/blocker theo từng người
6. Phát hiện task trễ, blocker và rủi ro deadline
7. Viết báo cáo tiến độ cho quản lý hoặc khách hàng
```

### Bottleneck

Bước 5 và bước 6 — tổng hợp tiến độ và phát hiện rủi ro là bottleneck chính. Với 15 người, trưởng nhóm phải xử lý quá nhiều thông tin rời rạc, dễ bỏ sót task trễ hoặc blocker quan trọng.

### Impact

Nếu mỗi thành viên có khoảng 3–5 task đang mở, trưởng nhóm phải theo dõi khoảng 45–75 task cùng lúc. Việc kiểm tra thủ công có thể mất khoảng 60–90 phút mỗi lần tổng hợp, làm chậm quá trình ra quyết định và khiến một số rủi ro chỉ được phát hiện khi deadline đã gần.

### Success metric

Giảm thời gian tổng hợp tiến độ từ khoảng 90 phút xuống dưới 30 phút, giảm số lần phải hỏi lại thành viên và giảm số blocker bị phát hiện muộn.

### Non-AI alternative

Dùng checklist cập nhật hằng ngày, template báo cáo cố định và dashboard Jira/Trello. Cách này giúp chuẩn hóa dữ liệu nhưng chưa giải quyết tốt phần tổng hợp thông tin rời rạc và phát hiện rủi ro.

### AI hypothesis

AI có thể hỗ trợ gom task theo từng thành viên/module, tóm tắt blocker, phát hiện task trễ hoặc lâu chưa cập nhật, sau đó draft báo cáo tiến độ. Trưởng nhóm vẫn review, chỉnh sửa và quyết định cuối cùng.

### Quick gut

Workflow.
