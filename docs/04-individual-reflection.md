# 04 — Individual Reflection

## Đóng góp cá nhân

| Hoạt động | Tôi đã làm gì? | Kết quả |
|---|---|---|
| Problem scan | Đưa ra các vấn đề liên quan đến quản lý dự án phần mềm | Nhóm có nhiều candidate về reporting, task tracking và blocker |
| Pitch | Pitch vấn đề trưởng nhóm quản lý 15 người bị quá tải thông tin | Problem được chọn làm hướng chính |
| Challenge | Đặt câu hỏi liệu có cần Agent hay chỉ cần Workflow | Nhóm không chọn Agent quá sớm |
| Workflow | Vẽ current/future workflow | Nhóm nhìn rõ bottleneck ở bước tổng hợp tiến độ và phát hiện risk |
| Research | Tìm các tool/pattern liên quan đến Jira, Trello, GitHub, Slack/Teams AI | Nhóm thấy có thể dùng Rule + Workflow thay vì build agent |
| Rule / Workflow / Agent | Lập luận chọn Workflow | Nhóm thống nhất decision |

## Bảng dùng AI trong reflection

| Phase | Tôi dùng AI để làm gì? | AI hữu ích ở đâu? | AI sai/hời hợt ở đâu? | Tôi sửa gì |
|---|---|---|---|---|
| Scan | Gợi ý thêm problem theo vai trò trưởng nhóm phần mềm | Giúp mở rộng từ “viết báo cáo” sang “phát hiện blocker/risk” | Một số ý quá rộng như AI tự quản lý dự án | Thu hẹp scope vào tổng hợp tiến độ và phát hiện rủi ro |
| Workflow | Nhờ AI chuyển mô tả thành current/future workflow | Dễ thấy bottleneck và human boundary | AI ban đầu có xu hướng tự động hóa quá nhiều | Giữ lại bước trưởng nhóm review |
| Research | Gợi ý tool tương tự | Giúp thấy các pattern như dashboard, summary, automation | Một số claim thiếu nguồn | Chỉ giữ ý chung, không dùng số liệu chưa kiểm chứng |
| Problem Statement | Nhờ AI phản biện field mơ hồ | Chỉ ra success metric cần đo bằng thời gian và số lần hỏi lại | AI đề xuất Agent quá sớm | Hạ về Workflow |
| RWA Analysis | So sánh Rule / Workflow / Agent | Giúp lập luận rõ hơn | Agent bị mô tả hấp dẫn nhưng quá rủi ro | Chọn Workflow cho bản đầu |

## Bài học

- Problem tốt không phải problem nghe “AI” nhất, mà là problem có actor, workflow, bottleneck và metric rõ.
- Với nhóm 15 người, pain không chỉ là viết báo cáo mà là tổng hợp nhiều tín hiệu rời rạc thành một bức tranh tiến độ.
- Rule vẫn cần thiết để chuẩn hóa dữ liệu đầu vào.
- Workflow phù hợp hơn Agent vì quy trình có thể kiểm soát và vẫn giữ người thật review.
- Human boundary rất quan trọng vì AI không nên tự đánh giá năng lực cá nhân hoặc tự quyết định điều phối nhân sự.

## Nếu làm lại

Tôi sẽ validate với nhiều trưởng nhóm phần mềm hơn để có baseline chính xác hơn về thời gian tổng hợp tiến độ và số blocker bị phát hiện muộn. Tôi cũng sẽ thử pilot với dữ liệu của một sprint thật để đo AI giúp giảm thời gian bao nhiêu.
