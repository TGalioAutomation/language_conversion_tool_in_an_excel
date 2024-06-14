# language_conversion_tool_in_an_excel
Một công cụ để chuyển đổi toàn bộ nội dung trong tệp Excel sang một ngôn ngữ mới
Công cụ Python dịch Excel
Giới thiệu
Công cụ này cho phép bạn dịch nội dung của một tệp Excel từ ngôn ngữ nguồn sang ngôn ngữ đích. Nó sử dụng thư viện googletrans để dịch và pandas để xử lý và ghi lại dữ liệu dịch.

Chuẩn bị
Trước khi sử dụng công cụ, bạn cần cài đặt các thư viện Python cần thiết bằng lệnh sau:

bash
Copy code
pip install pandas openpyxl googletrans==4.0.0-rc1
Cấu hình (config.yaml)
Bạn cần tạo một tệp cấu hình YAML (config.yaml) như sau:
```
excel_path: 'path_to_your_input_excel.xlsx'
src_lang: 'en'
dest_lang: 'vi'
```
excel_path: Đường dẫn tới tệp Excel bạn muốn dịch.
src_lang: Ngôn ngữ nguồn của nội dung trong tệp Excel (mặc định là 'en' cho tiếng Anh).
dest_lang: Ngôn ngữ đích mà bạn muốn dịch sang (mặc định là 'vi' cho tiếng Việt).

English version:
### Translating to English:
A tool to convert all content in an Excel file to a new language
**Python Tool for Translating Excel**
**Introduction**
This tool allows you to translate the contents of an Excel file from a source language to a target language. It utilizes the `googletrans` library for translation and `pandas` for processing and recording translated data.

**Setup**
Before using the tool, you need to install the necessary Python libraries with the following command:

```bash
pip install pandas openpyxl googletrans==4.0.0-rc1
```

**Configuration (config.yaml)**
You need to create a YAML configuration file (`config.yaml`) as follows:

```yaml
excel_path: 'path_to_your_input_excel.xlsx'
src_lang: 'en'
dest_lang: 'vi'
```

- `excel_path`: Path to the Excel file you want to translate.
- `src_lang`: Source language of the content in the Excel file (default is 'en' for English).
- `dest_lang`: Target language you want to translate into (default is 'vi' for Vietnamese).
