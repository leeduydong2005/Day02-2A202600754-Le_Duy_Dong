# 01 — Individual Problem Scan

## Mục tiêu

Phần này dùng để quét các vấn đề thực tế trước khi chọn một vấn đề chính. Trọng tâm không phải là nghĩ ngay đến giải pháp AI, mà là tìm ra workflow nào đang có pain rõ, lặp lại và đo được.

## Scan rộng

| # | Lăng kính          | Problem name                      | Problem quan sát được                                                  | Ai đang đau?                 | Dấu hiệu thật                                  |
| - | ------------------ | --------------------------------- | ---------------------------------------------------------------------- | ---------------------------- | ---------------------------------------------- |
| 1 | Tốn thời gian      | **Progress Tracking Overload**    | Trưởng nhóm phải hỏi nhiều người để nắm tiến độ dự án                  | Trưởng nhóm                  | Mất nhiều thời gian trước daily/weekly meeting |
| 2 | Lặp lại            | **Repeated Status Compilation**   | Mỗi ngày/tuần đều phải tổng hợp task done/doing/blocker                | Trưởng nhóm                  | Lặp lại theo sprint hoặc theo ngày             |
| 3 | Pain từ người khác | **Unclear Member Updates**        | Thành viên bị hỏi lại vì update chưa rõ                                | Developer, Tester, BA, UI/UX | Thông tin tiến độ rời rạc                      |
| 4 | Tốn thời gian      | **Scattered Project Information** | Trưởng nhóm phải kiểm tra task board, GitHub và tin nhắn nhóm          | Trưởng nhóm                  | Thông tin nằm ở nhiều nguồn                    |
| 5 | Rủi ro             | **Late Blocker Detection**        | Blocker bị phát hiện muộn, làm ảnh hưởng deadline                      | Cả team                      | Task bị trễ dây chuyền                         |
| 6 | AI có thể hỗ trợ   | **Task Delay Risk Detection**     | Khó nhận ra task nào đang có nguy cơ trễ                               | Trưởng nhóm                  | Một số task In Progress quá lâu                |
| 7 | Điều phối          | **Team Dependency Confusion**     | Khó biết ai đang chờ ai trong nhóm 15 người                            | Trưởng nhóm, thành viên      | Có dependency giữa frontend, backend, QA, BA   |
| 8 | Báo cáo            | **Manual Project Reporting**      | Khi quản lý hỏi tình trạng dự án, trưởng nhóm phải tổng hợp lại từ đầu | Trưởng nhóm, quản lý         | Báo cáo chưa sẵn hoặc thiếu context            |

## Top 3 Problems

| Rank | Problem name                   | Problem                                                       | Vì sao chọn                                                      | Điều còn chưa chắc                    |
| ---- | ------------------------------ | ------------------------------------------------------------- | ---------------------------------------------------------------- | ------------------------------------- |
| 1    | **Progress & Blocker Summary** | Trưởng nhóm khó tổng hợp tiến độ và blocker của team 15 người | Actor rõ, workflow lặp lại, impact lớn, có thể đo bằng thời gian | Cần xác định nguồn dữ liệu cụ thể     |
| 2    | **Late Blocker Detection**     | Blocker bị phát hiện muộn                                     | Ảnh hưởng trực tiếp deadline                                     | Cần có ví dụ thực tế để chứng minh    |
| 3    | **Scattered Team Updates**     | Thành viên update rời rạc khiến daily meeting kéo dài         | Pain xảy ra thường xuyên                                         | Có thể chỉ cần checklist nếu team nhỏ |

## Problem được chọn

**Problem name:** **Progress & Blocker Summary**

**Problem statement:**
Trưởng nhóm phần mềm quản lý 15 người mất nhiều thời gian để tổng hợp tiến độ, phát hiện blocker và xác định rủi ro dự án vì thông tin nằm rải rác ở nhiều nguồn như task board, GitHub và tin nhắn nhóm.

## Actor

Trưởng nhóm phần mềm quản lý một team khoảng 15 người, gồm developer, tester, BA, UI/UX và các vai trò hỗ trợ khác.

## Bối cảnh

Trước daily meeting, weekly meeting hoặc sprint review, trưởng nhóm cần biết:

* Ai đang làm task nào.
* Task nào đã xong.
* Task nào đang bị chậm.
* Thành viên nào đang gặp blocker.
* Module nào có nguy cơ ảnh hưởng deadline.
* Việc nào cần follow-up ngay.

## Current workflow

```text
1. Mở task board để xem trạng thái task
2. Đọc tin nhắn nhóm để tìm update mới
3. Kiểm tra GitHub/PR để xem task kỹ thuật đã tiến triển chưa
4. Hỏi lại từng thành viên nếu thông tin chưa rõ
5. Tổng hợp done / doing / blocker
6. Xác định task trễ và rủi ro deadline
7. Chuẩn bị nội dung cho daily/weekly meeting
```

## Bottleneck

Bottleneck nằm ở bước tổng hợp và xác định rủi ro. Với team 15 người, thông tin bị phân tán ở nhiều nguồn, khiến trưởng nhóm phải tự ghép các mảnh thông tin nhỏ để hiểu tình trạng thật của dự án.

## Impact

Nếu mỗi thành viên có 3–5 task đang mở, trưởng nhóm có thể phải theo dõi khoảng 45–75 task cùng lúc. Việc kiểm tra thủ công dễ làm mất thời gian, bỏ sót blocker và phát hiện rủi ro muộn.

## Success metric

| Metric                            |      Trước |     Sau kỳ vọng |
| --------------------------------- | ---------: | --------------: |
| Thời gian chuẩn bị update tiến độ | 60–90 phút |    Dưới 30 phút |
| Số nguồn phải đọc thủ công        |  3–4 nguồn |  1 bản tổng hợp |
| Số lần phải hỏi lại thành viên    |      Nhiều | Giảm khoảng 50% |
| Blocker phát hiện muộn            |         Có |            Giảm |

## Non-AI alternative

Có thể dùng checklist cập nhật hằng ngày, template meeting và dashboard task board. Cách này giúp chuẩn hóa dữ liệu nhưng chưa giải quyết tốt việc tổng hợp thông tin từ nhiều nguồn và phát hiện rủi ro sớm.

## AI hypothesis

AI có thể hỗ trợ gom thông tin tiến độ, phân loại task theo người/module, phát hiện dấu hiệu blocker hoặc task có nguy cơ trễ, sau đó tạo bản tổng hợp ngắn để trưởng nhóm review trước meeting.

## Phán đoán ban đầu

**Workflow.**

Vấn đề này phù hợp với hướng workflow vì có quy trình lặp lại rõ ràng: thu thập thông tin, tổng hợp tiến độ, phát hiện blocker, đánh giá rủi ro và chuẩn bị báo cáo trước meeting. AI không cần thay thế trưởng nhóm, mà đóng vai trò hỗ trợ tổng hợp và cảnh báo để trưởng nhóm ra quyết định nhanh hơn.
