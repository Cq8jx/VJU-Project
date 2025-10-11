---
id: GUIDE-GWS-AND-GEMINI-USAGE-GUIDE-VIETNAMESE
title: Cẩm nang sử dụng GWS/Gemini (Tiếng Việt)
issuer: Trường Đại học Việt Nhật
category: Guide
issue_date: null
status: active
languages:
- vi
source_pdf: ''
replaces: []
replaced_by: []
revision_history: []
tags:
- guide
---
# Cẩm nang sử dụng GWS/Gemini (Tiếng Việt)

Tài liệu này dành cho giảng viên và nhân viên trong trường đại học nhằm khai thác có hệ thống Google Workspace (GWS), họ dịch vụ AI sinh Gemini, cùng các công nghệ liên quan như Apps Script, Retrieval-Augmented Generation (RAG) và Multi-Channel Processing (MCP). Đi theo từng chương từ chia sẻ tệp cơ bản đến tự động hóa nâng cao, bạn có thể nắm được cách thiết lập môi trường, vận hành hàng ngày và quản trị theo từng bước.

---

## Lời mở đầu

Chương này liệt kê các dịch vụ và chức năng chính được đề cập, giúp bạn định hướng khi đọc. Chi tiết sẽ được giải thích ở các chương tiếp theo.

Tài liệu cũng giới thiệu các trường hợp sử dụng điển hình, kèm quy trình và lưu ý cụ thể trong từng chương liên quan.

1. **Tự động hóa biên bản cho họp kết hợp:** Ghi hình cuộc họp bằng Google Meet, lưu vào Drive, dùng Gemini để phiên âm và tóm tắt, sắp xếp hành động bằng Apps Script và chia sẻ trong Shared Drive.
2. **Liên kết thời gian thực giữa học liệu và bài làm của sinh viên:** Phát phiếu bài tập bằng Google Slides, cho phép sinh viên cùng viết trong một bộ slide, sau khi nộp dùng Gemini tóm tắt ý chính và trực quan hóa mức độ hiểu bài trên Google Sheets.
3. **Xây dựng kho tri thức cho dự án nghiên cứu:** Tổ chức tài liệu trên Shared Drive và Google Sites, nạp vào NotebookLM để so sánh tài liệu và tạo FAQ, kết hợp RAG để trả lời kèm trích dẫn nguồn mới nhất.
4. **Trợ lý số cho công việc thường nhật:** Tận dụng Gemini CLI để thiết lập và xử lý sự cố máy tính, máy in, tự động tải và cài ứng dụng, chỉnh sửa tệp nội bộ, phát hiện tệp không cần thiết và giải phóng dung lượng.

### Google Workspace (Chương 1)
- Google Groups: Trung tâm hóa liên lạc dạng mailing list và diễn đàn.
- Shared Drives: Lưu trữ thuộc sở hữu tổ chức, giải thích khác biệt với My Drive và quyền truy cập.
- Google Docs: Đồng biên tập thời gian thực, mẫu tài liệu và bình luận chia sẻ.
- Google Sheets: Chia sẻ và phân tích dữ liệu, pivot table, quản lý quyền.
- Google Slides: Soạn giáo trình, tài liệu họp chung, quản lý template.
- Google Forms: Thu thập đăng ký, khảo sát và tự động tổng hợp.
- Google Calendar: Lịch chia sẻ và quản lý tài nguyên.
- Google Meet: Họp trực tuyến, ghi hình và phụ đề.
- Google Sites: Công bố cẩm nang, cổng thông tin với kiểm soát truy cập.

### AI sinh (Chương 2)
- Gemini (Web): AI đối thoại trên trình duyệt cho soạn thảo, tóm tắt, dịch thuật.
- Google Notebook (NotebookLM): Nạp tài liệu để tóm tắt và hỏi đáp trong giao diện notebook.
- Google AI Studio: Môi trường thử nghiệm API Gemini, thiết kế prompt và quản lý mẫu.
- Gemini CLI: Công cụ dòng lệnh xử lý hàng loạt và tích hợp script với Gemini API.

### GAS và công nghệ liên kết (Chương 3)
- Google Apps Script (GAS): Tự động hóa GWS bằng JavaScript, quản lý phiên bản qua clasp.
- RAG (Retrieval-Augmented Generation): Kỹ thuật kết hợp tìm kiếm nội bộ với sinh nội dung.
- MCP (Multi-Channel Processing): Quy trình tích hợp văn bản, âm thanh, hình ảnh.

## Chương 1: Khai thác Google Workspace

Chương này hướng dẫn tối ưu hiệu suất và cộng tác bằng tính năng chuẩn của GWS mà không cần AI. Vì hoạt động trên đám mây, người dùng luôn truy cập thông tin mới nhất từ mọi nơi, mọi thiết bị.

### 1.1 Giao tiếp tổ chức với Google Groups
- **Tổng quan:** Google Groups đóng vai trò mailing list, diễn đàn và hộp thư chung, tập trung liên lạc theo khoa, ủy ban, dự án. Chủ đề có thể xem trên web ngoài email.
- **Liên kết dịch vụ khác:** Gắn địa chỉ nhóm vào lịch Google Calendar và Shared Drive để lịch, tài liệu, nhiệm vụ tự đồng bộ khi thành viên thay đổi.
- **Quản lý thành viên:** Quản trị viên thêm bớt theo vai trò, cập nhật hàng loạt khi điều chuyển hoặc nhập học. Nhóm động gắn theo đơn vị tổ chức giúp tự bảo trì và đồng bộ quyền Shared Drive, Calendar theo thao tác thành viên.
- **Hộp thư chung:** Bật collaborative inbox để phân công và theo dõi ticket — giống quy trình bộ phận hỗ trợ khách hàng hay help desk doanh nghiệp — giúp cả nhóm xử lý câu hỏi từ sinh viên và cán bộ.
- **Tình huống sử dụng:** Thông báo môn học, thông tin toàn trường, biên bản ủy ban, cộng tác nghiên cứu, hỏi đáp dự án sinh viên.
- **Lưu trữ:** Bài viết lưu trong kho tìm kiếm được, hỗ trợ bàn giao, kiểm toán và chia sẻ tri thức; email cá nhân xóa vẫn còn trong nhóm.
- **Kiểm duyệt:** Thiết lập phê duyệt, lọc spam, giữ lại theo từ khóa để đảm bảo chất lượng thông tin; hữu ích khi dùng làm diễn đàn hỏi đáp.
- **Tùy chọn thông báo:** Thành viên chọn nhận toàn bộ, bản tin tổng hợp hoặc tắt, tránh quá tải nhưng vẫn theo dõi thông tin thiết yếu.
- **Nhãn và phân loại:** Gán nhãn, phân mục để tìm kiếm nhanh và xây dựng thư viện FAQ.
- **Báo cáo:** Dùng bảng điều khiển quản trị Workspace xem log truy cập, báo cáo kiểm toán, phát hiện truy cập trái phép hoặc rò rỉ dữ liệu.
- **Bảo mật:** Cấp quyền chi tiết cho thành viên ngoài (chỉ xem, không đăng), bật phê duyệt hai bước hoặc thiết lập hết hạn cho nội dung nhạy cảm.
- **Tham khảo:** [Quản lý Google Groups (Google Groups Help)](https://support.google.com/groups?hl=ja)

### 1.2 Chia sẻ tệp và vận hành Shared Drive
- **Sở hữu tập thể vs. My Drive:** My Drive thuộc cá nhân, dễ thất lạc khi nghỉ việc; Shared Drive thuộc tổ chức, chuyển giao thuận lợi.
- **Đồng biên tập thời gian thực:** Nhiều người chỉnh sửa qua web hoặc di động mà không xung đột, lịch sử phiên bản cho phép khôi phục.
- **Log truy cập và kiểm toán:** Theo dõi xem/chỉnh/sửa quyền để kiểm soát nội bộ và ngăn rò rỉ; có thể tích hợp SIEM.
- **Cấu trúc thư mục chuẩn:** Đặt hệ thống ví dụ “00_Template”, “01_In Progress”, “10_Published”, “99_Archive” để nhóm liên phòng dễ tìm tài liệu.
- **Metadata và đặt tên:** Chuẩn hóa tên tệp (ví dụ “YYYYMMDD_DonVi_LoaiVanBan_Phiên”) và ghi tác giả, ngày cập nhật để thuận tiện tìm kiếm/kiểm tra.
- **Mẫu quyền và gán tự động:** Tạo bộ quyền (chỉ xem, nhận xét, chỉnh sửa, quản lý) và gán theo Google Group để giảm công sức quản trị.
- **Quản lý vòng đời:** Thể hiện trạng thái (đang soạn → phát hành → lưu trữ) bằng thư mục và rà soát định kỳ để tối ưu dung lượng.
- **Cộng tác bên ngoài:** Cấp quyền khách có thời hạn, hạn chế tải xuống; hết dự án tự thu hồi và lưu log.
- **Lưu trữ và khôi phục:** Shared Drive cho phép khôi phục trong 30 ngày; kết hợp Vault hoặc sao lưu dài hạn/eDiscovery.
- **Quản trị và đào tạo:** Văn bản hóa chính sách chia sẻ, bảo mật, tài liệu đào tạo, FAQ, checklist để bảo đảm tuân thủ.
- **Tham khảo:** [Tổng quan Shared Drive](https://support.google.com/a/answer/7212025?hl=ja), [Quản lý Shared Drive](https://support.google.com/a/answer/7281227?hl=ja)

### 1.3 Soạn thảo với Google Docs
- **Đồng biên tập:** Nhiều người chỉnh cùng lúc mà không xung đột; bình luận và chế độ gợi ý giúp minh bạch quyết định.
- **Mẫu tài liệu:** Lưu syllabus, biên bản họp, đơn từ vào Shared Drive để tái sử dụng nhanh.
- **Bố cục tab:** Khối xây dựng như trang/tab giúp tách buổi học, chủ đề, đơn vị.
- **Dịch tài liệu:** “Công cụ > Dịch tài liệu” tạo bản dịch riêng cho tài liệu đa ngữ hoặc họp quốc tế.
- **Lịch sử phiên bản:** Theo dõi phiên bản theo thời gian, so sánh hoặc khôi phục, hỗ trợ quy trình phê duyệt và lưu vết.
- **Bình luận & giao việc:** @nhắc tên để thông báo email và giao việc tự động, đẩy nhanh hiệu đính, phê duyệt.
- **Nhập liệu bằng giọng nói & khả năng truy cập:** Tăng tốc ghi chép bài giảng, xây dựng giáo trình dễ tiếp cận.
- **Smart Chip:** Chèn tệp, lịch, thông tin người dùng từ Drive để truy cập nhanh.
- **Quy trình phê duyệt:** “Tệp > Yêu cầu phê duyệt” cho phép chọn người duyệt, hạn chót, ghi chú; thao tác một cú nhấp để duyệt hoặc yêu cầu sửa, lưu lịch sử và nhắc hạn.
- **Tự động hóa:** Apps Script/add-on dựng nội dung mẫu, tạo tài liệu từ phản hồi biểu mẫu.
- **Tham khảo:** [Giới thiệu Google Docs](https://support.google.com/docs?hl=ja#topic=1382883), [Khối xây dựng như bảng tab](https://support.google.com/docs/answer/12112505?hl=ja)

### 1.4 Chia sẻ dữ liệu bằng Google Sheets
- **Dữ liệu thời gian thực:** Theo dõi điểm danh, ngân sách, danh sách sinh viên luôn cập nhật; lịch sử phiên bản lưu vết chỉnh sửa.
- **Đồng biên tập:** Giáo vụ, giảng viên, văn phòng làm việc song song; bình luận ghi lại thảo luận.
- **Phân tích:** Bộ lọc, pivot, Explore, biểu đồ trực quan.
- **Định dạng có điều kiện:** Tự tô màu giá trị vượt ngưỡng để phát hiện bất thường.
- **Xác thực dữ liệu:** Dropdown, regex kiểm soát nhập liệu, hạn chế sai sót/ trùng lặp.
- **Liên kết & tự động hóa:** Kết nối Form, Apps Script, Looker Studio để tổng hợp, thông báo, lập báo cáo tự động.
- **Hàm nhập:** Đồng bộ CSV, sheet ngoài, API (`IMPORTRANGE`, `IMPORTDATA`).
- **Tích hợp Shared Drive:** Lưu trong Shared Drive để quyền gắn theo nhóm; thành viên rời đi quyền cũng cập nhật.
- **Ứng dụng:** Mô phỏng ngân sách, tư vấn nghề nghiệp, khảo sát lớp, điều chỉnh thời khóa biểu.
- **Kiểm toán & bảo vệ:** Khóa ô, bảo vệ phạm vi, bật email thông báo thay đổi cho dữ liệu quan trọng.
- **Tham khảo:** [Giới thiệu Google Sheets](https://support.google.com/sheets?hl=ja#topic=2811806)

### 1.5 Quản lý lớp và họp với Google Slides
- **Đồng biên tập:** Sinh viên làm việc đồng thời trên các slide; giảng viên phản hồi theo thời gian thực.
- **Template & Master:** Gắn template toàn khoa trong master để thống nhất màu thương hiệu, logo, font; cập nhật tự động.
- **Phát hành & chia sẻ:** Công bố web, PDF, liên kết xem để cung cấp phiên bản mới nhất cho sinh viên/đối tác.
- **Ghi chú diễn giả:** Thêm giải thích, tài liệu tham khảo vào phần ghi chú để dùng làm tài liệu tự học/biên bản.
- **Bình luận & Q&A:** Thu thập câu hỏi, xử lý Q&A ngay trên slide.
- **Chèn đa phương tiện:** Nhúng video, âm thanh, smart chip để trình bày thí nghiệm, nghiên cứu tình huống.
- **Lịch sử phiên bản:** Lưu và so sánh phiên bản cũ cho từng năm học.
- **Quyền truy cập:** Thiết lập xem/nhận xét/chỉnh sửa, khóa chỉ xem khi cần bảo mật.
- **Hỗ trợ trình bày:** Dùng presenter view, con trỏ laser, phụ đề trực tiếp cho lớp online/hybrid.
- **Tự động hóa:** Apps Script/add-on dựng slide, dịch, chèn sơ đồ tự động.
- **Tham khảo:** [Giới thiệu Google Slides](https://support.google.com/slides?hl=ja#topic=9054607)

### 1.6 Thu thập thông tin với Google Forms
- **Tổng hợp tức thời:** Câu trả lời cập nhật Sheets theo thời gian thực, theo dõi tiến độ và gửi thông báo tự động.
- **Đăng ký & xin phép:** Dùng cho đăng ký tập huấn, đặt phòng, đánh giá môn học, đặt lịch tư vấn, sự kiện.
- **Rẽ nhánh:** Hiển thị câu hỏi phù hợp theo câu trả lời.
- **Hướng dẫn & kiểm tra:** Giới hạn nhập, gợi ý, thanh tiến độ giúp giảm lỗi, tăng tỷ lệ hoàn thành.
- **Tải tệp:** Nhận bài tập hoặc chứng từ trực tiếp vào Drive.
- **Thông báo & phê duyệt:** Kết hợp thông báo email, Apps Script và mẫu Gmail để xây dựng quy trình phê duyệt. Add-on như Form Approvals giúp thông báo tự động khi nhận đơn xin làm việc từ xa và cho phép quản lý bấm nút duyệt/ từ chối ngay trong email.
- **Đa ngôn ngữ:** Tách section hoặc dùng nhiều form để hỗ trợ song ngữ Nhật-Anh cho sinh viên quốc tế.
- **Chủ đề tùy chỉnh:** Gắn màu, logo trường để tăng độ tin cậy.
- **Chế độ công bố:** Giới hạn nội bộ, người có link, hay Q&A công khai tùy mục đích.
- **Phân tích:** Dùng Looker Studio hoặc Apps Script tạo dashboard chia sẻ ngay cho lãnh đạo.
- **Tham khảo:** [Giới thiệu Google Forms](https://support.google.com/docs/topic/6063584?hl=ja)

### 1.7 Lên lịch với Google Calendar
- **Lịch chung:** Quản lý họp, lớp, hạn chót để mọi người nắm lịch mới nhất.
- **Time slot đặt lịch:** Công bố khung giờ tư vấn, mượn thiết bị để người đăng ký chọn thời điểm trống.
- **Thư mời & đính kèm:** Gắn tài liệu Drive, liên kết liên quan vào lời mời để chuẩn bị trước.
- **Nhắc việc:** Kết hợp email, pop-up, thông báo di động để tránh bỏ sót.
- **Quyền truy cập:** Thiết lập chỉ xem, xem chi tiết, chỉnh sửa, quản trị theo vai trò.
- **Múi giờ:** Hiển thị nhiều múi giờ cho họp quốc tế.
- **Theo dõi tham dự:** Xem phản hồi RSVP trong Calendar, tự gửi email nhắc người vắng.
- **Đặt tài nguyên:** Đăng ký phòng họp, lớp học, thiết bị làm tài nguyên để xem lịch trống. Tại màn hình chỉnh sự kiện, chọn “Tùy chọn khác”, tìm phòng trong mục “Thêm phòng hoặc địa điểm”, hệ thống hiển thị giờ rảnh và cảnh báo nếu trùng. Đặt lịch định kỳ bằng chế độ lặp và ghi chú mục đích, bố trí trong phần mô tả.
- **Chồng lịch:** Xếp chồng lịch cá nhân/khoa/toàn trường và dùng màu phát hiện xung đột.
- **Lịch sử:** Kiểm tra ai chỉnh sự kiện và khi nào.
- **Tham khảo:** [Cơ bản Google Calendar](https://support.google.com/calendar?hl=ja#topic=10509771)

### 1.8 Họp trực tuyến với Google Meet
- **Tạo cuộc họp:** Kết hợp Calendar để tạo liên kết Meet và chia sẻ tự động.
- **Tương đồng với Zoom:** Hầu hết tính năng Zoom đang dùng — chia sẻ màn hình, ghi hình, breakout room, khảo sát — đều có trên Google Meet. Với tài khoản GWS của trường, bạn không cần đăng ký hay trả phí mới.
- **Ghi hình & chia sẻ:** Tự ghi vào Drive cho người vắng hoặc làm biên bản.
- **Phụ đề & dịch:** Cung cấp phụ đề và dịch đa ngôn ngữ, tăng khả năng tiếp cận.
- **Breakout room:** Tạo phòng thảo luận nhóm nhỏ cho lớp học, workshop.
- **Khảo sát & Q&A:** Thu phản hồi theo thời gian thực.
- **Bảng trắng:** Chia sẻ Google Slides như bảng trắng để cùng động não.
- **Bảo mật:** Phòng chờ, giới hạn tham gia, khử ồn, làm mờ nền nâng cao trải nghiệm.
- **Thiết bị:** Kết hợp Meet hardware, thiết bị di động cho lớp/họp hybrid.
- **Truyền trực tiếp:** Phát trực tiếp tới tối đa 100.000 người và lưu lại.
- **Tự động hóa:** Apps Script hoặc CLI lấy log điểm danh, tạo mẫu biên bản tự động.
- **Tham khảo:** [Tổng quan Google Meet](https://support.google.com/meet?hl=ja)

### 1.9 Google Sites và vận hành cổng thông tin
- **Cổng nội bộ:** Kết hợp tài liệu môn học, thủ tục, FAQ để thống nhất luồng thông tin.
- **Quyền truy cập:** Thiết lập nội bộ, theo khoa, công khai tùy độ nhạy cảm.
- **Template:** Dùng mẫu chung để chuẩn hóa thương hiệu, rút ngắn thời gian dựng site.
- **Chỉnh sửa trực quan:** Kéo thả bố cục, hình ảnh, nội dung dễ dàng.
- **Tích hợp Drive:** Nhúng Docs, Sheets, Slides, Forms luôn hiển thị bản mới nhất.
- **Điều hướng:** Cấu trúc trang, mục lục, tìm kiếm giúp truy cập nhanh.
- **Responsive:** Tự thích ứng PC, tablet, smartphone.
- **Tham khảo:** [Giới thiệu Google Sites](https://support.google.com/sites?hl=ja#topic=7184583)

---

## Chương 2: Khai thác AI sinh (Gemini và hơn thế nữa)

Chương này trình bày cách dùng dịch vụ Gemini của Google để hỗ trợ soạn thảo, phân tích và phát triển ứng dụng. Mỗi dịch vụ gồm tổng quan, bước khởi động, trường hợp sử dụng và ví dụ prompt.

Với dịch vụ Gemini thuộc môi trường Google Workspace của VJU, hợp đồng đảm bảo nội dung bạn nhập **không** được dùng lại làm dữ liệu huấn luyện của Google. Khi đăng nhập bằng tài khoản trường, prompt được xử lý trong môi trường riêng của tổ chức và không phản hồi vào quá trình huấn luyện mô hình.

### 2.1 Nguyên tắc sử dụng AI sinh
1. **Nêu rõ mục tiêu và ràng buộc:** Prompt cần mục đích, đối tượng, định dạng đầu ra, điều cấm.
2. **Chia nhỏ yêu cầu:** Tách nhiệm vụ lớn thành bước nhỏ để tăng độ chính xác.
3. **Quy trình kiểm tra:** Luôn rà soát kết quả, kiểm chứng trích dẫn, số liệu, tính tuân thủ.
4. **Bảo mật:** Ẩn danh hoặc tóm tắt dữ liệu cá nhân, nghiên cứu chưa công bố trước khi gửi AI.
5. **Phân loại dữ liệu:** Xác định mức độ nhạy cảm và phạm vi dữ liệu được phép dùng.
6. **Quản lý prompt:** Ghi lại prompt thành công/thất bại để chia sẻ kinh nghiệm và cải tiến.
7. **Human-in-the-loop:** Con người quyết định cuối cùng với nhiệm vụ quan trọng, AI chỉ hỗ trợ.
8. **Thử nghiệm pilot:** Chạy PoC quy mô nhỏ, kiểm chứng KPI và rủi ro rồi mới nhân rộng.
9. **Quyền và đạo đức:** Xem xét bản quyền, đạo đức nghiên cứu, bias; xây dựng và phổ biến chính sách.
10. **Học liên tục:** Phân tích log, phản hồi và cập nhật prompt, tài liệu đào tạo.

Ghi chép tài liệu, prompt dưới dạng Markdown — định dạng văn bản dễ đọc và thân thiện với AI — giúp quản lý phiên bản, tái sử dụng và tích hợp vào NotebookLM hoặc luồng RAG thuận tiện.

- **Tham khảo:** [Thực hành an toàn với AI sinh (Google AI Docs)](https://ai.google.dev/docs/safety?hl=ja)

### 2.2 Gemini (Web)
**Tổng quan:** AI đối thoại trên trình duyệt phục vụ soạn thảo, dịch, tóm tắt, gợi ý ý tưởng và nhiều hơn nữa.

**Bước khởi động:**
1. Đăng nhập Gemini bằng tài khoản Google (https://gemini.google.com/).
2. Đọc điều khoản sử dụng và chính sách dữ liệu.
3. Nếu cần, yêu cầu quản trị cấp license Gemini for Workspace.

**Trường hợp sử dụng:**
- Thiết kế đề cương bài giảng, bố cục syllabus, mục tiêu học tập.
- Điều chỉnh ngữ điệu email cho sinh viên, phụ huynh, bản tin nội bộ.
- Tóm tắt biên bản họp, trích xuất hành động, soạn email nhắc việc.
- Tải lên đề cương nghiên cứu, đơn xin tài trợ để nhận phản hồi về cấu trúc, phương pháp.
- Soạn bản nháp đề xuất nội bộ, bảo đảm tuân theo mẫu các hồ sơ đã được phê duyệt.
- Kiểm tra lỗi bất cẩn trong bộ hồ sơ (chính tả, thiếu mục, sai định dạng) và nhận gợi ý sửa.
- Kết nối với Gmail, Google Calendar, Google Drive để tóm tắt hộp thư, gợi ý trả lời, sắp xếp tài liệu và điều phối lịch hẹn trong một quy trình.
- Tạo tình huống học tập, câu hỏi thảo luận, bài tập.
- Sinh danh mục tài liệu tham khảo và từ khóa liên quan.
- Dịch và điều chỉnh tài liệu cho sinh viên quốc tế.
- Soạn template FAQ và kịch bản chatbot.
- Tạo và chia sẻ Gem (prompt công khai) đã nạp sẵn quy chế tuyển sinh/học bổng để trả lời đúng quy định; câu hỏi ngoài phạm vi sẽ được hướng dẫn liên hệ bộ phận phụ trách.
- Soạn phản hồi hỗ trợ sinh viên và mẫu email.
- Tóm tắt văn bản hành chính, so sánh phiên bản quy định.

**Ví dụ prompt:**
- **Tham khảo:** [Gemini (Google Help Center)](https://support.google.com/gemini?hl=ja)
```
Mục tiêu: Soạn kịch bản 90 phút cho buổi định hướng tân sinh viên.
Hướng dẫn:
- Cấu trúc gồm: mở đầu, tham quan campus, giải thích hệ thống đăng ký học phần, hỏi đáp.
- Liệt kê người phụ trách, tài liệu cần dùng, câu hỏi dự kiến cho từng phần.
- Đề xuất hoạt động ice-breaker đầu buổi để giảm căng thẳng.
```

```
Mục tiêu: Xây dựng tình huống cho workshop đạo đức nghiên cứu.
Hướng dẫn:
- Đưa ra kịch bản nghiên cứu lâm sàng cho học viên cao học khối STEM.
- Bao gồm bối cảnh, vấn đề, điểm cần thảo luận, tài liệu tham khảo.
- Chuẩn bị ba câu hỏi để người tham gia trao đổi.
```

```
Mục tiêu: Nhận phản hồi cho đề cương nghiên cứu (PDF) đính kèm.
Hướng dẫn:
- Đọc mục tiêu, phương pháp, tiến độ trong tệp và liệt kê điểm mạnh/yếu.
- Đánh giá ngắn gọn mức độ mới so với các nghiên cứu hiện hữu.
- Chỉ ra dữ liệu, quy trình kiểm chứng, yếu tố đạo đức còn thiếu.
- Chốt lại ba hạng mục cần sửa gấp trong lần cập nhật kế tiếp.
```

```
Mục tiêu: Phát hiện lỗi bất cẩn trong bộ hồ sơ nộp kèm.
Hướng dẫn:
- Liệt kê lỗi chính tả, mục trống (ngày tháng, họ tên...), phần sai định dạng.
- Đề xuất cách sửa và lý do cho từng lỗi, gắn mức ưu tiên Cao/Trung Bình/Thấp.
- Nếu mục bắt buộc bị bỏ trống, gợi ý nội dung mẫu phù hợp.
```

```
Mục tiêu: Soạn bản nháp đề xuất nội bộ dựa trên các mẫu đã được thông qua.
Hướng dẫn:
- Đọc các PDF trong thư mục “Reference Proposals” đính kèm và tóm tắt cấu trúc, giọng văn chung.
- Soạn đề xuất với chủ đề năm nay “Cải tiến chương trình đào tạo qua hợp tác vùng – doanh nghiệp”, theo thứ tự: tổng quan, mục tiêu, kế hoạch hoạt động, chỉ số đánh giá, ngân sách.
- Ghi chú phần nào tham khảo mẫu cũ và liệt kê thông tin bổ sung còn thiếu.
```

```
Mục tiêu: Tổng hợp việc cần làm trên Gmail, Calendar, Drive.
Hướng dẫn:
- Tóm tắt các thư Gmail gắn nhãn “Research Grant” trong 7 ngày qua và chỉ ra thư nào cần phản hồi.
- Xem thư mục Google Drive “/Grants/2025”, trích ý chính của 3 tài liệu cập nhật gần nhất và liệt kê nhiệm vụ chưa hoàn tất.
- Kiểm tra Google Calendar, đề xuất 3 khoảng thời gian trống trong tuần tới và soạn câu trả lời email gợi ý các khung giờ này.
```

### 2.3 Google Notebook (NotebookLM)
**Tổng quan:** AI dạng notebook nạp tài liệu (Docs, PDF, Slides...), hỗ trợ tối đa 50 nguồn, hiểu tài liệu chính xác và quản lý tri thức qua đối thoại.

**Trường hợp sử dụng:**
- Sinh câu hỏi kiểm tra từ toàn bộ syllabus cho bài tập và ôn tập.
- So sánh bài báo nghiên cứu theo mục tiêu, phương pháp, kết quả, thách thức.
- Phân loại báo cáo sinh viên theo rubric và đề xuất cải thiện.
- Trích luận điểm và quyết định từ biên bản ủy ban, văn bản chính sách.
- Tóm tắt báo cáo khảo sát kèm điểm nhấn, trích dẫn để chuẩn bị trình bày.
- Đăng ký PDF tham khảo và trích xuất từ khóa, chủ đề nổi bật.
- Tạo danh sách từ vựng, bài điền khuyết, tình huống hội thoại từ tài nguyên ngôn ngữ.
- Phân tích quy chế trường để xác định phạm vi sửa đổi, khác biệt.
- Gom nhóm ý kiến trả lời tự do trong khảo sát, đề xuất cải tiến sơ bộ.
- Tổng hợp tài liệu dự án, tóm tắt tiến độ, rủi ro, hành động tiếp theo.
- **Tham khảo:** [NotebookLM overview](https://support.google.com/notebooklm?hl=ja)

**Ví dụ prompt:**
```
Mục tiêu: Tóm tắt “Đề án cải cách chương trình 2024.pdf” và rút ra điểm cần thảo luận.
Hướng dẫn:
- Mỗi chương tóm tắt ≤200 ký tự.
- Liệt kê ba tác động tới sinh viên và ba hạng mục giảng viên cần chuẩn bị.
```

```
Mục tiêu: Tạo câu hỏi ôn tập cho Tuần 8.
Hướng dẫn:
- Dựa trên slide và tài liệu phát tay đã nạp, tạo ba câu trắc nghiệm và hai câu tự luận.
- Kèm đáp án và giải thích cho từng câu.
```

### 2.4 Google AI Studio
**Tổng quan:** Môi trường trình duyệt thử nghiệm Gemini API. Hỗ trợ thiết kế prompt, quản lý few-shot, cấp API key và kiểm chứng quy trình xử lý nhiều loại tệp — PDF, âm thanh, hình ảnh — để đánh giá độ chính xác khi chuyển thành văn bản hoặc tóm tắt.

**Bước khởi động:**
1. Truy cập Google AI Studio, tạo dự án mới.
2. Chọn mô hình (ví dụ Gemini 1.5 Pro) và định dạng phản hồi (text/JSON).
3. Thiết lập chỉ dẫn hệ thống, mẫu vào/ra để tinh chỉnh kết quả.
4. Tạo API key và tích hợp với Apps Script hay ứng dụng ngoài.
- **Tham khảo:** [Google AI Studio](https://ai.google.dev/aistudio?hl=ja)

**Ý tưởng ứng dụng:**
- Dựng nhanh chatbot FAQ, kênh trả lời thắc mắc.
- Thử nghiệm công cụ tóm tắt dữ liệu nghiên cứu trước khi nối với Apps Script.
- So sánh prompt nhằm đánh giá chỉ dẫn, nhiệt độ.
- Định nghĩa mẫu phản hồi JSON cho tích hợp hệ thống.
- Chia sẻ dự án cho đồng đội tái hiện kết quả với cấu hình giống nhau.
- Làm sandbox đào tạo trợ giảng, thực hành thiết kế prompt.
- Cấp API key chạy batch, kết hợp Apps Script/CLI để thử nghiệm.
- Lập bảng đánh giá chất lượng để so sánh phiên bản mô hình.
- Kiểm tra log, lỗi để nhận diện rủi ro quản trị.
- Thử prompt đa ngôn ngữ, đa phương thức cho kế hoạch mở rộng.
- Tải lên PDF, âm thanh, hình ảnh để chuyển văn bản hoặc tóm tắt, tự động hóa bước chuẩn bị tài liệu và biên bản.

### 2.5 Gemini CLI
**Tổng quan:** Công cụ dòng lệnh làm việc với Gemini API, mạnh về xử lý batch và workflow script, đồng thời kết hợp thao tác tệp và cấu hình thiết bị cục bộ.

**Bước khởi động:**
1. Cài Node.js bản LTS. Tải trình cài “LTS” từ trang chính thức (https://nodejs.org/ja) và làm theo hướng dẫn. Sau khi cài, chạy `node -v` và `npm -v` để xác nhận.
2. Cài CLI: `npm install -g @google/gemini-cli`.
3. Đăng nhập bằng `gemini login`.
4. Sử dụng các lệnh như `gemini prompt`, `gemini models list`.

**Trường hợp sử dụng:**
- Đặt cron dịch/tóm tắt định kỳ và lưu vào Drive.
- Đọc/ghi tệp cục bộ để tổ chức, chuyển đổi định dạng, sao lưu tự động.
- Script tải và cài phần mềm, tự động thiết lập đa số ứng dụng.
- Phân tích CSV, JSON để tạo báo cáo tóm tắt, dashboard.
- Quản lý phiên bản prompt tùy chỉnh trong repo để tái sử dụng.
- Tự động tiền xử lý dữ liệu nghiên cứu (mô tả cột, thống kê, phát hiện bất thường).
- Kiểm tra lỗi bất cẩn của tài liệu, bảng tính, cẩm nang trước khi nộp và trích xuất đề xuất sửa.
- Xử lý hàng loạt abstract để trích từ khóa, phân loại.
- Tạo template đề thi, bài tập với nhiều biến thể.
- Kết hợp công cụ workflow, shell script chạy batch ban đêm.
- Gửi kết quả CLI tới Slack/Chat webhook để thông báo nhóm.
- Hỗ trợ giải đáp vấn đề PC — cài đặt máy in, cập nhật driver, sự cố mạng.
- Tạo dữ liệu giả, bộ tiêu chí đánh giá prompt.
- Kết hợp Apps Script hoặc API ngoài để xây dựng backend AI serverless.
- **Tham khảo:** [Gemini API Quickstart (CLI)](https://ai.google.dev/gemini-api/docs/quickstart?hl=ja#cli)

**Ví dụ lệnh/prompt:**
```
cat syllabus.txt | gemini prompt \
  --model gemini-pro \
  --system "Bạn là trợ giảng hỗ trợ tóm tắt đề cương." \
  --prompt "Hãy trích mục tiêu học tập, phương thức đánh giá và lịch bài tập từ syllabus trên và trình bày dạng bảng."
```

```
cat application_form.md | gemini prompt \
  --model gemini-pro \
  --system "Bạn là cán bộ hành chính kiểm tra tài liệu nộp." \
  --prompt "Liệt kê lỗi chính tả, mục bắt buộc bỏ trống và phần sai định dạng trong tài liệu trên. Gợi ý cách sửa và đánh mức ưu tiên Cao/Trung Bình/Thấp."
```

```
cat survey.csv | gemini prompt \
  --model gemini-pro \
  --prompt "Đọc dữ liệu CSV, chỉ ra ba câu hỏi có điểm hài lòng thấp nhất và gợi ý cải thiện."
```

### 2.6 Thực hành thiết kế prompt
- **Định nghĩa vai trò:** Nêu rõ “Bạn là chuyên gia…” để đặt góc nhìn mong muốn.
- **Chuẩn bị đầu vào:** Tổ chức tài liệu nguồn (Markdown, bảng) để ngữ cảnh ổn định.
- **Ràng buộc:** Ghi cụ thể giọng điệu, định dạng, độ dài, ngôn ngữ, tài liệu tham chiếu.
- **Tinh chỉnh lặp:** Điều chỉnh prompt theo kết quả, lưu lại mẫu thành công.
- **Kiểm chứng:** Đối chiếu với tài liệu gốc, nhờ đồng nghiệp rà soát.
- **Thư viện prompt:** Lưu prompt trên Shared Drive hoặc repo để dễ tìm và tái sử dụng.
- **Đạo đức:** Nêu trực tiếp hạn chế (ví dụ không chứa dữ liệu cá nhân) trong prompt.
- **Kế hoạch dự phòng:** Chuẩn bị prompt thay thế hoặc quy trình thủ công khi hệ thống gặp sự cố.
- **Kiểm thử:** Thiết lập tiêu chí đánh giá (chính xác, giọng điệu, độ bao phủ) và bộ dữ liệu mẫu.
- **Khả năng tiếp cận:** Đảm bảo nội dung sinh ra đáp ứng tiêu chuẩn accessibility.

---

## Chương 3: Tự động hóa với GAS, RAG, MCP

Chương này mô tả cách kết hợp Apps Script, Gemini API và dịch vụ ngoài để xây dựng quy trình tự động hóa từ script nhỏ đến hệ thống quy mô lớn.

### 3.1 Tổng quan Apps Script, clasp, triển khai
- **Tính năng Apps Script:** Trình soạn thảo cloud, lập lịch trigger, tích hợp sâu với GWS.
- **Quy trình clasp:** Phát triển cục bộ, quản lý phiên bản và đẩy lên dự án Apps Script.
- **Triển khai:** Duy trì môi trường dev, staging, production; thiết lập quy tắc tránh sửa trực tiếp production.
- **Tự động kiểm thử:** Tích hợp CI/CD (GitHub Actions, Cloud Build) để lint, test, deploy tự động.
- **Xử lý lỗi:** Thiết lập logging, thông báo, retry; ghi log chi tiết vào Sheets hoặc BigQuery.
- **Bảo mật:** Giới hạn quyền tối thiểu, quản lý secret (Vault, Secret Manager), kiểm tra trigger.
- **Tham khảo:** [Kho GitHub của clasp](https://github.com/google/clasp)

### 3.2 Tích hợp Gemini API với Apps Script
- **Điều kiện:** Tạo dự án Google Cloud, bật Gemini API, quản lý API key an toàn.
- **Gửi HTTP:** Dùng `UrlFetchApp.fetch`, xử lý JSON và lỗi.
- **Mẫu prompt:** Lưu prompt theo phiên bản và biến môi trường để nhất quán.
- **Cache:** Dùng `CacheService` tái sử dụng phản hồi, giảm chi phí.
- **Logging:** Ghi metadata prompt/response vào Sheets hoặc BigQuery để truy vết.
- **Giao diện người dùng:** Xây web app hoặc chatbot Apps Script cho giảng viên, sinh viên.
- **Xử lý lỗi:** Định nghĩa trả lời fallback hoặc quy trình chuyển cho người phụ trách.
- **Tuân thủ:** Ẩn dữ liệu cá nhân, ghi nhận đồng ý, áp dụng chính sách tổ chức.
- **Tham khảo:** [Tổng quan Gemini API](https://ai.google.dev/gemini-api/docs?hl=ja)

### 3.3 Retrieval-Augmented Generation (RAG)
- **Pipeline:** Chuẩn hóa, embedding, lưu vector, truy xuất, sinh câu trả lời.
- **Nguồn dữ liệu:** Docs, Sheets, Sites, kho PDF; xử lý bằng Apps Script hoặc công cụ Google Cloud.
- **Kho vector:** Vertex AI Matching Engine, Firebase, hoặc dịch vụ bên thứ ba.
- **Soạn prompt:** Cài đoạn trích và trích dẫn để nâng độ tin cậy.
- **Đánh giá:** Đo độ chính xác, trích dẫn, độ trễ, mức hài lòng.
- **Bảo trì:** Cập nhật chỉ mục định kỳ, theo dõi phiên bản tài liệu, loại bỏ nội dung cũ.
- **Bảo mật:** Chỉ nạp nguồn được phê duyệt, quản lý khóa truy cập, log hoạt động truy xuất.
- **Tham khảo:** [Tổng quan RAG](https://cloud.google.com/architecture/rag-overview?hl=ja)

### 3.4 Multi-Channel Processing (MCP)
- **Khái niệm:** Kết hợp văn bản, âm thanh, hình ảnh, dữ liệu cấu trúc cho workflow nâng cao.
- **Triển khai:** Tích hợp Gemini API với nhận dạng giọng nói, dịch thuật, thị giác máy.
- **Tình huống:**
  - Chuyển bản ghi bài giảng, rút ý chính, tạo nhiệm vụ follow-up.
  - Đồng bộ nhật ký ảnh hiện trường, sinh báo cáo địa phương hóa.
  - Phân tích học liệu đa phương tiện, sinh tóm tắt, quiz, tài liệu bổ trợ.
- **Tham khảo:** [Tổng quan AI sinh đa phương tiện (Vertex AI)](https://cloud.google.com/vertex-ai/docs/generative-ai/multimodal/overview?hl=ja)

### 3.5 Thiết kế dự án và quản trị
- **Xác định yêu cầu:** Văn bản hóa mục tiêu, bên liên quan, luồng dữ liệu, yêu cầu bảo mật, SLA.
- **Quản lý phạm vi:** Tách MVP và mở rộng theo giai đoạn, đặt ưu tiên, lộ trình.
- **Tổ chức nhóm:** Rõ vai trò dev, IT, đơn vị sử dụng, kiểm toán.
- **Chiến lược kiểm thử:** Chuẩn bị test đơn vị, tích hợp, UAT, tình huống ngoại lệ.
- **Quản lý thay đổi:** Theo dõi thay đổi đặc tả, prompt qua ticket với quy trình phê duyệt.
- **Giám sát vận hành:** Định nghĩa log, cảnh báo lỗi, health check, quy trình leo thang.
- **Bảo mật:** Quản lý API key, OAuth cẩn thận, duy trì quyền tối thiểu, masking dữ liệu.
- **Tuân thủ:** Định kỳ rà soát bảo vệ dữ liệu cá nhân, đạo đức nghiên cứu, lưu trữ hồ sơ.
- **Đào tạo & hỗ trợ:** Cung cấp tài liệu, FAQ, kênh hỏi đáp, đào tạo định kỳ.
- **Cải tiến liên tục:** Đánh giá KPI, phản hồi, cập nhật kế hoạch cải tiến, lịch phát hành.
- **Tham khảo:** [Google Workspace Security Center](https://workspace.google.com/intl/ja/security/)

### 3.6 Checklist triển khai
1. **Quản lý dự án:** Duy trì Git, tài liệu, quy trình review mã nguồn.
2. **Truy xuất yêu cầu:** Theo dõi lịch sử thay đổi, phạm vi ảnh hưởng.
3. **Bảo mật:** Bảo vệ credential, tối thiểu quyền, mã hóa dữ liệu, kiểm toán log.
4. **Quan sát:** Thu thập log, metric, cảnh báo để phát hiện bất thường, quy định bước xử lý.
5. **Sao lưu:** Backup mã nguồn, cấu hình, dữ liệu định kỳ, kiểm tra khôi phục.
6. **SLA/SLO:** Đặt mục tiêu uptime, thời gian phản hồi, hỗ trợ và theo dõi thực tế.
7. **Đánh giá:** Đo thời gian tiết kiệm, giảm lỗi, mức hài lòng, chi phí.
8. **Đào tạo & truyền thông:** Cập nhật tài liệu, FAQ, tổ chức briefing định kỳ.
9. **Quản lý rủi ro:** Thiết kế fail-safe, xử lý ngoại lệ, quy trình can thiệp thủ công.
10. **Cải tiến liên tục:** Dùng phản hồi và log để cập nhật roadmap, kế hoạch phát hành.
- **Tham khảo:** [Google Workspace Learning Center](https://support.google.com/a/users?hl=ja)

---

## Phụ lục A: Hướng dẫn triển khai & vận hành

1. **Tài khoản**
   - Bật xác thực hai yếu tố cho tài khoản giảng viên, nhân viên.
   - Kiểm tra quyền Shared Drive định kỳ.
2. **Đào tạo**
   - Tổ chức ba cấp: cơ bản (GWS), trung cấp (AI sinh), nâng cao (GAS/RAG).
   - Cung cấp tài liệu on-demand (video, handbook) qua Google Sites.
3. **Quy tắc vận hành**
   - Xây dựng quy định dùng AI sinh (dữ liệu cấm, ví dụ prompt, quy trình rà soát).
   - Quy định quy trình review/phê duyệt trước khi đưa Apps Script/API vào production.
4. **Đánh giá & cải tiến**
   - Rà KPI hàng quý (giờ công, số lỗi, mức hài lòng).
   - Chia sẻ case thành công qua tọa đàm, newsletter để lan tỏa trong trường.

---

## Phụ lục B: Tài nguyên tham khảo

- [Google Workspace Admin Help](https://support.google.com/a?hl=ja)
- [Gemini for Workspace](https://workspace.google.com/products/gemini/?hl=ja)
- [Google AI Studio Documentation](https://ai.google.dev/aistudio?hl=ja)
- [Apps Script Sample Gallery](https://developers.google.com/apps-script/samples?hl=ja)
- Kho tri thức nội bộ (hướng dẫn sử dụng, bộ prompt, FAQ)

Hãy sử dụng sổ tay này để xây nền vững chắc với các tính năng chuẩn của Google Workspace, sau đó từng bước bổ sung AI sinh và tự động hóa. Áp dụng nội dung từng chương vào đào tạo và dự án thí điểm, duy trì vòng phản hồi liên tục để cân bằng giữa hiệu suất vận hành và chất lượng giáo dục, nghiên cứu.
