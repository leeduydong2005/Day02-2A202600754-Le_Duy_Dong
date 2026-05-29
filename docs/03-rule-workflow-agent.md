# 03 — Rule / Workflow / Agent

## Problem

Trưởng nhóm phần mềm quản lý 15 thành viên mất nhiều thời gian để tổng hợp tiến độ, phát hiện blocker và viết báo cáo vì thông tin nằm rải rác ở Jira/Trello, GitHub và tin nhắn nhóm.

## Rule

### Phương án

- Checklist cập nhật hằng ngày.
- Template báo cáo cố định.
- Dashboard Jira/Trello.
- Quy định deadline cập nhật trước daily/weekly meeting.

### Khi nào đủ

Rule đủ nếu:

- Team đã cập nhật task rất đều.
- Dashboard phản ánh đúng toàn bộ tiến độ.
- Báo cáo chỉ cần số liệu, không cần phân tích rủi ro hoặc narrative.

### Rủi ro / hạn chế

- Không xử lý tốt thông tin rời rạc trong chat.
- Không tự gom blocker theo module hoặc mức độ ảnh hưởng.
- Trưởng nhóm vẫn phải đọc và phân tích thủ công.
- Không giải quyết tốt phần phát hiện rủi ro sớm.

### Kết luận

Rule hữu ích cho bước chuẩn hóa dữ liệu đầu vào, nhưng chưa đủ để giải quyết toàn bộ bottleneck.

## Workflow

### Phương án

```text
Checklist/Jira/GitHub
→ AI tổng hợp theo người/module
→ AI phát hiện blocker/risk
→ AI draft report
→ Trưởng nhóm review và quyết định
```

### Khi nào phù hợp

Workflow phù hợp vì:

- Quy trình tương đối tuyến tính.
- Input có thể chuẩn hóa bằng checklist và task board.
- AI chỉ can thiệp vào các bước tổng hợp, phân loại, tóm tắt và draft.
- Trưởng nhóm vẫn kiểm tra trước khi dùng.
- Có thể pilot nhỏ trong 1 sprint.

### Rủi ro

- AI có thể bỏ sót task.
- AI có thể hiểu sai blocker.
- AI có thể tạo báo cáo chung chung.
- Dữ liệu đầu vào thiếu thì output cũng thiếu.

### Cách kiểm soát

- Bắt buộc AI chỉ dùng dữ liệu được cung cấp.
- Các mục thiếu thông tin phải đánh dấu “Needs confirmation”.
- Không cho AI xếp hạng năng lực cá nhân.
- Trưởng nhóm review trước khi gửi hoặc ra quyết định.

### Kết luận

Workflow là hướng phù hợp nhất cho bản đầu.

## Agent

### Phương án

Agent tự động:

- Đọc Jira/Trello.
- Đọc GitHub/PR.
- Đọc chat nhóm.
- Hỏi lại thành viên nếu thiếu thông tin.
- Phân tích risk.
- Đề xuất điều phối task.
- Gửi báo cáo.

### Khi nào phù hợp

Agent chỉ nên dùng khi:

- Có quyền truy cập dữ liệu rõ ràng.
- Có cơ chế kiểm soát hành động.
- Có logging và approval.
- Team đã có workflow ổn định.
- Risk của việc tự động hóa đã được đánh giá.

### Rủi ro

- Quá rộng cho bản đầu.
- Yêu cầu nhiều quyền truy cập.
- Dễ ảnh hưởng đến con người nếu agent đánh giá hoặc điều phối sai.
- Có rủi ro bảo mật dữ liệu dự án.
- Khó kiểm soát hallucination.

### Kết luận

Chưa chọn Agent cho scope hiện tại.

## Final choice

```text
Chọn Workflow.
```

## Decision rationale

- Rule đủ tốt cho phần chuẩn hóa dữ liệu, nhưng chưa đủ cho tổng hợp và phân tích rủi ro.
- Workflow giải quyết đúng bottleneck nhưng vẫn có human review.
- Agent quá rộng và nhiều rủi ro cho bản đầu.
- Bài toán cần AI ở một số bước cụ thể, không cần AI tự quản lý toàn bộ dự án.
