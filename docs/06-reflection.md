# 06 — Individual Reflection

## My Contribution

| Hoạt động | Tôi đã làm gì? | Kết quả |
|---|---|---|
| Problem scan | Tìm các vấn đề trong quản lý team phần mềm 15 người | Nhận ra blocker/dependency là pain khác với weekly report |
| Problem framing | Thu hẹp từ “AI quản lý dự án” thành “AI hỗ trợ phát hiện blocker ẩn” | Problem cụ thể hơn, dễ đo hơn |
| Workflow design | Vẽ current/future flow cho blocker triage | Thấy rõ bottleneck nằm ở dependency reasoning |
| RWA analysis | So sánh Rule / Workflow / Agent | Chọn Workflow thay vì Agent |
| Prompt design | Viết prompt để AI tạo blocker risk table | Có thể pilot bằng dữ liệu mẫu |
| Example design | Tạo sample input/output | Bài giống mini prototype hơn là mô tả chung chung |

## How I Used AI

| Phase | Tôi dùng AI để làm gì? | AI hữu ích ở đâu? | AI sai/hời hợt ở đâu? | Tôi sửa gì |
|---|---|---|---|---|
| Ideation | Gợi ý hướng từ case trưởng nhóm 15 người | Giúp mở nhiều hướng như report, risk, blocker | Ban đầu giống case weekly report | Đổi trọng tâm sang blocker/dependency |
| Problem Statement | Nhờ AI viết lại problem cụ thể | Giúp rõ actor, context, impact | Một số câu còn chung chung | Thêm ví dụ Frontend chờ API, PR chờ review |
| Workflow | Nhờ AI tách current/future flow | Dễ thấy bước AI can thiệp | AI có xu hướng tự động hóa quá nhiều | Giữ human boundary |
| Prompt | Nhờ AI tạo prompt blocker triage | Có format rõ | Cần thêm rule chống bịa và không đánh giá cá nhân | Bổ sung constraints |
| Reflection | Nhờ AI gợi ý cách trình bày | Có cấu trúc hơn | Cần viết lại theo trải nghiệm của nhóm | Cá nhân hóa nội dung |

## Lessons Learned

- Không nên bê nguyên case mẫu rồi thay tên actor.
- Một problem tốt cần khác biệt ở bottleneck, không chỉ khác ở nhân vật.
- Với team 15 người, pain lớn không phải chỉ là viết báo cáo mà là phát hiện blocker và dependency ẩn.
- Rule giúp chuẩn hóa input nhưng không đủ để suy luận dependency.
- Workflow là lựa chọn hợp lý vì AI hỗ trợ phân tích, còn trưởng nhóm vẫn quyết định.
- Agent không nên dùng sớm khi hành động của AI có thể ảnh hưởng đến con người.

## If I did it again

Tôi sẽ phỏng vấn thêm 2–3 trưởng nhóm phần mềm để kiểm tra xem blocker thường bị phát hiện muộn ở nguồn nào: task board, chat, GitHub hay daily meeting. Tôi cũng sẽ thử chạy prompt với dữ liệu một sprint thật để đo số blocker AI phát hiện đúng.
