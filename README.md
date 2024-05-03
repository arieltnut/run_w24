viết ứng dụng python thực hiện các bước sau:
- khai bao tên các ứng dụng đặc biệt ("chrome.exe", "Orbita-Browser.exe", "MacroRecorder.exe", "Click-auto.exe")
- khai báo đường dẫn đến file auto-click.exe ("C:\Users\dell\PycharmProjects\Click-auto\click.exe"), và đường dẫn đến thư mục chứa các tập tin .ink (C:\uChrome")
- khai báo số lượng tập tin .ink mở đồng thời
- kiểm tra và tắt các ứng dụng nào đặc biệt đang chạy
- mở tập tin .ink (là ứng dụng chrome.exe) lần lượt tới khi bằng số lượng tập tin .ink mở đồng thời cho phép
- kiểm tra số lượng tập tin .ink đang mở, khi tắt 1 tập tin .ink đang mở, mở tập tin tiếp theo, số lượng tập tập tin .ink (là ứng dụng chrome.exe) vần so sánh nhỏ hơn khai báo số lượng tập tin .ink mở đồng thời
