# 01 — Problem Scan

## Scan rộng

| # | Lens | Problem quan sát được | Ai đang đau? | Dấu hiệu thật |
|---|---|---|---|---|
| 1 | Hidden work | Task bị kẹt nhưng vẫn để In Progress | Trưởng nhóm, developer | Daily mới phát hiện ra |
| 2 | Dependency | Frontend chờ API backend nhưng board không thể hiện rõ | Frontend, backend, QA | Task bị trễ dây chuyền |
| 3 | Communication gap | Requirement đổi trong chat nhưng ticket chưa cập nhật | BA, dev, tester | Dev làm theo thông tin cũ |
| 4 | Review delay | Pull request bị chờ review quá lâu | Developer, reviewer | Task sau không thể bắt đầu |
| 5 | Testing delay | Tester chờ build hoặc test data | Tester, dev | QA bị dồn việc cuối sprint |
| 6 | Repeated question | Trưởng nhóm hỏi lại nhiều người cùng một thông tin | Trưởng nhóm, thành viên | Daily kéo dài |
| 7 | Risk detection | Rủi ro deadline chỉ rõ khi sprint gần kết thúc | Trưởng nhóm, quản lý | Không kịp điều chỉnh |
| 8 | Context scattered | Blocker nằm trong Jira comment, chat, PR, meeting note | Cả team | Không có một nơi tổng hợp |
| 9 | Priority confusion | Nhiều blocker nhưng không biết cái nào xử lý trước | Trưởng nhóm | Escalate sai thứ tự |
| 10 | Action tracking | Sau daily có action item nhưng dễ bị quên | Trưởng nhóm, assignee | Blocker lặp lại hôm sau |

## Top 3

| Rank | Problem | Vì sao chọn | Điều còn chưa chắc |
|---|---|---|---|
| 1 | Phát hiện blocker ẩn và dependency risk | Khác biệt, pain rõ với team 15 người, AI có ích | Cần input đủ tốt |
| 2 | Pull request review delay | Dễ đo, có data từ GitHub | Scope hơi hẹp |
| 3 | Requirement thay đổi nhưng ticket không cập nhật | Ảnh hưởng lớn đến dev/test | Khó thu thập dữ liệu nếu chỉ dùng chat |

## Selected Problem

Nhóm chọn problem số 1:

> Trưởng nhóm phần mềm quản lý 15 người thường phát hiện blocker quá muộn vì tín hiệu về task bị kẹt, phụ thuộc chéo và rủi ro deadline nằm rải rác trong task board, GitHub và tin nhắn nhóm.

## Vì sao đây là problem tốt

- Có actor cụ thể.
- Có workflow lặp lại trong mỗi daily/sprint.
- Có pain thật: blocker bị phát hiện muộn.
- Có impact đến deadline.
- Có thể đo bằng thời gian chuẩn bị daily, số blocker phát hiện muộn, số lần hỏi lại.
- Có thể so sánh Rule / Workflow / Agent.
- Không trùng bản chất với case weekly report.
