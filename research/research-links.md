# Research Links

| Tool / Source | Họ giải quyết phần nào? | Điểm mạnh | Khoảng trống / rủi ro | Bài học cho nhóm |
|---|---|---|---|---|
| Jira Reports | Dashboard/report từ task và sprint data | Tốt cho structured task data | Không tự gom context từ chat/GitHub thành narrative đầy đủ | Rule/dashboard tốt cho dữ liệu task, chưa đủ cho risk summary |
| Trello Automation / Butler | Tự động hóa rule trên board/task | Dễ dùng, phù hợp rule đơn giản | Không phân tích blocker sâu | Rule hữu ích để chuẩn hóa workflow |
| GitHub Projects | Theo dõi issue, PR và milestone | Gắn trực tiếp với code và pull request | Không gom đầy đủ update từ chat hoặc meeting | Nên dùng làm một nguồn input |
| Slack AI / Microsoft Teams Copilot | Tóm tắt hội thoại và tìm thông tin | Tốt cho recap conversation | Chỉ xử lý một nguồn, cần kiểm soát dữ liệu | Có thể dùng output chat summary làm input cho workflow |
| Project management AI assistants | Hỗ trợ summary, status update, task tracking | Giúp giảm effort tổng hợp | Rủi ro hallucination nếu không có nguồn rõ | AI nên draft, người thật review |

## Research takeaway

```text
Không nên build một agent tự quản lý toàn bộ dự án ngay từ đầu. Hướng hợp lý hơn là Workflow: chuẩn hóa dữ liệu đầu vào bằng checklist/rule, dùng AI để tổng hợp tiến độ và phát hiện risk, sau đó trưởng nhóm review trước khi gửi báo cáo hoặc ra quyết định.
```
