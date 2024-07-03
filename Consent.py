import streamlit as st

st.set_page_config(page_title="Medical Information and Consent")

# JavaScript to switch language and accept consent
switch_language_script = """
<script>
    function switchLanguage(lang) {
        document.getElementById('en').style.display = (lang === 'en') ? 'block' : 'none';
        document.getElementById('th').style.display = (lang === 'th') ? 'block' : 'none';
    }

    function acceptConsent() {
        window.location.href = 'https://nnnnnnnatsu-cough.hf.space';
    }
</script>
"""

# Language Switch Buttons
st.markdown("""
<div class="language-switch" style="text-align: right; margin-bottom: 10px;">
    <button onclick="switchLanguage('en')">English</button>
    <button onclick="switchLanguage('th')">ภาษาไทย</button>
</div>
""", unsafe_allow_html=True)

# English Content
st.markdown("""
<div id="en" class="section">
    <h2>Medical Information Details</h2>
    <p>This application is designed to analyze users' cough sounds to assess the risk of pneumonia, bronchitis, and COVID-19.</p>
    <p><strong>Limitations of Information:</strong></p>
    <ul>
        <li>This analysis cannot replace the examination and diagnosis by a healthcare professional.</li>
        <li>The results provided are only preliminary predictions and may not always be accurate.</li>
        <li>Users should consult a doctor or medical expert for an accurate diagnosis.</li>
    </ul>
    <p><strong>Additional Information:</strong></p>
    <ul>
        <li>The recorded sounds will not be saved or stored in our system.</li>
        <li>This application does not collect any personally identifiable information, such as name, address, or other personal data.</li>
        <li>The data used for analysis will be automatically deleted after the analysis is complete.</li>
    </ul>
    <p><strong>Privacy Rights:</strong></p>
    <ul>
        <li>This application respects and complies with data protection principles as required by applicable law.</li>
        <li>All data used for analysis will be kept confidential and will not be disclosed to third parties without the user's consent.</li>
    </ul>

    <h2>Consent Agreement</h2>
    <p>By using this application, you agree to the following terms:</p>
    <ul>
        <li><strong>Voluntary Participation:</strong> Your use of this application is voluntary. There is no coercion involved.</li>
        <li><strong>Data Usage:</strong> The application will use your cough sound for analysis without saving or storing any data. All data will be automatically deleted after the analysis is complete.</li>
        <li><strong>Accuracy of Information:</strong> The information derived from the analysis is only a preliminary prediction and cannot replace a diagnosis by a healthcare professional.</li>
        <li><strong>Data Protection:</strong> Your information will not be used for identification or shared with third parties without your consent.</li>
    </ul>
    <button class="consent-button" onclick="acceptConsent()">I accept and understand the above terms</button>
</div>
""", unsafe_allow_html=True)

# Thai Content
st.markdown("""
<div id="th" class="section" style="display: none;">
    <h2>รายละเอียดข้อมูลทางการแพทย์</h2>
    <p>แอปพลิเคชั่นนี้ถูกออกแบบมาเพื่อวิเคราะห์เสียงไอของผู้ใช้เพื่อตรวจสอบความเสี่ยงในการเป็นโรคปอดอักเสบ, โรคหลอดลมอักเสบ, และ COVID-19</p>
    <p><strong>ข้อจำกัดของข้อมูล:</strong></p>
    <ul>
        <li>การวิเคราะห์นี้ไม่สามารถทดแทนการตรวจสอบและวินิจฉัยโดยแพทย์ผู้เชี่ยวชาญได้</li>
        <li>ข้อมูลที่แสดงผลเป็นเพียงการคาดการณ์เบื้องต้นเท่านั้น และอาจไม่ถูกต้องเสมอไป</li>
        <li>ผู้ใช้ควรปรึกษาแพทย์หรือผู้เชี่ยวชาญด้านการแพทย์เพื่อรับการวินิจฉัยที่แม่นยำ</li>
    </ul>
    <p><strong>ข้อมูลเพิ่มเติม:</strong></p>
    <ul>
        <li>การอัดเสียงจะไม่ถูกบันทึกหรือเก็บข้อมูลใดๆ ในระบบของเรา</li>
        <li>แอปพลิเคชั่นนี้ไม่มีการเก็บข้อมูลที่สามารถใช้ในการระบุตัวตนผู้ใช้ เช่น ชื่อ, ที่อยู่, หรือข้อมูลส่วนบุคคลอื่นๆ</li>
        <li>ข้อมูลที่ถูกใช้ในการวิเคราะห์จะถูกลบอัตโนมัติหลังจากการวิเคราะห์เสร็จสิ้น</li>
    </ul>
    <p><strong>สิทธิ์ส่วนบุคคล:</strong></p>
    <ul>
        <li>แอปพลิเคชั่นนี้เคารพและปฏิบัติตามหลักการคุ้มครองข้อมูลส่วนบุคคลตามกฎหมายที่บังคับใช้</li>
        <li>ข้อมูลทั้งหมดที่ใช้ในการวิเคราะห์จะถูกเก็บรักษาเป็นความลับและไม่ถูกเปิดเผยต่อบุคคลภายนอกโดยไม่ได้รับความยินยอมจากผู้ใช้</li>
    </ul>

    <h2>ข้อตกลงยินยอม</h2>
    <p>โดยการใช้แอปพลิเคชั่นนี้ คุณตกลงและยอมรับข้อกำหนดดังต่อไปนี้:</p>
    <ul>
        <li><strong>ความสมัครใจ:</strong> การใช้แอปพลิเคชั่นนี้เป็นไปโดยความสมัครใจของคุณ ไม่มีการบังคับใดๆ</li>
        <li><strong>การใช้งานข้อมูล:</strong> แอปพลิเคชั่นจะใช้เสียงไอของคุณเพื่อการวิเคราะห์โรคโดยไม่บันทึกหรือเก็บข้อมูลใดๆ ข้อมูลทั้งหมดจะถูกลบอัตโนมัติหลังการวิเคราะห์เสร็จสิ้น</li>
        <li><strong>ความถูกต้องของข้อมูล:</strong> ข้อมูลที่ได้จากการวิเคราะห์จะเป็นเพียงการคาดการณ์เบื้องต้นเท่านั้น และไม่สามารถทดแทนการวินิจฉัยโดยแพทย์ผู้เชี่ยวชาญได้</li>
        <li><strong>การคุ้มครองข้อมูลส่วนบุคคล:</strong> ข้อมูลของคุณจะไม่ถูกใช้เพื่อการระบุตัวตนหรือแบ่งปันกับบุคคลภายนอกโดยไม่ได้รับความยินยอมจากคุณ</li>
    </ul>
    <button class="consent-button" onclick="acceptConsent()">ข้าพเจ้ายอมรับและเข้าใจข้อตกลงข้างต้น</button>
</div>
""", unsafe_allow_html=True)

st.markdown(switch_language_script, unsafe_allow_html=True)

# JavaScript to set default language to English
st.markdown("<script>switchLanguage('en');</script>", unsafe_allow_html=True)
