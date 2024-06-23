
## โปรเจค Line Chatbot สำหรับติดตามการโหวตเห็นชอบนายก

โปรเจคนี้ถูกพัฒนาขึ้นโดยใช้ Python Flask, Kafka, MongoDB, และ Line Chatbot โดยมีวัตถุประสงค์เพื่อดูจำนวนผู้ที่เห็นชอบหรือไม่เห็นชอบนายกรัฐมนตรี โปรเจคนี้ถูกสร้างขึ้นเพื่อการศึกษา

### คุณสมบัติ

-   **เพิ่มข้อมูล:** Endpoint สำหรับเพิ่มข้อมูลใหม่ลงในระบบ เช่น การโหวตและความคิดเห็นของผู้ใช้
-   **ดึงข้อมูล:** Endpoint สำหรับดึงข้อมูลจากระบบ เช่น จำนวนการโหวตและความคิดเห็นของผู้ใช้
-   **แก้ไขข้อมูล:** Endpoint สำหรับแก้ไขข้อมูลที่มีอยู่ในระบบ
-   **ลบข้อมูล:** Endpoint สำหรับลบข้อมูลออกจากระบบ

### ขั้นตอนการติดตั้ง

#### ขั้นตอนที่ 1: Clone โปรเจคและติดตั้งแพ็กเกจ

##### Python Version: 3.12.0

```bash
git clone https://github.com/Sathaphon44/line-vote-flask.git
cd line-vote-flask
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt`
```
#### ขั้นตอนที่ 2: การแก้ไขค่าตัวแปรสภาพแวดล้อม

#### สร้างไฟล์ `.env` ในโฟลเดอร์ `line-vote-flask/` โดยมีเนื้อหาดังนี้:
```bash 
# Line API configuration
LINE_ACCESS_TOKEN=your_line_access_token
API_LINE=your_api_line

# Kafka configuration
KAFKA_BOOTSTRAP_SERVERS=your_kafka_bootstrap_servers
CLOUDKAFKA_TOPIC=your_cloudkafka_topic
CLOUDKAFKA_USERNAME=your_cloudkafka_username
CLOUDKAFKA_PASSWORD=your_cloudkafka_password

# MongoDB configuration
MONGODB_URI=mongodb://your_mongodb_username:your_mongodb_password@your_mongodb_host:your_mongodb_port/your_database_name` 
```
-   แทนที่ `your_line_access_token` และ `your_api_line` ด้วยค่า Line access token และ API line ของคุณ
-   แทนที่ `your_kafka_bootstrap_servers`, `your_cloudkafka_topic`, `your_cloudkafka_username`, และ `your_cloudkafka_password` ด้วยค่าการตั้งค่า Kafka ของคุณ
-   แทนที่ `your_mongodb_username`, `your_mongodb_password`, `your_mongodb_host`, `your_mongodb_port`, และ `your_database_name` ด้วยค่าการตั้งค่า MongoDB ของคุณ

#### ขั้นตอนที่ 3: รันโปรเจค
```bash
# สำหรับการพัฒนา
flask run
```
# สำหรับการรันในโปรดักชั่น ให้ใช้ WSGI server แทนที่จะเป็น development server` 

### วิธีการใช้งาน

-   **ส่งข้อความไปยัง Line Chatbot:** ผู้ใช้สามารถโต้ตอบกับ Line Chatbot โดยการส่งข้อความ
-   **ดูจำนวนการโหวต:** ระบบจะประมวลผลข้อความและอัพเดทจำนวนการโหวตตามนั้น
-   **การเชื่อมต่อ Kafka:** ข้อความจะถูกส่งไปยัง Kafka topic เพื่อการประมวลผลต่อไป
-   **การจัดเก็บข้อมูลใน MongoDB:** ข้อมูลทั้งหมดจะถูกจัดเก็บใน MongoDB เพื่อความคงทน

### เครดิต
-   Sathaphon K.
