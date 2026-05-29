# Sample AI Output

## 1. Blocker Risk Table

| Blocker | Evidence from input | Affected people/module | Dependency chain | Risk level | Suggested leader action | Needs confirmation |
|---|---|---|---|---|---|---|
| Login API response format chưa được xác nhận | Backend 1 chờ BA; Frontend 1 và QA 1 đều chờ response ổn định | Authentication: Backend, Frontend, QA | BA confirmation → Backend API → Frontend integration → QA integration test | High | Hỏi BA và Backend trong daily, chốt response format trong ngày | No |
| Payment API PR chưa được review | Backend 2 nói PR mở 2 ngày chưa review; QA 2 chưa bắt đầu vì API chưa merge | Payment: Backend, QA | PR review → API merge → QA test cases/run | Medium | Gán reviewer cụ thể và deadline review | No |
| User Profile ticket chưa cập nhật theo design mới | Frontend 2 nói design đổi trong chat; UI/UX nói đã share Figma nhưng ticket có thể chưa update | User Profile: Frontend, QA, UI/UX | Design update → Ticket update → Frontend implementation → QA validation | High | Yêu cầu BA hoặc UI/UX cập nhật ticket trước khi dev tiếp tục | Yes |

## 2. Hidden Dependency Notes

- Authentication module có dependency chain rõ: BA chưa confirm response format làm backend, frontend và QA cùng bị ảnh hưởng.
- Payment module bị chậm do PR review delay, không phải do implementation chính.
- User Profile có risk vì source of truth không rõ: design trong Figma/chat khác với ticket.

## 3. Questions for Daily Meeting

### Authentication
- BA cần bao lâu để chốt Login API response format?
- Backend và BA có thể chốt field ngay sau daily không?
- QA có thể chuẩn bị test bằng mock response tạm thời không?

### Payment
- Ai là reviewer chính cho Payment API PR?
- PR có issue kỹ thuật hay chỉ đang chờ review?
- QA có thể chuẩn bị test case trước khi API merge không?

### User Profile
- Ticket nào là source of truth: Figma, chat hay Jira/Trello?
- Ai sẽ cập nhật lại requirement trong ticket?
- Frontend có cần dừng task này cho đến khi ticket rõ không?

## 4. Escalation Candidates

| Candidate | Reason |
|---|---|
| Login API response confirmation | Có thể ảnh hưởng Authentication demo trong 4 ngày |
| User Profile ticket mismatch | Dev có thể làm sai requirement nếu không chốt lại |
