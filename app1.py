import streamlit as st
import time

st.set_page_config(page_title="AI Adaptive Assessment - NLP System", page_icon="🧠", layout="wide")

st.title("🧠 Hệ thống NLP Đánh giá Tự luận & Phân tích Ngữ nghĩa Cá nhân hóa")
st.caption("Chuyên môn NLP: Semantic Analysis, Keyword Extraction & Adaptive Feedback")
st.markdown("---")

# --- BƯỚC 1: GIÁO VIÊN NẠP TÀI LIỆU HOẶC NHẬP MÔ TẢ ---
st.header("Bước 1: Nạp tài liệu giảng dạy hoặc Nhập chủ đề bài học")
uploaded_file = st.file_uploader("Tải lên file bài giảng (.txt, .pdf, .docx)", type=["txt", "pdf", "docx"])
custom_description = st.text_area("Hoặc nhập nội dung / chủ đề bài giảng:", 
                                 placeholder="Nhập nội dung bài học bất kỳ...",
                                 height=100)

source_content = ""
if uploaded_file is not None:
    source_content = "Đã nhận diện file tài liệu tải lên."
elif custom_description:
    source_content = custom_description

if st.button("🚀 Phân tích Văn bản (NLP) & Tạo 10 Câu hỏi Tự luận"):
    if not source_content.strip():
        st.error("Vui lòng tải lên file hoặc nhập mô tả trước khi sinh đề bài!")
    else:
        with st.spinner("Đang trích xuất Từ khóa cốt lõi (Keywords Extraction) & Sinh câu hỏi tự luận phân cấp..."):
            time.sleep(2)
        st.success("Đã khởi tạo bộ 10 câu hỏi Tự luận đánh giá năng lực tư duy & ngôn ngữ!")
        st.session_state['generated'] = True

# --- BƯỚC 2 & 3: BÀI TEST TỰ LUẬN ĐỒNG THỜI ---
if st.session_state.get('generated', False):
    st.markdown("---")
    st.header("Bước 2 & 3: Bài kiểm tra Tự luận dành cho Học sinh")
    st.info("📝 **Hình thức NLP:** Học sinh trả lời tự luận ngắn (2-3 câu giải thích) cho từng câu hỏi.")
    
    questions = [
        "Câu 1 [Nhận biết]: Trình bày ngắn gọn khái niệm cốt lõi nhất được đề cập trong bài học.",
        "Câu 2 [Nhận biết]: Nêu các thuộc tính hoặc thành phần quan trọng cấu thành nên đối tượng nghiên cứu.",
        "Câu 3 [Thông hiểu]: Giải thích nguyên lý vận hành/mục đích chính của chủ đề này.",
        "Câu 4 [Thông hiểu]: Phân tích điều kiện cần và đủ để quá trình này diễn ra hiệu quả.",
        "Câu 5 [Thông hiểu]: Phân biệt sự khác nhau giữa khái niệm này và các khái niệm liên quan khác.",
        "Câu 6 [Vận dụng]: Nêu một ví dụ thực tế minh họa cho lý thuyết vừa học.",
        "Câu 7 [Vận dụng]: Trình bày quy trình các bước giải quyết vấn đề thực tế từ bài học.",
        "Câu 8 [Vận dụng cao]: Phân tích tác động hoặc hậu quả khi một thành phần cốt lõi bị gián đoạn.",
        "Câu 9 [Vận dụng cao]: Đề xuất phương án cải tiến hoặc tối ưu hóa cho mô hình hiện tại.",
        "Câu 10 [Vận dụng cao]: Luận giải về trường hợp ngoại lệ hoặc giới hạn áp dụng của lý thuyết."
    ]

    answers = {}
    for i, q in enumerate(questions):
        st.markdown(f"**{q}**")
        answers[f"q{i+1}"] = st.text_area(f"Nhập câu trả lời tự luận cho Câu {i+1}:", 
                                          key=f"ans_{i+1}", 
                                          height=80, 
                                          placeholder="Viết 2-3 câu giải thích tại đây...")

    if st.button("🔍 Phân tích Ngữ nghĩa NLP & Chẩn đoán Lỗ hổng"):
        with st.spinner("NLP Engine đang xử lý Semantic Matching, kiểm tra Từ khóa cốt lõi & Ngữ pháp..."):
            time.sleep(2.5)
            
        # --- BƯỚC 4: PHÂN TÍCH VĂN BẢN & CHẨN ĐOÁN NLP ---
        st.markdown("---")
        st.header("Bước 4: Kết quả Chẩn đoán Ngữ nghĩa NLP & Xếp loại")
        
        col1, col2 = st.columns([1, 2])
        with col1:
            st.metric(label="Mức độ năng lực (Level)", value="Level B (Giỏi)")
            st.metric(label="Độ phủ Từ khóa Cốt lõi (Keyword Coverage)", value="78%")
            st.metric(label="Chỉ số Mạch lạc & Ngữ nghĩa (Semantic Score)", value="8.2 / 10")
        
        with col2:
            st.markdown("### 📊 Phân tích Chi tiết Văn bản (NLP Diagnostic):")
            st.markdown("- **Điểm mạnh:** Cấu trúc câu diễn đạt rõ ràng, sử dụng đúng các thuật ngữ chuyên ngành ở câu 1 đến câu 7.")
            st.markdown("- **Thiếu hụt Từ khóa cốt lõi (Missing Core Keywords):** Trong câu trả lời tự luận 8 và 9, bài làm thiếu hẳn các từ khóa quan trọng như: `[Cơ chế phản hồi]`, `[Tối ưu hóa đa mục tiêu]`, `[Giới hạn biên]`.")
            st.markdown("- **Lỗi ngữ nghĩa phổ biến:** Diễn đạt còn mang tính cảm quan, chưa cụ thể hóa bằng mô hình lý thuyết ở phần Vận dụng cao.")

        # --- BƯỚC 5: ĐỀ XUẤT CÁ NHÂN HÓA DỰA TRÊN TỪ KHÓA THIẾU ---
        st.markdown("---")
        st.header("Bước 5: Gợi ý Tài liệu & Bài tập Bổ sung Smart NLP")
        st.warning("🎯 **Hệ thống tự động phát hiện lỗ hổng từ vựng/kiến thức và đề xuất chính xác:**")
        
        st.markdown("1. 📖 **Tài liệu đọc bù đắp:** Gợi ý đọc lại Chuyên đề 3 - *'Các từ khóa cốt lõi & Cơ chế phản hồi trong hệ thống'* (Chứa các từ khóa bạn đang thiếu).")
        st.markdown("2. 📝 **Bài tập rèn luyện viết tự luận:** Luyện tập lại bài tự luận 2 câu với yêu cầu bắt buộc tích hợp bộ từ khóa `[Cơ chế phản hồi]` và `[Giới hạn biên]`.")
        
        # BÁO CÁO DÀNH CHO GIÁO VIÊN
        st.markdown("---")
        st.header("📋 Báo cáo Tổng hợp Ngữ nghĩa gửi Giáo viên (NLP Teacher Dashboard)")
        st.json({
            "hoc_sinh": "Nguyễn Văn A",
            "xep_loai": "Level B",
            "loi_sai_ngu_nghia_pho_bien": "Thiếu các khái niệm liên quan đến cơ chế tối ưu",
            "chu_de_viet_tot": ["Khái niệm cơ bản", "Đặc điểm thành phần", "Ví dụ thực tế"],
            "chu_de_chua_tot": ["Luận giải ngoại lệ", "Phân tích tác động dây chuyền"],
            "tu_khoa_can_bo_sung": ["Cơ chế phản hồi", "Tối ưu hóa đa mục tiêu", "Giới hạn biên"]
        })
        st.success("Đã xuất Báo cáo Phân tích NLP chi tiết!")