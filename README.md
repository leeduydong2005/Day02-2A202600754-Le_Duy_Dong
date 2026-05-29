# AI-assisted Project Progress & Risk Summary for a 15-person Software Team

## 1. Project Overview

Dự án này đề xuất một workflow sử dụng AI để hỗ trợ trưởng nhóm phần mềm quản lý tiến độ của một nhóm 15 người. Vấn đề chính không phải là thay thế trưởng nhóm, mà là giảm thời gian tổng hợp thông tin, phát hiện blocker và chuẩn bị báo cáo tiến độ.

## 2. Problem Statement

Một trưởng nhóm phần mềm đang quản lý 15 thành viên thường phải theo dõi nhiều task, nhiều nguồn thông tin và nhiều blocker cùng lúc. Thông tin tiến độ thường nằm rải rác ở Jira/Trello, GitHub, tin nhắn nhóm và các buổi họp daily/weekly.

Điều này khiến trưởng nhóm mất nhiều thời gian để tổng hợp tiến độ, phát hiện rủi ro và viết báo cáo cho quản lý hoặc khách hàng.

## 3. Actor

Trưởng nhóm phần mềm chịu trách nhiệm:

* Theo dõi tiến độ của 15 thành viên.
* Kiểm tra task đang làm, task đã hoàn thành và task bị trễ.
* Phát hiện blocker hoặc rủi ro ảnh hưởng deadline.
* Tổng hợp báo cáo tiến độ cho quản lý hoặc khách hàng.
* Điều phối công việc trong nhóm.

## 4. Current Workflow

```text
CURRENT STATE — khoảng 90 phút

[1 Mở Jira/Trello xem task: 15']
→ [2 Đọc tin nhắn nhóm/Zalo/Slack/Teams: 15']
→ [3 Hỏi từng thành viên về tiến độ: 20']
→ [4 Kiểm tra GitHub/commit/file nộp: 15']
→ [5 Tổng hợp task done/doing/blocker: 15']
→ [6 Viết báo cáo/risk update: 10']
```

## 5. Bottleneck

Bottleneck chính nằm ở bước tổng hợp và phân tích tiến độ. Trưởng nhóm phải tự đọc nhiều nguồn thông tin khác nhau, hỏi lại từng thành viên và xác định thủ công task nào đang trễ, ai đang bị block, module nào có nguy cơ ảnh hưởng deadline.

## 6. Impact

Với nhóm 15 người, nếu mỗi người có 3–5 task đang mở, trưởng nhóm có thể phải theo dõi khoảng 45–75 task cùng lúc. Việc kiểm tra thủ công làm mất nhiều thời gian, dễ bỏ sót blocker và khiến rủi ro chỉ được phát hiện khi deadline đã gần.

## 7. Success Metrics

| Metric                         |      Trước |     Sau kỳ vọng |
| ------------------------------ | ---------: | --------------: |
| Thời gian tổng hợp tiến độ     |    90 phút |    Dưới 30 phút |
| Số nguồn phải đọc thủ công     |  3–4 nguồn |  1 bản tổng hợp |
| Số lần phải hỏi lại thành viên |        Cao | Giảm khoảng 50% |
| Blocker phát hiện muộn         |         Có |            Giảm |
| Thời gian viết báo cáo         | 20–30 phút |       5–10 phút |

## 8. Proposed Future Workflow

```text
FUTURE STATE — khoảng 25–30 phút

[1 Thành viên cập nhật task theo form/checklist: 5']
→ [2 Script/API lấy task từ Jira/Trello/GitHub: 3']
→ [3 AI gom thông tin theo từng người/module: 2']
→ [4 AI phát hiện task trễ, blocker, risk: 3']
→ [5 AI draft báo cáo tiến độ: 2']
→ [6 Trưởng nhóm review, sửa, quyết định: 10–15']
```

## 9. AI Intervention Point

AI được dùng ở các bước:

* Tổng hợp task theo thành viên, module và trạng thái.
* Phát hiện task trễ, task lâu chưa cập nhật hoặc có phụ thuộc nguy hiểm.
* Tóm tắt blocker từ update của thành viên.
* Draft báo cáo tiến độ theo format cố định.
* Gợi ý câu hỏi trưởng nhóm nên hỏi trong buổi daily/weekly meeting.

AI không tự gửi báo cáo, không tự đánh giá năng lực thành viên và không tự ra quyết định điều phối nhân sự.

## 10. Rule / Workflow / Agent Comparison

| Mức      | Phương án                                                                                      | Khi nào phù hợp                                               | Rủi ro                                                 | Quyết định    |
| -------- | ---------------------------------------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------ | ------------- |
| Rule     | Checklist, template báo cáo, dashboard Jira                                                    | Phù hợp để chuẩn hóa dữ liệu đầu vào                          | Không giải quyết tốt phần tổng hợp và phân tích rủi ro | Dùng một phần |
| Workflow | Checklist/Jira/GitHub → AI tổng hợp → AI phát hiện risk → AI draft report → trưởng nhóm review | Phù hợp vì quy trình tuyến tính và có người kiểm tra cuối     | AI có thể hiểu sai hoặc bỏ sót thông tin               | Chọn          |
| Agent    | Agent tự đọc task, tự hỏi thành viên, tự đánh giá tiến độ, tự điều phối công việc              | Chỉ phù hợp khi hệ thống trưởng thành và có quyền truy cập rõ | Quá rộng, rủi ro cao, dễ ảnh hưởng con người           | Chưa chọn     |

## 11. Final Decision

Chọn hướng Workflow.

Lý do:

* Problem có actor rõ.
* Workflow hiện tại có bottleneck cụ thể.
* Có thể đo hiệu quả bằng thời gian, số blocker và số lần hỏi lại.
* AI chỉ hỗ trợ tổng hợp, phát hiện rủi ro và draft báo cáo.
* Trưởng nhóm vẫn là người review và quyết định cuối.

## 12. Smallest Pilot

Pilot nhỏ nhất:

* Chọn dữ liệu của 1 sprint hoặc 1 tuần gần nhất.
* Mỗi thành viên cập nhật 4 mục:

  1. Task đã làm.
  2. Task đang làm.
  3. Blocker.
  4. Dự kiến hoàn thành.
* AI tổng hợp thành báo cáo tiến độ.
* Trưởng nhóm kiểm tra:

  * Thời gian tổng hợp có giảm không.
  * AI có bỏ sót task hoặc blocker không.
  * Báo cáo có dùng được sau khi edit không.

## 13. Risks and Controls

| Rủi ro                                | Cách kiểm soát                                                   |
| ------------------------------------- | ---------------------------------------------------------------- |
| AI bịa task hoặc blocker              | Chỉ cho AI dùng dữ liệu được cung cấp                            |
| AI hiểu sai tiến độ                   | Trưởng nhóm review trước khi gửi                                 |
| Thành viên cập nhật thiếu             | Dùng checklist bắt buộc trước daily/weekly                       |
| AI đánh giá con người thiếu công bằng | Không dùng AI để xếp hạng năng lực cá nhân                       |
| Báo cáo quá chung chung               | Dùng format cố định: Done / Doing / Blocker / Risk / Next action |

## 14. Repository Structure

```text
docs/
  01-individual-problem-scan.md
  02-group-problem-statement.md
  03-rule-workflow-agent.md
  04-individual-reflection.md

assets/
  current-workflow.png
  future-workflow.png

research/
  research-links.md

prompts/
  ai-draft-report-prompt.md
```
