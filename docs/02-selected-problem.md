# 02 — Selected Problem

## Problem Card — Blocker & Dependency Triage

### Bài toán một câu

Trưởng nhóm phần mềm quản lý 15 người thường phát hiện blocker quá muộn vì tín hiệu về task bị kẹt, phụ thuộc giữa các thành viên và rủi ro deadline nằm rải rác trong task board, GitHub và tin nhắn nhóm.

### Actor

Trưởng nhóm phần mềm đang quản lý một team 15 người gồm backend, frontend, tester, UI/UX, BA và có thể có DevOps/support.

### Thời điểm / bối cảnh

Vấn đề xảy ra trước và trong daily meeting, sprint planning, sprint review hoặc khi deadline đang đến gần. Trưởng nhóm cần biết task nào đang bị block, ai đang chờ ai, module nào có risk và blocker nào cần xử lý trước.

### Current pain

Trong team 15 người, mỗi người thường có nhiều task. Một số task trông có vẻ đang tiến triển nhưng thực ra đang bị kẹt. Dấu hiệu blocker có thể nằm ở:

- Jira/Trello status.
- Comment trong task.
- Pull request chưa merge.
- Tin nhắn nhóm.
- Daily update.
- Requirement chưa được xác nhận.
- Design hoặc API chưa ổn định.

### Bottleneck

Trưởng nhóm phải tự đọc nhiều nguồn và tự suy luận dependency chain. Đây là bước tốn nhiều công sức nhất vì blocker không phải lúc nào cũng được ghi rõ là “blocked”.

### Impact

Nếu blocker bị phát hiện muộn:

- Một task có thể làm chậm nhiều task khác.
- Tester bị dồn việc cuối sprint.
- Frontend hoặc backend phải chờ nhau.
- Daily meeting chỉ trở thành buổi đọc status, không xử lý được vấn đề thật.
- Trưởng nhóm ra quyết định chậm.

### Success metric

| Metric | Baseline | Target |
|---|---:|---:|
| Thời gian chuẩn bị daily để tìm blocker | 45–60 phút | Dưới 15 phút |
| Số blocker phát hiện muộn | Cao | Giảm |
| Số câu hỏi cần hỏi lại trong daily | Nhiều | Giảm 50% |
| Số task In Progress lâu không có lý do | Khó biết | Được flag |
| Daily action item rõ ràng | Không ổn định | Có list trước daily |

### Boundary

AI chỉ hỗ trợ phát hiện và phân loại blocker. AI không tự đánh giá con người, không tự giao việc, không tự escalate và không tự ra quyết định thay trưởng nhóm.

### AI hypothesis

AI có thể gom các update rời rạc, nhận diện blocker, nhóm blocker theo module/dependency, đánh dấu mức độ ảnh hưởng và gợi ý câu hỏi trưởng nhóm nên hỏi trong daily meeting.

### Quick gut

Workflow.
