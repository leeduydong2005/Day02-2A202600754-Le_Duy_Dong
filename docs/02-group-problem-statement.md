# 02 — Group Problem Statement

## Group convergence

Nhóm xem xét các vấn đề liên quan đến quản lý dự án phần mềm, báo cáo tiến độ, phát hiện blocker và tổng hợp thông tin từ nhiều nguồn. Các problem được gom thành 4 cụm chính.

| Cluster | Candidate examples | Pattern chung |
|---|---|---|
| Báo cáo / tổng hợp tiến độ | Project update, sprint report, weekly report | Gom thông tin từ nhiều nguồn rồi viết lại cho người khác đọc |
| Theo dõi task / blocker | Task trễ, blocker, dependency | Cần phát hiện sớm rủi ro ảnh hưởng deadline |
| Tìm kiếm thông tin cũ | Tìm quyết định trong chat, tìm context cũ | Thông tin nằm rải rác và khó truy xuất |
| Điều phối nhóm | Hỏi từng người, chuẩn bị daily, follow-up action item | Nhiều việc bị rơi nếu không theo dõi sát |

## Shortlist và score

| Candidate | Actor rõ | Workflow rõ | Pain có evidence | Impact đo được | Làm trong lab | So sánh R/W/A được | Nhóm hiểu domain | Tổng |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Tổng hợp tiến độ và phát hiện risk cho nhóm 15 người | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 34 |
| Tìm kiếm quyết định cũ trong tin nhắn nhóm | 4 | 4 | 4 | 4 | 3 | 4 | 4 | 27 |
| Tự động viết báo cáo sprint | 4 | 5 | 3 | 4 | 5 | 4 | 4 | 29 |

Nhóm chọn: **Tổng hợp tiến độ và phát hiện risk cho nhóm phần mềm 15 người**.

## Vì sao chọn

- Có actor rõ: trưởng nhóm phần mềm.
- Có workflow lặp lại hằng ngày/hằng tuần.
- Có bottleneck rõ: tổng hợp thông tin rời rạc và phát hiện rủi ro.
- Có metric đo được: thời gian tổng hợp, số lần hỏi lại, số blocker phát hiện muộn.
- Có thể so sánh Rule / Workflow / Agent rõ ràng.
- Có thể pilot nhỏ bằng dữ liệu giả lập hoặc dữ liệu của một sprint.

## Vì sao không chọn các bài khác

- Tìm kiếm quyết định cũ trong tin nhắn nhóm: impact rộng nhưng phụ thuộc nhiều vào quyền truy cập dữ liệu chat.
- Tự động viết báo cáo sprint: dễ làm hơn nhưng scope hơi hẹp, chưa giải quyết phần phát hiện blocker/risk.

## Quick validation

Nhóm có thể validate nhanh bằng cách hỏi 2–3 trưởng nhóm hoặc sinh viên từng làm leader đồ án phần mềm.

| Nguồn | Số người | Tín hiệu xác nhận | Tín hiệu phản bác | Nhóm sửa problem thế nào |
|---|---:|---|---|---|
| Quick interview | 3 | Trưởng nhóm thường phải hỏi lại thành viên và tổng hợp thủ công | Một số team nhỏ dùng board tốt nên ít đau hơn | Thu hẹp vào nhóm 15 người, nơi lượng task đủ lớn |
| Mini poll trong lớp | 6 | Nhiều bạn từng bị trễ báo cáo hoặc thiếu update | Một số nhóm chỉ cần template | Thêm non-AI alternative: checklist + dashboard |

## Insight sau validation

```text
Pain thật không chỉ nằm ở việc viết báo cáo. Pain chính nằm ở việc biến nhiều tín hiệu rời rạc từ task board, code, chat và update của thành viên thành một bức tranh tiến độ đủ rõ để trưởng nhóm ra quyết định.
```

## Workflow before/after

### Current State

```text
CURRENT STATE — khoảng 90 phút

[1 Xem Jira/Trello: 15']
→ [2 Đọc tin nhắn nhóm: 15']
→ [3 Hỏi từng thành viên: 20']
→ [4 Kiểm tra GitHub/PR: 15']
→ [5 Tổng hợp Done/Doing/Blocker: 15']  <-- bottleneck
→ [6 Phát hiện risk: 5']                <-- bottleneck
→ [7 Viết báo cáo: 5']
```

### Future State

```text
FUTURE STATE — khoảng 25–30 phút

[1 Thành viên cập nhật checklist: 5']    -- Rule
→ [2 Auto-pull task từ Jira/GitHub: 3']  -- Rule/script
→ [3 AI tổng hợp theo người/module: 2']  -- Workflow step
→ [4 AI phát hiện blocker/risk: 3']      -- Workflow step
→ [5 AI draft report: 2']                -- Workflow step
→ [6 Trưởng nhóm review + quyết định: 10–15']  -- Human boundary
```

Fallback:

```text
AI tổng hợp sai hoặc thiếu dữ liệu → trưởng nhóm kiểm tra lại nguồn gốc và sửa thủ công.
```

## Before/after impact

| Metric | Trước | Sau kỳ vọng | Ghi chú |
|---|---:|---:|---|
| Tổng thời gian | 90 phút | Dưới 30 phút | Target chính |
| Số bước | 7 | 6 | Không giảm quá nhiều bước, nhưng giảm effort ở bước tổng hợp |
| Bước thủ công | 7/7 | 2/6 | Trưởng nhóm vẫn review và gửi |
| Bottleneck chính | Tổng hợp tiến độ + phát hiện risk | Review/confirm | Human boundary |
| Risk mới | Không có AI hallucination | Có hallucination risk | Cần kiểm tra nguồn trước khi dùng |

## Problem Statement v1

| Field | Nội dung |
|---|---|
| Actor | Trưởng nhóm phần mềm quản lý 15 thành viên |
| Workflow | Xem Jira/Trello → đọc chat → hỏi thành viên → kiểm tra GitHub/PR → tổng hợp tiến độ → phát hiện risk → viết báo cáo |
| Bottleneck | Tổng hợp tiến độ và phát hiện rủi ro từ nhiều nguồn rời rạc |
| Impact | Khoảng 60–90 phút mỗi lần tổng hợp; dễ bỏ sót blocker hoặc phát hiện risk muộn |
| Success Metric | Giảm thời gian tổng hợp xuống dưới 30 phút; giảm số lần hỏi lại thành viên; giảm blocker phát hiện muộn |
| Boundary | AI không tự giao việc quan trọng, không tự đánh giá năng lực cá nhân, không tự gửi báo cáo |
| AI intervention point | Sau khi dữ liệu từ checklist/Jira/GitHub/chat được gom lại, trước bước trưởng nhóm viết báo cáo và ra quyết định |
| Mức chọn | Workflow |
| Rủi ro & người thật kiểm tra | Risk: AI bịa task, bỏ sót blocker, hiểu sai tiến độ. Người thật review: trưởng nhóm kiểm tra trước khi dùng |

## Final decision

Decision:

```text
Go với scope nhỏ.
```

Pilot nhỏ nhất:

- Dùng dữ liệu của 1 sprint hoặc 1 tuần gần nhất.
- Mỗi thành viên cập nhật 4 mục: done, doing, blocker, expected finish.
- AI tổng hợp thành báo cáo tiến độ.
- Trưởng nhóm đo thời gian review, số lỗi AI, số blocker bị bỏ sót.

Exit / rollback:

- Nếu trưởng nhóm vẫn phải sửa hơn 70% draft trong 2 tuần liên tiếp, hạ xuống checklist + dashboard.
- Nếu AI bịa task hoặc hiểu sai blocker nghiêm trọng, không dùng output trực tiếp trong báo cáo.
