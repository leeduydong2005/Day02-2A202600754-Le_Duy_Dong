# 05 — Rule / Workflow / Agent

## Rule

### Cách làm

- Bắt buộc mỗi thành viên điền daily update theo format:
  - Task đang làm.
  - Tiến độ.
  - Blocker.
  - Cần ai hỗ trợ.
  - Deadline.
- Dùng label "Blocked" trên Jira/Trello.
- Dùng dashboard cho task quá hạn.
- Dùng checklist trước daily.

### Khi nào đủ

Rule đủ nếu:

- Team cập nhật rất kỷ luật.
- Mọi blocker đều được ghi rõ.
- Dependency giữa task đơn giản.
- Team nhỏ.

### Hạn chế

Với team 15 người, blocker không phải lúc nào cũng được ghi rõ. Nhiều blocker chỉ xuất hiện gián tiếp trong chat/comment/PR. Rule giúp chuẩn hóa input nhưng chưa đủ để phát hiện blocker ẩn.

## Workflow

### Cách làm

```text
Daily update + task board + PR status
→ AI gom tín hiệu
→ AI phát hiện blocker
→ AI nhóm dependency
→ AI đánh dấu risk
→ Trưởng nhóm review và xử lý
```

### Vì sao phù hợp

- Có input rõ.
- Có các bước xử lý tuyến tính.
- AI xử lý phần tóm tắt, phân loại, phát hiện pattern.
- Trưởng nhóm vẫn quyết định cuối.
- Có thể pilot nhỏ trong 1 sprint.

### Rủi ro

- AI có thể hiểu nhầm update.
- AI có thể đánh dấu nhầm risk level.
- AI có thể bỏ sót blocker nếu input thiếu.
- AI có thể suy diễn quá mức.

### Kiểm soát

- AI phải ghi "Needs confirmation" nếu thiếu dữ liệu.
- AI không được tự bịa blocker.
- AI không được đánh giá năng lực cá nhân.
- Trưởng nhóm review trước khi hành động.

## Agent

### Cách làm

Agent tự:

- Đọc task board.
- Đọc GitHub.
- Đọc chat.
- Nhắn hỏi thành viên.
- Tự escalate blocker.
- Tự reassign task.

### Vì sao chưa chọn

Agent quá rủi ro trong bản đầu vì ảnh hưởng trực tiếp đến quản lý con người. Nếu agent hỏi sai, escalate sai hoặc reassign sai, nó có thể gây mất tin tưởng trong team.

## Decision

```text
Chọn Workflow.
```

## Decision Rationale

- Rule cần thiết nhưng chưa đủ.
- Workflow giải quyết đúng bottleneck: phát hiện blocker ẩn và dependency risk.
- Agent chưa phù hợp vì nhiều quyền truy cập và rủi ro quản lý con người.
